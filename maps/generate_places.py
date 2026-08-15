#!/usr/bin/env python3
"""
Generate Google Maps import artifacts from the trip's named locations.

Outputs two files in this folder:
  - jackson-hole-places.csv  -> import into Google My Maps (bulk, auto-geocoded)
  - add-to-saved-list.md     -> clickable links to top up the existing
                                "Travel: Jackson Hole" Saved list by hand

Source of truth is the PLACES list below. Edit it and re-run:
    python3 maps/generate_places.py

Every place is pulled from the markdown in this repo (dining, activities,
lodging, logistics, itinerary). `query` is what Google geocodes — a plain
"Name, Area, WY" string resolves to the right pin more reliably than a
hand-typed street address, so that's what we use except where the repo gives
an explicit address.
"""

import csv
import io
import os
import sys
import urllib.parse

# (name, category, when, query, already_in_list, note)
PLACES = [
    # --- Lodging & Logistics ---
    ("Montreux House (the Airbnb)", "Lodging & Logistics", "Base", "3720 Morley Dr, Teton Village, WY 83025", True, "Booked. 5 BR / 6 beds for 13."),
    ("Jackson Hole Airport (JAC)", "Lodging & Logistics", "Thu / Mon", "Jackson Hole Airport, WY", True, "Fly in 10:19 AM Thu; depart 11:47 AM Mon. Rental pickup."),
    ("St. John's Health (hospital)", "Lodging & Logistics", "Emergency", "St. John's Health, 625 E Broadway, Jackson, WY", False, "Nearest 24-hr ER, ~25 min from the house."),
    ("Smith's Food and Drug", "Lodging & Logistics", "Thu", "Smith's Food and Drug, Jackson, WY", False, "Grocery run on arrival (ribeyes, sides)."),
    ("Albertsons", "Lodging & Logistics", "Thu", "Albertsons, Jackson, WY", False, "Grocery alternative to Smith's."),

    # --- Food & Drink ---
    ("Jackson Drug", "Food & Drink", "Thu", "Jackson Drug, Jackson, WY", False, "Huckleberry shake on the town square."),
    ("Snake River Brewing", "Food & Drink", "Thu night / Sun game", "Snake River Brewing, Jackson, WY", False, "Bar crawl stop 1; also the other brewery big enough for all 13 at the Saints game."),
    ("Silver Dollar Bar (Wort Hotel)", "Food & Drink", "Thu night", "Silver Dollar Bar, Wort Hotel, Jackson, WY", False, "Bar crawl stop 2 — silver-dollar bar top."),
    ("Million Dollar Cowboy Bar", "Food & Drink", "Thu night", "Million Dollar Cowboy Bar, Jackson, WY", False, "Bar crawl stop 3 — saddle stools."),
    ("Mangy Moose Saloon", "Food & Drink", "Thu night", "Mangy Moose, Teton Village, WY", False, "Bar crawl last stop — walkable from the house."),
    ("The Bunnery", "Food & Drink", "Fri AM", "The Bunnery, Jackson, WY", False, "Pastries/coffee on the way to the 8 AM van tour."),
    ("Cowboy Coffee Co.", "Food & Drink", "Fri AM", "Cowboy Coffee Co, Jackson, WY", False, "The must-do coffee stop on the square; to-go on the way to the van tour."),
    ("Pearl Street Bagels", "Food & Drink", "Burrito stash", "Pearl Street Bagels, Jackson, WY", False, "Breakfast-burrito vendor option for the early-start stash."),
    ("Picnic", "Food & Drink", "Burrito stash", "Picnic, Jackson, WY", False, "Breakfast-burrito vendor option for the early-start stash."),
    ("Cutty's Bar & Grill", "Food & Drink", "Fri / Sun", "Cutty's Bar & Grill, Wilson, WY", True, "Friday rafting lunch; Sunday Saints-game option (Hwy 22)."),
    ("Dornan's Pizza Pasta Co.", "Food & Drink", "Sun", "Dornan's Pizza Pasta Co, Moose, WY", False, "Deck pizza with full Teton views."),
    ("Corbet's Cabin (tram summit)", "Food & Drink", "Sun PM", "Corbet's Cabin, Teton Village, WY", False, "Waffles at 10,450 ft, top of the tram."),
    ("Gun Barrel Steak & Game House", "Food & Drink", "Alt dinner", "Gun Barrel Steak and Game House, Jackson, WY", False, "Wild-game steakhouse; Thursday dinner alt."),
    ("Leek's Pizzeria", "Food & Drink", "If up north", "Leek's Pizzeria, Grand Teton National Park, WY", False, "Jackson Lake / Colter Bay; only if that far north."),
    ("Mural Room (Jackson Lake Lodge)", "Food & Drink", "Aspirational", "Mural Room, Jackson Lake Lodge, WY", False, "Big Teton windows; reservations; ~45-60 min north."),
    ("Jenny Lake Dining Room", "Food & Drink", "Aspirational", "Jenny Lake Lodge Dining Room, Grand Teton, WY", False, "Upscale; reservations required; short fall season."),
    ("Jackson Hole Playhouse", "Food & Drink", "Optional", "Jackson Hole Playhouse, Jackson, WY", False, "Dinner + live Western musical; whole evening."),
    ("Pica's Mexican Taqueria", "Food & Drink", "Backup", "Pica's Mexican Taqueria, Jackson, WY", False, "Cheap, legendary, cash only."),
    ("Snake River Grill", "Food & Drink", "Backup", "Snake River Grill, Jackson, WY", False, "Upscale, on the square."),
    ("Persephone Bakery", "Food & Drink", "Backup", "Persephone Bakery, Jackson, WY", False, "Best coffee in town; croissants."),
    ("Nora's Fish Creek Inn", "Food & Drink", "Backup", "Nora's Fish Creek Inn, Wilson, WY", False, "Iconic Wyoming diner breakfast; cash only."),
    ("Thai Me Up", "Food & Drink", "Backup", "Thai Me Up, Jackson, WY", False, "Beloved locals' Thai spot."),
    ("Eleanor's", "Food & Drink", "Sun", "Eleanor's, Jackson, WY", False, "Saints-game watch option; verify pin."),
    ("Local Restaurant & Bar", "Food & Drink", "Fri dinner cand.", "Local Restaurant and Bar, Jackson, WY", False, "Friend rec; great happy hour. Top Friday 13-top candidate."),
    ("Gather", "Food & Drink", "Fri dinner cand.", "Gather, Jackson, WY", False, "Friend rec; group-friendly. Top Friday 13-top candidate."),
    ("The Bistro", "Food & Drink", "Fri dinner cand.", "The Bistro, Jackson, WY", False, "Friend rec for breakfast and dinner; Friday candidate."),
    ("Figs", "Food & Drink", "Fri dinner cand.", "Figs, Hotel Jackson, Jackson, WY", False, "Lebanese at Hotel Jackson; Friday candidate."),
    ("Kampai", "Food & Drink", "Splinter group", "Kampai, Jackson, WY", False, "Sushi; too small for 13 — splinter or pre-dinner."),
    ("Bin22", "Food & Drink", "Splinter group", "Bin22, Jackson, WY", False, "Wine bar + tapas; too small for 13 — pre-dinner stop."),
    ("Coe Tavern", "Food & Drink", "Drinks", "Coe Tavern, Jackson, WY", False, "Rooftop drinks + snacks; pre-dinner stop."),
    ("Roadhouse Brewing Co.", "Food & Drink", "Sun game / Thu alt", "Roadhouse Brewing Co, Jackson, WY", False, "Big enough to seat all 13 without a reservation — top Saints-game option; great happy hour Thursday."),
    ("Sidewinders Tavern", "Food & Drink", "Sun game", "Sidewinders Tavern, Jackson, WY", False, "Sports tavern just down from Teton Village — closest game-watching option to the house (Jeremy rec)."),
    ("The Verge", "Food & Drink", "Thu night alt", "The Verge, Jackson, WY", False, "Liquor in front, dive bar in back (AJAX rec). Bar-crawl flavor, not a dinner."),
    ("Jackson Whole Grocer", "Lodging & Logistics", "Thu", "Jackson Whole Grocer, Jackson, WY", False, "Third grocery/butcher option if Albertsons and Smith's are out of Prime."),
    ("D.O.G.", "Food & Drink", "Burrito stash", "D.O.G., Jackson, WY", False, "Friend's burrito pick; bulk-order option for the early-start stash."),
    ("Creekside Market & Deli", "Food & Drink", "Sun / cooler", "Creekside Market and Deli, Jackson, WY", False, "Sandwiches before heading into the parks."),
    ("Pearl Street Market (sloshies)", "Food & Drink", "Thu", "Pearl Street Market, Jackson, WY", False, "Friend's sloshie favorite; downtown quick hit."),
    ("Merry Piglets", "Food & Drink", "Backup", "Merry Piglets, Jackson, WY", False, "Tex-Mex near the square; casual backup."),
    ("Hand Fire Pizza", "Food & Drink", "Backup", "Hand Fire Pizza, Jackson, WY", False, "Pizza in the old theater; casual backup + burrito vendor."),
    ("Healthy Being Juicery", "Food & Drink", "Optional", "Healthy Being Juicery, Jackson, WY", False, "Smoothies/juices if anyone needs a reset."),

    # --- Grand Teton National Park ---
    ("Grand Teton — Moose / Visitor Center", "Grand Teton NP", "Fri/Sun", "Craig Thomas Discovery and Visitor Center, Moose, WY", False, "South park gateway; near Dornan's & Schwabacher."),
    ("Jenny Lake", "Grand Teton NP", "Optional hike", "Jenny Lake, Grand Teton National Park, WY", True, "Loop trail; get there before 8 AM."),
    ("Hidden Falls & Inspiration Point", "Grand Teton NP", "Optional hike", "Inspiration Point, Grand Teton National Park, WY", False, "Waterfall + panorama off Jenny Lake."),
    ("Cascade Canyon Trailhead", "Grand Teton NP", "Optional hike", "Cascade Canyon Trailhead, Grand Teton, WY", False, "To Lake Solitude; best fall colors."),
    ("Taggart Lake Trailhead", "Grand Teton NP", "Optional hike", "Taggart Lake Trailhead, Grand Teton, WY", False, "Taggart & Bradley Lakes loop."),
    ("Death Canyon Trailhead", "Grand Teton NP", "Optional hike", "Death Canyon Trailhead, Grand Teton, WY", False, "Dramatic canyon walls."),
    ("Lupine Meadows Trailhead", "Grand Teton NP", "Optional hike", "Lupine Meadows Trailhead, Grand Teton, WY", False, "Access for Amphitheater Lake."),
    ("String Lake", "Grand Teton NP", "Optional", "String Lake, Grand Teton National Park, WY", False, "Calm paddling; no motors."),
    ("Oxbow Bend", "Grand Teton NP", "Sun sunrise", "Oxbow Bend, Grand Teton National Park, WY", False, "Moose/elk + classic Teton reflection."),
    ("Schwabacher Landing", "Grand Teton NP", "Sun sunrise", "Schwabacher Landing, Grand Teton National Park, WY", False, "The signature sunrise; first light ~6:40."),
    ("Mormon Row Historic District", "Grand Teton NP", "Sun sunrise", "Mormon Row Historic District, WY", False, "Barns + bison against the Tetons."),
    ("Antelope Flats Road", "Grand Teton NP", "Sun sunrise", "Antelope Flats Road, Grand Teton, WY", False, "Pronghorn, bison, coyotes."),
    ("Moose-Wilson Road", "Grand Teton NP", "Sun sunrise", "Moose-Wilson Road, Grand Teton, WY", False, "Moose and bears; drive slow."),
    ("Jackson Lake Lodge (Willow Flats)", "Grand Teton NP", "Optional", "Jackson Lake Lodge, WY", False, "Moose hotspot at Willow Flats."),
    ("Jackson Hole Aerial Tram", "Grand Teton NP", "Sun PM", "Jackson Hole Aerial Tram, Teton Village, WY", False, "Rendezvous Mtn summit; Corbet's waffles up top."),
    ("Colter Bay Village", "Grand Teton NP", "If up north", "Colter Bay Village, Grand Teton National Park, WY", True, "Jackson Lake; near Leek's Marina."),

    # --- Yellowstone National Park ---
    ("Yellowstone South Entrance", "Yellowstone NP", "Sat", "Yellowstone South Entrance, WY", False, "~1 hr from Jackson; our gate (unaffected by 2026 closures)."),
    ("Old Faithful", "Yellowstone NP", "Sat", "Old Faithful, Yellowstone National Park, WY", True, "Check predicted eruption (~90-min cycle)."),
    ("Grand Prismatic Spring", "Yellowstone NP", "Sat — skippable", "Grand Prismatic Spring, Yellowstone, WY", True, "The boardwalk. If you do the overlook, you can skip going close to it."),
    ("Fairy Falls Trailhead (overlook)", "Yellowstone NP", "Sat — 1st stop", "Fairy Falls Trailhead, Yellowstone, WY", False, "Grand Prismatic overlook — do this FIRST, then skip the boardwalk below."),
    ("West Thumb Geyser Basin", "Yellowstone NP", "Sat", "West Thumb Geyser Basin, Yellowstone, WY", True, "On the way back; quick and worth it."),
    ("Emerald Spring (Norris)", "Yellowstone NP", "🚫 Next trip", "Emerald Spring, Norris Geyser Basin, Yellowstone, WY", False, "Jeremy's favorite pool — but it's Norris, well past our 3 PM turnaround."),
    ("Norris Geyser Basin", "Yellowstone NP", "🚫 Next trip", "Norris Geyser Basin, Yellowstone, WY", True, "Hottest, most active; Steamboat Geyser. Too far for our Sat window."),
    ("Mammoth Hot Springs", "Yellowstone NP", "🚫 Next trip", "Mammoth Hot Springs, Yellowstone, WY", True, "Travertine terraces (far north). Too far for our Sat window."),
    ("Artists' Paintpots", "Yellowstone NP", "🚫 Next trip", "Artists Paintpots, Yellowstone, WY", False, "Accessible, less crowded. Too far for our Sat window."),
    ("Grand Canyon of the Yellowstone", "Yellowstone NP", "🚫 Next trip", "Grand Canyon of the Yellowstone, WY", True, "Artist Point is the iconic view. Adding it blows the 3 PM return."),
    ("Lamar Valley", "Yellowstone NP", "🚫 Next trip", "Lamar Valley, Yellowstone National Park, WY", False, "'America's Serengeti'; wolves, bison (far NE) — 3+ hrs one-way."),
    ("Hayden Valley", "Yellowstone NP", "🚫 Next trip", "Hayden Valley, Yellowstone National Park, WY", False, "Bison, grizzlies; well past our West Thumb turnaround."),
    ("Yellowstone Lake", "Yellowstone NP", "Sat (en route)", "Yellowstone Lake, WY", False, "Osprey, eagles, cutthroat trout; you drive its shore between West Thumb and the South Entrance."),
    ("Mount Washburn", "Yellowstone NP", "🚫 Next trip", "Mount Washburn, Yellowstone, WY", False, "Lookout tower; 360° views; central park, too far."),

    # --- Jackson Town ---
    ("Jackson Town Square (antler arches)", "Jackson Town", "Thu", "Jackson Town Square, Jackson, WY", False, "Antler arches, western shops, bars."),
    ("National Elk Refuge", "Jackson Town", "Optional", "National Elk Refuge, Jackson, WY", False, "Early for winter herds but worth a look."),
    ("National Museum of Wildlife Art", "Jackson Town", "Optional", "National Museum of Wildlife Art, Jackson, WY", False, "World-class collection; elk refuge views."),
    ("Spirits & Spice", "Jackson Town", "Shopping", "Spirits and Spice, Jackson, WY", False, "Friend's favorite shop; Thu midday gap or Sun afternoon."),
]

