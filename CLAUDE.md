# CLAUDE.md

Trip-planning repo for a 13-person Jackson Hole / Yellowstone trip, **Sep 17–21, 2026**. No build, no tests — markdown plus one static HTML dashboard.

## Keep it short

This is a guys' trip, not a program. The docs exist so somebody can find a phone number at 6 AM — **not** to record how a decision was reached. Write the outcome, drop the reasoning, and let git history be the changelog. If a section would still be correct after deleting it, delete it.

Specifically, don't reintroduce: owner/deadline/default tables for every open item, "what happens if nobody does anything" defaults, dated changelog markers (🆕, "changed 9/9") inside the prose, tiered contingency playbooks, or a scoring rubric.

## The one rule: keep the layers in sync

1. **Markdown folders are the source of truth** (`/itinerary`, `/dining`, `/logistics`, `/budget`, `/activities`, `/lodging`, `/packing`, plus README → *Open Items*).
2. **`index.html` is a hand-maintained mirror** — one offline-capable dashboard of the same content. When you change plan content in a markdown file, **make the matching edit in `index.html`** (search it for the same keyword). JS only enhances (countdown, localStorage checkmarks, last-tab memory, TODAY badge) — the page must stay fully usable with zero JS, so keep the static progress-label counts (`0 of N`) matching the real checkbox counts.
3. **`/maps` is generated.** Never hand-edit `jackson-hole-places.csv` or `add-to-saved-list.md`. Edit the `PLACES` list in `maps/generate_places.py` and run:

   ```bash
   python3 maps/generate_places.py
   ```

   `--check` verifies the outputs match without rewriting them; CI runs it on every push/PR.

4. **`apple-touch-icon.png` is generated too** — change the art constants in `icons/generate_icon.py` and run it (`--check` verifies). Keep it at the repo root; that's where Safari looks. **`manifest.json`** is the Android equivalent and is hand-maintained — if the app name or theme color in `index.html`'s `<head>` changes, update it to match.

## Conventions

- Open items live in **README → Open Items**, mirrored into the `index.html` To-Do tab — **those two, and nowhere else.**
- The trip's fixed constraints — check these before suggesting plan changes:
  - Friday is **booked dawn-to-dusk** (8 AM Teton Expeditions safari + 1 PM JHWW rafting — **both out of 945 W Broadway**, check in 7:45; leave the house ~6:45).
  - Saturday: Yellowstone via the **South Entrance only**, leaving **6:15 AM** with a hard **2:00 PM turnaround at West Thumb** (home ~3:50) for the 5:30 PM LSU game.
  - Sunday: **6:00 AM** wildlife drive (sunrise ~7:07; Schwabacher is ~45 min out), Saints at 11 AM MT.
  - Headcount is **locked at 13**; lodging is booked (Montreux House, Teton Village).
- Times are Mountain unless marked CT.
- **Drive times and operating calendars are load-bearing — check them against the outside world, not against this repo.** Past reviews found the Yellowstone legs understated by half, an impossible sunrise, a lift closed for the season, and a closed road. Two standing facts: **Moose-Wilson Road is closed Sep 8 – Nov 15, 2026** (every park drive goes WY-390 → WY-22 → US-26/89/191 through Jackson), and the **Bridger Gondola's season ends Sep 13** while the **Aerial Tram runs to Oct 4**.
