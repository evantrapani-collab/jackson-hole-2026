# Trip Rubric — grading the plan out of 100

A fixed scorecard for judging whether this trip plan is actually ready, not just long. Re-grade whenever plan content changes materially (a booking lands, a constraint moves, an open item closes or rots past its deadline).

**Current grade: 100/100** *(re-graded 2026-08-21, third pass — found at **94**, restored to 100; see the notes at the bottom)*

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

| Category | Points | 6/12 baseline | After 6/12 decisions | 8/4 re-grade | 8/15 found | 8/15 after | 8/20 found | 8/20 after | **8/21 found** | **8/21 after** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. Bookings & critical path | 20 | 18 | 20 | 20 | 17 | 20 | 19 | 20 | **17** | **20** |
| 2. Schedule feasibility | 15 | 14 | 15 | 15 | 15 | 15 | 14 | 15 | **8** | **15** |
| 3. Risk, safety & contingency | 15 | 14 | 15 | 15 | 13 | 15 | 15 | 15 | **15** | **15** |
| 4. Meals | 12 | 10 | 12 | 12 | 11 | 12 | 11 | 12 | **12** | **12** |
| 5. Money | 12 | 11 | 12 | 12 | 9 | 12 | 12 | 12 | **12** | **12** |
| 6. Group coordination | 10 | 9 | 9 | 10 | 7 | 10 | 10 | 10 | **9** | **10** |
| 7. Three layers in sync | 10 | 9 | 10 | 10 | 7 | 10 | 10 | 10 | **10** | **10** |
| 8. Dashboard usability | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | **6** | **6** |
| **Total** | **100** | **91** | **99** | **100** | **85** | **100** | **97** | **100** | **89** | **100** |

### What the baseline lost points for → what changed

- **Meals (−2):** Friday and Sunday dinners were "TBD" with no default. → **Defaults decided**: Friday = house (book Local/Gather by **6/30** only if the crew wants the 13-top; after that the house *is* the plan). Sunday = early Dornan's ~5 PM, backup the house.
- **Bookings (−1 recovered):** the Friday 13-top had no decision rule or expiry — now it has the 6/30 fence and a fallback that holds with zero action.
- **Schedule (−1):** Monday had no house-exit time and checkout was never on the confirm list. → Out-by-~9:45 AM added; the host ask now covers check-in **and** checkout.
- **Risk (−1):** no printable contacts card; weather fallback was just "town." → Key Contacts table added to `/logistics` + dashboard; National Museum of Wildlife Art named as the indoor scrub-day move.
- **Money (−1):** no all-in number. → ≈ **$1,150–1,400 + flights** roll-up added to `/budget` + dashboard.
- **Sync (−1):** dashboard Friday timeline listed the PM burrito pickup before the 11:30 AM lunch. → Reordered.

### 6/12 crew decisions (post-refinement re-grade)

- **Groceries have an owner: Chris Psilos** — the last ownerless load-bearing task. Bookings → 20/20 (the Friday 13-top stays unbooked, but per the scoring rules an owner + deadline + a default that holds with zero action scores full marks).
- **Explorer planned as a 7-seater → 14 seats for 13** — the seat math now works on the planning estimate. Hardie's item shifts from "confirm the trim" to "verify the 3rd row is on the reservation," and it no longer gates the trip (only the rafting refund item keeps the ⭐).

### 7/11 re-grade (expert-panel review pass)

- **Friday dinner closed as designed:** the 6/30 booking fence passed with no reservation, so the house default held with zero action — the open item is checked off everywhere, not deleted. No point change (the decision rule already scored full marks).
- **Sync fixes, no point change:** the "Now" buckets rolled June → July; the maps layer was brought back in line with the docs' triage — the permanently closed Boiling River pin removed, the far-side Yellowstone stops relabeled 🚫 "Next trip" instead of "If time," Yellowstone Lake marked as the en-route stop it is; the SLC drive time now reads ~5 hrs in both places; the dashboard's misconnect note points at `/logistics` where the playbook actually lives.
- **Grade holds at 99** — the remaining point is still the real-world verification below, not a document gap.

### 7/11 dashboard pass (same day, later)

