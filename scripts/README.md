# ECON 0150 maintenance commands

This repository owns both the public-safe course sources and the files served by GitHub
Pages. Restricted MiniExams, grading material, and student data stay in the separate
private `ECON_0150` repository.

There is no site build. The part pages render `course-content.yaml.js` in the browser
(see `COURSE_CONTENT.md`). Before committing a content change, run both read-only checks:

```bash
scripts/check-course
scripts/check-site
```

`check-course` validates the content file and the page shells with the checker shared by
every course site (it lives in `tayweid.github.io/course-assets`, cloned beside this
repository). `check-site` checks the custom domain, every local HTML/PDF the content links
to, the public MiniExam demo allowlist, local machine paths, and notebook JSON. Neither
renders, copies, commits, or pushes. The GitHub Actions workflow repeats `check-course` on
every push and publishes the site only when it passes.

Only render decks whose `.qmd` sources changed:

```bash
scripts/render part-1-2
scripts/render part-1-2 part-3-1
```

With no arguments, `scripts/render` renders every current `concept_*.qmd` deck. That is
occasionally useful, but should not be the routine workflow. Rendering writes reveal.js
HTML and its support files beside each source. It does not create PDFs; keep the existing
PDF unless you deliberately export a new one through your usual PDF workflow.

PowerPoint copies are optional local output:

```bash
scripts/export-pptx
```

They are written to the ignored `/pptx/` directory. Both rendering commands require Quarto;
`scripts/check-site` uses Ruby's standard library and `scripts/check-course` uses Node.

None of these commands commit or push. After a deliberate write, inspect `git status` and
`git diff`, rerun the checks, and commit only the artifacts you intended to change. Do not
alter `CNAME` while `econ-0150.tayweid.io` remains the production domain.
