// News-image entry for make.fun, news-image-20261119 (Node 22, stdlib only).
// The entry is the entry.png beside this file: this program copies it
// to /output/entry.png, where the gate and the judge read it. It makes
// no network calls and writes the same bytes on every run.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL("./entry.png", import.meta.url),
  join(outDir, "entry.png"));
