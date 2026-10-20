# Garden Bed Designer

A single-page web app for planning a garden one square foot at a time. Paint square beds and paths, add round
beds, ring beds, keyhole beds and herb spirals, place plants and companions, pick varieties or adjust a plant's
needs, and get spacing, soil, mulch, stone, water, weight, a cost estimate with your own prices, and a planting
calendar. A plant library lists every plant with its varieties, photos, companions and planting months.
Draft data: verify before building anything.

**Live site:** `https://YOUR-USERNAME.github.io/YOUR-REPO/` (after you turn on GitHub Pages, below)

## What's in it
- **Bed designer**: four guided steps (space, plants, companions, soil). Square beds are painted on the grid;
  round structures are added from step 1 and edited with the Select tool or the structure panel.
  - Round bed: rings, wedges, or spiral rows
  - Ring bed: a circle of beds around a center path
  - Keyhole bed: a notch to reach in and a compost basket in the middle
  - Herb spiral: a raised stone spiral, dry at the top and moist at the bottom
- **Plant library** (`#library`): search plants and varieties, open a plant for its facts, companions and
  variety table, and open any variety for its photo, what's different from a typical plant (spacing, height, sun,
  days to harvest, color), a side-by-side comparison, and a button to use it in your plan.
- **Light calculator** (`#light`): supplemental light by month, using each plant's (or your adjusted) target.

## Run it on your computer
Double-click `index.html`, or from this folder run `python -m http.server 8000` and open http://localhost:8000.
There is no server, database, or login. Saved designs, prices and adjusted plant needs live in each visitor's
browser (localStorage). Photos need an internet connection.

## Publish on GitHub Pages
1. Create a new repository on GitHub (public).
2. Upload everything in this folder (drag and drop in the web page, or use `git` below).
3. In the repo, go to **Settings > Pages**. Under **Build and deployment**, choose **Deploy from a branch**,
   branch **main**, folder **/ (root)**, and Save.
4. Wait about a minute. The site appears at the address shown at the top of the Pages settings.

```bash
git init
git add .
git commit -m "Garden Bed Designer"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

## Update the data
The data lives in the Garden AIO workbook (`Garden_AIO_Data.xlsx`), which is **not** committed (see NOTICE.md).
1. Edit the workbook, check that every row in the `14_DataQuality` tab shows 0 issues, and save it in Excel
   (saving stores the calculated values the build script reads).
2. Put the file at `data/Garden_AIO_Data.xlsx` (it is git-ignored) or pass its path:
   `pip install -r requirements.txt` then `python build/build_app.py path/to/Garden_AIO_Data.xlsx`
3. Commit and push the regenerated `index.html`. Pages updates automatically.

Only plants with **Bed designer ready = Y** in the `2_Crops` tab appear in the app.

The build also joins cultivar details (sun, water, color, size, shape, flavor, description, pests) from the
[Wind River Greens Plant Variety Database](https://github.com/bripatch/plant-variety-database) (CC BY 4.0). It
downloads `data/varieties.csv` from that repo to `data/wrg_varieties.csv` the first time (git-ignored). Delete that
file to pick up their monthly updates. If the download fails, the build continues without the extra details.

## Photos
By default the app loads one photo per plant from Wikipedia and Wikimedia Commons, and searches Wikimedia Commons
for a photo of each variety by name when you open it, with the photographer and license shown under each photo.
Tomato, bell pepper, sweet corn, beet, onion and strawberry varieties also get an example studio photo from the
[Fruits 360 dataset](https://github.com/Horea94/Fruit-Images-Dataset) (MIT), matched by color and shape (the
rules are in `fruitKey` in `build/app_template.html`; the images are in `img/fruits360/`). An exact Commons match
replaces it. Varieties with neither show the species photo. To use your own photos for a plant or a specific variety:
1. Put the images in `img/`.
2. Copy `images.example.json` to `images.json` and list them (`"Tomato"` for a plant, `"Tomato|Brandywine"`
   for a variety).
3. Rebuild with `build/build_app.py`. Your photos replace the Wikipedia ones.

## Credits and data licenses
See `NOTICE.md`. The variety data requires attribution (CC BY 4.0) and the app footer already carries it.

## Limits
- Data are drafts. Pet flags, spacing, soil depth, planting windows, and pairings need verification
  (the workbook marks each row Draft, Imported, or Verified).
- Monthly sunlight values used by the light calculator are placeholders until replaced with NASA POWER data.
- Round structure soil and stone figures are geometric estimates; herb spiral stone depends on the stone you use.
- No accounts or sync: designs are saved per browser, or moved with the design code or link.
