# Data sources and attribution

- **Plant varieties:** Wind River Greens Plant Variety Database, licensed CC BY 4.0
  (https://plants.windrivergreens.com, https://github.com/bripatch/plant-variety-database). Changes: filtered to the plants
  in this app, mapped to species, spacing and height reduced to midpoints, descriptions shortened.
- **Plant spacing:** UC Master Gardener tables, University of Georgia B577, University of Missouri G6201, UC ANR edible plant
  spacing, and square-foot-gardening charts (Phipps Conservatory; UC Master Gardeners Tulare-Kings). Herbs and flowers use
  lower-tier sources noted in the workbook.
- **Soil mixes, settling, mulch, water:** University of Minnesota Extension, Iowa State Extension, University of Maryland
  Extension, Illinois Extension, UC Cooperative Extension, Missouri IPM and Ask Extension (gravel layers).
- **Light targets:** Michigan State University Extension, Purdue Extension, Hort Americas.
- **Pet safety flags:** drafted from the ASPCA toxic and non-toxic plant lists; confirm at https://www.aspca.org/toxic.
- **Variety details:** sun, water, color, size, shape, flavor, descriptions, disease resistance and pests from the Wind River
  Greens Plant Variety Database (CC BY 4.0), joined by variety name; descriptions shortened.
- **Plant and variety photos:** loaded at runtime from Wikipedia and Wikimedia Commons (variety photos are matched by name
  and may not be exact); each photo shows its author and license (most are CC BY-SA or public domain). Photos listed in `images.json` are the site owner's own.
- **Temperature data in the workbook:** FAO EcoCrop via the Recocrop R package (not used directly by this web app).

The workbook that feeds this app also contains copies of imported datasets. Do not publish it unless you have checked each
dataset's license: Wind River Greens requires credit (CC BY 4.0), and the Recocrop package is GPL-3 or later with underlying
FAO terms to confirm.

All figures are planning estimates, not engineering or agronomic advice. Test soil for lead, follow local codes, and get a
structural check before placing soil on a roof or deck.
