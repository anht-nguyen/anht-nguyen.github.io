# Tuan Anh Nguyen — Academic Portfolio

Personal academic website for Tuan Anh Nguyen (publishing as Anh T. Nguyen), a Bioengineering Ph.D. candidate at the University of Pennsylvania.

Built from [Academic Pages](https://github.com/academicpages/academicpages.github.io), with its Jekyll layouts, responsive author sidebar, navigation, and light/dark themes. Template attribution and the upstream MIT license are retained.

## Content

- `index.html`: biography, research themes, selected publications, and academic highlights.
- `_portfolio/`: research project overviews.
- `_publications/`: one Markdown file per publication; `category` separates journals, proceedings, and preprints.
- `_pages/`: research and publication indexes, CV, teaching/service, sitemap, and 404 page.
- `_config.yml`: name, affiliation, contact details, scholarly links, and site configuration.
- `_data/navigation.yml`: primary navigation.
- `files/Tuan-Anh-Nguyen-CV.pdf`: September 2026 academic CV.
- `assets/css/academic.css`: personal styling layered over the template.

The original `/assets/BIRO24_0379_FI.pdf` and `/assets/2024-biorob-flo-poster.pdf` URLs are preserved. Other publications link to publisher, PubMed, or arXiv records. The initials graphic in `images/monogram.svg` can be replaced with a headshot by changing `author.avatar`.

## Local build

Use Ruby 3.3 with Bundler, Node.js 20 or newer, and Python 3 for link validation. On Windows, RubyInstaller with Devkit or a Ruby-enabled WSL environment can provide the Ruby toolchain.

```sh
bundle config set --local path vendor/bundle
bundle install
npm run build
bundle exec jekyll build --trace
python scripts/check-site.py _site
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000`. The JavaScript build uses Node's standard library and requires no npm install. Run it again after changing JavaScript. Restart Jekyll after changing `_config.yml`.

## GitHub Pages

In the repository's **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. The included workflow builds and validates pull requests, and deploys pushes to `main`. It can also be started manually on `main`. No repository settings are changed by this local patch.

## Updating the academic record

Use the `year` field for publication years; no artificial publication dates are needed. Set `status` and `category` explicitly, and update preprints when their publication status changes. Only mark `featured: true` for work that should appear on the homepage. Keep project descriptions clear about pilot studies, replay evaluations, and completed versus ongoing work.

Local assistant/editor folders, dependencies, and generated build output are ignored by Git and excluded from the generated website.
