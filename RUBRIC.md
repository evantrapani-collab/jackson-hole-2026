# Trip Rubric — grading the plan out of 100

A fixed scorecard for judging whether this trip plan is actually ready, not just long. Re-grade whenever plan content changes materially (a booking lands, a constraint moves, an open item closes or rots past its deadline).

**Current grade: 100/100** *(re-graded 2026-08-28 — found at **95**, restored to 100; see the notes at the bottom)*

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
- `/maps` regenerated whenever places change; no hand-edits to generated files (−2 per violation)
- Open Items (README) ↔ To-Do tab (dashboard) match (−1 per drift)

### 8. Dashboard usability (6)

- Works offline, zero-JS functional (−2 if not)
- Timelines in chronological order, times labeled MT/CT correctly (−1 each defect)
- Open items carry their owner/deadline tags (−1 if stripped)

---

## Scorecard

Current standing, and where the three 8/21 passes found gaps. Earlier columns lived here for ten passes; they're summarised in the re-grade log below and written out in git history.

| Category | Points | 8/21 #1 | 8/21 #2 | 8/21 #3 | **Now** |
|---|---|---|---|---|---|
| 1. Bookings & critical path | 20 | 17 | 19 | 20 | **20** |
| 2. Schedule feasibility | 15 | 8 | 15 | 15 | **15** |
| 3. Risk, safety & contingency | 15 | 15 | 13 | 15 | **15** |
| 4. Meals | 12 | 12 | 8 | 12 | **12** |
| 5. Money | 12 | 12 | 12 | 12 | **12** |
| 6. Group coordination | 10 | 9 | 10 | 10 | **10** |
| 7. Three layers in sync | 10 | 10 | 10 | 6 | **10** |
| 8. Dashboard usability | 6 | 6 | 3 | 4 | **6** |
| **Total** | **100** | **89** | **90** | **94** | **100** |

> Read across a row: every category has been the weak one at least once, and no pass found the same weakness twice. §2 collapsed to 8 when the drive times were checked against the world; §4 to 8 when a default turned out to be a meal nobody serves; §7 and §8 fell once the cost of *duplication* was scored rather than the completeness of each copy.

---

## Verified external facts — re-checked 2026-08-28

Maintainer's ledger. These are the claims the plan *depends on* that live outside this repo, and the two most recent passes proved that confident prose is no evidence any of them were ever checked. Re-check before the trip; anything with a date fence rots silently.

