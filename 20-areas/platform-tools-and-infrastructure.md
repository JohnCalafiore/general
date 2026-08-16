---
area: Platform, Tools, and Infrastructure
updated: 2026-08-16
tags: [area]
---

# Platform, Tools, and Infrastructure

Standing area for Dude Talk Dinners — matches the Morning brief look-back category of
the same name. Ongoing facts, decisions, and developments that belong to this
responsibility but not to a specific dated project get logged here.

## Log

<!-- Newest first. One H2 per atomic entry (## YYYY-MM-DD Short title) with a source
     line, so entries can be linked as [[platform-tools-and-infrastructure#...]] and harvested by the brief. -->

## 2026-08-15 Search Console: Events structured data issues confirmed fixed
- "**Google has validated your fix for Events structured data issues on
  dudetalkdinners.org.**" The problem first flagged Aug 9 (6 issues) and again Aug 14 (1
  more) is closed. Still unresolved in the record: the **duplicate-canonical indexing
  issue** raised Aug 10.
- category: Platform, Tools, and Infrastructure
- source: Google Search Console validation email 2026-08-15
- links: [[platform-tools-and-infrastructure#2026-08-14 Search Console validating the structured-data fixes; Andrew requests a Workspace upgrade]]

## 2026-08-15 CRM digest jumps: 10 new contacts in a day
- "Activity yesterday: **10 new contacts · 2 emails sent.**" A step-change from the
  one-or-two-per-day pattern of the previous digests — worth checking whether these are the
  Aug 14 template tests and test signups or genuine inbound, since the count lands on the
  day the whole email suite was exercised.
- category: Platform, Tools, and Infrastructure
- source: DTD reminders digest 2026-08-15
- links: [[platform-tools-and-infrastructure#2026-08-14 The whole automated-email suite tested in one sitting — seven templates]]

## 2026-08-14 The new DTD website is live
- John's board-report line, stated flatly: "**New DTD website is live and active!**" — the
  refresh that has been "on track within the next 10 days" since Aug 6, and the thing Erik
  called "a huge win" for the Buena Vista chapter page. Alongside it: "**CRM testing live**."
- category: Platform, Tools, and Infrastructure
- source: John's board-report draft, Slack DM to Andrew 2026-08-14
- links: [[support-for-existing-communities#2026-08-06 Startup materials taking shape: facilitator guide, welcome video, site refresh]]

## 2026-08-14 The whole automated-email suite tested in one sitting — seven templates
- Every CRM email template was exercised end to end from support@dudetalkdinners.org, and
  the copy is worth keeping since it's now DTD's automated voice:
  - **Newsletter welcome** — candid about status: the newsletter "**is currently in
    development**."
  - **Donation thank-you** — "Thank you for your gift of $50.00... **Givebutter has sent
    your tax receipt separately; this note is just us saying it matters. Your support keeps
    the table set.**" (This is the acknowledgment layer the Aug 12 session was for.)
  - **General inquiry** — "**A real person reads every message.**"
  - **Intro / good to meet you** — "men gather over dinner for **real conversation, with
    real dudes, making real connections**."
  - **Wants to support** — "Your generosity **keeps seats at the table**."
  - **Wants to start a community** — "That takes initiative, and **that's how each Dinner
    begins**."
  - **Community welcome** — reworded from Aug 13 to say "joining a Dude Talk **Dinner**"
    and "someone from that **Community**," capitalizing Dinner and Community per the
    house style.
- A test signup ("Test Tester," Idaho Springs, org-level) also ran through the form to the
  CRM the same afternoon.
- category: Platform, Tools, and Infrastructure
- source: seven "[Test]" sends + signup-form notification 2026-08-14
- links: [[platform-tools-and-infrastructure#2026-08-13 Welcome automation tested — routes a signup to their named community]]

## 2026-08-14 Cal.com's first real booking; Andrew's page is live too
- Andrew posted **cal.com/andrew-wolff/30min** in Slack and a **30-minute Andrew/John
  meeting was booked for Tue Aug 18** through it — the setup works for real bookings one
  day after being configured. The cross-calendar blocking bug is still unresolved in the
  record, so external sharing remains the risk to watch.
- category: Platform, Tools, and Infrastructure
- source: Cal.com confirmation email + Slack DM 2026-08-14
- links: [[platform-tools-and-infrastructure#2026-08-13 DECISION: Cal.com is DTD's scheduling tool — free tier, with one blocking bug]]

## 2026-08-14 Search Console validating the structured-data fixes; Andrew requests a Workspace upgrade
- Google has **started validating the Events structured-data fixes** for dudetalkdinners.org
  — so the issues flagged Aug 9 and Aug 14 were addressed, though the duplicate-canonical
  problem from Aug 10 hasn't been mentioned since.
- Separately, **Andrew requested a Google Workspace upgrade to Business Standard**, pending
  an admin decision. Worth connecting to Thursday's reasoning, where a $3/user/mo Workspace
  upgrade was rejected as too expensive across 10+ accounts.
- action #open (John, as admin): decide on Andrew's Business Standard request
- category: Platform, Tools, and Infrastructure
- source: Search Console validation email + Workspace notification 2026-08-14

## 2026-08-13 DECISION: Cal.com is DTD's scheduling tool — free tier, with one blocking bug
- Google Calendar's free booking pages capped DTD at **one booking page per user**, which
  breaks the moment you want separate 30- and 60-minute links. The alternatives were priced
  out explicitly: **Google Calendar upgrade at $3/user/mo** (rejected because it applies
  across **10+ DTD Workspace accounts**), **Calendly at ~$15/user/mo**, and **Setmore**,
  rejected on function rather than price — its free plan is **one-way sync**, so events
  added directly in Google Calendar don't block Setmore availability.
- Chosen: **Cal.com's free individual plan** — unlimited booking pages and event types.
  Team scheduling would cost $12–$16/user/mo, deferred as acceptable.
- Andrew's account is configured: **30/45/60-min event types; availability Tue–Fri
  10am–4pm MT; 24-hour minimum notice; 15-minute buffers either side; bookings limited to
  21 days out.** John's own links went live the same day (cal.com/john-calafiore/15min,
  /30min, /45min, /60min) and were sent to Andrew.
- **Open bug, and it matters:** testing showed **Cal.com does not block availability
  against secondary calendars** (Andrew's Wolff Coaching calendar), so the tool will offer
  slots he isn't actually free for. Flagged as a double-booking risk that must be fixed
  **before links are shared externally**.
- action #open (Andrew): fix the secondary-calendar blocking, then send **Chris Kyle** a
  30-min link
- category: Platform, Tools, and Infrastructure
- source: Fathom recap, "CRM login and learn" 2026-08-13 (fathom.video/calls/783087731);
  "Test Calendar" email 2026-08-13

## 2026-08-13 CRM lockout ran deeper than the invite — reset flow was broken too, now fixed
- The Aug 12 diagnosis was incomplete. Thursday's 91-minute session found that beyond the
  expired invite, **the password reset flow itself failed with "invalid credentials,"** and
  clearing cache and cookies didn't help. Nine days after the first report, Andrew still
  could not get in.
- John repaired the reset email that afternoon and posted the working path to Andrew:
  login → "Forgot password?" → link in the fresh email → "You're almost in" → set a
  password → **2FA setup screen** → code → dashboard. Signup completion is on Andrew.
- Why it blocks more than Andrew: the lockout **prevents testing the new-lead automations**,
  including the workflow meant to answer Travis Payne.
- category: Platform, Tools, and Infrastructure
- source: Fathom recap 2026-08-13; Slack DM to Andrew 2026-08-13
- links: [[platform-tools-and-infrastructure#2026-08-12 CRM: Andrew locked out by a 24-hour invite expiry; Givebutter now flowing via API]]

## 2026-08-13 Welcome automation tested — routes a signup to their named community
- A test send from support@dudetalkdinners.org shows the new-lead welcome email working:
  "Hi Sam, Thanks for your interest in joining a Dude Talk Dinners community. **We saw your
  note about Idaho Springs and someone from that table will reach out soon** with details on
  the next dinner." The template picks up the community the person named and promises a
  local handoff — the automation the CRM lockout has been holding up.
- The daily digest the same morning reported real movement: "**1 email sent · 2 follow-ups
  created · 1 new user joined · 1 invite sent.**"
- category: Platform, Tools, and Infrastructure
- source: "[Test] Welcome to Dude Talk Dinners, Sam" + DTD reminders digest 2026-08-13

## 2026-08-13 Candid rejected the wrong document — it needs the EIN issuance or affirmation letter
- Candid will not accept a **letter of determination** for profile-manager verification
  "as it is a **publicly available document on the IRS site**... we require documents that
  are typically only available to authorized individuals of the organization." That is what
  Wednesday's reply actually contained, despite being labelled as the EIN letter.
- Only two documents work: the **EIN issuance letter** (the first letter the IRS sent after
  assigning the EIN) or an **IRS affirmation letter dated after 2000**. Replacements: IRS
  Business & Specialty Tax Line **800-829-4933** for the EIN letter, **800-829-3676** or
  IRS.gov/forms for an affirmation letter. Candid attached acceptable and non-acceptable
  examples.
- A "Welcome to Candid" email arrived the same morning, so the account exists — only the
  manage-profile permission is pending.
- action #open (John): locate the actual EIN issuance letter (CP 575) or request an
  affirmation letter, and resend
- category: Platform, Tools, and Infrastructure
- source: "Candid - Profile Permissions follow up" 2026-08-13
- links: [[platform-tools-and-infrastructure#2026-08-12 Candid profile claim in progress — identity verification requested]]

## 2026-08-14 Search Console: one more Events structured data issue
- A further alert: "your site is affected by **1 Events structured data issue(s)**" — on top
  of the 6 flagged Aug 9 and the duplicate-canonical problem from Aug 10. Three
  site-health notices in six days, all still unaddressed in the record.
- category: Platform, Tools, and Infrastructure
- source: Google Search Console email 2026-08-14
- links: [[platform-tools-and-infrastructure#2026-08-09 Search Console flags 6 Events structured data issues on dudetalkdinners.org]]

## 2026-08-12 CRM: Andrew locked out by a 24-hour invite expiry; Givebutter now flowing via API
- Root cause found for the auth-invite problem that's been open since Aug 5: the
  **Supabase invite link expires after 24 hours**, so Andrew's link was dead before he
  used it. Fix agreed: **set the expiry to 7 days and point the email templates at the
  auth-confirm route.**
- Real progress alongside it: **Givebutter donation data is now integrated via API**, and
  the CRM has a **Task Manager** Andrew will test once he's in. A "**CRM login and learn**"
  session was booked for Thu Aug 13, 10–11am to walk him through it.
- Other platform items from the same session: **verify the Givebutter account by SMS**;
  **complete the Candid nonprofit profile**; and Andrew to **fix a Google Workspace admin
  setting that is blocking google.com**.
- action #open (John): raise the Supabase invite expiry to 7d and repoint templates; SMS-
  verify Givebutter
- action #open (Andrew): fix the Workspace admin block and send John the steps
- category: Platform, Tools, and Infrastructure
- source: Fathom recap, "DTD Thank You email and donation receipts" 2026-08-12
- links: [[platform-tools-and-infrastructure#2026-08-05 CRM live: first activity digest, plus an auth-invite bug]]

## 2026-08-12 Candid profile claim in progress — identity verification requested
- Candid asked for more information "to verify your identity and affiliation with the
  organization" on John's request to manage DTD's **Candid nonprofit profile**; John sent
  the **IRS EIN Issuance Letter** two minutes later. The Candid profile is what funders
  check, so this is groundwork for the grant push.
- Incidental fact for context.md: John signed this one **"Chief Operating Officer"** —
  slightly different from the "Chief Operations Officer" on the July TechSoup email.
- category: Platform, Tools, and Infrastructure
- source: Candid support thread 2026-08-12

## 2026-08-12 Andrew's AI tooling: WhisperFlow, Claude Opus, and a plan to train on DTD's voice
- From the same session: Andrew installed **WhisperFlow** for voice-to-text, will use
  **Claude's Opus model** for planning and concept generation, and the stated future goal
  is to **train Claude on DTD's voice and style using past emails and meeting
  transcripts** — which is essentially what this vault accumulates.
- action #open (John): build a WhisperFlow voice profile for Andrew
- category: Platform, Tools, and Infrastructure
- source: Fathom recap 2026-08-12
- links: [[30-resources/ai-for-nonprofits-dpp-roundtable|AI for nonprofits — DPP roundtable]]

## 2026-08-12 CRM testing resumes: Brevo connector plus a dinner-announcement template
- Two test sends went out from **support@dudetalkdinners.org** — a third DTD sending
  address alongside idahospringsco@ and crm@:
  - "This is a test message from the DTD CRM **Brevo connector**."
  - A **dinner-announcement template** with structured **WHEN** and **WHERE** fields
    ("Tuesday, 8/12 at 12pm" / "Test place, Idaho Springs, CO 80452") and the footer
    "You're receiving this because you connected with us at a dinner or through our
    [site]." This is the reminder that went out manually on Aug 10 being turned into a
    templated send.
- category: Platform, Tools, and Infrastructure
- source: test sends from support@dudetalkdinners.org 2026-08-12
- links: [[platform-tools-and-infrastructure#2026-08-10 Reminder send had problems: four bounces and "a couple of issues along the way"]]

## 2026-08-11 Email signature template being trialled; TechSoup adds a second representative
- Ken sent John a "Signature test" using the placeholder DTD signature (Full Name / Title /
  Dude Talk Dinners / dudetalkdinners.org / name@dudetalkdinners.org) — the org is
  standardizing signatures, matching the branded blocks Andrew and John already use.
- TechSoup notified admin@dudetalkdinners.org that "**a new representative has been invited
  to act on behalf of your organization**," following Sunday's qualification.
- category: Platform, Tools, and Infrastructure
- source: "Signature test" 2026-08-11; TechSoup notification 2026-08-11
- links: [[platform-tools-and-infrastructure#2026-08-09 TechSoup validation came through — DTD is qualified for nonprofit offers]]

## 2026-08-10 Reminder send had problems: four bounces and "a couple of issues along the way"
- Monday's Idaho Springs reminder went out from **idahospringsco@dudetalkdinners.org** —
  DTD is sending per-community from dedicated addresses — and produced **four hard
  bounces**: kjboyl@gmail.com, indrehas64@gmail.com, ktbuy2@gmail.com, and
  dcakrendude@yahoo.com (550 5.1.1 / 552, "address not found"). The last is a near-twin of
  dcakrondude@yahoo.com, which is also on the list and delivered — a data-entry typo
  sitting in the list alongside the good address.
- John told Chris Gould he "had a couple of issues along the way" sending the reminders,
  and the send landed at 1:45pm for a 6pm dinner.
- action #open (John): clean the four dead addresses from the Idaho Springs list and
  de-dupe the dcakr*ndude pair; worth checking whether bounce handling is automated
- category: Platform, Tools, and Infrastructure
- source: mailer-daemon failures + "Re: Topic for tomorrow" 2026-08-10

## 2026-08-10 DMARC digest: 192 emails, 98% aligned — and ActiveCampaign is in the stack
- The Postmark DMARC weekly digest for dudetalkdinners.org (Aug 2–9): **192 emails
  processed, 98% SPF or DKIM aligned, 2% not aligned**. The named sending sources are
  **ActiveCampaign** and **Postmark** — two more pieces of the CRM/email stack alongside
  Brevo and Supabase, and evidence DMARC monitoring is already running.
- category: Platform, Tools, and Infrastructure
- source: Postmark DMARC weekly digest 2026-08-10
- links: [[platform-tools-and-infrastructure#2026-08-03 CRM stack partially confirmed: Brevo + Supabase]]

## 2026-08-09 TechSoup validation came through — DTD is qualified for nonprofit offers
- TechSoup: "Your organization has been validated to receive offers through TechSoup.
  Requests that have already been placed will be processed within three business days."
  This closes the validation John submitted Jul 29 and unlocks discounted/donated
  software (the same channel as Google for Nonprofits) for the tooling build-out.
- Note the recipient: the notice went to **admin@dudetalkdinners.org**, so TechSoup's
  account lives on the admin alias rather than John's mailbox.
- category: Platform, Tools, and Infrastructure
- source: TechSoup "Your Organization Has Been Qualified" email 2026-08-09

## 2026-08-09 Second Search Console problem: pages dropped as duplicates
- A second Search Console alert, one day after the structured-data one: pages on
  dudetalkdinners.org "are not being indexed due to the following new reason: **Duplicate,
  Google chose different [canonical]**." Two indexing problems in two days on a site
  that's mid-refresh — the community pages are the likely surface, since they share a
  template.
- action #open (John): check canonical tags/duplicate URLs alongside the Events markup fix
- category: Platform, Tools, and Infrastructure
- source: Google Search Console email 2026-08-09
- links: [[platform-tools-and-infrastructure#2026-08-09 Search Console flags 6 Events structured data issues on dudetalkdinners.org]]

## 2026-08-09 Search Console flags 6 Events structured data issues on dudetalkdinners.org
- Google Search Console: "Search Console has identified that your site is affected by 6
  Events structured data issue(s)" for the dudetalkdinners.org property. Events markup is
  what makes dinners eligible for rich results in Google — worth fixing before the
  community/"find a dinner" pages get their refresh (site update was said to be "on track
  within the next 10 days").
- action #open (John): review the 6 Events structured-data errors and run validation
- category: Platform, Tools, and Infrastructure
- source: Google Search Console email 2026-08-09
- links: [[support-for-existing-communities#2026-08-06 Startup materials taking shape: facilitator guide, welcome video, site refresh]]

## 2026-08-08 New CRM sending address in use: crm@dudetalkdinners.org
- A password-reset email arrived **from crm@dudetalkdinners.org** — the first appearance
  of that address in the record. The CRM now has its own mailbox/sending identity
  alongside the Brevo transactional setup, which is the kind of thing that matters for
  deliverability and for the auth-invite flow Andrew got stuck on.
- category: Platform, Tools, and Infrastructure
- source: password-reset email 2026-08-08
- links: [[platform-tools-and-infrastructure#2026-08-05 CRM live: first activity digest, plus an auth-invite bug]]

## 2026-08-05 CRM live: first activity digest, plus an auth-invite bug
- The daily reminders digest reported real activity for the first time: "2 new contacts
  (1 from the website form) · 1 text sent, **1 failed** · 2 new opt-outs, 2 revoked."
- Andrew hit a snag on the Supabase auth invite: "The link sends me to a login page. Did
  you create credentials for me?" — invite flow needs fixing before other users onboard.
- action #open (John): fix the CRM invite/credentials flow for Andrew; look at the failed SMS
- category: Platform, Tools, and Infrastructure
- source: CRM digest + Andrew's "You've been invited" reply 2026-08-05

## 2026-08-04 Website review session with Ken; test site already influencing copy
- John and Ken Farber held a 45-minute Website Review (2:15–3:00pm MT) working from
  Ken's "DTD Test Website Notes." Notably, Ken's proposed mission statement came
  straight off **John's test update to the site** ("One aim… to put a seat at the table
  within reach of every Dude possible") — the site work is feeding the board's
  mission/vision debate.
- category: Platform, Tools, and Infrastructure
- source: calendar event + Ken's Mission/Vision email 2026-08-04
- links: [[governance-and-org-development#2026-08-04 Mission & Vision debate: "walks" challenged; two new candidates]]

## 2026-08-03 CRM stack partially confirmed: Brevo + Supabase
- Brevo alerted that a new SMTP key named **supabase-auth-invites** was created in the
  DTD account — direct evidence the CRM pairs **Brevo** (transactional email) with
  **Supabase** (auth/database), consistent with the custom /app/ dashboards. The Zoho
  question from the Jul 20 meeting title remains open.
- category: Platform, Tools, and Infrastructure
- source: Brevo account alert 2026-08-03
- links: [[platform-tools-and-infrastructure#2026-07-22 DTD CRM build in active testing (Brevo email connector, reminders digest)]]

## 2026-08-02 Google for Nonprofits: DTD verified; Workspace activation requested
- Google confirmed "Your organization has been verified!" (Aug 2 evening), closing the
  Goodstack verification/documentation loop that had been open since Jul 30. A Google
  **Workspace for Nonprofits activation request** for dudetalkdinners.org was received
  Aug 3 morning — awaiting activation. This is the free-Workspace saving flagged at the
  Leadership Circle as a 501(c)(3) benefit.
- action #done (John): Goodstack verification + documentation
- category: Platform, Tools, and Infrastructure
- source: Google for Nonprofits emails 2026-08-02/03

## 2026-07-31 Website review underway; Google for Nonprofits needs docs
- Ken shared "DTD Test Website Notes" (Google Doc, edit access for John) — feedback
  feeding the community-web-pages launch push (due ~Aug 9).
- Goodstack (processing the Google for Nonprofits application) asked John to upload
  documentation proving association with DTD. action #done — verified 2026-08-02.
- category: Platform, Tools, and Infrastructure
- source: Drive share + Goodstack emails 2026-07-31

## 2026-07-30 Google for Nonprofits application + CRM signup form in testing
- Google for Nonprofits application underway (Goodstack email verification step). The
  CRM's public signup form is live in testing — two test submissions captured name,
  email, phone, location, interest, and SMS consent, feeding /app/contacts.
- Per the Leadership Circle: John (Operations) owns the central tech stack; DTD Central
  is researching a central messaging platform (e.g. Discord) and building dedicated
  community web pages on the DTD Central site (John to launch all pages within ~10 days).
- category: Platform, Tools, and Infrastructure
- source: Goodstack email + CRM test submissions 2026-07-30; Fathom recap

## 2026-07-29 TechSoup account created; DTD validation docs submitted
- John registered DTD with TechSoup (discounted nonprofit software/resources), added the
  organization, and submitted the IRS 501(c)(3) determination letter with EIN 41-4806880
  for validation. Awaiting TechSoup approval.
- category: Platform, Tools, and Infrastructure
- source: TechSoup emails + John's validation reply 2026-07-29
- links: [[governance-and-org-development#2026-07-19 IRS approves 501(c)(3) status for Dude Talk Dinners, Inc.]]

## 2026-07-24 Telnyx messaging verification approved
- Telnyx accepted the ID verification for Telnyx Messaging and upgraded the account to
  verified level — SMS sending capability is now cleared for use.
- category: Platform, Tools, and Infrastructure
- source: Telnyx verification emails 2026-07-24

## 2026-07-23 Telnyx account upgraded to full (paid) — likely part of the CRM stack
- John's Telnyx account went freemium → full with a successful payment (receipt PDF not
  opened, amount unknown). Telnyx is a telephony/SMS API provider; alongside this week's
  Brevo-connector and reminders-digest tests it points to SMS capability in the CRM
  build — stack confirmation still pending in needs-clarification.
- category: Platform, Tools, and Infrastructure
- source: Telnyx upgrade + payment emails 2026-07-23
- links: [[platform-tools-and-infrastructure#2026-07-22 DTD CRM build in active testing (Brevo email connector, reminders digest)]]

## 2026-07-22 DTD CRM build in active testing (Brevo email connector, reminders digest)
- Two system-test emails from support@dudetalkdinners.org landed in John's inbox: a
  "DTD CRM test email" from the CRM's Brevo connector, and a "Your DTD reminders" daily
  digest test linking to /app/follow-ups and /app/calendar dashboards. Andrew is already
  asking for a CRM home for funding opportunities, and Monday's meeting with Patricia was
  titled "Zoho CRM setup and grant strategy" (Granola metadata — content not ingested).
  Exact stack to confirm — see needs-clarification.
- category: Platform, Tools, and Infrastructure
- source: test emails 2026-07-22; Granola meeting title 2026-07-20; Andrew's email 2026-07-22
- links: [[funding-and-financial-development#2026-07-22 Funding-opportunities prospect list received; where to track it?]]

## 2026-07-21 Standardizing DTD email signatures (Ken + John)
- Ken Farber built a Base64-HTML signature (with Gemini's help) injected into a Mac
  mailsig file; the logo renders when sent to an external (xfinity) address but not in
  Gmail. John previously built a signature for Andrew and finds Gmail difficult with
  signatures.
- action #open (John, due 2026-07-22): write up the approach used for Andrew and send it
  to Ken to test whether it works for a second person
- category: Platform, Tools, and Infrastructure
- source: "Signature file attempt" email thread 2026-07-21

## 2026-07-21 Mighty Networks Launch Plan active at $95/month
- Payment confirmed for the Dude Talk Dinners network: Launch Plan, billed monthly,
  $95.00 including taxes.
- category: Platform, Tools, and Infrastructure
- source: Mighty Networks payment-confirmation email 2026-07-21

## 2026-07-21 Granola can transcribe phone calls
- John shared with Andrew that Granola's phone icon captures phone calls exactly like
  meetings (background transcription).
- category: Platform, Tools, and Infrastructure
- source: Slack DM John→Andrew 2026-07-21
