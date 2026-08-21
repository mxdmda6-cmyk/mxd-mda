# MXD–MDA Signal Engine

Living Palimpsest is a working direct-to-fan commerce prototype for personalized reflective art. A visitor selects a tension, reveals a generated signal, keeps the fragment, and chooses a paid artifact tier.

## Offer ladder

- **$29 — Personal Signal Artifact:** six-page personalized PDF, wallpaper, share card, and reflection prompt.
- **$79 — Deep Signal Edition:** three fragments, an audio transmission, alternate artwork, and a hidden Codex clue.
- **$15/month — Living Archive:** one new monthly artifact, printable ritual page, and chapter unlock.

The current form is a local proof flow only: it captures no payment and makes no therapeutic, diagnostic, or divinatory claim.

## Run locally

```bash
npm install
npm run dev
```

## Verify

```bash
node node_modules/vite/bin/vite.js build
node scripts/prepare-sites-build.mjs
node --test tests/sites-worker.test.mjs
```

## Revenue proof points

- $2,013 gross: 40 Personal + 7 Deep + 20 Archive members.
- $3,526 gross: 55 Personal + 14 Deep + 55 Archive members.
- $5,005 gross: 70 Personal + 20 Deep + 93 Archive members.

These are planning scenarios, not forecasts. The next validation is paid conversion from a small owned audience.
