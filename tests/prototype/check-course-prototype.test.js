'use strict';

const assert = require('node:assert/strict');
const { spawnSync } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const test = require('node:test');

const SITE_ROOT = path.resolve(__dirname, '..', '..');
const VALIDATOR = path.join(SITE_ROOT, 'scripts', 'check-course-prototype');

function indent(text, spaces) {
  const prefix = ' '.repeat(spaces);
  return text
    .trimEnd()
    .split('\n')
    .map(line => `${prefix}${line}`)
    .join('\n');
}

function checkpoint(partNumber) {
  return `checkpoint:
  number: '${partNumber}'
  description: Checkpoint for part ${partNumber}.
  demo:
    name: Demo ${partNumber}
    desc: Demonstration for part ${partNumber}.
    video: abcdefghijk
  demo_links:
  - label: Demo
    href: ME/demo.pdf
  - label: Solutions
    href: ME/solutions.pdf
  next: ${partNumber + 1}`;
}

function project() {
  return `project:
  id: final-project
  nav: Final Project
  title: Final Project
  description: Bring the course ideas together.
  prompts:
  - label: Research Question
    kind: research
    text: Ask a focused question.
  - label: Data Source
    kind: data
    text: Identify suitable data.
  - label: Methods
    kind: methods
    text: Select an appropriate method.
  - label: Main Finding
    kind: finding
    text: Explain the result.
  requirements:
  - Prepare a short presentation.
  - Write a short report.
  links:
  - label: Guidelines
    href: projects/guidelines.pdf
    icon: fa-file-pdf-o
  - label: Notebook
    href: https://example.edu/project-notebook
    icon: fa-external-link`;
}

function part(partNumber) {
  const ending = partNumber === 6 ? project() : checkpoint(partNumber);
  return `'${partNumber}':
  title: Part ${partNumber}
  tagline: Tagline for part ${partNumber}
  introduction: Intro to part ${partNumber}.
  blocks:
  - id: '${partNumber}.1'
    nav: Topic ${partNumber}
    title: Topic ${partNumber}
    description: Description for topic ${partNumber}.
    episode:
      name: Episode ${partNumber}
      desc: Episode description ${partNumber}.
      video: dQw4w9WgXcQ
      links:
      - label: Slides
        href: parts/example.pdf
        icon: fa-file-pdf-o
    steps:
    - name: Exercise ${partNumber}.1
      kind: exercise
      sub: Practice data
      video: abcdefghijk
      links:
      - label: Notebook
        href: https://example.edu/notebook-${partNumber}
    - name: Homework ${partNumber}.1
      kind: homework
      due: Due Friday at 5PM.
      links:
      - label: Assignment
        href: parts/example.pdf
    - name: Livestream ${partNumber}.1
      kind: livestream
      video: abcdefghijk
${indent(ending, 2)}`;
}

function goodManifest() {
  const parts = Array.from({ length: 6 }, (_, index) => indent(part(index + 1), 2));
  return `code: ECON 0150
title: Economic Data Analysis
brand:
- ECONOMIC
- DATA
- ANALYSIS
home: econ-0150.html
extra_nav:
- label: Projects
  href: projects.html
stylesheet: https://example.edu/course.css
script: https://example.edu/course.js
parts:
${parts.join('\n')}
`;
}

function replaceFixture(manifest, search, replacement) {
  assert.ok(manifest.includes(search), `fixture mutation target is missing: ${search}`);
  return manifest.replace(search, replacement);
}

function copyPrototypeFile(relativePath, destinationRoot) {
  const source = path.join(SITE_ROOT, relativePath);
  assert.ok(fs.existsSync(source), `prototype test prerequisite is missing: ${relativePath}`);
  const destination = path.join(destinationRoot, relativePath);
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.copyFileSync(source, destination);
}

function writeEmptyFile(root, relativePath) {
  const destination = path.join(root, relativePath);
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.writeFileSync(destination, 'fixture\n');
}

function makeSite(t, manifest = goodManifest()) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'econ-0150-prototype-test-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));

  fs.writeFileSync(path.join(root, 'course-content-prototype.yml'), manifest);

  for (let partNumber = 1; partNumber <= 6; partNumber += 1) {
    copyPrototypeFile(`part-${partNumber}-yaml.html`, root);
  }
  for (const relativePath of [
    'assets/scripts/yaml-course-page.js',
    'assets/vendor/js-yaml.min.js'
  ]) {
    copyPrototypeFile(relativePath, root);
  }
  if (fs.existsSync(path.join(SITE_ROOT, 'assets/styles/prototype.css'))) {
    copyPrototypeFile('assets/styles/prototype.css', root);
  }

  for (const relativePath of [
    'econ-0150.html',
    'projects.html',
    'parts/example.pdf',
    'ME/demo.pdf',
    'ME/solutions.pdf',
    'projects/guidelines.pdf'
  ]) {
    writeEmptyFile(root, relativePath);
  }

  return root;
}

