---
area: Funding and Financial Development
updated: 2026-08-24
tags: [area]
---

# Funding and Financial Development

Standing area for Dude Talk Dinners — matches the Morning brief look-back category of
the same name. Ongoing facts, decisions, and developments that belong to this
responsibility but not to a specific dated project get logged here.

## Log

<!-- Newest first. One H2 per atomic entry (## YYYY-MM-DD Short title) with a source
     line, so entries can be linked as [[funding-and-financial-development#...]] and harvested by the brief. -->

## 2026-08-23 A $1,000 DAF grant is waiting on DTD sending an EIN — and a $500 reimbursement
- **Mark** (msd27611@gmail.com), described by Andrew as "**one of the guys in my men's
  group**," is ready to complete a pledge: "please do resend [the EIN] along with the
  address attached to it and I'll then, as we previously arranged, be able to **make a $1K
  grant from my Fidelity Charitable Gift Fund** and you then **reimburse me for the $500 cash
  advance I sent a number of weeks ago**."
- Two things to notice. First, a **donor-advised fund gift** is DTD's first — the DAFpay
  documentation John shared on Aug 17 is suddenly relevant. Second, the **$500 already sent**
  needs reimbursing, which is an accounting action, not just a thank-you.
- Andrew's ask of John: "Let's talk about this tomorrow or Tuesday if possible, and also
  **decide on a process to get thank you emails out**" — the acknowledgment layer built on
  Aug 12 still isn't operating.
- action #open (John/Andrew): send Mark the EIN and mailing address; arrange the $500
  reimbursement; agree the thank-you process
- category: Funding and Financial Development
- source: "Fwd: Re: We just got our 501(c)(3) - Balance of my pledge" 2026-08-23
- links: [[funding-and-financial-development#2026-08-07 Donation receipts and thank-you emails get a working session]]

## 2026-08-23 Givebutter verification hits a final reminder — three days to act
- "This is your **final reminder** to log in to your Givebutter dashboard and complete the
  required action to continue your verification. **If you do not finish this step within 3
  days**..." The verification flagged as "optional" on Aug 19 now carries a deadline, and
  Givebutter is the rail the whole tiered community-fundraising plan runs on.
- action #open (John, by ~Aug 26): finish Givebutter verification
- category: Funding and Financial Development
- source: "[Final Reminder] Finish Givebutter Verification" 2026-08-23
- links: [[funding-and-financial-development#2026-08-19 Givebutter moves payouts to Wallet; verification still unfinished]]

## 2026-08-22 The grant scanner is live — first sweep names Elevance as a 4/5 fit
- John built and ran the **DTD Grant & Fundraiser Finder**, an automated opportunity
  scanner writing into a **`discovered_opportunities` table in Supabase** for review in the
  CRM. **Weekly scans run automatically every Monday at 10am**, deduped and incremental —
  this is the "custom AI bot to score and prioritize grants" from Thursday, built two days
  later.
- Seed sweep results:
  - **Elevance Health Foundation, Behavioral Health Grant Program — fit 4/5.** Opens **Jan 1,
    deadline Jan 31 2027**, 1–3 year grants. It "**explicitly names reducing loneliness among
    people with mental health/SUD conditions** as a program goal — close to a direct match
    for DTD's mission." Catch: the local track covers only 10 states (not Colorado), so DTD
    would apply under "**national programs demonstrating scalable change**." Note this is
    almost certainly the "Elevents Health" Trip Starkey mentioned on Aug 14 — same January
    cycle.
  - **Humana Foundation, Connected Healthy Lives — fit 3/5**, opens Q1 2027. The foundation
    "just announced **$12.2M in new emotional-health/senior-loneliness grants**," though that
    round is awarded. Action: **register on their portal now**.
  - **DOJ Office on Violence Against Women FY2026 — fit 2/5, deadline Sep 8 2026.** Notable
    for a fact new to the vault: "**DTD's new SAM.gov registration clears the
    federal-application hurdle**." Scored low deliberately — "**flagging rather than
    force-fitting, per the opioid-RFA lesson**."
- Screened out and stored so they don't resurface: **Movember** (England-only) and **The
  Greater Sum** pitch competition (incubator alumni only). The federal sweep returned mostly
  **NIH R01/R34 research grants** DTD has no infrastructure for, and GivingTuesday/corporate
  matching turned out to be **donor-education tactics, not applications** — worth revisiting
  as a December campaign tactic.
- action #open (John): review/promote the three open items in the CRM; **calendar the
  Elevance (Jan 1–31 2027) and Humana (Q1 2027) windows**
- category: Funding and Financial Development
- source: "DTD Grant & Fundraiser Finder — Seed Sweep" 2026-08-21
- links: [[funding-and-financial-development#2026-08-20 DECISION: add a grant writer and pivot from government grants to private foundations]], [[partnerships-and-strategic-relationships#2026-08-14 Trip's two leads: a pro bono lawyer route and the Elevents Health grant cycle]]

## 2026-08-21 Board adopts the fundraising strategy — with numbers attached
- The board signed off on the multi-pronged plan and put figures on it:
  - **Family foundations** are the primary early target, sized at **$50k–$75k donations**.
  - **Individual asks** through 1:1 meetings, sourced from board and facilitator networks.
  - **Grant co-writing** with community organizations.
  - **Year-end campaign** for **Colorado Gives Day and Giving Tuesday**, with a specific
    mechanic: **default Givebutter to monthly** to build recurring donors.
  - **Social media**: organic campaigns and **media appearances (podcasts, news) over paid
    ads**.
- New channel, new revenue model: **corporate training at $5k–$10k per engagement** for
  companies — construction and **law enforcement** named — to build internal programs. Plus
  local employer asks (**Kramer, Henderson Mine**) and one memorable target: "**Ideal
  Sponsor: Ken will approach DudeWipes.**"
- action #open (Ken): contact **Nick Williams** to kickstart corporate training
- action #open (Andrew): meet Justin to plan the grassroots monthly donor campaign; call
  **Nadia and Allison** for their view on a centralized financial model
- category: Funding and Financial Development
- source: Fathom recap, "DTD Board Meeting 3rd Friday" 2026-08-21
- links: [[funding-and-financial-development#2026-08-18 DECISION: fundraising strategy set — Andrew to ~90% fundraising, foundations first]]

## 2026-08-20 DECISION: add a grant writer and pivot from government grants to private foundations
- Two days after the fundraising strategy session, the budget adds a **second hire: a grant
  writer role**, to raise application capacity against "**a robust pipeline of foundation
  grants**" that's been identified.
- The strategic reasoning is a genuine shift: move **away from government grants, "which may
  be drying up," toward private foundations**. That squares with the Aug 18 view of
  foundations as efficient "giving businesses," and it changes what DTD chases after the
  RMCP federal grant.
- Tooling to match: "**a custom AI bot is being built to score and prioritize grants by
  application deadline**" — the practical version of the AI-for-outreach plan.
- This is the **one material budget change being announced to the board** on Friday.
- action #open (John): follow up with **Jennifer Ashley (Vibrant.org, JXA Advisors)** for
  potential strategic guidance
- category: Funding and Financial Development
- source: Fathom recap, "DTD Budget review" 2026-08-20 (fathom.video/calls/791797417)
- links: [[funding-and-financial-development#2026-08-18 DECISION: fundraising strategy set — Andrew to ~90% fundraising, foundations first]], [[funding-and-financial-development#2026-08-12 DECISION: budget a $52k Year 1 Fundraising Manager against a 3x ROI target]]

## 2026-08-20 Greg agrees to the accounting call — evenings, via a scheduler link
- "Yeah, not a problem. **Evenings are probably easiest for me, but I'll see your scheduler
  link when you send it.**" The pass-through-vs-centralized accounting question now has a
  conversation booked in principle; Andrew owes him a Cal.com link.
- action #open (Andrew): send Greg a Cal.com link for an evening slot
- category: Funding and Financial Development
- source: "Re: DTD - Accounting question" 2026-08-20
- links: [[governance-and-org-development#2026-08-20 DECISION: present the budget high-level to the board and defer accounting to a CPA]]

## 2026-08-19 Givebutter moves payouts to Wallet; verification still unfinished
- Three Givebutter changes in half an hour: **phone 2FA enabled** on John's account, the
  **Givebutter Wallet is live** and "**we've automatically updated your Payout**" settings
  so donations now flow to the Wallet rather than straight to the bank, and a standing
  prompt: "**[Action Required] Finish Givebutter Verification** ... Verification is optional
  and not required to fundraise."
- Worth attention because the fundraising plan leans on Givebutter for **per-community
  campaign pages** (Clear Creek, Silverthorne, BV, Grand Junction) — payout routing and
  verification status affect how community money actually lands.
- action #open (John): finish Givebutter nonprofit verification; confirm the Wallet payout
  change is what DTD wants
- category: Funding and Financial Development
- source: Givebutter notifications 2026-08-19
- links: [[funding-and-financial-development#2026-08-18 DECISION: community fundraising goes tiered — struggling communities keep what they raise]]

## 2026-08-19 Final budget session booked for Thursday, the day before the board
- Andrew scheduled "**DTD Budget review**," **Thu Aug 20, 3–4pm MDT** with John — the last
  working session before the board sees the budget Friday morning. That makes three budget
  conversations in three days (CP Tuesday, this one Thursday, board Friday).
- category: Funding and Financial Development
- source: calendar invitation 2026-08-19
- links: [[governance-and-org-development#2026-08-17 Board meeting confirmed: Fri Aug 21, 10–11:30am — packet circulated]]

## 2026-08-18 DECISION: fundraising strategy set — Andrew to ~90% fundraising, foundations first
- The Andrew/Ben session (56 min, John present) produced the prioritized plan the budget has
  been implying. **Fundraising is the top priority and Andrew will spend ~90% of his time on
  it** — the operational version of the 70–90% budget allocation agreed Aug 10.
- Priority order: **individual donors** for immediate cash, **family foundations** for the
  highest upside. The reasoning on foundations is worth keeping: they are "**giving
  businesses** with clear processes, making them **more efficient targets than individual
  donors**." Tactic — find the named contact at each foundation and email directly, **linking
  DTD's NPR/CPR articles**, to land an intro call.
- Where the individual donors come from: Andrew will **call every board member** for
  introductions to their networks, and ask **passionate facilitators** for their contacts.
- A **5–7 minute pitch deck** goes to Friday's board meeting, doubling as Andrew's practice
  run and as a concrete ask of the board.
- Andrew will **use AI to build corporate-giving and family-foundation contact lists** for
  fast targeted outreach.
- category: Funding and Financial Development
- source: Fathom recap, "Andrew : Ben (DTD fundraising)" 2026-08-18
  (fathom.video/calls/789674484)
- links: [[funding-and-financial-development#2026-08-10 DECISION: budget restructured — cash expense lines, and Andrew re-cast as 70–90% fundraising]]

## 2026-08-18 DECISION: community fundraising goes tiered — struggling communities keep what they raise
- The delicate question — whether communities should raise money for DTD Central — got a
  clear answer: **a tiered, case-by-case approach using Givebutter campaigns.**
  - **Struggling communities (e.g. Buena Vista)**: given the Givebutter platform as a tool
    to **fundraise for their own dinners**.
  - **Stable communities (e.g. Bailey)**: asked to **fundraise for DTD Central**, framed as
    supporting the national mission.
- On fiscal sponsors, Andrew will hold **transparent conversations** with **All Access
  Wellness (Bailey)** and **Building Hope Summit (Nadia)** to agree a collaborative approach
  rather than competing for the same local dollars.
- The **Community Support Fund** gets a second rationale beyond sustainability: as a budget
  line it "allows DTD to raise funds beyond its immediate operational needs, **preventing
  the appearance of being 'overfunded' to donors**."
- action #open (John): set up Givebutter pages for **Clear Creek, Silverthorne, BV, Grand
  Junction** and share QR/links; schedule fundraising calls with BV, Grand Junction,
  Gunnison, CP, Bailey/Conifer and Summit; email **Allison (All Access Wellness)** and
  **Nadia (Building Hope)**
- category: Funding and Financial Development
- source: Fathom recap, "Andrew : Ben (DTD fundraising)" 2026-08-18
- links: [[funding-and-financial-development#2026-07-30 Buena Vista funding gap — the test case for community funding]]

## 2026-08-18 Four more channels opened: co-granting, corporate lunch-and-learns, year-end, merch
- **Co-written grants**: partner with established 501(c)(3)s such as **Resilience 1220** to
  "leverage their history for a higher success rate" — action to email **Erica at
  Resilience**. The framing behind it is a keeper: "**DTD is a 'gateway to therapy,' not a
  competitor**," which makes referrals, co-grants and sponsorships natural with Man Therapy
  and Resilience alike.
- **Corporate giving**: lower priority, pursued for sponsorships and as an indirect route to
  well-off individuals in leadership. Tactic — offer a "**lunch and learn**" that **models a
  DudeTalk conversation** rather than pitching at employees.
- **Year-end**: a coordinated campaign for **Colorado Gives Day and Giving Tuesday**; Andrew
  to call Colorado Gives about their platform and matching-fund model.
- **Merch**: "a low-effort, high-potential idea (e.g. a catchy t-shirt)" at roughly **5% of
  time**.
- category: Funding and Financial Development
- source: Fathom recap, "Andrew : Ben (DTD fundraising)" 2026-08-18
- links: [[partnerships-and-strategic-relationships#2026-08-14 DECISION: Man Therapy will promote DTD — a tile and a blog post, no "partner" language]]

## 2026-08-18 Principal Business is a $50k seed application — with a stated mission-fit doubt
- The clearest description yet: "**A $50k seed funding application to Principal Business is
  pending, but the group's 'capitalist' nature may not align with DTD's mission.**" So the
  amount is $50,000, it is submitted and awaiting a decision, and the room already has
  reservations about the funder.
- category: Funding and Financial Development
- source: Fathom recap, "Andrew : Ben (DTD fundraising)" 2026-08-18
- links: [[funding-and-financial-development#2026-08-17 RESOLVED: "Principled Business" is a grant application, and it's being submitted]]

## 2026-08-18 Budget review with Chris Peterson held ahead of the board meeting
- The 3:00–3:30pm call happened, arranged by email the same morning after CP's note that
  she'd reviewed **v8** and "overall the main budget looks good." **Neither Granola nor
  Fathom captured it**, so her questions and whatever they resolved are not in the vault —
  three days before the board sees the budget.
- category: Funding and Financial Development
- source: "Budget discussion" thread + calendar 2026-08-18; absence of meeting capture
- links: [[funding-and-financial-development#2026-08-17 Chris Peterson is reviewing budget v8 — "the main budget looks good"]]

## 2026-08-17 Walmart Spark Good Local: a per-chapter grant strategy, $250–$5,000 a time
- Andrew's ED update explains what the "Walmart SPARK Grant" work actually is: DTD is
  **registering for local Walmart Spark Good Local grants** — "**small ($250–$5,000) cash
  grants that local Walmart, Sam's Club, and Distribution Center facilities award to nearby
  501(c)(3)s** based on mission fit, trust, and community impact."
- The strategy is the interesting part and it fits the Community Support Fund thinking
  exactly: "**since each Walmart facility gives locally, a DTD chapter could apply to the
  Walmart or Sam's Club nearest that community for a grant to cover dinner costs**" — many
  small, accessible grants rather than one central ask.
- category: Funding and Financial Development
- source: Andrew's ED update, #executive-director-updates 2026-08-17
- links: [[funding-and-financial-development#2026-08-10 DECISION: a "Community Support Fund" replaces the assumption that in-kind donations last]]

## 2026-08-17 RESOLVED: "Principled Business" is a grant application, and it's being submitted
- Andrew lists it under Finance and Fundraising: "**Principled Business Grant Application
  in process of submission**." So the Aug 10 budget session was preparing a **grant
  application**, not a partner presentation — which is why the budget had to be defensible
  line by line.
- Also restated: DTD is a **subgrantee on the opioid abuse prevention grant alongside RMCP,
  "written in for $50k/year for 3 years"** — the $150k figure from July, confirmed in
  Andrew's own words.
- category: Funding and Financial Development
- source: Andrew's ED update, #executive-director-updates 2026-08-17
- links: [[funding-and-financial-development#2026-07-30 RMCP submitted the opioid-response grant: $150K to DTD if won]]

## 2026-08-17 Chris Peterson is reviewing budget v8 — "the main budget looks good"
- CP replied on the pre-board budget conversation: "I've been **reviewing v8 of the budget**
  and have some questions, but **overall the main budget looks good**." She offered
  **Tue 3–4pm, or Wed 12–1 or 2:45–3:15** — her week is tight ahead of Friday's board
  meeting.
- action #open (John): take one of CP's slots before Friday
- category: Funding and Financial Development
- source: "Budget discussion" email from Chris Peterson 2026-08-17
- links: [[governance-and-org-development#2026-08-17 Board meeting confirmed: Fri Aug 21, 10–11:30am — packet circulated]]

## 2026-08-15 First recurring donor: Michael Davis, $100/month
- Givebutter: "**Michael Davis** just supported your campaign 🎉 Michael made their **1st
  monthly donation for a total of $100.00**." This is the **first recurring gift in the
  record** — $1,200/year if it holds — and it arrives days after the donation
  acknowledgment layer was built and the PayPal/Givebutter rails were finished.
- John forwarded it to Andrew ("FYI in case you didn't receive this"), who asked back:
  "**Its from the Dude Central campaign, right? Do you know who this is?**" — neither knows
  the donor, so the attribution question is open (see needs-clarification).
- action #open (John/Andrew): identify Michael Davis and thank him — Givebutter's own
  prompt is "Say thanks by replying to this email"
- category: Funding and Financial Development
- source: Givebutter notification + forward and Andrew's reply 2026-08-15
- links: [[funding-and-financial-development#2026-08-07 Donation receipts and thank-you emails get a working session]]

## 2026-08-14 Budget update for the board: contract fundraiser plus a sustainability reserve fund
- John's own summary of where the budget landed: "Latest iteration of budget updated and
  **progress will be shared at the board meeting**. Notable updates include **adding a
  fundraising position (contract) in year 1**, **adding a sustainability reserve fund that
  takes surplus funds and allocates them to supporting communities**, and general
  streamlining of budget format."
- Two things this pins down: the $52k fundraiser is budgeted as a **contract** role, and
  the "Community Support Fund" concept from Aug 10 now exists in the document as a
  **sustainability reserve fund fed by surplus** — a mechanism, not just an aspiration.
- category: Funding and Financial Development
- source: John's board-report draft, Slack DM to Andrew 2026-08-14
- links: [[funding-and-financial-development#2026-08-10 DECISION: a "Community Support Fund" replaces the assumption that in-kind donations last]], [[funding-and-financial-development#2026-08-12 DECISION: budget a $52k Year 1 Fundraising Manager against a 3x ROI target]]

## 2026-08-14 New grant lead: Elevents Health foundation, cycle opens January
- Trip Starkey's funding suggestion in the Man Therapy call — apply to the **Elevents
  Health foundation grant cycle**, which **opens in January**. Noted against DTD's stated
  need for operating funds "and to pay its founders."
- action #open: put the Elevents Health cycle on the grant calendar for January
- category: Funding and Financial Development
- source: Fathom recap, "DTD : Man Therapy" 2026-08-14
- links: [[partnerships-and-strategic-relationships#2026-08-14 Trip's two leads: a pro bono lawyer route and the Elevents Health grant cycle]]

## 2026-08-14 PayPal Giving Fund enrollment confirmed
- "We're excited to welcome **Dude Talk Dinners, Inc to PayPal Giving Fund**" — the day
  after charity status and the 1.99% rate were confirmed. Giving Fund listing exposes DTD
  to PayPal/eBay-driven donation surfaces beyond its own checkout.
- category: Funding and Financial Development
- source: PayPal Giving Fund welcome email 2026-08-14
- links: [[funding-and-financial-development#2026-08-13 PayPal charity status confirmed — reduced rate of 1.99%, Venmo now available]]

## 2026-08-14 Second DPP session offered: AI for donor outreach, Tue Aug 18
- Louis Diez invited John to an "**AI Practice Session: Prospect Strategy at Scale — Using
  AI to Build and Personalize Donor Outreach Plans**," Tue Aug 18, 11am–12pm MDT on Zoom.
  A hands-on follow-up to the Aug 12 roundtable; no registration in the record yet.
- category: Funding and Financial Development
- source: Luma invitation 2026-08-14
- links: [[30-resources/ai-for-nonprofits-dpp-roundtable|AI for nonprofits — DPP roundtable]]

## 2026-08-13 PayPal charity status confirmed — reduced rate of 1.99%, Venmo now available
- "Congratulations! **The charitable status of your account has been confirmed. You'll now
  get our reduced rate of 1.99%**" — closing the action open since Aug 3 and cutting the
  processing cost on every PayPal donation. PayPal also invited DTD to **create a Venmo
  charity profile**, a third donation rail alongside PayPal and Givebutter.
- action #done (John): confirm PayPal charity status
- action #open (John/Andrew): decide whether to add a Venmo charity profile
- category: Funding and Financial Development
- source: "You're a PayPal confirmed charity" + Venmo invitation 2026-08-13
- links: [[funding-and-financial-development#2026-08-03 PayPal account live and verified for DTD]]

## 2026-08-13 Budget review with Ken finally happened — no content captured
- Ken **accepted the rescheduled Thursday slot** (shortened to 11:30am–12:00pm) two hours
  before it ran, after declining the earlier version. Neither Granola nor Fathom captured
  it, so what the budget landed on before the board meeting still isn't in the vault.
- category: Funding and Financial Development
- source: calendar acceptance 2026-08-13; absence of meeting capture
- links: [[funding-and-financial-development#2026-08-12 Budget follow-up stalled: Ken declined Thursday's session, nothing rebooked]]

## 2026-08-12 DECISION: budget a $52k Year 1 Fundraising Manager against a 3x ROI target
- The 116-minute Wednesday session named the underlying problem plainly — "**we lack
  dedicated fundraising capacity**" — and answered it with a **Fundraising Manager line of
  $52,000 for Year 1**: 10 hrs/week at $100/hr, scoped to **broad fundraising (grants,
  campaigns, corporate giving), not just grant writing**. The bar set for the hire is a
  **3x ROI — $156k raised** — to justify the investment.
- This is the second major budget decision in three days and it goes into the same
  document heading to the board: Andrew re-cast at 70–90% fundraising, now with a paid
  fundraiser beneath him.
- action #open (John): add the $52k Y1 fundraising-manager line to the budget and send to
  Andrew
- category: Funding and Financial Development
- source: Fathom recap, "DTD Thank You email and donation receipts" 2026-08-12
  (fathom.video/calls/780168206)
- links: [[funding-and-financial-development#2026-08-10 DECISION: budget restructured — cash expense lines, and Andrew re-cast as 70–90% fundraising]]

## 2026-08-12 DECISION: GrantStation via TechSoup ($200/yr) as the interim grant engine
- Until a fundraiser is hired, DTD will **buy a one-year GrantStation membership through
  TechSoup for $200** — the first concrete use of the TechSoup qualification that landed
  Aug 9. Rationale from the room: it "**builds internal capacity and finds targeted grants
  for new 501(c)(3)s**." The intended workflow is to **use the platform to identify
  prospects, then contract a writer for specific proposals** — cheaper than retaining a
  consultant to do both.
- action #open (John): purchase the GrantStation membership
- category: Funding and Financial Development
- source: Fathom recap 2026-08-12
- links: [[platform-tools-and-infrastructure#2026-08-09 TechSoup validation came through — DTD is qualified for nonprofit offers]]

## 2026-08-12 Walmart SPARK Grant submitted — stalled on a 3-day bank verification
- The application **is in**, held up only by bank verification: Andrew supplied a **Chase
  bank statement to John by text** ("for security"), and the platform's **3-day
  verification** is pending. This closes the loop on the Aug 12 working session, which
  itself produced no recording.
- category: Funding and Financial Development
- source: Fathom recap 2026-08-12
- links: [[funding-and-financial-development#2026-08-07 "Spark Grant" identified: Walmart SPARK Grant, session Wed Aug 12]]

## 2026-08-12 Grant-readiness consultant on the table: Knudsen Coaching & Consulting
- **Daniel Knudsen** (Knudsen Coaching & Consulting, "Let's Do Good Well™," Colorado
  Certified Prevention Specialist II) met Andrew Mon Aug 10 and followed up with two
  deliverable samples, which Andrew forwarded to John: a **Grant Ready Checklist** and a
  **Grant Landscape Survey** sample. On the survey: "the sample shows 2 opportunities so
  you can get an idea of the detail... For our last few landscape survey clients, **the
  number of opportunities has ranged from eight up to 20.** It's highly dependent on the
  organization's mission and alignment with funders."
- The introduction came from **Gina Moran**, a nonprofit consultant who has been informally
  advising Andrew: "Andrew asked today about grant writing and I shared that **KC&C would
  be a great resource, even if it's just to do some consulting around grant readiness**."
- Now a third route to grant capacity alongside GrantStation and Amanda Kearney-Smith
  (Patricia Markwell's recommendation) — no decision in the record.
- action #open (Andrew/John): decide whether to engage KC&C, and how it fits with
  GrantStation and the planned fundraising hire
- category: Funding and Financial Development
- source: "Fwd: Introduction" thread forwarded by Andrew 2026-08-12
- links: [[relationships#Daniel Knudsen]], [[relationships#Gina Moran]], [[partnerships-and-strategic-relationships#2026-07-20 Grant platform meeting with Patricia Markwell (RMCP)]]

## 2026-08-12 Budget follow-up stalled: Ken declined Thursday's session, nothing rebooked
- Tuesday's 12:30–2pm Budget Review with Ken went ahead but **left no captured content**
  (no Granola recording, no Fathom recap), so whatever was settled isn't in the vault.
  John then created a **second Budget Review for Thu Aug 13, 11am–12** and Ken **declined
  it within the hour**; no replacement time is on the calendar. John instead holds a
  three-hour unlabeled "block" Thursday afternoon.
- This matters because the refined budget is due to the board meeting that sets the
  employment tranches.
- action #open (John): rebook the budget session with Ken, or confirm the work is done
- category: Funding and Financial Development
- source: calendar events + Ken's decline 2026-08-11; absence of meeting capture
- links: [[governance-and-org-development#2026-08-10 Board meeting will set "tranches" — the benchmarks that trigger Andrew's and Ken's employment]]

## 2026-08-12 John attended the DPP roundtable on AI and nonprofit fundraising
- John registered Aug 11 and attended the **Donor Participation Project** roundtable "AI
  and the Future of Nonprofit Work" (Wed Aug 12, 10–11am MDT, Zoom) — the session Andrew
  forwarded on Aug 10. Panel: **Gayle Roberts, Remy Reya, and Paul Roach**, hosted by
  Louis Diez, on "how **fundraising teams** are adapting to AI... how teams are actually
  using these tools today, where adoption is going wrong."
- No takeaways are in the record; if anything from it should shape DTD's tooling or
  fundraising approach, it isn't captured yet.
- category: Funding and Financial Development
- source: Luma registration, reminder, and post-event email 2026-08-11/12

## 2026-08-10 DECISION: a "Community Support Fund" replaces the assumption that in-kind donations last
- At the 92-minute "Budget for Principled Business" session (Andrew, Ken, John), the
  central call was that **the current budget model is unrealistic** — local in-kind food
  and space donations reliably fall off after a few months. Evidence cited in the room:
  **Idaho Springs now pays $400/month for food.**
- Decided: create a **Community Support Fund** that covers those cash costs as communities
  mature, scaling with the number of communities — **$100k (Y1) → $250k (Y2) → $500k
  (Y3)**. The stated goal is that **no community launches without a clear, sustainable
  funding plan**, and the fund doubles as a credibility signal to donors.
- This is the structural answer to the Buena Vista funding crunch: instead of solving one
  community's $700 gap ad hoc, DTD budgets for the pattern.
- category: Funding and Financial Development
- source: Fathom recap, "Budget for Principled Business" 2026-08-10 (fathom.video/calls/777309313)
- links: [[funding-and-financial-development#2026-07-30 Buena Vista funding gap — the test case for community funding]]

## 2026-08-10 DECISION: budget restructured — cash expense lines, and Andrew re-cast as 70–90% fundraising
- Specific changes agreed for the budget presented to Principal Business:
  - Revenue line renamed from "Food and Location Donations" to the standard **"Food and
    Event Space In-Kind Donations."**
  - New expense lines for real cash costs: **"DudeCentral Dinner Expense"** and
    **"DudeCentral Event Space Expense."**
  - **Andrew's personnel allocation reallocated to 70–90% fundraising**, 10–30% program
    services/admin — the budget now states on its face that fundraising is the top
    priority, which was described as a stronger narrative for donors.
  - In-kind projections revised down to match the new cash model.
- Presentation strategy: show a high-level budget, but be able to speak to any line
  without opening the document.
- action #open (John): create a sandbox copy of the budget; make all of the above edits;
  add the Community Support Fund, tranches, and Y1–3 assumptions; send to Andrew and Ken
- action #open (John): email the Principal Business budget PDF to Andrew, who then preps
  Q&A with Chris Peterson
- action #done (John): send Ken the invite for the Tue Aug 11 12:30 working session
- category: Funding and Financial Development
- source: Fathom recap, "Budget for Principled Business" 2026-08-10

## 2026-08-10 Budget Review booked Tue Aug 11, 12:30–2pm — the finalizing session
- John created the follow-up working session immediately after Monday's meeting; **Ken
  Farber accepted, Andrew is not on the invite**. This is the "finalize the budget before
  the board meeting" step from the recap.
- category: Funding and Financial Development
- source: calendar event created 2026-08-10; Ken's acceptance 2026-08-10
- links: [[funding-and-financial-development#2026-08-10 DECISION: budget restructured — cash expense lines, and Andrew re-cast as 70–90% fundraising]]

## 2026-08-07 "Spark Grant" identified: Walmart SPARK Grant, session Wed Aug 12
- Andrew scheduled a **Walmart SPARK Grant** working session (Wed Aug 12, 12–1pm MDT,
  John invited) — this names the unidentified "Spark Grant application" block from Aug 3.
  It matches the Leadership Circle strategy of applying to large retailers
  (Walmart/Target) for community grants to fund local dinners.
- category: Funding and Financial Development
- source: calendar invitation 2026-08-07
- links: [[funding-and-financial-development#2026-07-30 Buena Vista funding gap — the test case for community funding]]

## 2026-08-07 Donation receipts and thank-you emails get a working session
- "DTD Thank You email and donation receipts" scheduled Wed Aug 12 (originally
  11am–12:30, revised to **11am–12pm**) — building the acknowledgment layer now that
  PayPal and Givebutter are live and all donations are tax-deductible (receipts are a
  501(c)(3) requirement for donors).
- category: Funding and Financial Development
- source: calendar invitation + update 2026-08-07
- links: [[funding-and-financial-development#2026-08-03 PayPal account live and verified for DTD]]

## 2026-08-06 Gilpin BoCC invites a 2027 county funding application
- Jamie Fanselow: the **Gilpin Board of County Commissioners** "have taken quite a bit of
  interest in DTDs" and **encouraged her to apply to their Gilpin County Community
  Funding for 2027** — county-level backing beyond the HHS/Public Health money she
  already secured.
- action #open (Jamie): apply for Gilpin County Community Funding 2027
- category: Funding and Financial Development
- source: Jamie Fanselow's email in the Weld thread 2026-08-05 (received 08-06)

## 2026-08-04 Dawson Wolf drafting a fundraising script
- **Dawson Wolf** shared a Google Doc, "Fundraising script rough draft," with John for
  editing (cc Andrew) — the day after joining the BV fundraising and sustainability
  call. First appearance of his full name; he is now producing fundraising material for
  DTD (role still unconfirmed — see needs-clarification).
- action #open (John): review/edit the fundraising script draft
- category: Funding and Financial Development
- source: Drive share notification 2026-08-04

## 2026-08-03 Budget Monday: six sessions, budget sent to Andrew, Spark Grant work
- The day ran: Spark Grant application 10:30–11, BV fundraising and sustainability
  11–12, Andrew/John budget review 11:30–1, DTD Budget Review 1–2 with Chris Peterson,
  Andrew:Ken 2:30–3, Mission Vision convo 3–4. John emailed Andrew the budget
  ("Budget attached") at 4:19pm. **A new "Spark Grant application" working session
  appeared on the calendar — a grant not previously in the record** (see
  needs-clarification). No meeting content was captured (no Granola recordings, no
  Fathom recaps), so decisions from these sessions aren't in the vault.
- category: Funding and Financial Development
- source: calendar events + sent mail 2026-08-03

## 2026-08-03 PayPal account live and verified for DTD
- A PayPal account for Dude Talk Dinners, Inc. was created, the JPMorgan Chase bank
  account confirmed by micro-deposits, and the account **verified with sending limits
  removed** — a second donation rail alongside Givebutter. PayPal is prompting to
  confirm charity status for the nonprofit discount rate.
- action #open (John): confirm PayPal charity status for the discounted rate
- category: Funding and Financial Development
- source: PayPal emails 2026-08-03

## 2026-08-04 CP suggests studying a members-club financial model for DTD budgets
- After the budget review, Chris Peterson flagged the **International Men's Club of
  America** (imcofa.com) — surfaced via a BHB partner's speaker referral — as a possible
  reference for "how we get DTD budgets and pass through a set up properly without too
  much headache." She's explicit that the club's model (paid membership, invitation
  only, men who travel internationally) is "not a model I at all like for DTD," but
  thinks the financial structure could point in the right direction. Asks whether Andrew
  or John wants to dig deeper.
- action #open (Andrew/John): decide whether to research the IMCofA financial model
- category: Funding and Financial Development
- source: "Another avenue to look into, maybe?" email from Chris Peterson 2026-08-04
- links: [[governance-and-org-development#2026-07-30 Liability: formal Community Agreement needed]]

## 2026-07-31 Workday Human Connection Microgrant application submitted at the wire
- Andrew submitted DTD's application to the **Workday Foundation Human Connection
  Microgrant Program** at 11:29 PM on deadline day (Jul 31, 11:59 PM PT cutoff).
  The program funds community organizations strengthening neighbors' social ties.
  **Decisions announced September 21.** Application on record: 501(c)(3), EIN
  41-4806880, mailing address PO Box 992, Idaho Springs, CO 80452; Andrew is primary
  contact; mission statement: "Dude Talk Dinners connects men in communities across
  Colorado and beyond - where friendships are built from meaningful conversation, free
  dinner, and a welcoming atmosphere."
- Two grant decisions now pending: this one (Sep 21) and the RMCP opioid-response grant
  (late September).
- category: Funding and Financial Development
- source: Google Forms receipt forwarded by Andrew 2026-08-01

## 2026-08-01 BV fundraising call set: Monday Aug 3, 11am–12pm
- "DTD BV fundraising and sustainability" — Andrew, John, Justin Hall, Erik Jacobsen,
  and Mike Mayer (Google Meet). This closes Andrew's action to schedule the BV
  fundraising call. Scheduling note: it overlaps the Andrew/John budget review
  (11:30–1:00) by 30 minutes.
- update 2026-08-03: **Dawson (dawsonjwolf03@gmail.com) was added to this invite** —
  his second appearance on a DTD meeting after the Jul 31 three-hour session, now on a
  fundraising/sustainability call (identity still unconfirmed — see needs-clarification).
- category: Funding and Financial Development
- source: calendar invitation 2026-08-01
- links: [[funding-and-financial-development#2026-07-30 Buena Vista funding gap — the test case for community funding]]

## 2026-07-30 RMCP submitted the opioid-response grant: $150K to DTD if won
- Patricia Markwell completed and submitted the **Community-Rooted Opioid Response
  Grant**: "Stronger Together: Rural Men's Opioid Prevention & Recovery Network," built
  on the RMCP–DTD partnership. DTD is the community engagement lead (outreach, chapter
  development, volunteer recruitment, partnerships, sustainability); RMCP handles
  project management, training, evaluation, and grant administration. The budget carries
  a **$50,000/year subcontract to DTD for each of three years — $150,000 total**.
- Outcome expected **late September**. Patricia is on maternity leave Aug 6 → Oct 2;
  contact Erik or Bev at RMCP meanwhile.
- category: Funding and Financial Development
- source: email from Patricia Markwell 2026-07-30
- links: [[partnerships-and-strategic-relationships#2026-07-20 Grant platform meeting with Patricia Markwell (RMCP)]]

## 2026-07-30 Buena Vista funding gap — the test case for community funding
- BV has a **$700 shortfall for its next dinner**; facilitators Mike Mayer and Erik
  Jacobsen wrote they'll "overextend ourselves" to keep dinners alive (quality food
  matters to the container) and want to learn fundraising. Andrew cautioned against
  burnout and offered to build a short-term fix plus a sustainable funding stream;
  scheduling a call (Fri 4pm or weekend slots), bringing Justin in.
- Solutions discussed at the Leadership Circle: local retailer community grants
  (Walmart/Target), simpler menus, channeling tax-deductible donations through DTD
  Central's 501(c)(3), asking attendees for local business connections, and framing DTD
  as a whole-community benefit for funders (the approach that won Jamie Fanselow HHS +
  Public Health funding).
- action #done (Andrew, 2026-08-01): fundraising call scheduled for Mon Aug 3 11am;
  sponsorship-ask draft still pending
- category: Funding and Financial Development
- source: "Fundraising - We Believe in DTD" thread 2026-07-30/31 + Fathom recap
- links: [[community-growth-and-expansion#2026-07-30 Leadership Circle recap: growth strong, funding is THE challenge, committees forming]]

## 2026-07-30 Budget review sessions set for Monday Aug 3
- Andrew/John budget working session 11:30–1:00 MT, followed by the DTD Budget Review
  1:00–2:00pm with Chris Peterson (both accepted).
- category: Funding and Financial Development
- source: calendar invitations 2026-07-30

## 2026-07-22 Board fundraising asks: 100% giving, network outreach, $250K seed fund
- Andrew emailed the board following the 7/17 meeting with four asks: (1) a personal
  donation of any size, targeting a 100% board giving rate (some already given);
  (2) reach out to personal/professional networks using Ben Shay's outreach script;
  (3) favor 1:1 coffee/Zoom conversations over events (events still welcome; Andrew will
  join any ask); (4) update LinkedIn profiles to show board positions — a DTD LinkedIn
  page now exists and Ken will follow up with details. Ben's script (draft) frames the
  campaign: raising a **$250,000 seed fund** for local dinners and central infrastructure,
  and cites CPR/NPR attention, the launch of "Dude Talk Central," and seven active
  communities (counts to be confirmed — see needs-clarification).
- John replied same day with copy edits (subject line, remove em dashes, indentation,
  item-3 rewording): "Everything else looks good!"
- action #open (all board): personal donations toward 100% participation
- action #open (Ken): send board members LinkedIn profile-update details
- category: Funding and Financial Development
- source: "Following up from Friday — our fundraising asks" email thread 2026-07-22
- links: [[governance-and-org-development]], [[relationships#Benjamin Shay]]

## 2026-07-22 Funding-opportunities prospect list received; where to track it?
- Andrew forwarded Lauren Vanderpool's (Social Impact Solutions) list of 14 funding
  prospects — local CO government/foundation, corporate, and national — now filed as
  [[funding-opportunities]]. Andrew asked whether the CRM will have a place to keep
  "possible funding opportunities."
- action #open (John): answer Andrew re a funding-opportunities section in the CRM
- category: Funding and Financial Development
- source: "Fwd: Dude Talk Dinners Followup | Funding Sources & Ideas" email 2026-07-22
- links: [[30-resources/funding-opportunities|funding-opportunities]], [[relationships#Lauren Vanderpool]]

## 2026-07-22 John registered for Givebutter fundraising webinar
- Registration confirmed for "Grow giving year-round: How to unlock untapped fundraising
  potential" (Zoom) — the webinar he flagged to Andrew on Jul 21.
- category: Funding and Financial Development
- source: Zoom registration confirmation 2026-07-22
