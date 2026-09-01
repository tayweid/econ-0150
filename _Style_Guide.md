# Style

This repo follows **Graphite**, the visual system shared by the video series and every
course site: `~/Projects/Graphite`, github.com/tayweid/Graphite.

- Values live in `tokens.json` there. Change a color there first, run the checker, then
  propagate.
- The web surface (tokens, type, layout, figures in pages, slides) is `docs/web.md` there.
- The part pages take all of it from the shared stylesheet, `https://tayweid.github.io/course-assets/course.css`. The reveal decks under `parts/` carry their own `custom.css`; the slides rule in `docs/web.md` governs them.

Open here: older pages still load `prototype.css` or Bootstrap. Migrate them to `course.css` as they come up for revision, and re-render notebook images that ship default palettes onto the Graphite marks.