Dashboard-only sync + usability work; no plan content changed, so the grade holds at 99.

- **Sync gaps closed:** the confirmed bed math (5 kings + 1 queen across 3 levels, 2 air mattresses for 13) now appears on the Crew tab, and the room/bed-assignments open item joined the To-Do tab — both were README/`/lodging` facts the dashboard never carried. The Money tab picked up the bring-cash note (guide tips + Pica's/Nora's), Logistics picked up the weather-scrub indoor move (National Museum of Wildlife Art) and the JHWW/Jeff contact row.
- **Misconnect playbook mirrored:** the DFW Tier 0–3 summary now lives on the Logistics tab itself — the dashboard is exactly the thing you'd be holding at DFW, so pointing at `/logistics` wasn't enough.
- **Usability:** the page now prints properly (light palette, all tabs shown, itinerary days auto-open) — the "print this" contacts card was previously unprintable in practice — and the pure-CSS tabs are keyboard-accessible (focusable radios + visible focus ring), still with zero JS required.

### 7/11 dashboard overhaul (same day, third pass)

Dashboard + maps-layer work; no plan facts changed, so the grade holds at 99.

- **Maps drift closed:** `Cowboy Coffee Co.` (dining's "must-do coffee stop"), `Pearl Street Bagels`, and `Picnic` (both named burrito-stash vendors) were in the docs but missing from the `PLACES` list — added via `generate_places.py` and regenerated (76 places).
- **Dashboard grew two tabs:** **Activities** (Sunday-afternoon choices, the Yellowstone fits-Saturday triage table, the hike reference shelf, wildlife cheat sheet, booking notes) and **Maps** (one-tap Google Maps links for every on-plan spot, grouped by day, using the same queries as the generated maps layer).
- **Full mirrors, not excerpts:** the packing checklist now carries all 47 items from `/packing` (grouped), and the To-Do tab carries all 25 open README items with owner/deadline tags — previously both were partial.
- **New surfaced-from-docs content:** who-owns-what board on Crew (named vs. open roles), on-the-ground estimates + booking tracker on Money, grocery-delivery tiers and backup-spots table on Eat & Drink, a Saturday route strip with drive times on Itinerary, getting-around + safety cards on Logistics.
- **JS enhancements (still zero-JS functional):** deadline-aware countdown messages, a hero milestone strip (8/1 → 9/10 → 9/17), computed days-left chips, a TODAY badge on the itinerary during the trip, and last-tab memory (with the restored tab scrolled into view in the nav). Checklist storage keys versioned to `_v2` so grown lists don't mis-map old saved checkmarks.
- **Sync now enforced, not just graded:** `generate_places.py --check` verifies the generated maps files match the `PLACES` list without rewriting them, and a new CI workflow (`maps-check.yml`) runs it on every push/PR — hand-edits to generated files or an unregenerated `PLACES` edit now fail loudly.

### 8/4 re-grade (date-rot pass)

First re-grade after a deadline actually passed. The rubric says to re-grade when an open item rots past its deadline — two did.

**Found at 97 (−2 from 99):**
- **−1 Money:** the 8/1 Airbnb balance came and went, and the *amount* had never been written down anywhere — every doc said "total minus deposit," which is not a number you can Venmo. §5 requires per-person amounts to be explicit.
- **−1 Bookings:** Hardie's Explorer 3rd-row verification sat in a bucket labeled "Now (July)" into August. §1 requires a deadline, and a bucket that names a month that has ended is not one.

**Restored to 99 by this pass:**
- The balance is now a number in `/budget`, README, and the dashboard: **$7,229.82 − $6,500 (13 × $500) = $729.82 ≈ $56/person** — with the honest flag that Drewes quoted ~$600/person, so it may be ~$100 and someone has to ask him which.
- The Explorer item got a hard date (**8/15**) and a ⭐ — it's the last open item that can still force a booking change, and Jackson rental inventory doesn't improve as September approaches.

**Also closed this pass (no point change — these were below the deduction line but real):**
- **Meals:** Saturday lunch had no answer at all and Monday breakfast had none either — §4 wants every slot Thu–Mon to resolve. Both now have plans (cooler lunch at West Thumb; hold burritos back for Monday). Caught only because §4 is enumerated by slot rather than judged by feel.
- **Sync:** the tram confirmation and "name who isn't on the group itinerary" existed in `/logistics` and `/activities` but never reached README's Open Items — §7 drift. Both added.
- **Travel insurance** now says what's actually still buyable in August (delay/interruption/medical, not CFAR) instead of implying the full menu is open.

### 8/4, second pass — the last point closes (100/100)

The crew called it: **the Explorer's 3rd row won't be verified in advance.** We find out at the JAC counter and make it work.

That sounds like it should *cost* a point, and under a naive reading it would — the seat math stays unconfirmed until Thursday. But §6 says pending-external-info items can't score full marks *while open*, and this one is no longer open: it's decided. The rubric's own scoring rule (top of the file) is that it **does not penalize future human actions if the plan gives them an owner, a deadline, and a default that holds if the action never happens.** An owner (Hardie, at the counter), a moment (before baggage claim), and a default that holds with zero advance work (add a third car if it's 12 seats) is exactly that.

