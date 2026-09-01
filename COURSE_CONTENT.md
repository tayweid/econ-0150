# Editing the ECON 0150 website

All course content lives in `course-content.yaml.js`. Edit the YAML between the two backtick
lines, open the affected `part-*.html` page (double-click it, or run
`scripts/preview.command`), refresh, and run `scripts/check-course` before committing. There
is no build step for the pages. (`scripts/render` still renders the reveal.js decks under
`parts/` with Quarto; that is a separate, occasional step.)

The format, the renderer, and the checker are shared with every course site and live in
`tayweid.github.io/course-assets`; the format is documented in
[COURSE_CONTENT.md](https://github.com/tayweid/tayweid.github.io/blob/main/course-assets/COURSE_CONTENT.md)
there. `scripts/check-course` expects that repository to be cloned beside this one.

Local to this site: every step is written out under `steps:` with a `kind` of exercise,
homework, or livestream; each part ends in a `checkpoint` (shown as a MiniExam) except
Part 6, which ends in the final `project`. `econ-0150.html` and `projects.html` are
hand-written pages and are not generated. `scripts/check-site` keeps its production checks
(the custom domain, the public MiniExam allowlist, machine paths, notebook JSON) and runs
alongside the content check.