| Fact | Value | Re-check at |
|---|---|---|
| Aerial Tram season | May 16 – Oct 4, 2026, 8:30–5 · $54 adult | jacksonhole.com |
| Bridger Gondola season | **Ends Sept 13** — closed for our trip | jacksonhole.com |
| Corbet's Cabin | 8:30–5, with the tram | jacksonhole.com |
| Moose-Wilson Road | **Closed Sep 8 – Nov 15, 2026** (shuts end of day 9/7, Moose ↔ LSR Preserve). LSR Preserve still reachable from the **Granite Canyon entrance** | nps.gov/grte |
| Death Canyon Road + Trailhead | **Closed all 2026 season** | nps.gov/grte |
| Teton-area fire restrictions | Stage 1 in force **Jul 22 → lifted Aug 26, 2026**; danger now moderate. Stage 1 bans charcoal, allows propane | Teton Interagency Fire |
| Old Faithful overpass work | Jul 20 – ~Aug 14, 2026 — **finished before the trip** | nps.gov/yell |
| Craig Pass (West Thumb ↔ Old Faithful) | **Scheduled open May 8 – Oct 31, 2026**; still first to close for snow | nps.gov/yell — **check day-of** |
| House → Yellowstone South Entrance | ~1 hr 30 | maps, day-of |
| South Entrance → Old Faithful | 39 mi / ~1 hr 15 | NPS |
| Grand Prismatic overlook | 1.6 mi round trip on foot from Fairy Falls lot | NPS |
| Sunrise, Sun Sep 20 | ~7:07 AM (usable light ~6:40) | almanac |
| Dornan's | 11:30 AM – 7 PM daily, year-round | (307) 733-2415 |
| Cowboy Coffee drive-thru | 1007 S US-89, opens 6 AM | cowboycoffee.com |
| Sidewinders | 11:30 AM – 9:30 PM, 30+ TVs, no reservations | (307) 734-5766 |
| JHWW "Classic Raft" | **No lunch included** (that's their scenic float) | (307) 733-1007 |
| Bear Aware kiosk, JAC | Baggage claim #3, Jun–Oct, ~$28/canister capped | bearaware.com |
| Park entry | $35/vehicle/park, **7-day**; +$100 non-resident surcharge (2026) | nps.gov |
| DFW→JAC nonstops | 2 daily, year-round | AA app |
| LSU–Ole Miss | Sat 9/19, 5:30 PM MT (6:30 CT), ABC — re-confirmed 8/28 | — |
| Saints @ Ravens | Sun 9/20, 11:00 AM MT (noon CT), CBS — re-confirmed 8/28 | — |

---

---

## Re-grade log

### Earlier re-grades — summarised

Ten passes ran between 6/12 and 8/20; the full write-ups are in git history. The short version: the plan reached 100 four separate times on **structure** — every open item owned, dated, and carrying a default that holds with zero action — and each later pass found that structure was necessary but not sufficient.

| Pass | Found at | The lesson it added |
|---|---|---|
| 6/12 – 7/11 (×4) | 82 → 100 | Decisions need an owner and a deadline, not just a discussion |
| 8/4 (×2) | 97 → 100 | Deadlines rot; a date that has passed is a defect |
| 8/15 (×3) | 85 → 100 | A decision pointed only at a future call is still open — it needs a zero-action default |
| 8/20 | 97 → 100 | Confirmations can correct the plan, not just confirm it (two outfitters, one address) |

---

### 8/21 re-grade — the outside world gets checked (found at 89, restored to 100)

The previous six passes graded the plan against **itself**: is every open item owned, dated, defaulted; do the days' internal arithmetic close. That's most of what a rubric can do, and it had taken the plan to 100 three times running.

This pass did something the rubric had never actually forced: **it checked the plan's factual claims against the operators, the park service, and a clock.** Nine claims went out; five came back wrong. That's the finding worth recording — a plan can be perfectly self-consistent, fully owned, comprehensively defaulted, and still be **wrong about the world**, and no amount of internal review will surface it. §2 in particular has been scoring "every day's timing arithmetic actually works" against *the drive times written in this repo*, which is circular whenever those numbers are guesses.

**Found at 89 (−11).** Every deduction below is a fact the repo asserted that a five-minute check would have falsified — none of them are new developments.

| # | Cat | Deduction | What was wrong |
|---|---|---|---|
| −4 | §2 | **Saturday's clock was built on drive times that are roughly half the real ones** | The table said the Yellowstone South Entrance was "~1 hr" away and Old Faithful "~30 min" past the gate. It is **~1 hr 30** from the house (which is in Teton Village, not Jackson — the table measured from the wrong place) and **~1 hr 15** gate to Old Faithful (39 miles at 45 mph). Old Faithful → house is **~2 hr 15**, not 1.5. On the old numbers a 7:00 departure gets home at 3:00; on the real ones it gets home at **4:35** — 55 minutes before kickoff, with 13 raw ribeyes and a grill that needs two batches. This is the single largest defect any pass has found: the day *reads* fine, the internal arithmetic is self-consistent, and it doesn't work |
| −2 | §2 | **Sunday's sunrise arithmetic was physically impossible** | "Leaving the house at 6:30 puts you at Schwabacher right at first light (~6:40)" — a ten-minute drive to a place **~45 minutes away**, on a morning when **sunrise is ~7:07**. Nobody had ever checked either number. The whole point of the block is the light, so this was a highlight quietly scheduled to be missed |
| −2 | §1 | **A scheduled activity was closed before we arrive** | Thursday's afternoon plan rode on "the gondola at Teton Village." The **Bridger Gondola's 2026 season ends Sept 13**; we land the 17th. §1 explicitly grades *"anything the trip depends on that a vendor could simply not be running"* — and this had been carried through four passes as a live block, with the only flagged risk being the *tram/gondola confusion*, never whether either was operating |
| −1 | §2 | **A road the plan drives on is closed** | **Moose-Wilson Road is shut Sep 8 – Nov 15, 2026** (NPS Phase II construction). It was a named Sunday wildlife stop, and — worse — it's the short route from Teton Village to Moose, so its closure quietly invalidated *every* park drive time in the repo, including the "~10 min" JAC→house figure the Explorer seat-count fallback leans on (it's **~30–35 min**) |
| −1 | §6 | **A real cost was missing from the budget** | Sunday's plan is the tram to Corbet's Cabin. Tram tickets are **~$55/person** — potentially **~$715** across 13 — and the budget carried **no tram line at all**. §6 wants the all-in number to be honest; it was light by up to 5% of the on-the-ground total |
| −1 | §1 | **A time-fence rotted past its deadline without being recorded** | The Cowboy Steakhouse 30-day window opened 8/17 and closed 8/18. As of 8/21 every document still described it in the future tense — *"the window opens 8/17"* — which is exactly the "an open item rots past its deadline" trigger this file names in its own re-grade instruction. The outcome (nobody called, the house steak nights stand) was the expected default; not recording that it *fired* leaves a live-looking item that will eat time on the Sep 10 call |

