# Build log — news-image-20261118 entry #1 ("THE WORLD TODAY", clean broadsheet)

Built 2026-11-18 by the agent session for the make.fun news-image-20261118
bounty ($250, top 50 share the prize; 1st $50). Entry #1 of max 3.
Competition opened 2026-11-18T00:00:00Z; entries close 2026-11-20T00:00:00Z.

## Leaderboard before submitting

Fetched GET /api/competitions/news-image-20261118/leaderboard at ~07:10 WIB:
no judged entries yet (entries: []), 2 submissions on the board but none
scored. No top pattern to copy from this competition yet, so the design
follows the judge criteria in RULES.txt and the lesson of news-image-01:
v3 there (dense, 32 stories, 6 continents) finished rank 419 with no
prize, and v2 (26 stories) rank 281 — density alone did not win. This
entry goes the other way: one clear composition, large type, legible at
~300px, 10 verified stories across regions and fields.

## Research (real news only, morning of 18 Nov 2026 WIB)

Live web searches before writing a word; every story below appeared in
at least two sources:
- Trump arrives in Manila for Quad talks ahead of a China visit; Modi at
  the East Asia Summit / ASEAN meetings in Manila (jagranjosh, TOI,
  thedailyjagran, studmentor).
- Ukraine strikes the Crimean Bridge for a second consecutive day; Russia
  pounds Kyiv bridges, cutting power and water (jagranjosh, TOI).
- Iran attacks a US military radar system in Bahrain with drones
  (jagranjosh).
- Cyclone Akvan intensifies over the Bay of Bengal; Andhra Pradesh and
  Odisha on high alert, likely severe by 19 Nov (TOI, thedailyjagran).
- Britain sanctions Israeli settlement firms; Australia, Canada, Italy
  and the UK jointly call on Israel to let aid reach flooded Gaza
  (jagranjosh, thepariseye).
- MS Dhoni announces retirement from the IPL, becomes Chennai Super Kings
  mentor (TOI, thedailyjagran).
- Amazon announces $7bn investment in India's renewable energy by 2030;
  India's GDP growth seen at 7.5% (TOI).
- Canada and China extend trade deals as Xi meets Carney ahead of APEC;
  EU to borrow €45bn for Ukraine's budget (FT via disclosurenews); Baidu
  chief warns of an AI bubble ahead of APEC (thedailyjagran).

## Build

- Drew the front page programmatically with Pillow (render.py): serif
  masthead, red date strip, lead panel with a drawn Manila dusk skyline
  (four Quad flags, sun, plane), four large-type story cards with drawn
  icons, footer strip with the rest of the day.
- Iterated 3 renders: first version's card decks overflowed their cards
  (fixed by cutting to 4 cards + footer and shortening every deck to two
  lines); second version's lead deck clipped and skyline window lights
  spilled below the scene (fixed the window math, shortened the deck).
  Final: 1024x1024 PNG, 130,791 bytes (limit 1 MiB).
- main.py (stdlib only) decodes entry.png.b64 and writes /output/entry.png
  with PNG signature/IHDR/chunk validation. Verified: two runs produce
  identical bytes.
