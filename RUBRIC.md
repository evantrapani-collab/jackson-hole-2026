# Trip Rubric — grading the plan out of 100

A fixed scorecard for judging whether this trip plan is actually ready, not just long. Re-grade whenever plan content changes materially (a booking lands, a constraint moves, an open item closes or rots past its deadline).

**Current grade: 100/100** *(re-graded 2026-08-30 — found at **97**, restored to 100; see the notes at the bottom)*

> **This file is a maintainer's tool, not trip content.** Nothing in the crew-facing site links to it or quotes a score — `index.html` and the README carry the plan, and the grade lives here. A number like "99/100" sitting on a dashboard is one more thing to keep in sync and tells the crew nothing they can act on.

---

## How scoring works

Each category starts at full points; deduct per the criteria. The rubric grades **the plan and its documents** — it does not award points for the trip itself going well, and it does not penalize future human actions *if* the plan gives them an owner, a deadline, and a default that holds if the action never happens.

Three rules of thumb that decide most edge cases:

1. **The zero-action test.** For every open item, ask: *if nobody does anything, what happens?* If the answer is a written outcome, it scores. If the answer is "we'd figure it out," it doesn't — that's a gap wearing a plan's clothes.
2. **The decision-funnel rule.** An open decision whose only path to resolution is a future group call is **still open**, no matter how well documented the tradeoffs are. Calls slip, and a call carrying ten decisions decides two. A decision pointed at a call scores full marks only when it also carries a default that survives the call not happening.
3. **A number is not explicit until it's a number.** "Total minus deposit," "$784 or $534 depending," "TBD" — none of these are things a person can Venmo, pack, or buy. Ranges are fine for estimates; ambiguity is not fine for amounts owed.

| # | Category | Points |
|---|---|---|
| 1 | Bookings & the critical path | 20 |
| 2 | Schedule feasibility vs. fixed constraints | 15 |
| 3 | Risk, safety & contingency | 15 |
| 4 | Meals — every slot has a plan | 12 |
| 5 | Money — totals, splits, deadlines | 12 |
| 6 | Group coordination (13 guys) | 10 |
| 7 | Three layers in sync (markdown ↔ dashboard ↔ maps) | 10 |
| 8 | Dashboard usability | 6 |
| | **Total** | **100** |

### 1. Bookings & the critical path (20)

- Everything bookable is booked, or has an owner + deadline + written fallback (−2 each gap)
- The trip-gating items (⭐) are flagged and tracked (−3 if not)
- Anything time-fenced (refund cutoffs, books-out-months venues, shoulder-season operating dates) has its real deadline written down (−2 each)
- Load-bearing tasks aren't ownerless (−1 each). *"Someone should call X" is ownerless. Where an institution will only talk to one person — the guest of record, the cardholder, the renter — the plan should say so and name him; that's not an assignment, it's a fact*
- Anything the trip depends on that a vendor could simply not be running (a tram, a lift, a shoulder-season kitchen) **has had its operating calendar actually checked**, and has a named replacement for the block it fills (−2 if unchecked, −1 if checked but unreplaced). *Sharpened 8/21: three passes flagged the tram-vs-gondola ambiguity and none of them asked whether either was running. One was not.*

### 2. Schedule feasibility vs. fixed constraints (15)

The fixed constraints (CLAUDE.md): Friday booked dawn-to-dusk; Saturday Yellowstone via South Entrance, **hard 2:00 PM turnaround at West Thumb** for the 5:30 LSU game; Sunday **6:00 AM** drive + 11 AM Saints; 13 locked; Montreux House booked.

- Every day's timing arithmetic actually works **against verified drive times, not the ones written in this repo** (−2 per broken day, −4 if the error is large enough to break the day's hard constraint). *Added 8/21: self-consistency is not the test. A day can be internally perfect and still be an hour and a half wrong, and only an outside source catches that*
- Roads and lifts the plan drives on or rides are checked against current closures (−1 each unchecked)
- No suggested activity violates a fixed constraint without a 🚫 triage flag (−2 each)
- Arrival and departure days have explicit timelines, including the house exit (−1 each gap)

### 3. Risk, safety & contingency (15)

- Travel failure modes have a playbook (the 43-min DFW connection) (−3 if not)
- Weather-scrub plan exists **with a named indoor option**, not just "town" (−1)
- Safety basics written for a no-cell-service trip: nearest ER, bear spray, offline maps, DD plan for drinking nights (−2 each gap)
- A single printable contacts card exists (house, manager, outfitter, airline, ER, money hub) (−1 if scattered)
- Refund exposure (rafting 7-day cutoff) has an owner and a cost-split rule deadline (−2 if not)

