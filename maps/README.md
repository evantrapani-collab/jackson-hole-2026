# Maps — getting the trip's places onto Google Maps

**The honest constraint first:** Google does **not** offer any public API to
write to a **Saved list** (the "Travel: Jackson Hole" list in the app, the kind
you star/save places into). It's not in Google Maps Platform and there's no
import button for it. So there is *no* way to fully automate places into that
exact list — anyone who tells you otherwise is selling a browser script that
will break. What you *can* automate is the data prep and, if you're open to it,
a one-shot bulk import into **Google My Maps** (a separate, shareable custom
map).

Two practical paths, best first:

## Option A — Google My Maps (bulk, one import) ✅ most automated

This is the closest thing to "automated," and it's better for a group of 13
anyway: one shareable map, color-coded by category, with driving directions
between pins.

1. Go to **[mymaps.google.com](https://www.google.com/mymaps)** → **Create a new map**.
2. **Import** → upload **`jackson-hole-places.csv`** (in this folder).
3. When prompted:
   - Columns to position placemarks: **`Search Query`**
   - Column for the marker titles: **`Name`**
4. It geocodes every place in the CSV and drops the pins. Then **Style → Group places by
   → Category** to color them (Food, Yellowstone, Grand Teton, etc.).
5. **Share** the map link with the crew. In the Google Maps app it shows under
   **You → Maps**.

> Caveat: a My Maps map is **not** the same object as your "Saved" list, so
> these pins live on a custom map rather than inside "Travel: Jackson Hole."
> For a group trip that's usually the better container.

## Option B — top up your existing "Travel: Jackson Hole" Saved list (manual, fast)

If you specifically want them *in that list*, open
**[`add-to-saved-list.md`](./add-to-saved-list.md)**. It's a checklist of every
place as a one-tap Google Maps link. Tap → **Save** → pick **Travel: Jackson
Hole**. Items already visible in your current 19 pins are flagged so you can
skip them. It's manual, but it's seconds per place and there's no faster
*reliable* way into a Saved list.

## Regenerating

Both files are generated from one source list so they never drift:

```bash
python3 maps/generate_places.py
```

Edit the `PLACES` list in
[`generate_places.py`](./generate_places.py) (add/remove a spot, fix a note) and
re-run. Everything here is pulled from the trip markdown — dining, activities,
lodging, logistics, itinerary.

To verify the outputs are in sync without rewriting them (CI runs this on
every push/PR via `.github/workflows/maps-check.yml`):

```bash
python3 maps/generate_places.py --check
```

## Files

| File | What it's for |
|---|---|
| `jackson-hole-places.csv` | Import into Google My Maps (Option A) |
| `add-to-saved-list.md` | One-tap links for your Saved list (Option B) |
| `generate_places.py` | Source list + generator for both files |