**Restored to 100 by this pass:**

- **Saturday was rebuilt on real numbers, and given a rule instead of a hope.** Departure moves to **6:15 AM**, and the day now carries one hard constraint — 🕐 **wheels rolling south out of West Thumb by 2:00 PM** — which lands the house at ~3:50, the grill lit at ~4:15, and everyone eating before the 5:30 kickoff. The full clock is in `/itinerary` and mirrored on the dashboard's route strip. It also resolved a contradiction nobody had noticed: `/itinerary` said "back by ~3 PM" while `/logistics` said "leave Yellowstone by ~3 PM" — two different instructions, ~2 hours apart.
- **The Grand Prismatic overlook is described as what it is.** Every document treated it as a stop; it's a **1.6-mile round-trip walk** from the Fairy Falls lot (~1 hr for 13 guys), and that lot fills early. That hour was never on any clock.
- **Sunday leaves at 6:00**, with the real sunrise (~7:07), the real drive (~45 min), and the closed road cut from the loop. A headlamp moved onto the packing list because the plan now genuinely involves standing on a dirt path in the dark.
- **The gondola closure became an asset, not a hole.** Its 3:00–4:00 PM slot is now **the errand hour** — the home for the grocery run that five separate ⚠️ callouts across this repo had been trying to wedge into somebody's beer. It also permanently settles the tram-vs-gondola ambiguity that three passes flagged and none could close: only one lift is running, so the **tram is Sunday's**, and the ✅ **confirmed Aerial Tram season (May 16 – Oct 4, 8:30–5)** closes the "will it be operating?" open item that has been live since July. Only the purchase remains, and it's now in the budget.
- **Bear spray stopped being a chore.** It was the most-flagged ⚠️ in the repo — "Thursday is the only window," repeated in five files. **Bear Aware staffs a kiosk at JAC baggage claim #3, June–October**: rent two canisters for **~$56 total**, return them to the same box Monday. It costs **zero minutes**, saves ~$44 against buying, and answers the question every version of this plan left dangling — *you can't fly home with bear spray*, so bought canisters get abandoned. A §3 safety item went from "must be squeezed into a schedule" to "happens while you wait for your bag."
- **Two smaller checks paid off.** **Dornan's opens at 11:30** — Thursday's clock had us arriving 11:15 — and is open **daily 11:30–7 year-round**, which closes the standing "confirm fall hours" action on Sunday's dinner default. And **Cowboy Coffee has a drive-thru at 1007 S US-89** that opens at 6 AM, ~2 min from the boathouse and *on* the route in, versus the Town Square store which is a backtrack east past it — so Friday's tightest hour got a better answer and a 6:45 departure.
- **The park fee got two true clarifications:** each $35 is a **7-day** pass, so Saturday's Grand Teton fee at Moran covers Sunday's Oxbow Bend (the $140 total is still right — it's 2 vehicles × 2 parks, not 4 entries), and **2026 introduced a $100 non-resident surcharge** worth one question in the chat.
- **Sync:** the all-in number reads **$1,100–1,390** in both layers (tram added, bear spray reduced), the Decision Defaults table and the dashboard Crew tab match on all five closures, the maps generator carries the two closures plus the drive-thru and the Bear Aware kiosk (**83 places**, regenerated, `--check` clean), and the to-do checklist gained the three day-of timing items and a corrected count.

**A rubric change this pass earned.** §2's criterion should be read as *"every day's timing arithmetic works **against verified drive times**"* — self-consistency is not the test. Same for §1's vendor criterion: *"has a named replacement"* is worth less than *"someone checked the operating calendar."* Four passes at 100 didn't catch a closed lift, a closed road, an impossible sunrise, or a two-hour error on the tightest day of the trip, because none of them looked outside the repo.

**Grade: 100/100.** The plan's structure was never the problem — every one of these defects sat inside a well-owned, well-defaulted item. What this pass adds is that the numbers underneath the structure are now checked rather than assumed.

---

---

### 8/21, second pass — a fictional default, and a site nobody could read

Two findings, one of each kind the previous pass warned about.

**Found at 90 (−10).**

| # | Cat | Deduction | What was wrong |
|---|---|---|---|
| −4 | §4 | **Friday's lunch default was a meal nobody serves** | Every document carried *"the outfitter's deli lunch, eaten at 945 W Broadway"* as the zero-action default. JHWW **does** provide lunch — **on their scenic float trips.** We booked the **whitewater "Classic Raft"**; its inclusions are guide, paddles, splash gear and the shuttle. **No food.** The scenic float was triaged out of this trip in the spring and its lunch quietly stayed behind. Run §4's own zero-action test honestly and the answer was *13 guys with no lunch getting on a Class 2–3 river at 1:00 PM having last eaten at 6:45 AM.* A default that doesn't exist is worse than no default, because it stops anyone from looking |
| −3 | §8 | **The dashboard had become a maintainer's document** | 12 tabs, three of them near-duplicates (Game Day restated kickoff times the Itinerary already had, in three places). ~30 lines of **correction archaeology** — *"this table was wrong," "the docs used to say ~1 hr"* — which is changelog, not trip content, and which I added in the previous pass. A **fully settled** money tab still carrying its per-man ledger, four "(in full 8/11)" datestamps, the Gunter $250 story told three times, and a historical cost-per-attendance table. Ten `new` pills dated across three different weeks, which means nothing reads as new. §8 grades whether 13 guys can *use* this on a phone; it had been graded on whether it was complete |
| −2 | §3 | **The one weather event that breaks Saturday wasn't named** | §3 credits a weather-scrub plan, and the repo had one — "town fallback," the Wildlife Art museum. But the specific failure is **Craig Pass (8,262 ft)**, the West Thumb ↔ Old Faithful segment, which is the first park road NPS closes for early snow — **and our out-and-back crosses it twice.** A mid-morning closure strands the group on the far side with only the long way round the figure-eight. Low probability (September averages 1.3" of snow), high impact, free to check |
| −1 | §1 | **An open item that a lookup could close** | *"Verify the evening DFW→JAC nonstop runs Thu Sep 17"* sat on the 1–2-weeks-out list on the theory that post-Labor-Day schedules thin out. AA flies JAC **year-round, 2 nonstops daily, 14 weekly** — the structural risk never existed |

**Restored to 100:**

- **Friday lunch has a real default:** sandwiches packed from the Thursday grocery run, eaten on a tailgate at the boathouse — zero travel, zero queue. It needed a genuine change to `grocery-list.md`, not just a word swap: **Friday's lunch cannot come from Friday's leftovers**, because Friday dinner happens after it, so the deli line doubles to 6 lb and the fajita module's "skip the deli meat" bonus is now correctly scoped to Saturday only. **Sidewinders** (next door, opens 11:30, **30+ TVs, 24 taps, no reservations**) is the named upgrade; **Cutty's is cut** — 25 minutes of a 45-minute window for a table available next door. The Sidewinders check also effectively pre-answers the Sunday game-venue recon: every brewery on the list was described as *"nobody's TV setup is great."*
- **The site was cut, not extended.** **12 tabs → 9** (Game Day folded into Itinerary; Crew and Money merged; Activities' next-trip hike shelf and duplicated Yellowstone table dropped, its two live cards moved to Itinerary). All correction archaeology removed — the plan now states what to do, not what it used to say. The money tab is one sentence. All `new` pills gone. **~15KB and 260 lines out of `index.html`**, with panel/radio/label/CSS sets verified to match and a pre-existing missing `#t-groc` focus-visible selector fixed on the way through. `budget.md` lost its settled ledger, payment timeline and historical attendance table; four links to the removed ledger anchor were repointed, and a **pre-existing dead anchor** (`#monday-breakfast--use-what-is-left` vs. the actual `…-whats-left`) was found and fixed by a full link/anchor sweep.
- **Craig Pass has a check and a replacement:** verify status at nps.gov/yell Friday night and again at 6 AM; if it's closed, **swap to a Grand Teton morning** — an hour closer, no new plan, back well before kickoff.
- **Assorted:** the DFW item closes (with the honest caveat that *2 a day* makes the evening flight the last chance, and 13 seats on it is a lot); Sunday afternoon gets a clock because the tram and a 5 PM Dornan's are **back-to-back with no slack** (last tram down is 5:00); and JHWW's practical details are recorded — **your bus seat is your locker, the driver stays with the bus**, changing rooms at the shop, no cotton.

**The rubric change this pass earns.** §8 should read *"a crew member can find what they need on a phone in under 15 seconds"* — not "the dashboard mirrors the markdown in full." Completeness and usability are in tension, and six passes of graded-for-completeness produced a document that mirrors beautifully and reads badly. **Length is now a defect, not a neutral.** Corollary: a review pass that only ever *adds* is not maintaining a plan, it's growing one.

---

---

### 8/21, third pass — cold-eyes read of the README

The previous pass cut the dashboard and left the README untouched. Read cold, the README had become the thing the dashboard just stopped being.

**Found at 94 (−6).**

| # | Cat | Deduction | What was wrong |
|---|---|---|---|
| −3 | §7 | **The same settled decision explained in four places** | Measured, not guessed: **bear spray — a solved, zero-effort item — appeared 39 times across 5 files** (README ×9, logistics ×8, itinerary ×5, dining ×1, dashboard ×16), with the full rent-vs-buy rationale written out in the README's Current Status, the 8/21 review section, the Decision Defaults table, *and* twice in Open Items. Moose-Wilson ×37, Sidewinders/lunch ×30. Every copy is a thing that can drift out of sync |
| −2 | §8 | **A changelog had grown inside the README** | An entire `### 🔎 8/21 review — five things checked against the outside world` section, added by the previous pass, duplicating Decision Defaults and Open Items wholesale. Plus **8 completed `[x]` items still written as full paragraphs** — 6 of them over 200 characters — so ~40 lines of *finished* business sat inside a to-do list. Closed items need one line |
| −1 | §7 | **Dated parentheticals as permanent furniture** | "(8/20)", "(new 8/21)", "(confirmed 8/15)", "moved in from 7:00 on 8/21", "🆕 Also 8/15" — 22 of them across the markdown. A reader in September does not care when a fact was learned. Attribution (*"Jeremy"*, *"Austin's BIL"*) is worth keeping; the datestamp never was |

**Restored to 100:** the changelog section deleted; completed items collapsed to one line each; settled decisions reduced to one canonical explanation plus short pointers; all 22 datestamps stripped while keeping the names. **README: 32.6KB → 24.1KB (−26%)**, and the same sweep across dining, logistics, itinerary, budget and activities. The dashboard's last dated fragments went with them.

**The rule this pass earns, and it generalises past this repo:** *the cost of a fact is the number of places it is written, not the number of words.* Two passes have now been spent deleting text that a previous pass added in good faith. The discipline that prevents a third is: **when a decision closes, delete its reasoning and keep its outcome.** The reasoning is what git history is for.

---

---

### 8/28 re-grade — the calendar moved and the docs didn't

Six days on from the last pass, with nothing about the trip changed except the date. **Found at 95 (−5)** — and four of the five deductions are the same failure in different clothes: *documents written in a tense that expired.*

| # | Cat | Deduction | What was wrong |
|---|---|---|---|
| −2 | §1 | **A deadline rotted past its date without being recorded** | The RMR call was due **8/22**. As of 8/28 the README still read *"DUE TOMORROW (8/22), and it's the last live August item,"* the dashboard still showed a live warn pill, and `grocery-list.md` still said *"that's tomorrow as of this writing."* This is the exact defect the 8/4 pass named — *deadlines rot; a date that has passed is a defect* — recurring on a different item |
| −1 | §3 | **A fallback that a public-lands rule can void** | The grill contingency has always been *"charcoal → 2 bags + a chimney."* Nobody had checked fire restrictions. **Teton-area Stage 1 restrictions were in force Jul 22 – Aug 26**, and Stage 1 bans charcoal while explicitly permitting propane — so for five weeks of planning, the written fallback was the one option that would have been illegal. They're lifted now, and the fall forecast is warm and dry |
| −1 | §8 | **The list broke its own promise of chronological order** | Open Items says *"in chronological order — work top to bottom,"* and the two **9/7** items (tram tickets, the park-pass question) sat below a block of **9/10** items in both layers, because the buckets were named for a month that's ending |
| −1 | §7 | **Dashboard drift on three settled facts** | The to-do tab still asked to *"confirm late-Sept tram operating dates"* and *"confirm Dornan's fall hours"* — both confirmed and closed in the markdown weeks ago; its intro claimed **two** ⭐ gating items where the README says one; and the zero-JS progress label read **"0 of 28 done"** against **36** checkboxes, 3 of them pre-checked |

**Restored to 100:**

- **The 8/22 fence is recorded as blown, and what fired is written down.** Its three questions — checkout, Ciolino's surface, the grill — each had a default, and those defaults are now simply *the plan*: ~10 AM checkout, an air mattress in Ciolino's bag, the grill eyeballed Thursday. What's left is one email, not another call, and the docs say so in all five places it appears.
- **The buckets are named for fences, not months:** *Now — by 9/7* → *By Sep 10* → *The week before* → *On the trip*, with the tram and park-pass items moved up where they belong. Same order on the dashboard.
- **The charcoal branch carries its condition.** Fire restrictions are checked, dated, and written into both the grocery list and the grill-check section: *if Stage 1 comes back, propane is legal and charcoal isn't.*
- **The dated ledger above was re-run against the outside world.** Everything load-bearing held: Moose-Wilson (closes end of day 9/7, LSR Preserve still reachable via Granite Canyon), the tram (May 16 – Oct 4, $54), both kickoffs, the $35/7-day park fee and the 2026 non-resident surcharge. Three facts are new: **Craig Pass is scheduled open through Oct 31** (so a September closure would be snow, not the season — worth knowing when you make the day-of check), the **Old Faithful overpass work finished in August**, and **Death Canyon Road and its trailhead are closed for all of 2026**, which puts a 🚫 on a reference hike and a note on its map pin.

**The rule this pass earns:** *a plan is written in a tense, and tense expires.* Every "tomorrow," "this week," "the last live item" is a fact with a shelf life, and the cheapest possible review — read the docs on a date nobody wrote them for — catches it. Worth doing on a fixed cadence, not only when something changes.
