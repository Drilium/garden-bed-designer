"""Join cultivar details from the Wind River Greens Plant Variety Database (CC BY 4.0) onto the app's varieties.

Adds sun, water, color, size, shape, flavor, a fuller description, container use, difficulty, season,
disease resistance, common pests and the source page to each variety the database knows. Used by build_app.py.
The CSV is downloaded to data/wrg_varieties.csv on first use (git-ignored).
"""
import csv
import pathlib
import re
import urllib.request

URL = "https://raw.githubusercontent.com/bripatch/plant-variety-database/main/data/varieties.csv"


def load(path):
    path = pathlib.Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        print(f"downloading {URL}")
        urllib.request.urlretrieve(URL, path)
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def sun_hours(t):
    """Least sun the variety is said to tolerate, in hours: 'Full sun (6+ hours)' -> 6, 'partial shade (4-6 hours)' -> 4."""
    t = (t or "").lower()
    if not t:
        return None
    nums = [float(n) for n in re.findall(r"(\d+(?:\.\d+)?)", t)]
    if "full shade" in t and "sun" not in t:
        return min(nums) if nums else 2
    if "shade" in t or "part sun" in t or "partial sun" in t:
        return min(nums) if nums else 4
    return min(nums) if nums else 6


def clip(s, n):
    s = re.sub(r"\s+", " ", (s or "")).strip()
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "..."


def details(r):
    b = lambda v: 1 if v == "true" else 0 if v == "false" else None
    d = dict(sun=clip(r["sun_requirement"], 60), sh=sun_hours(r["sun_requirement"]), wat=clip(r["water_requirement"], 60),
             col=clip(r["color"], 70), sz=clip(r["size"], 50), shp=clip(r["shape"], 70), fl=clip(r["flavor_profile"], 110),
             d=clip(r["description"], 450), u=r["url"], ct=b(r["is_container_friendly"]), df=clip(r["growing_difficulty"], 30),
             se=clip(r["growing_season"], 40), dr=clip(r["disease_resistance"], 200), pe=clip(r["common_pests"], 140),
             sci=clip(r["scientific_name"], 70))
    return {k: v for k, v in d.items() if v not in ("", None)}


def attach(varieties, rows):
    """Append a details dict (or None) to every variety list. Returns how many matched."""
    idx = {}
    for r in rows:
        m = re.search(r"'([^']+)'", r["name"])
        for key in {norm(m.group(1) if m else r["name"]), norm(r["name"])}:
            idx.setdefault(key, []).append(r)
    hit = 0
    for species, lst in varieties.items():
        word = norm(species).split()[0] if species else ""
        for v in lst:
            name = v[0]
            keys = [norm(name)]
            if "," in name:
                a, b = name.split(",", 1)
                keys.append(norm(b + " " + a))
            cand = list({r["id"]: r for k in keys for r in idx.get(k, [])}.values())
            if len(cand) > 1:
                cand = [r for r in cand if word in norm(r["name"] + " " + r["category"] + " " + r["slug"])] or cand
            v.append(details(cand[0]) if cand else None)
            hit += bool(cand)
    return hit
