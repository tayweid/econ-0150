(function () {
    'use strict';

    const page = document.querySelector('[data-part]');
    if (!page) return;

    page.dataset.courseRendererStarted = 'true';
    if (window.__courseRendererWatchdog) {
        window.clearTimeout(window.__courseRendererWatchdog);
    }
    const startupError = page.querySelector('.course-render-error');
    if (startupError) startupError.hidden = true;
    page.setAttribute('aria-busy', 'true');

    const partId = page.dataset.part;
    const source = page.dataset.courseSource || 'course-content-prototype.yml';
    const output = page.querySelector('[data-course-output]');
    const status = page.querySelector('[data-course-status]');
    const leftSlot = document.querySelector('[data-course-left-nav]');
    const rightSlot = document.querySelector('[data-course-right-nav]');
    const STEP_KINDS = new Set(['exercise', 'homework', 'livestream']);

    class CourseDataError extends Error {
        constructor(path, message) {
            super(`${path}: ${message}`);
            this.name = 'CourseDataError';
        }
    }

    function element(tag, className, text) {
        const node = document.createElement(tag);
        if (className) node.className = className;
        if (text !== undefined && text !== null) node.textContent = String(text);
        return node;
    }

    function object(value, path) {
        if (
            !value ||
            typeof value !== 'object' ||
            Array.isArray(value) ||
            ![Object.prototype, null].includes(Object.getPrototypeOf(value))
        ) {
            throw new CourseDataError(path, 'must be a mapping');
        }
        return value;
    }

    function keys(value, path, required, optional = []) {
        object(value, path);
        const allowed = new Set([...required, ...optional]);
        required.forEach(key => {
            if (!Object.prototype.hasOwnProperty.call(value, key)) {
                throw new CourseDataError(`${path}.${key}`, 'is required');
            }
        });
        Object.keys(value).forEach(key => {
            if (['__proto__', 'prototype', 'constructor'].includes(key) || !allowed.has(key)) {
                throw new CourseDataError(`${path}.${key}`, 'is not an allowed field');
            }
        });
    }

    function array(value, path, options = {}) {
        if (value === undefined && options.optional) return [];
        if (!Array.isArray(value)) throw new CourseDataError(path, 'must be a list');
        if (!options.allowEmpty && value.length === 0) {
            throw new CourseDataError(path, 'must not be empty');
        }
        return value;
    }

    function string(value, path, options = {}) {
        if (value === undefined && options.optional) return '';
        if (typeof value !== 'string') throw new CourseDataError(path, 'must be text');
        if (!options.allowEmpty && value.trim() === '') {
            throw new CourseDataError(path, 'must not be empty');
        }
        return value;
    }

    function safeFragment(value, path) {
        const fragment = string(value, path);
        if (!/^[A-Za-z][A-Za-z0-9_-]*$/.test(fragment)) {
            throw new CourseDataError(path, 'must start with a letter and contain only letters, numbers, hyphens, or underscores');
        }
        return fragment;
    }

    function safeUrl(value, path) {
        const href = string(value, path).trim();
        if (/[\u0000-\u001F\u007F]/.test(href)) {
            throw new CourseDataError(path, 'must not contain control characters');
        }
        if (/^https:\/\//i.test(href)) {
            try {
                const parsed = new URL(href);
                if (parsed.protocol !== 'https:') throw new Error('not HTTPS');
            } catch (_error) {
                throw new CourseDataError(path, 'must be a valid HTTPS URL');
            }
            return href;
        }
        if (
            href === '' ||
            /^[A-Za-z][A-Za-z0-9+.-]*:/.test(href) ||
            href.startsWith('/') ||
            href.includes('\\')
        ) {
            throw new CourseDataError(path, 'must be a relative URL or an HTTPS URL');
        }
        const pathOnly = href.split('#', 1)[0].split('?', 1)[0];
        if (pathOnly === '') throw new CourseDataError(path, 'must identify a relative file');
        let decodedPath;
        try {
            decodedPath = decodeURIComponent(pathOnly);
            if (decodedPath.split('/').some(segment => segment === '.' || segment === '..')) {
                throw new Error('path traversal');
            }
            const resolved = new URL(href, document.baseURI);
            if (location.protocol !== 'file:' && resolved.origin !== location.origin) {
                throw new Error('cross-origin relative URL');
            }
        } catch (_error) {
            throw new CourseDataError(path, 'must be a valid relative URL');
        }
        return href;
    }

    function safeIcon(value, path) {
        if (value === undefined) return '';
        const icon = string(value, path);
        if (!/^fa-[a-z0-9-]+$/.test(icon)) {
            throw new CourseDataError(path, 'must be a Font Awesome icon name such as fa-file-powerpoint-o');
        }
        return icon;
    }

    function videoId(value, path, options = {}) {
        if (value === undefined && options.optional) return '';
        const id = string(value, path);
        if (!/^[A-Za-z0-9_-]{11}$/.test(id)) {
            throw new CourseDataError(path, 'must be an eleven-character YouTube video ID');
        }
        return id;
    }

    function validateLinks(value, path) {
        return array(value, path, { optional: true, allowEmpty: true }).map((item, index) => {
            const itemPath = `${path}[${index}]`;
            keys(item, itemPath, ['label', 'href'], ['icon']);
            string(item.label, `${itemPath}.label`);
            safeUrl(item.href, `${itemPath}.href`);
            safeIcon(item.icon, `${itemPath}.icon`);
            return item;
        });
    }

    function validateEpisode(value, path, options = {}) {
        const episode = object(value, path);
        keys(episode, path, ['name', 'desc'], ['video', 'links']);
        string(episode.name, `${path}.name`);
        string(episode.desc, `${path}.desc`);
        videoId(episode.video, `${path}.video`, { optional: true });
        if (options.requireVideo && episode.video === undefined) {
            throw new CourseDataError(`${path}.video`, 'is required');
        }
        validateLinks(episode.links, `${path}.links`);
        return episode;
    }

    function validateStep(value, path) {
        const step = object(value, path);
        keys(step, path, ['name', 'kind'], ['sub', 'due', 'video', 'links']);
        string(step.name, `${path}.name`);
        const kind = string(step.kind, `${path}.kind`);
        if (!STEP_KINDS.has(kind)) {
            throw new CourseDataError(`${path}.kind`, `must be one of ${Array.from(STEP_KINDS).join(', ')}`);
        }
        string(step.sub, `${path}.sub`, { optional: true, allowEmpty: true });
        string(step.due, `${path}.due`, { optional: true, allowEmpty: true });
        videoId(step.video, `${path}.video`, { optional: true });
        if (kind === 'livestream' && step.video === undefined) {
            throw new CourseDataError(`${path}.video`, 'is required for a livestream');
        }
        validateLinks(step.links, `${path}.links`);
        return step;
    }

    function validateCheckpoint(value, path, expectedNumber, partIds) {
        const checkpoint = object(value, path);
        keys(checkpoint, path, ['number', 'description', 'demo', 'demo_links', 'next']);
        string(checkpoint.number, `${path}.number`);
        if (checkpoint.number !== expectedNumber) {
            throw new CourseDataError(`${path}.number`, `must match Part ${expectedNumber}`);
        }
        string(checkpoint.description, `${path}.description`, { allowEmpty: true });
        validateEpisode(checkpoint.demo, `${path}.demo`, { requireVideo: true });
        validateLinks(checkpoint.demo_links, `${path}.demo_links`);
        const expectedNext = Number(expectedNumber) + 1;
        if (!Number.isInteger(checkpoint.next) || checkpoint.next !== expectedNext) {
            throw new CourseDataError(`${path}.next`, `must be the integer ${expectedNext}`);
        }
        if (!partIds.includes(String(checkpoint.next))) {
            throw new CourseDataError(`${path}.next`, `references missing Part ${checkpoint.next}`);
        }
        return checkpoint;
    }

    function validateProject(value, path) {
        const project = object(value, path);
        keys(project, path, ['id', 'nav', 'title', 'description', 'prompts', 'requirements', 'links']);
        safeFragment(project.id, `${path}.id`);
        if (!/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(project.id)) {
            throw new CourseDataError(`${path}.id`, 'must be a lowercase, hyphenated HTML id');
        }
        string(project.nav, `${path}.nav`);
        string(project.title, `${path}.title`);
        string(project.description, `${path}.description`, { allowEmpty: true });
        const promptKinds = new Set();
        array(project.prompts, `${path}.prompts`).forEach((prompt, index) => {
            const promptPath = `${path}.prompts[${index}]`;
            keys(prompt, promptPath, ['label', 'kind', 'text']);
            string(prompt.label, `${promptPath}.label`);
            const kind = string(prompt.kind, `${promptPath}.kind`);
            if (!['research', 'data', 'methods', 'finding'].includes(kind)) {
                throw new CourseDataError(`${promptPath}.kind`, 'must be research, data, methods, or finding');
            }
            if (promptKinds.has(kind)) throw new CourseDataError(`${promptPath}.kind`, 'must be unique');
            promptKinds.add(kind);
            string(prompt.text, `${promptPath}.text`);
        });
        array(project.requirements, `${path}.requirements`).forEach((requirement, index) => {
            string(requirement, `${path}.requirements[${index}]`);
        });
        validateLinks(project.links, `${path}.links`);
        return project;
    }

    function blockElementId(id) {
        return `part-${id.replace(/[^A-Za-z0-9]/g, '')}`;
    }

    function validatePart(value, path, currentPartId, partIds) {
        const part = object(value, path);
        keys(part, path, ['title', 'tagline', 'introduction', 'blocks'], currentPartId === '6' ? ['project'] : ['checkpoint']);
        string(part.title, `${path}.title`);
        string(part.tagline, `${path}.tagline`);
        string(part.introduction, `${path}.introduction`);
        const blocks = array(part.blocks, `${path}.blocks`);
        const blockIds = new Set();
        const elementIds = new Set();
        blocks.forEach((block, index) => {
            const blockPath = `${path}.blocks[${index}]`;
            keys(block, blockPath, ['id', 'nav', 'title', 'description', 'episode', 'steps']);
            const id = string(block.id, `${blockPath}.id`);
            if (!new RegExp(`^${currentPartId}\\.[1-9][0-9]*$`).test(id)) {
                throw new CourseDataError(`${blockPath}.id`, `must use the form ${currentPartId}.N`);
            }
            if (blockIds.has(id)) throw new CourseDataError(`${blockPath}.id`, `duplicates block ${id}`);
            blockIds.add(id);
            const elementId = blockElementId(id);
            if (elementIds.has(elementId)) {
                throw new CourseDataError(`${blockPath}.id`, `collides with another block at #${elementId}`);
            }
            elementIds.add(elementId);
            string(block.nav, `${blockPath}.nav`);
            string(block.title, `${blockPath}.title`);
            string(block.description, `${blockPath}.description`);
            validateEpisode(block.episode, `${blockPath}.episode`);
            array(block.steps, `${blockPath}.steps`).forEach((step, stepIndex) => {
                validateStep(step, `${blockPath}.steps[${stepIndex}]`);
            });
        });

        if (part.checkpoint_raw !== undefined) {
            throw new CourseDataError(`${path}.checkpoint_raw`, 'raw HTML is not supported; use the structured project field');
        }
        const tails = [part.checkpoint !== undefined, part.project !== undefined].filter(Boolean).length;
        if (tails > 1) throw new CourseDataError(path, 'may define either checkpoint or project, not both');
        if (currentPartId === '6' && part.project === undefined) {
            throw new CourseDataError(`${path}.project`, 'is required for Part 6');
        }
        if (currentPartId !== '6' && part.checkpoint === undefined) {
            throw new CourseDataError(`${path}.checkpoint`, `is required for Part ${currentPartId}`);
        }
        if (part.checkpoint !== undefined) validateCheckpoint(part.checkpoint, `${path}.checkpoint`, currentPartId, partIds);
        if (part.project !== undefined) validateProject(part.project, `${path}.project`);
        return part;
    }

    function validateManifest(value) {
        const manifest = object(value, 'course');
        keys(manifest, 'course', ['code', 'title', 'brand', 'home', 'extra_nav', 'stylesheet', 'script', 'parts']);
        string(manifest.code, 'course.code');
        string(manifest.title, 'course.title');
        const brand = array(manifest.brand, 'course.brand');
        brand.forEach((line, index) => string(line, `course.brand[${index}]`));
        safeUrl(manifest.home, 'course.home');
        validateLinks(manifest.extra_nav, 'course.extra_nav');
        safeUrl(manifest.stylesheet, 'course.stylesheet');
        safeUrl(manifest.script, 'course.script');
        const parts = object(manifest.parts, 'course.parts');
        const partIds = Object.keys(parts);
        if (partIds.length !== 6 || !['1', '2', '3', '4', '5', '6'].every(id => partIds.includes(id))) {
            throw new CourseDataError('course.parts', 'must define Parts 1 through 6 exactly once');
        }
        partIds.forEach(id => {
            if (!/^[1-9][0-9]*$/.test(id)) {
                throw new CourseDataError(`course.parts.${id}`, 'part IDs must be positive integers');
            }
        });
        if (!Object.prototype.hasOwnProperty.call(parts, partId)) {
            throw new CourseDataError(`course.parts.${partId}`, 'is missing');
        }
        partIds.forEach(id => validatePart(parts[id], `course.parts.${id}`, id, partIds));
        return { manifest, partIds: partIds.sort((left, right) => Number(left) - Number(right)) };
    }

    function iconFor(link) {
        if (link.icon) return link.icon;
        const href = link.href.toLowerCase().split(/[?#]/, 1)[0];
        if (/^https:\/\//.test(href)) return 'fa-external-link';
        if (/\.(?:html?|qmd)$/.test(href)) return 'fa-desktop';
        if (/\.(?:ipynb|py|r)$/.test(href)) return 'fa-file-code-o';
        if (/\.(?:pptx?|key)$/.test(href)) return 'fa-file-powerpoint-o';
        if (/\.(?:csv|tsv|xlsx?|json)$/.test(href) || href.startsWith('data/')) return 'fa-file-text-o';
        return 'fa-file-pdf-o';
    }

    function resourceLink(item) {
        const link = element('a', 'download-link');
        link.href = safeUrl(item.href, 'rendered link');
        link.target = '_blank';
        link.rel = 'noopener';
        link.setAttribute('aria-label', `${item.label} (opens in a new tab)`);
        const icon = element('i', `fa ${iconFor(item)}`);
        icon.setAttribute('aria-hidden', 'true');
        link.append(icon, document.createTextNode(` ${item.label}`));
        return link;
    }

    function resourceLinks(items) {
        if (!items || items.length === 0) return null;
        const container = element('div', 'path-links');
        items.forEach(item => container.append(resourceLink(item)));
        return container;
    }

    function youtubeUrl(id) {
        return `https://www.youtube.com/watch?v=${id}`;
    }

    function youtubeThumbnail(id, compact) {
        return `https://img.youtube.com/vi/${id}/${compact ? 'mqdefault' : 'hqdefault'}.jpg`;
    }

    function videoImage(id, compact) {
        const image = element('img');
        image.src = youtubeThumbnail(id, compact);
        image.alt = '';
        image.loading = 'lazy';
        image.decoding = 'async';
        image.referrerPolicy = 'no-referrer';
        image.width = compact ? 320 : 480;
        image.height = compact ? 180 : 270;
        return image;
    }

    function videoLink(name, id, compact) {
        const link = element('a', compact ? 'path-thumb' : 'card-video prototype-video-link');
        link.href = youtubeUrl(id);
        link.target = '_blank';
        link.rel = 'noopener';
        link.setAttribute('aria-label', `Watch ${name} on YouTube (opens in a new tab)`);
        link.append(videoImage(id, compact));
        if (!compact) {
            const play = element('span', 'play-button', '▶');
            play.setAttribute('aria-hidden', 'true');
            link.append(play);
        }
        return link;
    }

    function placeholderVideo() {
        const container = element('div', 'card-video prototype-video-placeholder');
        container.setAttribute('aria-label', 'Video not yet available');
        const image = element('img', 'placeholder-bg');
        image.alt = '';
        image.width = 480;
        image.height = 270;
        container.append(image);
        return container;
    }

    function renderEpisode(episode, headingId) {
        const panel = element('div', 'path-episode');
        panel.setAttribute('aria-labelledby', headingId);
        panel.append(episode.video ? videoLink(episode.name, episode.video, false) : placeholderVideo());
        const heading = element('h3', 'path-name', episode.name);
        heading.id = headingId;
        if (episode.desc) heading.append(document.createTextNode(' '), element('span', 'path-desc', episode.desc));
        panel.append(heading);
        const links = resourceLinks(episode.links);
        if (links) panel.append(links);
        return panel;
    }

    function renderStep(step) {
        const livestream = step.kind === 'livestream';
        const item = element('li', `path-step${livestream ? ' path-step-alt prototype-livestream' : ''}`);
        const dot = element('span', `path-dot${livestream ? ' path-dot-alt' : ''}`);
        dot.setAttribute('aria-hidden', 'true');
        const body = element('div');
        const where = step.kind === 'exercise' ? 'in class' : step.kind === 'homework' ? 'home' : 'optional';
        const name = element('p', 'path-name', step.name);
        name.append(document.createTextNode(' '), element('span', 'path-where', where));
        body.append(name);
        if (step.sub) body.append(element('p', 'path-sub', step.sub));
        const links = resourceLinks(step.links);
        if (links) body.append(links);
        if (step.due) body.append(element('p', 'path-due', step.due));
        item.append(dot, body);
        if (step.video) item.append(videoLink(step.name, step.video, true));
        return item;
    }

    function renderBlock(block) {
        const section = element('section', 'block');
        section.id = blockElementId(block.id);
        const headingId = `${section.id}-heading`;
        section.setAttribute('aria-labelledby', headingId);
        const heading = element('h2', 'subtitle', `Block ${block.id} | ${block.title}`);
        heading.id = headingId;
        section.append(heading, element('p', 'block-description', block.description));
        const path = element('div', 'path');
        path.append(renderEpisode(block.episode, `${section.id}-episode`));
        const steps = element('ol', 'path-steps');
        block.steps.forEach(step => steps.append(renderStep(step)));
        path.append(steps);
        section.append(path);
        return section;
    }

    function renderCheckpoint(checkpoint) {
        const section = element('section', 'block checkpoint');
        section.id = 'miniexam';
        section.setAttribute('aria-labelledby', 'miniexam-heading');
        const heading = element('h2', 'subtitle', `MiniExam ${checkpoint.number}`);
        heading.id = 'miniexam-heading';
        section.append(heading);
        if (checkpoint.description) section.append(element('p', 'block-description', checkpoint.description));

        const path = element('div', 'path');
        path.append(renderEpisode(checkpoint.demo, 'miniexam-demo-heading'));
        const steps = element('ol', 'path-steps path-checkpoint');

        const demo = element('li', 'path-step');
        const demoDot = element('span', 'path-dot');
        demoDot.setAttribute('aria-hidden', 'true');
        const demoBody = element('div');
        const demoName = element('p', 'path-name', `Demo ${checkpoint.number}`);
        demoName.append(document.createTextNode(' '), element('span', 'path-where', 'home'));
        demoBody.append(demoName);
        const links = resourceLinks(checkpoint.demo_links);
        if (links) demoBody.append(links);
        demo.append(demoDot, demoBody);
        steps.append(demo);

        const exam = element('li', 'path-step path-step-checkpoint');
        const examDot = element('span', 'path-dot path-dot-big');
        examDot.setAttribute('aria-hidden', 'true');
        const examBody = element('div');
        const examName = element('p', 'path-name', `MiniExam ${checkpoint.number}`);
        examName.append(document.createTextNode(' '), element('span', 'path-where', 'in class'));
        examBody.append(examName);
        exam.append(examDot, examBody);
        steps.append(exam);

        if (checkpoint.next !== undefined) {
            const next = element('li', 'path-step path-step-next');
            next.setAttribute('aria-hidden', 'true');
            const nextDot = element('span', 'path-dot');
            nextDot.setAttribute('aria-hidden', 'true');
            const nextBody = element('div');
            nextBody.append(element('p', 'path-name', `Part ${checkpoint.next}`));
            next.append(nextDot, nextBody);
            steps.append(next);
        }
        path.append(steps);
        section.append(path);
        return section;
    }

    function renderProject(project) {
        const section = element('section', 'block checkpoint');
        section.id = project.id;
        const headingId = `${project.id}-heading`;
        section.setAttribute('aria-labelledby', headingId);
        const heading = element('h2', 'subtitle', project.title);
        heading.id = headingId;
        section.append(heading);
        if (project.description) section.append(element('p', 'block-description', project.description));

        const path = element('div', 'path');
        const prompts = element('div', 'path-episode path-text');
        project.prompts.forEach(prompt => {
            const detail = element('p', 'project-detail');
            detail.append(element('span', `project-label ${prompt.kind}`, prompt.label), document.createTextNode(' '), element('em', null, prompt.text));
            prompts.append(detail);
        });
        path.append(prompts);

        const steps = element('ol', 'path-steps path-checkpoint path-project');
        const item = element('li', 'path-step path-step-checkpoint');
        const dot = element('span', 'path-dot path-dot-big');
        dot.setAttribute('aria-hidden', 'true');
        const body = element('div');
        body.append(element('h3', 'path-name', project.title));
        const requirements = element('ol', 'path-brief');
        project.requirements.forEach(requirement => requirements.append(element('li', null, requirement)));
        body.append(requirements);
        const links = resourceLinks(project.links);
        if (links) body.append(links);
        item.append(dot, body);
        steps.append(item);
        path.append(steps);
        section.append(path);
        return section;
    }

    function renderHeader(part) {
        const header = element('header', 'description');
        const title = element('h1', 'title title-tight', `Part ${partId} | ${part.title}`);
        title.id = 'part-title';
        const tagline = element('p', 'subtitle-text', part.tagline);
        const rule = element('hr', 'title-rule');
        rule.setAttribute('aria-hidden', 'true');
        header.append(title, tagline, rule, element('p', null, part.introduction));
        return header;
    }

    function renderLeftNavigation(manifest, partIds) {
        const nav = element('nav');
        nav.setAttribute('aria-label', 'Course');
        const brand = element('a', 'course-brand-link');
        brand.href = safeUrl(manifest.home, 'course.home');
        brand.setAttribute('aria-label', `${manifest.code} home`);
        manifest.brand.forEach(line => brand.append(element('span', 'course-brand-line', line)));
        nav.append(brand);
        const rule = element('hr', 'nav-hr');
        rule.setAttribute('aria-hidden', 'true');
        nav.append(rule);
        const list = element('ul');
        partIds.forEach(id => {
            const item = element('li');
            const link = element('a', id === partId ? 'active' : null, `Part ${id}`);
            link.href = `part-${id}-yaml.html`;
            if (id === partId) link.setAttribute('aria-current', 'page');
            item.append(link);
            list.append(item);
        });
        (manifest.extra_nav || []).forEach(entry => {
            const item = element('li');
            const link = element('a', null, entry.label);
            link.href = safeUrl(entry.href, 'course.extra_nav href');
            item.append(link);
            list.append(item);
        });
        nav.append(list);
        leftSlot.replaceChildren(nav);
    }

    function rightNavigationItems(part) {
        const items = part.blocks.map(block => ({
            href: `#${blockElementId(block.id)}`,
            label: `${block.id} | ${block.nav}`
        }));
        if (part.checkpoint) items.push({ href: '#miniexam', label: `MiniExam ${part.checkpoint.number}` });
        if (part.project) items.push({ href: `#${part.project.id}`, label: part.project.nav });
        return items;
    }

    function renderRightNavigation(part) {
        const nav = element('nav');
        nav.setAttribute('aria-label', 'On this page');
        nav.append(element('p', 'prototype-nav-heading', 'Contents'));
        const rule = element('hr', 'nav-hr-right');
        rule.setAttribute('aria-hidden', 'true');
        nav.append(rule);
        const list = element('ul');
        rightNavigationItems(part).forEach((entry, index) => {
            const item = element('li', index === 0 ? 'nav-item-no-margin' : null);
            const link = element('a', `nav-link-right${index === 0 ? ' active' : ''}`, entry.label);
            link.href = entry.href;
            if (index === 0) link.setAttribute('aria-current', 'location');
            item.append(link);
            list.append(item);
        });
        nav.append(list);
        rightSlot.replaceChildren(nav);
    }

    function renderMobileNavigation(manifest, partIds) {
        document.querySelectorAll('.prototype-mobile-nav').forEach(node => node.remove());
        const current = partIds.indexOf(partId);
        const previous = current > 0
            ? { href: `part-${partIds[current - 1]}-yaml.html`, label: `Part ${partIds[current - 1]}` }
            : { href: manifest.home, label: `${manifest.code} home` };
        const extra = (manifest.extra_nav || [])[0];
        const next = current < partIds.length - 1
            ? { href: `part-${partIds[current + 1]}-yaml.html`, label: `Part ${partIds[current + 1]}` }
            : extra || { href: manifest.home, label: `${manifest.code} home` };
        const nav = element('nav', 'mobile-nav-bar prototype-mobile-nav');
        nav.setAttribute('aria-label', 'Part navigation');
        const previousLink = element('a', null, '‹');
        previousLink.href = safeUrl(previous.href, 'mobile previous link');
        previousLink.setAttribute('aria-label', `Previous: ${previous.label}`);
        const nextLink = element('a', null, '›');
        nextLink.href = safeUrl(next.href, 'mobile next link');
        nextLink.setAttribute('aria-label', `Next: ${next.label}`);
        nav.append(
            previousLink,
            element('span', 'mobile-nav-divider'),
            element('span', 'mobile-nav-label', `Part ${partId}`),
            element('span', 'mobile-nav-divider'),
            nextLink
        );
        document.body.append(nav);
    }

    function setupRightNavigation() {
        const links = Array.from(rightSlot.querySelectorAll('.nav-link-right'));
        if (links.length === 0) return;
        let scheduled = false;
        const update = () => {
            scheduled = false;
            const middle = window.scrollY + window.innerHeight / 2;
            let selected = links[0];
            let distance = Infinity;
            links.forEach(link => {
                const target = document.getElementById(link.hash.slice(1));
                if (!target) return;
                const candidate = Math.abs(middle - (target.offsetTop + target.offsetHeight / 2));
                if (candidate < distance) {
                    distance = candidate;
                    selected = link;
                }
            });
            links.forEach(link => {
                const active = link === selected;
                link.classList.toggle('active', active);
                if (active) link.setAttribute('aria-current', 'location');
                else link.removeAttribute('aria-current');
            });
        };
        window.addEventListener('scroll', () => {
            if (scheduled) return;
            scheduled = true;
            window.requestAnimationFrame(update);
        }, { passive: true });
        update();
    }

    function renderCourse(manifest, partIds) {
        const part = manifest.parts[partId];
        const fragment = document.createDocumentFragment();
        fragment.append(renderHeader(part));
        part.blocks.forEach(block => fragment.append(renderBlock(block)));
        if (part.checkpoint) fragment.append(renderCheckpoint(part.checkpoint));
        if (part.project) fragment.append(renderProject(part.project));
        fragment.append(element('div', 'bottom-spacer'));

        output.replaceChildren(fragment);
        renderLeftNavigation(manifest, partIds);
        renderRightNavigation(part);
        renderMobileNavigation(manifest, partIds);
        setupRightNavigation();
        document.title = `${manifest.code} | Part ${partId}`;
        page.removeAttribute('aria-busy');
        page.dataset.courseReady = 'true';
        status.hidden = true;

        if (location.hash) {
            window.requestAnimationFrame(() => {
                let id;
                try {
                    id = decodeURIComponent(location.hash.slice(1));
                } catch (_error) {
                    return;
                }
                const target = document.getElementById(id);
                if (target) target.scrollIntoView();
            });
        }
        document.dispatchEvent(new CustomEvent('course-content-ready', { detail: { part: partId } }));
    }

    function showError(error) {
        page.removeAttribute('aria-busy');
        page.dataset.courseError = 'true';
        output.replaceChildren();
        status.hidden = false;
        status.className = 'renderer-status renderer-error';
        status.setAttribute('role', 'alert');
        status.replaceChildren(document.createTextNode(`The course preview could not be loaded. ${error.message}`));
        if (page.dataset.courseFallback) {
            const fallback = element('a', null, 'Open the standard page.');
            fallback.href = page.dataset.courseFallback;
            status.append(document.createTextNode(' '), fallback);
        }
        console.error(error);
    }

    async function fetchText(url, timeoutMs) {
        const controller = new AbortController();
        const timeout = window.setTimeout(() => controller.abort(), timeoutMs);
        try {
            const response = await fetch(url, { cache: 'no-cache', signal: controller.signal });
            if (!response.ok) throw new Error(`${url} returned ${response.status}`);
            return await response.text();
        } catch (error) {
            if (error.name === 'AbortError') throw new Error(`${url} did not respond within ${Math.round(timeoutMs / 1000)} seconds`);
            throw error;
        } finally {
            window.clearTimeout(timeout);
        }
    }

    async function load() {
        try {
            if (!output || !status || !leftSlot || !rightSlot) {
                throw new Error('The preview page shell is incomplete');
            }
            if (!window.jsyaml || typeof window.jsyaml.load !== 'function') {
                throw new Error('The YAML reader did not load');
            }
            safeUrl(source, 'page data-course-source');
            const parsed = window.jsyaml.load(await fetchText(source, 10000), {
                maxDepth: 100,
                maxTotalMergeKeys: 1000
            });
            const validated = validateManifest(parsed);
            renderCourse(validated.manifest, validated.partIds);
        } catch (error) {
            showError(error instanceof Error ? error : new Error(String(error)));
        }
    }

    load();
}());
