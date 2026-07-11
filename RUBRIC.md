# Trip Rubric — grading the plan out of 100

A fixed scorecard for judging whether this trip plan is actually ready, not just long. Re-grade whenever plan content changes materially (a booking lands, a constraint moves, an open item closes or rots past its deadline).

**Current grade: 99/100** *(re-graded 2026-07-11 — grade unchanged; see the 7/11 note at the bottom)*

---

## How scoring works

Each category starts at full points; deduct per the criteria. The rubric grades **the plan and its documents** — it does not award points for the trip itself going well, and it does not penalize future human actions *if* the plan gives them an owner, a deadline, and a default that holds if the action never happens.

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
- The two trip-gating items (⭐) are flagged and tracked (−3 if not)
- Anything time-fenced (refund cutoffs, books-out-months venues) has its real deadline written down (−2 each)
- Load-bearing tasks aren't ownerless (−1 each)

### 2. Schedule feasibility vs. fixed constraints (15)

The fixed constraints (CLAUDE.md): Friday booked dawn-to-dusk; Saturday Yellowstone via South Entrance, back ~3 PM for the 5:30 LSU game; Sunday 6:30 AM drive + 11 AM Saints; 13 locked; Montreux House booked.

- Every day's timing arithmetic actually works (drive times, eruption windows, kickoff buffers) (−2 per broken day)
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
- Early starts (Sat 7 AM, Sun 6:30 AM) have a no-cooking answer (−2 if not)
- 13-top reality acknowledged: reservations flagged where needed, walk-in assumptions justified (−2 if not)
- The grocery plan covers acquisition (who/how/when), incl. the 13-ribeye volume problem (−2 if not)

### 5. Money — totals, splits, deadlines (12)

- Per-person amounts, due dates, and who collects are explicit (−2 each gap)
- A single **all-in per-person planning number** exists (−1 if you have to add it up yourself)
- Cash needs (tips, cash-only spots) called out (−1)
- Booking tracker reflects reality (−1 if stale)

### 6. Group coordination (10)

- Headcount, roster, and seat math (13 bodies vs. vehicle seats) tracked with the gap flagged (−2 if not)
- Bed math (13 vs. 6 beds) acknowledged with an assignment plan/deadline (−2 if not)
- Drivers, DDs, grill captain, departure-time owners: named or explicitly pending with a deadline (−1 each ownerless role)
- Pending-external-info items (e.g., Explorer trim, bed count) can't score full marks until answered (−1 each while open)

### 7. Three layers in sync (10)

- Every plan fact appears identically in markdown and `index.html` (−1 per divergence)
- `/maps` regenerated whenever places change; no hand-edits to generated files (−2 per violation)
- Open Items (README) ↔ To-Do tab (dashboard) match (−1 per drift)

### 8. Dashboard usability (6)

- Works offline, zero-JS functional (−2 if not)
- Timelines in chronological order, times labeled MT/CT correctly (−1 each defect)
- Open items carry their owner/deadline tags (−1 if stripped)

---

## Scorecard

| Category | Before (6/12 baseline) | After refinements | After 6/12 crew decisions |
|---|---|---|---|
| 1. Bookings & critical path | 18 | 19 | 20 |
| 2. Schedule feasibility | 14 | 15 | 15 |
| 3. Risk, safety & contingency | 14 | 15 | 15 |
| 4. Meals | 10 | 12 | 12 |
| 5. Money | 11 | 12 | 12 |
| 6. Group coordination | 9 | 9 | 9 |
| 7. Three layers in sync | 9 | 10 | 10 |
| 8. Dashboard usability | 6 | 6 | 6 |
| **Total** | **91** | **98** | **99** |

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
- **JS enhancements (still zero-JS functional):** deadline-aware countdown messages, a hero milestone strip (8/1 → 9/10 → 9/17), computed days-left chips, a TODAY badge on the itinerary during the trip, and last-tab memory. Checklist storage keys versioned to `_v2` so grown lists don't mis-map old saved checkmarks.

### The remaining point (honest, not fixable by documents)

- **−1 Group coordination:** bed math (what the house actually sleeps) is pending the host's answer, and the Explorer's 7 seats is an estimate until the reservation is verified; room/seat assignments can't be finished until both land.

Close those in the real world and this is a 100.
