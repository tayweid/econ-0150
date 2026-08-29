# econ-0150.tayweid.io — Graphite Style Guide (web)

This site is the ECON 0150 **desk** in the Graphite system: graphite ground,
CMU Serif voice, Source Sans body — one world shared with the other course
sites and the video stage.

Authority chain: canonical values live in the **Graphite repo**
(`~/Projects/Graphite`, github.com/tayweid/Graphite — `tokens.json` +
palette checker) → `course.css`, served from
`https://tayweid.github.io/course-assets/course.css` → this site's pages.
This file covers the website surface; if/when 0150 gets its own video
series, it gets its own animation guide the way ECON 0100 has one
(`ECON_0100/Parts/_Style_Guide.md` is the template for what that looks like).

## Tokens

Same as the main site's guide (see `tayweid.github.io/_Style_Guide.md`):
ground `#212121`, body `#C8C8C8`, link/accent azure `#4A8FF0`, gold
`#E5C044` sparingly for defined terms.

**Figures and charts** — this being the data-analysis course, this rule does
the most work here: any chart embedded in a page (matplotlib, plotly, SVG)
uses the six Graphite marks in order of need — teal `#128A9B`, orange
`#E2803A`, green `#34B57A`, red `#C63944`, purple `#A99CF2`, pink
`#C95AC0` — on the graphite ground, with `#696969` axes and `#9E9E9E` axis
captions, exactly like the video stage. Use the Graphite repo's
`styles/graphite-dark.mplstyle` (`plt.style.use(...)`). No default
matplotlib/plotly palettes. The set is CVD-validated as a group (checker in
the Graphite repo); label series directly rather than relying on color alone.

## Slides

**Slides are the stage without motion** (decided 2026-08-28). They are
projected in the same rooms and the same lecture flow as the in-class
animations, and students don't receive them — so they take the *stage*
tokens, not a light "paper" treatment: graphite ground, azure flush-left
title, CAPTION `#9E9E9E` for the question line under it, code in dark cards.
A bright slide between dark animation beats would flash the room; dark keeps
the projected experience continuous.

**Figures on slides — one rule, two jobs:**

- **Demonstration** (the code is on the slide: `sns.histplot(...)` → its
  output): keep matplotlib's *default* styling — that white figure is
  exactly what students' own notebooks will produce, and restyling it would
  break the slide's promise. Don't fight the white box; **frame it**: give
  the figure the same card treatment as the code blocks (matching corner
  radius, padding, a margin of stage ground around it). A raw white
  rectangle reads as a hole; a white card reads as a window into the
  student's notebook.
- **Illustration** (you're showing data; the code isn't the point): the
  figure wears Graphite — `styles/graphite-dark.mplstyle` from the Graphite
  repo — and sits seamlessly on the stage.

*If the code is on the slide, the figure wears the notebook card; if it
isn't, the figure wears Graphite.*

Type: CMU Serif headings, Source Sans 3 body — both come with `course.css`.
The `.course-econ-0150` variants (wider nav, course home, projects
components) live in `course.css`; extend them there, not per page.

## The rules in brief

1. Every hue is a noun; color never decorates.
2. Azure is the voice (links, accents) — never a data series.
3. Gold is text, never a mark.
4. Every page loads the shared `course.css` and nothing else.
5. Words as glyphs — prefer a colored word to an icon.

Full rationale: the Graphite design document,
https://claude.ai/code/artifact/24060dd6-bb64-4ebb-aa94-e9e81cab29f7

## Porting list (this repo)

- [ ] Confirm every page (index, parts, projects) loads `course.css` and
      only it; migrate any stragglers.
- [ ] Re-render notebook/plot images that ship default palettes onto the
      Graphite marks as they come up for revision.