HERE = os.path.dirname(os.path.abspath(__file__))


def render_csv():
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["Name", "Category", "When", "Search Query", "Notes"])
    for name, cat, when, query, _in_list, note in PLACES:
        w.writerow([name, cat, when, query, note])
    return buf.getvalue()


def maps_link(query):
    q = urllib.parse.quote_plus(query)
    return f"https://www.google.com/maps/search/?api=1&query={q}"


def render_links_md():
    cats = []
    for p in PLACES:
        if p[1] not in cats:
            cats.append(p[1])

    lines = [
        "# Add these to your \"Travel: Jackson Hole\" Saved list",
        "",
        "Google has **no API for Saved lists**, so this is the fast manual path.",
        "Tap a link → it opens the place in Google Maps → **Save** → pick",
        "**\"Travel: Jackson Hole\"**. Works on phone (opens the app) and desktop.",
        "",
        "Boxes marked _(already in your list)_ are the ones visible in your",
        "current 19 pins — skip those.",
        "",
        f"**{len(PLACES)} places total.**",
        "",
    ]
    for cat in cats:
        lines.append(f"## {cat}")
        lines.append("")
        for name, c, when, query, in_list, note in PLACES:
            if c != cat:
                continue
            tag = " _(already in your list)_" if in_list else ""
            lines.append(f"- [ ] [{name}]({maps_link(query)}){tag} — {note}")
        lines.append("")
    return "\n".join(lines)


OUTPUTS = {
    "jackson-hole-places.csv": render_csv,
    "add-to-saved-list.md": render_links_md,
}


def check():
    """Exit nonzero if the files on disk don't match the PLACES list —
    catches both hand-edits to generated files and a PLACES edit that
    was never regenerated."""
    stale = []
    for fname, render in OUTPUTS.items():
        path = os.path.join(HERE, fname)
        try:
            with open(path, newline="") as f:
                on_disk = f.read()
        except FileNotFoundError:
            on_disk = None
        if on_disk != render():
            stale.append(fname)
    if stale:
        print("STALE — generated maps files don't match the PLACES list:")
        for fname in stale:
            print(f"  maps/{fname}")
        print("Fix: edit PLACES in maps/generate_places.py (never the files) "
              "and re-run: python3 maps/generate_places.py")
        return 1
    print(f"OK — maps/ outputs match the PLACES list ({len(PLACES)} places).")
    return 0


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        sys.exit(check())
    for fname, render in OUTPUTS.items():
        with open(os.path.join(HERE, fname), "w", newline="") as f:
            f.write(render())
    print(f"Wrote {len(PLACES)} places to:")
    for fname in OUTPUTS:
        print(f"  {os.path.join(HERE, fname)}")