### 4. Meals — every slot has a plan (12)

- Every breakfast/lunch/dinner slot Thu–Mon resolves to a venue, the house, or a stocked default (−1 per open slot)
- Early starts (Sat 6:15 AM, Sun 6:00 AM) have a no-cooking answer (−2 if not) — *and nothing in Jackson is open before either, so "grab something on the way" doesn't count*
- 13-top reality acknowledged: reservations flagged where needed, walk-in assumptions justified (−2 if not)
- The grocery plan covers acquisition (who/how/when), incl. the 13-ribeye volume problem (−2 if not)

### 5. Money — totals, splits, deadlines (12)

- Per-person amounts, due dates, and who collects are explicit (−2 each gap). **Every man's number is a single number** — an "or" in an amount owed is a gap, not a nuance (−2), and it closes with a tiebreak rule, not with a promise to ask
- A single **all-in per-person planning number** exists (−1 if you have to add it up yourself)
- Cash needs (tips, cash-only spots) called out (−1)
- Booking tracker and every money line reflect reality (−1 per stale figure — superseded balances, "TBD" amounts that have since been settled)

### 6. Group coordination (10)

- Headcount, roster, and seat math (13 bodies vs. vehicle seats) tracked with the gap flagged (−2 if not). The roster and the money ledger name the same 13 men in a way you can match one-to-one (−1 if a name appears in one and not the other)
- Bed math (13 vs. 6 beds) acknowledged with an assignment plan/deadline (−2 if not)
- Drivers, DDs, grill captain, departure-time owners: named, or carrying a **default owner** with a deadline (−1 each role that is neither)
- Pending-external-info items (e.g., Explorer trim, bed count) can't score full marks until answered (−1 each while open)
- No single meeting is the only path to more than a couple of decisions (−1 per decision stacked on a call without its own default) — see the decision-funnel rule above

### 7. Three layers in sync (10)

- Every plan fact appears identically in markdown and `index.html` (−1 per divergence)
- **Any number that appears in two places matches in both** (−1 per mismatched figure). This is the cheapest deduction to earn and the easiest to miss: totals, ranges, per-person amounts, place counts, item counts. A figure quoted in prose ("the full 76-place file") counts as one of the two places
- **When a fact is corrected, the old value is gone from every file** — grep the string you replaced and confirm zero hits before calling it fixed (−1 per survivor). A canonical copy being right is not the same as the wrong copy being gone
- `/maps` regenerated whenever places change; no hand-edits to generated files (−2 per violation)
- Open Items (README) ↔ To-Do tab (dashboard) match (−1 per drift)

### 8. Dashboard usability (6)

- Works offline, zero-JS functional (−2 if not)
- Timelines in chronological order, times labeled MT/CT correctly (−1 each defect)
- Open items carry their owner/deadline tags (−1 if stripped)

---

## Scorecard

Current standing, and where the four most recent passes found gaps. Earlier columns lived here for ten passes; they're summarised in the re-grade log below and written out in git history.

| Category | Points | 8/21 #1 | 8/21 #2 | 8/21 #3 | 8/28 found | **Now** |
|---|---|---|---|---|---|---|
| 1. Bookings & critical path | 20 | 17 | 19 | 20 | 18 | **20** |
| 2. Schedule feasibility | 15 | 8 | 15 | 15 | 15 | **15** |
| 3. Risk, safety & contingency | 15 | 15 | 13 | 15 | 15 | **15** |
| 4. Meals | 12 | 12 | 8 | 12 | 9 | **12** |
| 5. Money | 12 | 12 | 12 | 12 | 12 | **12** |
| 6. Group coordination | 10 | 9 | 10 | 10 | 10 | **10** |
| 7. Three layers in sync | 10 | 10 | 10 | 6 | 6 | **10** |
| 8. Dashboard usability | 6 | 6 | 3 | 4 | 3 | **6** |
| **Total** | **100** | **89** | **90** | **94** | **88** | **100** |

> Read across a row: every category has been the weak one at least once. §2 collapsed to 8 when the drive times were checked against the world; §4 to 8 when a default turned out to be a meal nobody serves; §7 and §8 fell once the cost of *duplication* was scored rather than the completeness of each copy. **8/28 is the first pass to find the same weaknesses twice** — §4's fictional lunch and §7's stale drive times, still alive in copies the earlier fixes never reached. Hence §7's new grep test.

