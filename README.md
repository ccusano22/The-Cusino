# Dealer's Choice Poker Catalog

A GitHub Pages-ready poker reference site with:

- A responsive home page that displays every game as a playing-card-style tile.
- Search, game-type filtering, a visible result count, and a random-game button.
- One permanent rules URL per game, such as `/games/low-chicago/`.
- Uniform player count, game family, pot format, special-card rules, dealer call, directions, variations, winning condition, source, and tip fields.
- A separate house-rules page and a complete single-page catalog.
- A build script that keeps the individual pages synchronized with one master Markdown document.

## Recommended publishing method

The repository includes a GitHub Actions workflow that generates the game pages and deploys the Jekyll site to GitHub Pages. The workflow handles project-site paths automatically, so you do not need to edit `baseurl` for a normal repository such as `dealers-choice-poker`.

### Publish using the GitHub website

1. Create a new **public** GitHub repository. A name such as `dealers-choice-poker` works well. Do not initialize it with another README if you plan to upload this complete folder.
2. Extract the downloaded ZIP on your computer.
3. Upload the **contents inside** the extracted folder to the repository root. Do not upload the outer folder as a single nested directory.
4. Confirm that `.github/workflows/pages.yml`, `_config.yml`, `index.html`, `catalog.md`, and the `_games` folder are present in the repository.
5. Open **Settings > Pages**.
6. Under **Build and deployment**, set **Source** to **GitHub Actions**.
7. Open the repository's **Actions** tab and select the latest `Deploy Dealer's Choice catalog to GitHub Pages` run.
8. After the deployment succeeds, open **Settings > Pages > Visit site**.

The normal project-site address is:

```text
https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/
```

For a root account site, name the repository exactly `YOUR-USERNAME.github.io`.

> The `.github` directory is hidden by default in some desktop file browsers. If it does not appear in the upload, use GitHub Desktop or the command-line method below.

### Publish using Git

Create an empty GitHub repository, then run these commands from inside this project folder:

```bash
git init
git add .
git commit -m "Publish dealer's choice poker catalog"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Then set **Settings > Pages > Source** to **GitHub Actions**.

## Content architecture

`catalog.md` is the editable master. Each game follows a strict Markdown template. During deployment, `scripts/build_games.py` parses that master and writes one Jekyll collection page to `_games/` for every game.

The home page does not contain a hand-maintained list. It reads the `_games` collection and creates the cards automatically. This means player counts, summaries, categories, and links stay aligned with the rules pages.

### Files you will edit most often

| File | Purpose |
|---|---|
| `catalog.md` | Master long-form catalog and game rules. |
| `house-rules.md` | Dealer-call protocol, definitions, and table checklist. |
| `_data/categories.yml` | Browsing category names and descriptions. |
| `assets/css/style.css` | Visual design, card grid, mobile layout, and print styles. |
| `assets/js/catalog.js` | Search, filtering, query-string state, and random selection. |
| `_config.yml` | Site title, description, collection settings, and exclusions. |

Do not hand-edit `_games/*.md` as the primary editing method. The build script regenerates those files from `catalog.md`.

## Editing a game

1. Open `catalog.md`.
2. Find the game's `##` heading.
3. Edit the existing fields without renaming their bold labels:
   - `Family`
   - `Players`
   - `Pot format`
   - `Wild / kill / pay cards`
   - `Call before the deal`
   - `Deal and play`
   - `Winning condition`
   - `Variations`
   - `Game tip`
   - `Source`
4. Keep the HTML anchor immediately above the heading, for example `<a id="low-chicago"></a>`.
5. Run the generator locally, or commit the change and let the GitHub Actions workflow run it.

To change the short text shown on a home-page card, edit the corresponding `Defining feature` cell in the quick-index table inside `catalog.md`.

## Adding a game

1. Add a unique anchor and a new templated game section to `catalog.md`.
2. Add the game to the appropriate quick-index table.
3. Increase `main_catalog_games` or `supplemental_calls` in the `catalog.md` front matter.
4. Add the new anchor slug to `CATEGORY_BY_SLUG` in `scripts/build_games.py`.
5. Run `python3 scripts/build_games.py` and verify that the new `_games/<slug>.md` file is created.

The script fails rather than silently publishing an incomplete page when a required field, anchor, category, or expected game count is missing.

## Local preview

Requirements: Python 3, Ruby, and Bundler.

```bash
gem install bundler
bundle install
python3 scripts/build_games.py
bundle exec jekyll serve --baseurl ""
```

Open `http://127.0.0.1:4000/` in a browser. Stop the preview with `Ctrl+C`.

Validate that committed game pages match the master catalog:

```bash
python3 scripts/build_games.py --check
```

## URL and navigation behavior

All internal links use Jekyll's `relative_url` filter. The included Pages workflow obtains the repository base path from GitHub, so links work for both:

- Project sites: `https://username.github.io/repository/`
- Account sites: `https://username.github.io/`

Search and category filters update the page query string, which makes filtered catalog views bookmarkable. The full card remains a normal link, so the catalog and every rules page still work when JavaScript is disabled.

## Source notes

The catalog contains original rules summaries and direct source links. It is not a verbatim copy of OnlinePoker.net. Material source inconsistencies and room-dependent rules are called out in editorial notes and dealer-call fields.

## Official GitHub references

- [Configuring a publishing source for GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [About GitHub Pages and Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)
- [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
