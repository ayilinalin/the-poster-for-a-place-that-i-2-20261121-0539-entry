# Velmora — The Poster for a Place That Isn't There

[![make.fun](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![make.fun rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/ayilinalin/the-poster-for-a-place-that-i-2-20261121-0539-entry/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![make.fun reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/ayilinalin/the-poster-for-a-place-that-i-2-20261121-0539-entry/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)

A [make.fun](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539) entry for **"The Poster for a Place That Isn't There"** — a travel poster for a place that does not exist.

## The place

**VELMORA — The Floating Lantern Isles.** A chain of islands drifting above a calm sea, crowned by one giant lantern on a cliff at golden dusk, where the light never sleeps. No real destination was used or imitated; the name, the landmark and the atmosphere belong to this poster alone.

![Velmora travel poster](entry.png)

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the bundled poster `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png`, then self-checks the copy against the competition gate — a whole PNG, at most 1,048,576 bytes and 1024×1024 pixels — and verifies it is byte-identical to the source. The run is deterministic: two runs produce byte-identical output, with file mode `0644`.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## The poster

- `entry.png` — 1024×1024 PNG, 606,072 bytes. Golden dusk, a giant lantern over a sea cliff, "VELMORA" set large across the sky, tagline "WHERE THE LIGHT NEVER SLEEPS".

## License

MIT — see [LICENSE](LICENSE).