---

## Verified external facts — checked 2026-08-21, re-checked 2026-08-28

Maintainer's ledger. These are the claims the plan *depends on* that live outside this repo, and the 8/21 passes proved that confident prose is no evidence any of them were ever checked. Re-check before the trip; anything with a date fence rots silently.

**Re-verified 8/28 and unchanged:** the Aerial Tram season, the Bridger Gondola's Sept 13 close, the Moose-Wilson closure, Dornan's hours, Sidewinders, both kickoff times/networks, and Sunday's sunrise. The park-service pages (Craig Pass status, road conditions) still want a day-of check — that one can't be pre-verified.

| Fact | Value | Re-check at |
|---|---|---|
| Aerial Tram season | May 16 – Oct 4, 2026, 8:30–5 · ~$55/pp | jacksonhole.com |
| Bridger Gondola season | **Ends Sept 13** — closed for our trip | jacksonhole.com |
| Corbet's Cabin | 8:30–5, with the tram | jacksonhole.com |
| Moose-Wilson Road | **Closed Sep 8 – Nov 15, 2026** | nps.gov/grte |
| Craig Pass (West Thumb ↔ Old Faithful) | Open, but first to close for snow | nps.gov/yell — **check day-of** |
| House → Yellowstone South Entrance | ~1 hr 30 | maps, day-of |
| South Entrance → Old Faithful | 39 mi / ~1 hr 15 | NPS |
| Grand Prismatic overlook | 1.6 mi round trip on foot from Fairy Falls lot | NPS |
| Sunrise, Sun Sep 20 | ~7:07 AM (usable light ~6:40) | almanac |
| Dornan's | 11:30 AM – 7 PM daily, year-round | (307) 733-2415 |
| Cowboy Coffee drive-thru | 1007 S US-89, opens 6 AM | cowboycoffee.com |
| Sidewinders | 11:30 AM – 9:30 PM, 30+ TVs, no reservations | (307) 734-5766 |
| JHWW "Classic Raft" | **No lunch included** (that's their scenic float) | (307) 733-1007 |
| Parking, 945 W Broadway | **"Extremely limited"** per JHWW; shared with Barker-Ewing + Rendezvous River Sports; they suggest walking or a taxi | jhww.com/trip-info |
| JHWW check-in windows | **30 min** before whitewater, **15 min** before a scenic float | jhww.com/trip-info |
| Bear Aware kiosk, JAC | Baggage claim #3, Jun–Oct, ~$28/canister capped | bearaware.com |
| Park entry | $35/vehicle/park, **7-day**; +$100 non-resident surcharge (2026) | nps.gov |
| DFW→JAC nonstops | 2 daily, year-round | AA app |
| LSU–Ole Miss | Sat 9/19, 5:30 PM MT, ABC | — |
| Saints @ Ravens | Sun 9/20, 11:00 AM MT, CBS | — |

---

---

## Re-grade log

### Earlier re-grades — summarised

Thirteen passes ran between 6/12 and 8/21; the full write-ups are in git history. The short version: the plan reached 100 seven separate times on **structure** — every open item owned, dated, and carrying a default that holds with zero action — and each later pass found that structure was necessary but not sufficient.

| Pass | Found at | The lesson it added |
|---|---|---|
| 6/12 – 7/11 (×4) | 82 → 100 | Decisions need an owner and a deadline, not just a discussion |
| 8/4 (×2) | 97 → 100 | Deadlines rot; a date that has passed is a defect |
| 8/15 (×3) | 85 → 100 | A decision pointed only at a future call is still open — it needs a zero-action default |
| 8/20 | 97 → 100 | Confirmations can correct the plan, not just confirm it (two outfitters, one address) |
| 8/21 #1 | 89 → 100 | **Self-consistency is not the test.** Checking nine claims against the operators, the NPS and a clock returned five wrong: the Yellowstone legs understated by half, an impossible sunrise, a lift closed for the season, a closed road, a missing $715 budget line. §1 and §2 were rewritten to grade against *verified* facts |
| 8/21 #2 | 90 → 100 | **A default that doesn't exist is worse than none** (JHWW feeds scenic floats, not whitewater — Friday had no lunch), and **length is a defect, not a neutral**: 12 tabs → 9, ~15KB out of the dashboard |
| 8/21 #3 | 94 → 100 | **The cost of a fact is the number of places it is written.** Bear spray appeared 39 times across 5 files. When a decision closes, delete its reasoning and keep its outcome |

---

### 8/28 re-grade — the copies drift, and a deadline rots (found at 88, restored to 100)

The 8/21 passes fixed the *canonical* statement of five facts. This pass asked a narrower question: **did every copy get fixed?** Mostly, but not everywhere — and the copies that didn't are all in `index.html`, which is the layer the crew actually reads on a phone.

**Found at 88 (−12).**

| # | Cat | Deduction | What was wrong |
|---|---|---|---|
| −4 | §7 | **Four facts that disagree with themselves across the layers** | (1) **The butcher.** `dining.md` says *"start at Albertsons — usually the one carrying Prime… call the Albertsons butcher first,"* and eleven lines later *"call the Smith's butcher counter ahead."* The dashboard contradicted itself the same way, and the README and grocery list both said Smith's. Psilos has exactly one call to make and the plan named two different stores. (2) **The corrected drive time didn't reach two files:** `lodging.md` still read *"Yellowstone is ~1 hr north via Hwy 89"* and the dashboard's Maps tab still labelled the South Entrance *"~1 hr from Jackson"* — the precise claim the 8/21 pass took −4 for. (3) **Old Faithful → the house was listed at ~2 hr 15** in a table whose own two legs (40 min to West Thumb + 1 hr 50 home) sum to **~2 hr 30**. (4) **The old Yellowstone clock survived in three places** — *"back from Yellowstone ~3 PM," "a 7 AM–3 PM Yellowstone day," "Yellowstone 7 AM → ~3 PM"* — against the real 6:15 AM–3:50 PM |
| −3 | §8 | **The dashboard re-opened four questions the markdown had closed** | The tram's operating dates are confirmed (May 16 – Oct 4) in five places — and the dashboard still said *"Confirm fall operating dates… if it isn't running"* in the Sunday-afternoon card **and** in the To-Do list. Dornan's hours are confirmed year-round — and the dashboard still said *"confirm fall hours"* on the dinner row **and** carried a whole extra to-do item, *"Confirm Dornan's fall hours,"* that exists in no README. Plus a pointer to a **"Game Day" tab that was deleted on 8/21**, and a *"Sun lunch — Dornan's"* row that the same page's own Sunday clock makes impossible (the 11 AM game runs to ~2:15, the tram takes 2:30–3:40, and Dornan's is the 5 PM dinner) |
| −3 | §4 | **The fictional lunch came back — in the layer people read** | The dashboard's Groceries tab still opened with *"Friday breakfast is Cowboy Coffee and lunch is the rafting outfitter."* That is the exact default §4 scored **−4** for on 8/21, alive in the one place a crew member checks while standing in an aisle — and directly contradicted by a line further down the same tab (*"two cooler lunches: Fri at the boathouse + Sat at West Thumb"*) |
| −2 | §1 | **A load-bearing deadline rotted, and every layer still spoke of it in the future tense** | The RMR call was due **8/22**. As of 8/28 the README said *"DUE TOMORROW (8/22)"* and *"the last live August item,"* the grocery list said *"that's tomorrow as of this writing,"* and the dashboard's countdown nudge pointed at a date that had passed. This is the defect the 8/4 passes named — *a date that has passed is a defect* — and the only reason it cost 2 points rather than more is that all three of the call's questions carry defaults that held when it slipped |

**Restored to 100:**

- **One butcher.** Albertsons everywhere (it's the sourced Prime read), Smith's and Jackson Whole Grocer as the named backups — in `dining.md`, `grocery-list.md`, the README, the dashboard, and the `maps` generator's store pins, which were regenerated.
- **The rotted deadline is honest rather than hidden.** The RMR call moved to the existing **9/7** batch, labelled *"slipped its 8/22 date"* rather than silently re-dated. The README's `🔴 Now (August)` bucket became `✅ Closed in August`, a live `🔴 Now — through Sep 10` bucket holds the call, the milestone strip and the countdown nudge follow, and the dashboard's To-Do mirrors all of it.
- **Every surviving copy of a corrected fact was fixed:** both "~1 hr" drive times, the three stale Yellowstone return times, and Old Faithful → the house (now ~2 hr 30, with its two legs shown so it can't drift from them again). The one derived claim that moved with it — *"a 7:00 AM departure gets you home at 4:35"* — is now **~4:50**, which is a stronger argument for the 6:15 departure, not a weaker one.
- **Four closed questions stay closed**, the dead Game-Day pointer is gone, the impossible Sunday lunch became what Sunday's lunch actually is (the 11 AM game spread, already on the grocery list), and the ⭐ count on the To-Do tab matches the README's — **one**, not two.
- **Re-checked against the outside world, not the repo** (per §1/§2): the Aerial Tram's **May 16 – Oct 4, 8:30–5** season, the Bridger Gondola ending **Sept 13**, **Moose-Wilson closed Sep 8 – Nov 15**, Dornan's **11:30–7 daily**, Sidewinders **11:30–9:30 with 30+ TVs**, **LSU–Ole Miss 6:30 CT / ABC**, **Saints @ Ravens noon CT / CBS**, and Sunday's **~7:07 sunrise / ~6:40 civil twilight**. All eight hold. The ledger above is re-dated accordingly.

**The rule this pass earns.** The previous three passes each fixed a fact. None of them ran the cheapest possible check afterwards: **grep the old wrong value.** Every deduction here would have been caught by searching the repo for the string the correction replaced — *"~1 hr from Jackson," "~3 PM," "Smith's butcher," "confirm fall hours," "the rafting outfitter."* So §7 gains an operational test: **when you correct a fact, search for the old value and confirm zero hits before you call it fixed.** A correction is not done when the canonical copy is right; it's done when the wrong one is gone.

**Grade: 100/100.**

---

### 8/30 re-grade — the dashboard was a duplicate of itself (found at 97, restored to 100)

No fact moved and no deadline rotted since 8/28; the eight external checks above still hold, so §1–§6 are unchanged. This pass graded **§8 only**: is the page the crew reads on a phone actually usable, or just complete?

**Found at 97 (−3).**

| # | Cat | Deduction | What was wrong |
|---|---|---|---|
| −2 | §8 | **An entire tab that was a copy of the other tabs** | The Overview tab restated the spine, the five days, the deadlines and the locked-in list — every one of which is stated better on the tab that owns it. It's the same defect as the 8/21 tab cull and the 8/21 #3 rule (*the cost of a fact is the number of places it is written*), one level up: not a duplicated fact, a duplicated **tab**. Meanwhile the day-by-day bullets had grown into paragraphs — a 6:15 AM alarm should not need four sentences of justification on the phone screen you read it from |
| −1 | §8 | **A pointer to a table that doesn't exist** | The Crew & **Money** tab carried one line of money and said *"per-person estimates are on the Logistics tab."* They are not on the Logistics tab, and never were — they're in `/budget`. Same family as the dead "Game Day" pointer from 8/28: a cross-reference nobody followed |

**Restored to 100:**

- **Two tabs deleted, nine → seven; Itinerary is the landing tab.** Overview restated the other tabs and went whole. **Crew & Money** went the same way once its parts were read one at a time: *Who Owns What* turned out to be duplicated in full — every job, owner and status already appears on the To-Do list, in Key Contacts or in Getting Around — so it is gone, and the roster of 13 names with it (`logistics/roster.md` is the source; no page linked to it).
- **The three parts that were load-bearing moved rather than died:** the per-person money table from `/budget` (paid, food, tips/gas/entry, optional tram, **≈$1,100–1,390 all in**) now opens the **Logistics** tab; the Montreux House bed layout sits above Key Contacts on the same tab; and **Decision Defaults** moved to the bottom of the **To-Do** tab, directly under the items it defaults — a better home than it had, since "what happens if nobody does anything" belongs beside the list of things nobody has done. `CLAUDE.md` was re-pointed to match.
- **Every tab cut to what a phone can read**: itinerary bullets tightened to a line each, closed decisions reduced to their outcome (the Cowboy Steakhouse row and the two settled To-Do items came off the open lists and survive as one closing line), and the two duplicate Moose-Wilson notes on Logistics merged into one. `index.html` is **~26KB smaller** with no fact removed.
- **Layers re-synced:** the README's Open Items and Decision Defaults match the dashboard item-for-item (**32 open items** in both), and the "what the docs used to say" corrections in `itinerary.md`, `logistics.md` and `activities.md` are gone — the corrected numbers stay, the changelog belongs to git.

**The rule this pass earns.** Length is a defect (8/21 #2) and duplication is a defect (8/21 #3) — this pass adds that **the two compound**: a tab whose job is to summarize the other tabs is duplication *and* length, and it is always the first thing to cut. §8 gains a test: **if a section would be correct after deleting it, delete it.**

**Grade: 100/100.**
