#!/usr/bin/env python3
"""Discord harvester for the second brain's nightly run.

Pulls messages posted since the last run from the operational channels of the Dude Talk
Dinners guild and writes them to raw/discord.md in the same H2-block / `---` divider format
as the other raw dumps, so scripts/prefilter.py picks the file up with no changes.

Scope is deliberately narrow. Only channels where the org talks about running itself are
read: Dude Central, Leadership Circle, per-community leadership and dinner channels, plus
#announcements and #next-dinner. The rooms members talk in -- #general, #general-men-only,
#introduce-yourself, #feedback, #activities and every #<community>-chat -- are never read.
Dinner conversation is confidential; a generated summary is not the place for it.

Bots cannot read user-to-user DMs, so the Andrew/John DM thread that Slack used to carry
has no equivalent here. That gap is permanent and is noted in the dump header.

Environment:
  DISCORD_BOT_TOKEN   required -- bot token, needs View Channel + Read Message History
  DISCORD_GUILD_ID    optional -- defaults to the Dude Talk Dinners guild

Usage:
  python3 scripts/harvest_discord.py              # window starts at state/seen.json last_run
  python3 scripts/harvest_discord.py --since 2026-09-01T00:00:00Z
  python3 scripts/harvest_discord.py --dry-run    # print the channel plan, fetch nothing
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
LEDGER = ROOT / "state" / "seen.json"
OUTPUT = RAW_DIR / "discord.md"

API = "https://discord.com/api/v10"
DEFAULT_GUILD_ID = "1024015443582799913"
DISCORD_EPOCH_MS = 1420070400000

# Channel types that carry messages worth reading.
TEXT_TYPES = {0, 5}          # GUILD_TEXT, GUILD_ANNOUNCEMENT
THREAD_TYPES = {10, 11, 12}  # ANNOUNCEMENT_THREAD, PUBLIC_THREAD, PRIVATE_THREAD

# --- scope policy -----------------------------------------------------------------
# Named channels always read.
ALLOW_EXACT = {
    "board-chat",
    "staff-chat",
    "leadership-circle-chat",
    "facilitators",
    "coordinators",
    "announcements",
    "next-dinner",
}
# Suffix patterns, so a new community's channels are picked up the day it launches
# without anyone editing this file.
ALLOW_SUFFIX = ("-leadership", "-dinners")

# Never read, even if a future channel name happens to match a pattern above.
# These are the rooms members speak in, plus the plumbing channels.
DENY_EXACT = {
    "general",
    "general-men-only",
    "introduce-yourself",
    "feedback",
    "activities",
    "resources",
    "welcome",
    "ground-rules",
    "how-to-verify",
    "verify",
    "test",
    "bot-logs",
}
DENY_SUFFIX = ("-chat",)
# Exception: the leadership/staff "-chat" channels are operational, not member-facing.
DENY_SUFFIX_EXCEPTIONS = {"board-chat", "staff-chat", "leadership-circle-chat"}


def in_scope(name: str) -> bool:
    """True if this channel name is one the nightly harvest is allowed to read."""
    if name in DENY_EXACT:
        return False
    if name.endswith(DENY_SUFFIX) and name not in DENY_SUFFIX_EXCEPTIONS:
        return False
    if name in ALLOW_EXACT:
        return True
    return name.endswith(ALLOW_SUFFIX)


# --- discord api ------------------------------------------------------------------

def api_get(path: str, token: str, params: dict | None = None, attempt: int = 0):
    """GET an API path, honouring 429 retry_after and backing off on 5xx."""
    url = f"{API}{path}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bot {token}",
            "User-Agent": "DTDSecondBrain (https://github.com/JohnCalafiore/general, 1.0)",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 429 and attempt < 5:
            try:
                retry_after = float(json.loads(exc.read().decode("utf-8")).get("retry_after", 1))
            except Exception:
                retry_after = 1.0
            time.sleep(min(retry_after + 0.25, 30))
            return api_get(path, token, params, attempt + 1)
        if exc.code in (500, 502, 503, 504) and attempt < 4:
            time.sleep(2 ** attempt)
            return api_get(path, token, params, attempt + 1)
        raise


def snowflake_for(dt: datetime) -> int:
    """Discord message IDs encode their timestamp; build the lower bound for `after`."""
    ms = int(dt.timestamp() * 1000) - DISCORD_EPOCH_MS
    return max(ms, 0) << 22


def fetch_messages(channel_id: str, token: str, after_id: int) -> list[dict]:
    """All messages in a channel newer than after_id, oldest first."""
    collected = []
    cursor = after_id
    while True:
        batch = api_get(
            f"/channels/{channel_id}/messages", token, {"limit": 100, "after": cursor}
        )
        if not batch:
            break
        batch.sort(key=lambda m: int(m["id"]))
        collected.extend(batch)
        cursor = int(batch[-1]["id"])
        if len(batch) < 100:
            break
        if len(collected) >= 1000:  # a runaway channel shouldn't blow up the run
            collected.append({"_truncated": True})
            break
    return collected


# --- rendering --------------------------------------------------------------------

def describe_author(msg: dict) -> str:
    author = msg.get("author") or {}
    name = author.get("global_name") or author.get("username") or "unknown"
    return f"{name} (bot)" if author.get("bot") else name


def render_message(msg: dict, channel_name: str, guild_id: str, channel_id: str) -> str:
    if msg.get("_truncated"):
        return (
            f"## discord-truncated #{channel_name}\n\n"
            "- More than 1000 messages in this channel this window; the harvest stopped early.\n"
            "- Raise the cap in scripts/harvest_discord.py or narrow the window."
        )

    mid = msg["id"]
    ts = msg.get("timestamp", "")
    try:
        when = datetime.fromisoformat(ts.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M UTC")
    except ValueError:
        when = ts

    author = describe_author(msg)
    permalink = f"https://discord.com/channels/{guild_id}/{channel_id}/{mid}"

    lines = [f"## discord-{mid} #{channel_name} — {author}", ""]
    lines.append(f"- from: {author}, {when}")
    lines.append(f"- channel: #{channel_name}")
    lines.append(f"- permalink: {permalink}")

    if msg.get("edited_timestamp"):
        lines.append("- edited after posting")
    if msg.get("type") == 19 and msg.get("referenced_message"):
        ref = msg["referenced_message"]
        lines.append(f"- in reply to {describe_author(ref)}: \"{(ref.get('content') or '')[:120]}\"")

    lines.append("")

    content = (msg.get("content") or "").strip()
    if content:
        lines.extend(f"> {line}" if line.strip() else ">" for line in content.splitlines())
    else:
        lines.append("> _(no text)_")

    extras = []
    for att in msg.get("attachments") or []:
        filename = att.get("filename", "file")
        size = att.get("size")
        extras.append(f"attachment: {filename}" + (f" ({size} bytes)" if size else ""))
    for emb in msg.get("embeds") or []:
        title = emb.get("title") or emb.get("url") or emb.get("description") or "untitled"
        extras.append(f"embed: {str(title)[:160]}")
    if extras:
        lines.append("")
        lines.extend(f"- {e}" for e in extras)

    if not content and not extras:
        lines.append("")
        lines.append("- No text and no attachment returned. Content unknown.")

    return "\n".join(lines)


def write_dump(body_blocks: list[str], window_start: datetime, window_end: datetime,
               channels_read: int, skipped: list[str], failed: bool = False,
               error: str | None = None) -> None:
    RAW_DIR.mkdir(exist_ok=True)
    header = [
        "# Discord",
        f"harvest window: {window_start.strftime('%Y-%m-%dT%H:%M:%SZ')} → "
        f"{window_end.strftime('%Y-%m-%dT%H:%M:%SZ')}",
    ]
    if failed:
        header.append("")
        header.append("**HARVEST FAILED — this is not a quiet night.**")
    else:
        header.append(
            f"scope: operational channels only ({channels_read} read). "
            "Member conversation channels are never harvested."
        )
        header.append(
            "note: bots cannot read user-to-user DMs, so direct messages between people "
            "are not captured here."
        )
    if skipped:
        header.append(f"no access: {', '.join(sorted(set(skipped)))}")

    parts = ["\n".join(header)]

    if failed:
        parts.append(
            f"## discord-harvest-failed {window_end.strftime('%Y-%m-%d')}\n\n"
            f"- The Discord harvest did not run on {window_end.strftime('%Y-%m-%d')}.\n"
            f"- Error: {error}\n"
            "- Treat Discord as uncovered for this window. An empty Discord section today "
            "means the sweep broke, not that nothing was said.\n"
            "- Fix: check DISCORD_BOT_TOKEN on the routine and the bot's Read Message "
            "History permission."
        )
    elif body_blocks:
        parts.extend(body_blocks)
    else:
        parts.append(
            f"## discord-quiet {window_end.strftime('%Y-%m-%d')}\n\n"
            f"- No messages in the {channels_read} operational channels this window.\n"
            "- The sweep ran and found nothing, which is different from the sweep not running."
        )

    OUTPUT.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")


# --- main -------------------------------------------------------------------------

def resolve_window(since_arg: str | None) -> datetime:
    if since_arg:
        return datetime.fromisoformat(since_arg.replace("Z", "+00:00")).astimezone(timezone.utc)
    if LEDGER.exists():
        try:
            last_run = json.loads(LEDGER.read_text()).get("last_run")
            if last_run:
                return datetime.fromisoformat(last_run).astimezone(timezone.utc)
        except (json.JSONDecodeError, ValueError):
            pass
    return datetime.now(timezone.utc) - timedelta(hours=48)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", help="ISO8601 window start; overrides state/seen.json")
    parser.add_argument("--dry-run", action="store_true", help="print the channel plan only")
    args = parser.parse_args()

    guild_id = os.environ.get("DISCORD_GUILD_ID", DEFAULT_GUILD_ID)
    token = os.environ.get("DISCORD_BOT_TOKEN", "").strip()
    window_start = resolve_window(args.since)
    window_end = datetime.now(timezone.utc)

    if not token and not args.dry_run:
        msg = "DISCORD_BOT_TOKEN is not set"
        write_dump([], window_start, window_end, 0, [], failed=True, error=msg)
        print(f"discord harvest FAILED: {msg} -> {OUTPUT.relative_to(ROOT)}", file=sys.stderr)
        return 1

    try:
        if args.dry_run and not token:
            print("No token; cannot list channels. Scope policy:")
            print(f"  allow exact:  {sorted(ALLOW_EXACT)}")
            print(f"  allow suffix: {list(ALLOW_SUFFIX)}")
            print(f"  deny exact:   {sorted(DENY_EXACT)}")
            print(f"  deny suffix:  {list(DENY_SUFFIX)} except {sorted(DENY_SUFFIX_EXCEPTIONS)}")
            return 0

        channels = api_get(f"/guilds/{guild_id}/channels", token)
        targets = [
            c for c in channels
            if c.get("type") in TEXT_TYPES and in_scope(c.get("name", ""))
        ]

        # Threads hang off a parent channel; include those whose parent is in scope.
        try:
            active = api_get(f"/guilds/{guild_id}/threads/active", token).get("threads", [])
            in_scope_ids = {c["id"] for c in targets}
            targets.extend(
                t for t in active
                if t.get("type") in THREAD_TYPES and t.get("parent_id") in in_scope_ids
            )
        except urllib.error.HTTPError:
            pass  # thread listing is a bonus, not a requirement

        if args.dry_run:
            print(f"{len(targets)} channels in scope:")
            for c in sorted(targets, key=lambda c: c.get("name", "")):
                print(f"  #{c.get('name')}  ({c['id']})")
            skipped_names = sorted(
                c.get("name", "") for c in channels
                if c.get("type") in TEXT_TYPES and not in_scope(c.get("name", ""))
            )
            print(f"\n{len(skipped_names)} channels deliberately skipped:")
            print("  " + ", ".join(f"#{n}" for n in skipped_names))
            return 0

        after_id = snowflake_for(window_start)
        blocks, no_access, total = [], [], 0

        for channel in sorted(targets, key=lambda c: c.get("name", "")):
            name, cid = channel.get("name", "unknown"), channel["id"]
            try:
                messages = fetch_messages(cid, token, after_id)
            except urllib.error.HTTPError as exc:
                if exc.code in (403, 404):
                    no_access.append(f"#{name}")
                    continue
                raise
            for msg in messages:
                total += 1
                blocks.append(render_message(msg, name, guild_id, cid))

        write_dump(blocks, window_start, window_end, len(targets), no_access)
        print(
            f"{total} messages from {len(targets)} channels -> {OUTPUT.relative_to(ROOT)}"
            + (f" ({len(no_access)} channels not readable)" if no_access else "")
        )
        return 0

    except Exception as exc:  # noqa: BLE001 - the nightly run must not die silently
        write_dump([], window_start, window_end, 0, [], failed=True, error=f"{type(exc).__name__}: {exc}")
        print(f"discord harvest FAILED: {exc} -> {OUTPUT.relative_to(ROOT)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