What earned the point was writing the fallback down rather than leaving "we'll make it work" as a feeling:
- The **worst case is named** — 5 + 7 = 12 seats for 13, one short.
- The **two failure modes are separated**, which nobody had done: the airport legs are trivially fixable (JAC→house is ~10 min, do a second run), but **Saturday and Sunday are not** — all 13 have to move at once, 1.5 hrs out, and no amount of shuttling solves that. That distinction is the whole reason a third car might be needed, and it was invisible while the item was phrased as "verify the trim."
- The **fix is priced** (~$400–500 ÷ 13 ≈ $35/person) so it's a shrug at the counter, not a debate.
- The **decision moment is placed** — Hardie and Schick already hit the rental counter before baggage claim, so the seat count is known while there's still a counter to solve it at.

**Grade: 100/100.** Every remaining open item now has an owner, a deadline, or a default that holds without anyone doing anything. The trip can still go sideways — that's trips — but it won't go sideways because of something this repo failed to say.

*(The bed-math half of the old deduction closed earlier: the house is confirmed at 5 kings + 1 queen across 3 levels, and beds-on-arrival is a decision, not a gap.)*

---

### 8/15 re-grade — found at 85, restored to 100

Eleven days and a lot of group-chat traffic after the last pass: Drewes posted the final $784.14 number (8/10), four guys paid in full (8/11), the brewery recon and the reservations question landed. The plan got **more decided** in that window and **less finished**, which is the failure mode this rubric exists to catch.

**Found at 85 (−15).** Two of the deductions are new rot; most are gaps the 8/4 pass graded generously, and the rubric now has language that makes them unmissable.

| # | Cat | Deduction | What was actually wrong |
|---|---|---|---|
| −3 | §1 | Three ownerless load-bearing tasks | Check-in/checkout, Ciolino's ⭐ sleeping surface, and the grill/propane check were all "someone should call." The dashboard was honest enough to tag one of them `needs owner`, which is a gap admitting to itself. The tram — the thing the whole Sunday afternoon rests on — had no date and no answer for "what if it isn't running" |
| −2 | §3 | No DD plan | "Name designated drivers per SUV" had been in three documents since June without ever naming one. A plan to make a plan is not a plan, and this is the drinking-and-driving line item |
| −1 | §4 | Friday menu had no zero-action default | The grocery list carried both branches, so Psilos was covered — but nobody had said which meal happens if the Sep 10 call never picks |
| −2 | §5 | Two men's amounts weren't numbers | Austin and Solak each owed "**$784.14 — or $534.14** if the Gunter $250 counts." Nine days of it sitting there, one Venmo away from either double-paying or shorting the guy fronting $10k |
| −1 | §5 | Stale money lines | `/lodging` still showed "**Balance due 8/1** — total minus $500 deposit"; `/logistics` still said Drewes "collects closer to the trip; final amount depends on headcount." Both superseded on 8/10 |
| −3 | §6 | Three ownerless roles | Grill captain, park pass, bear spray. The README *named the problem out loud* — "six decisions still have no name attached… all pointed at the same Sep 10 call, which is how a call runs 90 minutes and decides nothing" — and then left all six pointed at that call. Naming a risk is not mitigating it |
| −3 | §7 | Three number divergences | All-in per person read **$1,150–1,400** on the Overview tab and **$1,100–1,330** on the Money tab of the same page; the Crew tab still said the seat math "works once the 3rd row is verified" eleven days after we decided not to verify it; the Maps tab advertised a **76**-place file that the generator builds with **75** |

