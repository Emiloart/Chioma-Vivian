# Mogaha Chioma Vivian — Portfolio

A personal portfolio site for Mogaha Chioma Vivian: Customer Support Specialist, IT Support professional, and Computer Science graduate.

## Stack

- HTML5 and hand-written CSS (no framework)
- TypeScript, compiled to plain JS for the browser, for the small interactive behaviors (mobile nav, copy-email button)
- No build tooling required to view the site: `index.html` references the already-compiled `js/main.js`

## Palette

Sky blue, milk, white, and coffee brown (used sparingly, mostly in the header, buttons, and the closing contact section).

## Developing

```bash
npm install        # installs TypeScript
npm run build       # compiles src/main.ts -> js/main.js
npm run watch        # recompiles on change
```

Then open `index.html` directly, or serve the folder with any static server:

```bash
python3 -m http.server 8080
```

## Structure

```
index.html
css/style.css
src/main.ts        # TypeScript source
js/main.js          # compiled output, committed so the site runs with no build step
assets/              # favicon, downloadable CV
scripts/build_cv_pdf.py   # regenerates assets/Mogaha-Chioma-Vivian-CV.pdf from the same verified content as the site
```

## Deploying to GitHub Pages

Settings → Pages → Deploy from branch → `main` → `/ (root)`. No build step is needed since the compiled JS is committed.
