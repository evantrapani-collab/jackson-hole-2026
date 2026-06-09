# CLAUDE.md

Trip-planning repo for a 13-person Jackson Hole / Yellowstone trip, **Sep 17–21, 2026**. No build, no tests — it's markdown plus one static HTML dashboard.

## The one rule: keep the three layers in sync

1. **Markdown folders are the source of truth** (`/itinerary`, `/dining`, `/logistics`, `/budget`, `/activities`, `/lodging`, `/packing`, plus the README's *Open Items*).
2. **`index.html` is a hand-maintained mirror** — a single offline-capable dashboard of the same content (schedule, open items/to-do checklist, dining tables, money). When you change plan content in any markdown file, **make the matching edit in `index.html`** (search it for the same keyword). It's plain static HTML; JS only adds a countdown and localStorage checkmarks.
3. **`/maps` is generated.** Never hand-edit `jackson-hole-places.csv` or `add-to-saved-list.md`. If a place is added/removed/renamed anywhere, edit the `PLACES` list in `maps/generate_places.py` and run:

   ```bash
   python3 maps/generate_places.py
   ```

## Conventions

- Open items live in **README → Open Items**, mirrored into the `index.html` to-do checklist. Load-bearing items get an owner + deadline (and ⭐ if they gate the trip).
- The trip's fixed constraints — check these before suggesting plan changes:
  - Friday is **booked dawn-to-dusk** (8 AM van tour + 1 PM rafting).
  - Saturday: Yellowstone via the **South Entrance only**, back by ~3 PM for the 5:30 PM LSU game. Anything past Old Faithful / West Thumb doesn't fit.
  - Sunday: 6:30 AM wildlife drive, Saints game at 11 AM MT.
  - Headcount is **locked at 13**; lodging is booked (Montreux House, Teton Village).
- Reference content that doesn't fit the schedule stays in the docs but gets triaged honestly (see the 🚫 flags in `activities.md` and the "triaged against our schedule" section in `dining.md`) rather than deleted.
- Times are Mountain Time unless marked CT.