**Restored to 100 by this pass.** One structural change did most of the work — a **Decision Defaults** table in the README, mirrored to the dashboard's Crew tab, that gives every open decision an owner, a date, and *what happens if nobody does anything*:

- **The three ownerless calls became one owned call.** RMR only takes questions from the guest of record, so the check-in, cot, and grill questions route through **Drewes** by **8/22** — and each has a default that holds if the call never happens: the times we already assume, a mattress Ciolino packs regardless, and a grill you eyeball Thursday at check-in with an oven reverse-sear behind it. Ciolino's item **loses its ⭐** for the same reason the Explorer did: a fallback that needs no advance work isn't a gate.
- **The DD gap closed on a fact nobody had written down.** Only Hardie and Schick are on the rental agreements, so they're the only two insured to drive those SUVs — the DD question was already answered by the contracts. Rotating means adding an authorized driver at the JAC counter, which is a 60-second ask you're standing in line for anyway.
- **The $250 got a tiebreak instead of a conversation:** unsettled by 8/22 → send the full $784.14, because an overpayment comes back with one Venmo and a shortfall sits on the man who already paid the VRBO and the outfitter.
- **Park pass stopped being a role and became arithmetic** — 2 vehicles × 2 parks × $35 = $140 against $160 for two passes, so the default is the gate and the only action left is one question in the chat. Bear spray stopped being a role by riding a trip someone already owns, at ~$8/man on the grocery bill.
- **Both game-night branches got dinners.** Steak night stays Saturday; if it moves, Saturday drops to the house off grocery stock and Dornan's is void. Friday's menu defaults to the fajita bar — the branch whose leftovers *are* Saturday's cooler lunch.
- **Sync:** the all-in number reads $1,100–1,330 in both places (and the estimate line was re-added correctly at ~$120–220 now that bear spray and park entry are per-man figures), the Crew tab matches the Explorer decision, the maps count reads 75, and the two breweries that became real Saints-game candidates got their `PLACES` entries updated and regenerated.

**Grade: 100/100.** The test this pass was built around: *for every open item, if nobody does anything, what happens?* Ten items had no answer to that on 8/15. All ten have one now, and the Sep 10 call went from carrying the plan to confirming it.

### 8/15, second pass — the money closes, a new fence opens

Same day, after the crew's own updates landed: **everyone paid Drewes.** All 13 settled, $10,193.82 collected, and the Gunter $250 ambiguity — the §5 deduction from this morning — closed with it rather than by the 8/22 tiebreak rule. The rule did its job by existing: it stopped being needed. **Grade holds at 100**; §5's fix went from "a tiebreak that makes the number explicit" to "the number is paid," which is strictly better.

Three things the same batch of notes surfaced, and what the rubric did with them:

- **A new time-fence, caught by §1.** The Cowboy Steakhouse books **30 days out**, so the window for our dates opens **8/17** and closes on its own. That's exactly the "books-out-months venue" criterion, and it was a day away from being missed. It's in Open Items with a date and a default (*nobody calls, house steak nights stand*) — and Snake River Grill's **private room** is now written down, since a room is the one thing that makes a 13-top easy.
- **An assumption got falsified, which is worth more than a fix.** Late September isn't shoulder season here — **shoulder season now starts in October, and September is one of the busier months.** That assumption was load-bearing in four places: walk-in odds for a 13-top (worse than we thought), tram operating dates and Dornan's fall hours (*better* than we thought), and — the one that actually matters — **JAC rental inventory**, which is the fallback behind the whole Explorer seat-count plan. All four now read honestly. §2 and §3 hold because the *plans* didn't change; what changed is that they no longer rest on a wrong belief.
- **Route advice adopted, and honestly triaged.** A frequent visitor's Yellowstone routing is now the Saturday plan — **Grand Prismatic overlook first, then skip the boardwalk** (which buys back a stop on our tightest day), then Old Faithful, then West Thumb. The half of his route we can't take (Emerald Spring, the canyon waterfalls) went into the 🚫 bucket with the drive-time reasoning, per the repo's triage-don't-delete convention. His offline audio-tour rec is now on the pre-trip list, which is a genuine fit for a park with no signal.

