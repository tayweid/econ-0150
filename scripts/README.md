# ECON 0150 maintenance commands

This repository owns both the public-safe course sources and the files served
by GitHub Pages. Restricted MiniExams, grading material, and student data stay
in the separate private `ECON_0150` repository.

There is no routine site build. The normal check is read-only:

```bash
scripts/check-site
```

It checks the custom domain, generated root/part pages, every local HTML/PDF
listed in `course-content.yml`, the public MiniExam demo allowlist, local
machine paths, and notebook JSON. It does not render, copy, commit, or push.

Only regenerate the seven course pages after intentionally changing page text
or links in `course-content.yml`:

```bash
scripts/build-course
scripts/check-site
```

`build-course` rewrites `index.html` and `part-1.html` through `part-6.html` in
place. It does not render linked slides, notes, or notebooks.

Only render decks whose `.qmd` sources changed:

```bash
scripts/render part-1-2
scripts/render part-1-2 part-3-1
```

With no arguments, `scripts/render` renders every current `concept_*.qmd`
deck. That is occasionally useful, but should not be the routine workflow.
Rendering writes reveal.js HTML and its support files beside each source. It
does not create PDFs; keep the existing PDF unless you deliberately export a
new one through your usual PDF workflow.

PowerPoint copies are optional local output:

```bash
scripts/export-pptx
```

They are written to the ignored `/pptx/` directory. Both rendering commands
require Quarto; `scripts/check-site` and `scripts/build-course` use Ruby's
standard library.

None of these commands commit or push. After a deliberate write, inspect
`git status` and `git diff`, rerun `scripts/check-site`, and commit only the
artifacts you intended to change. Do not alter `CNAME` while
`econ-0150.tayweid.io` remains the production domain.
