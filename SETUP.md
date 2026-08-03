# Setup — publishing the profile

## 1. Where it goes
A profile README renders on your GitHub profile page **only** when it lives in a repo named exactly after your username:

```
github.com/lalitmore/lalitmore   ←  repo name MUST equal your username
```

## 2. Folder structure
```
lalitmore/                 (the special profile repo)
├── README.md              ← the profile, renders automatically
├── build_assets.py        ← regenerates the banner (optional to keep)
├── SETUP.md               ← this file (optional to keep)
├── SOURCES.md             ← asset provenance (optional to keep)
└── assets/
    └── banner.svg         ← the only visual asset
```

## 3. Publish
On GitHub: click **New repository**, name it exactly `lalitmore`, set it **Public**, and create it. Then, on your machine:

```bash
git clone https://github.com/lalitmore/lalitmore.git
cd lalitmore
# copy README.md, build_assets.py, SETUP.md, SOURCES.md and the assets/ folder in
git add .
git commit -m "Add profile README"
git push
```

Open `https://github.com/lalitmore` — it renders immediately, caret animation included.

> No terminal? You can also drag the files into the repo page on github.com via **Add file → Upload files**, then commit. (Upload `README.md`, the three docs, and the `assets` folder.)

## 4. Two source links to confirm before pushing  ⚠️

| Location in README | Current link | Action |
|---|---|---|
| **VO2** | `github.com/lalitmore?tab=repositories` | **Placeholder** — no repo URL was available. Point it at the real VO2 repo (add a Devpost/live link too if you have one). |
| **CCI Agent** | `github.com/lalitmore/ai-research-agent` | Confirmed by you — leave as-is. |

`Atlas AI` links to `github.com/lalitmore/Atlas-AI`. The old live-demo link was removed (endpoint retired). Everything else — name, education, roles, cert, skills — is straight from your résumé.

## 5. Editing the banner
The banner is generated from one small script so the palette stays consistent.

```bash
python3 build_assets.py     # rewrites assets/banner.svg
```

Common edits, all near the top of `build_assets.py`:
- **Colors** — the palette block (`BG`, `ACCENT`, `TXT`, …). `ACCENT` (`#F2A65A`) is the honey highlight; change it in one place to re-tone the whole banner.
- **Role line / subline** — the `role` and `sub` strings in `build_banner()`. If you change `role`, the caret repositions automatically (its x is derived from the text length; tweak `char_w` if it drifts).

## 6. Notes on GitHub rendering
- Animated SVG via `<img>` **does** animate on GitHub — the one caret uses SMIL (`<animate>`), which survives the camo image proxy. No `<script>` or CSS is used, because GitHub strips those from READMEs.
- The banner is dark and self-lit, so it looks identical in GitHub's light and dark themes — no theme-variant asset needed.
- Text uses **system font stacks**, so it renders on any machine without loading webfonts. To bake in an exact display face, convert the text to outlines in a vector editor and re-export.
- GitHub caches images hard. If you update the banner and don't see it, hard-refresh or wait a couple of minutes.
