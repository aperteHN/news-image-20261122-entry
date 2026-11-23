// Entry for make.fun news-image-20261122 (Node 22, standard library only).
// The picture of 22 November 2026 world news is stored as base64 in
// image-data.ts (drawn by generate.py); this program decodes it and writes
// it to /output/entry.png, byte for byte the same on every run.
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { writeFileSync } from "node:fs";
import { join } from "node:path";
import { imageBase64 } from "./image-data.ts";

const dst = join(process.env.MAKEFUN_OUTPUT_DIR ?? "/output", "entry.png");
writeFileSync(dst, Buffer.from(imageBase64, "base64"));