One open decision was **added** rather than closed: Drewes's idea to open Thursday at **Dornan's** (~8 min from JAC) to decompress and acclimate before hitting town. It scores fine because it arrived with a default already attached — the current Thursday plan holds unless someone calls it — and with the knock-on named: if Dornan's happens Thursday, Sunday's dinner slot needs re-picking.

### 8/15, third pass — check-in lands, and Thursday gets a real clock

**Check-in is 4:00 PM, confirmed.** That answers a third of the RMR call and, more usefully, *sizes the day*: the gap from a 10:19 AM landing is **~5 hours**, not the "4–5" these docs had been guessing, and all thirteen guys' luggage rides along for it. Early check-in is asked for but not promised and may carry a charge — so it's recorded as a bonus, not a plan. §1 holds: the item narrows to checkout + cot + grill, each still carrying its default.

Drewes's afternoon (**Dornan's → brewery in town → gondola at Teton Village → 4 PM check-in → out for the night**) went from *option with a default* to *the shape of the day*, and writing it as a clock is what surfaced three things a prose paragraph would have hidden:

1. **Bear spray falls off the itinerary, and it's the one item that can't slip.** You can't fly with it and Friday is booked dawn-to-dusk, so Thursday is the only window — the new plan quietly deleted the stop that was carrying it. §3 would have taken −2 for a safety item with no place on the schedule; instead it has two written solves and a rule ("don't leave for Teton Village without a canister in each vehicle").
2. **The DD job now starts at lunch.** Beer at Dornan's around 11:30, more at the brewery at 1:15, then two drives. The §3 fix from this morning — Hardie and Schick are the only insured drivers — was written for *one* leg at night. Under this plan it's a much bigger ask, and saying so is the honest version.
3. **Two lifts, not one.** Thursday says "gondola," Sunday says "tram." At Teton Village those are different rides — the Bridger Gondola to mid-mountain and the Aerial Tram to the 10,450 ft summit where the Corbet's waffles are. If Thursday ends up on the tram, **Sunday's afternoon needs a different answer**. Same class of catch as the Dornan's double-booking: a plan can collide with itself, and §2's timing arithmetic won't catch it because nothing about the clock is wrong.

**Grade holds at 100.** Nothing here was a deduction — the plan absorbed a confirmed fact and a new proposal without opening a gap, which is what the Decision Defaults structure was built to do. The clock table is the pattern worth reusing: *when a day's plan gets more than three moving parts, write the times down, because the seams only show up next to a clock.*

---

### 8/20 re-grade — the Friday confirmations land (found at 97, restored to 100)

Both Friday confirmations came in on the same day: **Teton Expeditions** for the 8 AM Grand Teton sunrise safari (party of 13, 4 hours) and **Jackson Hole Whitewater** for the 1:00–4:30 PM "Classic Raft." Two facts in them reshaped the day, and one of them corrected these docs.

**What the confirmations changed, and what it didn't cost:**

- **Friday is two outfitters, not one.** Every document in this repo said "JHWW van + boat" — one vendor, one contract. It's two. **That costs nothing under §1**: the repo faithfully recorded what the crew believed, and a confirmation email is exactly the mechanism that corrects a belief. The plan didn't change; the names on it did. What it *does* change is real: **two tips, not one**, and two numbers to call on a dawn-to-dusk day.
- **Both trips leave from the same building — 945 W Broadway.** This is a schedule fact the plan was working around without knowing it existed. Friday's midday reposition, which every version of these docs quietly assumed, doesn't exist.

**Found at 97 (−3).** All three are things the repo could have said before the email arrived, not things the email revealed:

