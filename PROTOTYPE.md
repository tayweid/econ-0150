# ECON 0150 YAML-rendering prototype

`course-content-prototype.yml` is a mechanically copied snapshot of
`course-content.yml`, with two data-only
normalizations for the browser-rendering prototype:

1. `Sampling &amp; CLT` is stored as the text `Sampling & CLT` so a renderer can
   insert it safely with `textContent` without showing an encoded entity.
2. Part 6's `checkpoint_raw` HTML string is represented by the structured
   `project` object documented below.

No top-level metadata was added. All existing course content and URLs are
otherwise unchanged.

The prototype lives beside the current site rather than replacing it:

- `part-1.html` through `part-6.html` remain the standard pages.
- `part-1-yaml.html` through `part-6-yaml.html` are the browser-rendered previews.
- The preview pages are marked `noindex` and always offer a link back to their
  standard counterpart if JavaScript, the parser, or the YAML file cannot load.

## Everyday workflow

Edit `course-content-prototype.yml`, then run the complete local preflight:

```sh
node scripts/check-course-prototype
node --test tests/prototype/*.test.js
```

The first command checks YAML syntax, the exact data schema, safe URLs, YouTube
IDs, all local link targets, and the six page shells. It prints every problem in
one run and returns a nonzero status when anything is wrong. It requires Node.js
but no Ruby, package installation, or generated HTML.

To preview locally, serve the site directory rather than opening an HTML file
directly (browsers do not allow a `file:` page to fetch YAML):

```sh
python3 -m http.server 8000
```

Then open `http://127.0.0.1:8000/part-1-yaml.html`.

## What happens after a push

`.github/workflows/course-prototype-check.yml` repeats the preflight on relevant
pull requests and pushes to `main`. If a `main` push fails, it opens or updates
one persistent GitHub issue named **Course prototype validation failed**, mentions
the person who pushed, and links to the failing run. The next successful run
comments on and closes that issue.

For an additional email signal, make this one-time GitHub account setting:
**Settings → Notifications → System → Actions → Email**, with **Only notify for
failed workflows** selected. GitHub documents those controls in
[Managing GitHub Actions notifications](https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-github-actions-notifications).

This prototype check does not control the repository's current branch-based
GitHub Pages deployment. That is deliberate while these files sit beside the
standard pages: a broken preview cannot replace `part-1.html` through
`part-6.html`. Before making the YAML pages canonical, move the Pages deployment
into a GitHub Actions job that depends on the validation job. That makes a
successful check a hard prerequisite for publishing, so the last known-good site
stays live when validation fails.

## Editing rules

- Keep authored text as text. Do not use HTML entities such as `&amp;` or raw
  HTML fields; the renderer creates safe DOM nodes.
- Use root-contained relative paths for site files and `https://` for external
  links. The preflight confirms that every relative file exists, including on
  case-sensitive Linux in CI.
- Keep YouTube values as the 11-character video ID, not a full URL.
- Keep `due` as opaque display text. If machine-readable dates are added later,
  use a separate quoted ISO field rather than parsing the prose.
- Preserve list order; it is the displayed course order.
- When the shared renderer/parser changes, update the cache-version query in all
  six thin shells together.

The browser YAML reader is vendored as js-yaml 4.3.2 so previews do not depend
on a package CDN at class time. Its MIT license is retained at
`assets/vendor/js-yaml.LICENSE.txt`.

## Exact schema

Fields marked `optional` may be absent. Part identifiers remain quoted YAML
strings (`'1'` through `'6'`). Relative `href` values resolve from a course page
at the site root.

```text
Course
  code: string
  title: string
  brand: string[]
  home: string
  extra_nav: NavLink[]
  stylesheet: string
  script: string
  parts: mapping<string, Part>

NavLink
  label: string
  href: string

Part
  title: string
  tagline: string
  introduction: string
  blocks: Block[]
  checkpoint: Checkpoint             # optional; Parts 1-5
  project: Project                   # optional; Part 6

Block
  id: string
  nav: string
  title: string
  description: string
  episode: Episode
  steps: Step[]

Episode
  name: string
  desc: string
  video: string                      # optional; YouTube video ID
  links: ResourceLink[]              # optional

Step
  name: string
  kind: "exercise" | "homework" | "livestream"
  sub: string                        # optional
  due: string                        # optional; display text, not parsed as a date
  video: string                      # optional except required for livestreams; YouTube video ID
  links: ResourceLink[]              # optional

ResourceLink
  label: string
  href: string
  icon: string                       # optional; Font Awesome class

Checkpoint
  number: string
  description: string
  demo: Demo
  demo_links: ResourceLink[]
  next: integer

Demo
  name: string
  desc: string
  video: string

Project
  id: string
  nav: string
  title: string
  description: string
  prompts: ProjectPrompt[]
  requirements: string[]
  links: ResourceLink[]

ProjectPrompt
  label: string
  kind: "research" | "data" | "methods" | "finding"
  text: string
```

The browser renderer uses `project.nav` in the right-hand contents navigation,
`project.prompts[].kind` values only as known presentation variants, and
`project.title` for both visible “Final Project” labels from the previous
markup. It renders the prompt text, requirements, and links as DOM nodes; it
does not accept raw HTML from the manifest.

## Part 6 project data shape

```yaml
project:
  id: final-project
  nav: Final Project
  title: Final Project
  description: Here's where we tie it all together.
  prompts:
  - label: Research Question.
    kind: research
    text: What is an interesting question to YOU that you can answer with data?
  - label: Data Source.
    kind: data
    text: What dataset could you use to answer your research question?
  - label: Methods.
    kind: methods
    text: What statistical methods would you need for your question?
  - label: Main Finding.
    kind: finding
    text: You may find something interesting!
  requirements:
  - Prepare a 3-minute presentation with 1-2 slides.
  - Write a 1-2 page report of your findings.
  - Organize a replication folder with your data and code.
  links:
  - label: Guidelines
    href: projects/project_guidelines.pdf
    icon: fa-file-pdf-o
  - label: Data Sources
    href: projects/data_sources.pdf
    icon: fa-file-pdf-o
  - label: Project Template Notebook
    href: https://colab.research.google.com/drive/1eHmy9zJb-E1-zDmsFEhw7o5OA7o8FgDb?usp=sharing
    icon: fa-external-link
```
