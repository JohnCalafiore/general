---
area: Platform, Tools, and Infrastructure
updated: 2026-08-06
tags: [area]
---

# Platform, Tools, and Infrastructure

Standing area for Dude Talk Dinners — matches the Morning brief look-back category of
the same name. Ongoing facts, decisions, and developments that belong to this
responsibility but not to a specific dated project get logged here.

## Log

<!-- Newest first. One H2 per atomic entry (## YYYY-MM-DD Short title) with a source
     line, so entries can be linked as [[platform-tools-and-infrastructure#...]] and harvested by the brief. -->

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