| # | Cat | Deduction | What was actually wrong |
|---|---|---|---|
| −1 | §1 | The outfitter contact row was a placeholder | The Key Contacts card — the printable one, for a trip with no cell service — carried *"number is on the signed contract, copy it here when printing"* for the single vendor running the only fully-booked day of the trip. A contacts card with a TODO in it is not a contacts card. **JHWW is 307-733-1007**; it's written down now, in both layers |
| −1 | §2 | Friday had no arithmetic before 8:00 AM | §2 wants each day's timing to actually work. Friday's schedule started *at* the tour: no house departure, no drive time, no arrival buffer — while the same page told everyone to be 30 minutes early for the afternoon boat. The confirmation's **"15 minutes prior"** turns that into a real clock: **7:45 check-in → ~7:00 wheels up**, with coffee as the only stop that fits. That hour existed before the email; nobody had written it |
| −1 | §4 | Friday lunch was a slot premised on a drive | The plan put lunch at *"Cutty's — between the van tour and the rafting put-in."* There is no *between*; both trips stage from the same lot. The slot had a venue but the wrong shape — a ~45-minute window in a parking lot, not a stop on a route |

**Restored to 100 by this pass:**

- **The day is now clocked end to end** — leave ~7:00, check in 7:45, safari 8:00–~noon, lunch, raft check-in 12:30, water 1:00–4:30 — in `/itinerary`, the dashboard's Friday block, and both Key Times tables. The flagged risk is the honest one: **getting 13 guys out the door by 7 is harder than the drive.**
- **Friday lunch got re-decided against the real constraint.** Default is the **outfitter deli** (zero travel, nobody misses the boat); **Sidewinders is next door** in the same complex; **Cutty's is now a ~25-min round trip out of a ~60-min window** and is relabeled a Sunday option. Free win: Sidewinders was already on the Sunday game-venue recon list, and we're parked next to it for six hours — **the recon is now a lunch stop**, not a separate errand.
- **A new open item, with a default:** JHWW requires **every party member to sign the online waiver before arrival**, and says the confirmation email can be forwarded. It carries an owner (whoever holds the confirmation), a date (**9/10**, riding along with the call everything else points at), and a zero-action default — *thirteen guys filling out forms in the boathouse lot at 12:15, out of a ~45-minute lunch break.* Per §1 that scores full marks: it's a cost, not a gate. **No new ⭐** — the rafting late-cancel rule is still the only one.
- **The no-alcohol rule got bigger and is stated as such.** Teton Expeditions bans it outright in writing; JHWW's rule covers the van and the boat. Friday's only drinking window is the lunch hour, and it's the hour before a Class 2–3 river. Worth saying plainly to a group whose Thursday is a bar crawl.
- **Sync + maps:** the boathouse is a new `PLACES` entry (**81 places**, regenerated, `--check` clean), Sidewinders' and Cutty's entries were corrected to match their real geography, and the Teton Expeditions / JHWW split now reads identically in the README, `/itinerary`, `/logistics`, `/dining`, `/activities`, `/budget`, `/packing` and `index.html`.

**One thing left open on purpose:** Teton Expeditions' email doesn't mention a waiver either way. That's a question on the pre-trip list, not an assumption — and the default (there's one to sign on-site) is the safe reading.

**Grade: 100/100.** The pass didn't add a plan; it removed a phantom drive, put an hour back on the clock that nobody had written down, and gave a vendor requirement an owner before it could become a parking-lot scramble.

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

## Verified external facts — checked 2026-08-21

Maintainer's ledger. These are the claims the plan *depends on* that live outside this repo, and the two most recent passes proved that confident prose is no evidence any of them were ever checked. Re-check before the trip; anything with a date fence rots silently.

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
| Bear Aware kiosk, JAC | Baggage claim #3, Jun–Oct, ~$28/canister capped | bearaware.com |
| Park entry | $35/vehicle/park, **7-day**; +$100 non-resident surcharge (2026) | nps.gov |
| DFW→JAC nonstops | 2 daily, year-round | AA app |
| LSU–Ole Miss | Sat 9/19, 5:30 PM MT, ABC | — |
| Saints @ Ravens | Sun 9/20, 11:00 AM MT, CBS | — |

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
