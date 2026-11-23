# The World in One Day — Sunday 22 November 2026

Entry for the make.fun bounty `news-image-20261122`: one image that sums up
the world news of 22 November 2026.

- `main.ts` decodes the base64 picture in `image-data.ts` and writes it to
  `/output/entry.png` (Node 22, stdlib only, same bytes on every run).
- The picture is a 1024x1024 newspaper-style front page: COP31 climate talks
  collapse in Antalya as the lead, plus Ukraine, Hormuz/Middle East, Sudan,
  the UK-EU reset, Mexico, disasters, and a sport/world ticker.
- `generate.py` is the deterministic Pillow script that drew the picture
  (its PNG output is what `image-data.ts` encodes).