function runValidator(siteRoot) {
  return spawnSync(process.execPath, [
    VALIDATOR,
    '--manifest', path.join(siteRoot, 'course-content-prototype.yml'),
    '--site-root', siteRoot
  ], {
    cwd: SITE_ROOT,
    encoding: 'utf8',
    env: { ...process.env, NO_COLOR: '1' }
  });
}

function diagnostics(result) {
  return [
    `exit status: ${result.status}`,
    result.error ? `spawn error: ${result.error.message}` : '',
    `stdout:\n${result.stdout || '(empty)'}`,
    `stderr:\n${result.stderr || '(empty)'}`
  ].filter(Boolean).join('\n');
}

function assertPasses(result) {
  assert.equal(result.status, 0, diagnostics(result));
}

function assertFails(result) {
  assert.notEqual(result.status, 0, diagnostics(result));
}

test('the renderer page selector matches every prototype shell', () => {
  const renderer = fs.readFileSync(
    path.join(SITE_ROOT, 'assets/scripts/yaml-course-page.js'),
    'utf8'
  );
  const selectorMatch = renderer.match(
    /document\.querySelector\(\s*(['"])(\[data-([a-z0-9-]+)\])\1\s*\)/
  );
  assert.ok(selectorMatch, 'renderer must select its page by one data-* attribute');

  const attribute = `data-${selectorMatch[3]}`;
  const datasetProperty = selectorMatch[3].replace(/-([a-z])/g, (_match, letter) =>
    letter.toUpperCase()
  );
  assert.match(
    renderer,
    new RegExp(`page\\.dataset\\.${datasetProperty}\\b`),
    `renderer selects ${attribute} but does not read dataset.${datasetProperty}`
  );

  for (let partNumber = 1; partNumber <= 6; partNumber += 1) {
    const shell = fs.readFileSync(
      path.join(SITE_ROOT, `part-${partNumber}-yaml.html`),
      'utf8'
    );
    const declaration = new RegExp(`${attribute}=["']${partNumber}["']`);
    assert.match(
      shell,
      declaration,
      `Part ${partNumber} shell does not declare the renderer's ${attribute}`
    );
  }
});

test('accepts a complete, safe manifest whose local targets exist', t => {
  assert.ok(fs.existsSync(VALIDATOR), `validator is missing: ${VALIDATOR}`);
  assertPasses(runValidator(makeSite(t)));
});

test('rejects malformed YAML', t => {
  assertFails(runValidator(makeSite(t, "parts:\n  '1': [\n")));
});

test('rejects an unsupported step kind', t => {
  const manifest = replaceFixture(goodManifest(), 'kind: exercise', 'kind: quiz');
  assertFails(runValidator(makeSite(t, manifest)));
});

test('rejects a missing local link target', t => {
  const manifest = replaceFixture(
    goodManifest(),
    'parts/example.pdf',
    'parts/missing.pdf'
  );
  assertFails(runValidator(makeSite(t, manifest)));
});

test('rejects an unsafe URL scheme', t => {
  const manifest = replaceFixture(
    goodManifest(),
    'https://example.edu/project-notebook',
    'javascript:alert(1)'
  );
  assertFails(runValidator(makeSite(t, manifest)));
});

test('rejects the legacy checkpoint_raw field', t => {
  const manifest = replaceFixture(
    goodManifest(),
    "    checkpoint:\n      number: '1'",
    "    checkpoint_raw: '<section>legacy markup</section>'\n    checkpoint:\n      number: '1'"
  );
  assertFails(runValidator(makeSite(t, manifest)));
});

test('rejects raw HTML in a text field', t => {
  const manifest = replaceFixture(
    goodManifest(),
    'introduction: Intro to part 1.',
    'introduction: "<strong>Intro to part 1.</strong>"'
  );
  assertFails(runValidator(makeSite(t, manifest)));
});

test('rejects an invalid YouTube video ID', t => {
  const manifest = replaceFixture(goodManifest(), 'dQw4w9WgXcQ', 'too-short');
  assertFails(runValidator(makeSite(t, manifest)));
});
