# CLAUDE.md

Trip-planning repo for a 13-person Jackson Hole / Yellowstone trip, **Sep 17–21, 2026**. No build, no tests — it's markdown plus one static HTML dashboard.

## The one rule: keep the three layers in sync

1. **Markdown folders are the source of truth** (`/itinerary`, `/dining`, `/logistics`, `/budget`, `/activities`, `/lodging`, `/packing`, plus the README's *Open Items*).
2. **`index.html` is a hand-maintained mirror** — a single offline-capable dashboard of the same content (schedule, open items/to-do checklist, dining tables, money). When you change plan content in any markdown file, **make the matching edit in `index.html`** (search it for the same keyword). It's plain static HTML; JS only enhances (countdown + deadline math, localStorage checkmarks, last-tab memory, TODAY badge) and is never required — the page must stay fully usable with zero JS.
3. **`/maps` is generated.** Never hand-edit `jackson-hole-places.csv` or `add-to-saved-list.md`. If a place is added/removed/renamed anywhere, edit the `PLACES` list in `maps/generate_places.py` and run:

   ```bash
   python3 maps/generate_places.py
   ```

   `--check` verifies the outputs match `PLACES` without rewriting them; CI runs it on every push/PR (`.github/workflows/maps-check.yml`).

4. **`apple-touch-icon.png` is generated too.** It's the home-screen icon iOS uses when you "Add to Home Screen" (without it Safari draws a plain letter tile). Never hand-edit the PNG — change the art constants in `icons/generate_icon.py` and run `python3 icons/generate_icon.py` (`--check` verifies it's current). Keep it at the repo root: that's where Safari probes for it, and GitHub Pages publishes the root as-is.

## Conventions

- Open items live in **README → Open Items**, mirrored into the `index.html` to-do checklist. Load-bearing items get an owner + deadline (and ⭐ if they gate the trip).
- The trip's fixed constraints — check these before suggesting plan changes:
  - Friday is **booked dawn-to-dusk** (8 AM Teton Expeditions safari + 1 PM JHWW rafting — **both out of 945 W Broadway**, check in 7:45 AM; leave the house ~6:45).
  - Saturday: Yellowstone via the **South Entrance only**, leaving **6:15 AM** with a hard **2:00 PM turnaround at West Thumb** (home ~3:50) for the 5:30 PM LSU game. Anything past Old Faithful / West Thumb doesn't fit.
  - Sunday: **6:00 AM** wildlife drive (sunrise ~7:07; Schwabacher is ~45 min out), Saints game at 11 AM MT.
  - Headcount is **locked at 13**; lodging is booked (Montreux House, Teton Village).
- Every open decision carries a **default that holds with zero action** (README → *Decision Defaults*, mirrored on the dashboard's Crew tab). When you add an open item, add what happens if nobody does anything.
- `RUBRIC.md` is a **maintainer's scorecard, not trip content** — re-grade it when plan content changes materially, but never link it or quote a score from `index.html` or the README.
- Reference content that doesn't fit the schedule stays in the docs but gets triaged honestly (see the 🚫 flags in `activities.md` and the "triaged against our schedule" section in `dining.md`) rather than deleted.
- Times are Mountain Time unless marked CT.
- **Drive times and operating calendars are load-bearing — check them against the outside world, not against this repo.** The 8/21 review found the Yellowstone legs understated by ~half, an impossible sunrise arithmetic, a lift closed for the season, and a closed road, all sitting inside items that were otherwise well-owned and well-defaulted. Two standing facts that shape everything: **Moose-Wilson Road is closed Sep 8 – Nov 15, 2026** (so every park drive goes WY-390 → WY-22 → US-26/89/191 through Jackson), and the **Bridger Gondola's season ends Sep 13** while the **Aerial Tram runs to Oct 4**.
