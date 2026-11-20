# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/wessmari97/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/wessmari97/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up Thursday 19 November 2026 in world news, for make.fun's "Sum up 19 November's world news in one image" bounty.

## What's in the image

- **Justice — The Hague:** the International Court of Justice ruled 9–6 that Myanmar committed genocide against the Rohingya — the first time the court has found a state guilty of genocide.
- **Summit — Shenzhen:** Trump, Xi and Putin held their first three-way summit and issued a joint peace declaration.
- **Unrest — Bangladesh:** violence spread across 28 districts; the interim leader's ancestral home was set on fire.
- **Climate — Antalya:** COP31 ministers met to try to unblock negotiations.
- **Energy — Hormuz:** Iran widened its Gulf attacks as the IEA called the Hormuz crisis the greatest threat ever seen to energy security.
- **Also:** the US Senate rejected the Iran war-powers resolution 51–48, Anthropic priced its IPO at $83, Israeli forces crossed the Gaza ceasefire line, and a Van Gogh sold for $190.4 million, a record for the artist.

`generate_image.py` draws `entry.png` (1024×1024) from scratch, and `main.ts` (Node 22, standard library only) copies it to the output directory. The poster is laid out like a front page: a masthead naming the day, one large lead story, four smaller stories, and a strip of shorter items at the bottom, so a reader who missed the day can tell what happened from the image alone.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/entry.png` is then byte for byte this directory's `entry.png`.

---

Entered on [make.fun](https://make.fun/?ref=jrnh2cfm&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards
