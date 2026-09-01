# ECON 0150 | Skillsheet | Draft for Spec-Based Grading

Every skill students have actually been assessed on, written as a spec:
a thing a student either demonstrates or doesn't. Drafted for the move
to spec-based grading.

**Scope.** This is an audit of *assessment*, not coverage. Each spec
below is here because it appeared on a MiniExam, a homework, or the
final project — not because it was taught. Skills that are taught but
never assessed are listed at the end, separately, so the distinction
stays visible.

**Sources.** All MiniExam versions and demos (`ME_1`–`ME_5`, including
F25/S26 variants and the ME1/ME2 question banks), the ME4 S26 and ME5
F25/S26/F26 rubrics, all 26 homework assignments, and the final project
guidelines and rubric.

**Format.** Follows the existing `ME_5_F26_Rubric.md` draft: each spec
has pass criteria that are all-required, an explicit "not yet"
condition, and a note on judgment calls. Specs are **pass / not yet** —
no partial credit inside a spec.

---

## How the specs are organized

**27 exam specs across 5 bundles, plus 4 project specs — 31 total.**
Each bundle corresponds to a MiniExam and to a part of the course.

| Bundle | Part | Specs | Standard | Advanced ★ |
|---|---|---|---|---|
| A — Describing Data | 1 | A1–A5 | A1–A4 | A5 |
| B — Relationships & Transformation | 2 | B1–B5 | B1–B5 | — |
| C — Inference | 3 | C1–C5 | C1–C5 | — |
| D — The Bivariate Model | 4 | D1–D6 | D1–D5 | D6 |
| E — Controls & Interactions | 5 | E1–E6 | E1–E5 | E6 |
| P — Project | 6 | P1–P4 | P1–P4 | — |

Passing the standard specs in every bundle is the course's competence
bar; ★ specs are the stretch tier if you run two. **The pass threshold
per bundle is left open** — your ME5 draft uses 4 of 5, but see decision
2 below, since a uniform threshold lets a student permanently skip one
spec per bundle.

---

## Bundle A — Describing Data
*Assessed on ME1 (six data tables, no code) and HW 1.1–1.5*

### A1. Classify a dataset's structure and variables

**Tested by:** ME1 Q1–Q6 (part a); HW 1.1 Q2–Q5

**Pass criteria (all required):**
1. Names the data structure: cross-section, time series, or panel
2. Names each variable's type: categorical (binary/nominal/ordinal) or numerical (discrete/continuous)
3. States the number of variables

**Not yet:** Confuses time series with panel; calls an ordinal variable numerical; misses the index variable.

> This is the foundation spec — every later visualization choice depends
> on it. Assessed six times on ME1, so a student has ample opportunity
> to demonstrate it. Require at least 4 of 6 correct.

### A2. Choose the appropriate visualization for a data type

**Tested by:** ME1 Q1–Q6 (part b); ME1 Demo Bank Q2, Q3, Q6; HW 1.2 Q3, HW 1.3 Q4

**Pass criteria (all required):**
1. Chooses a display that matches the variable types and structure
2. The choice is defensible in one sentence when asked

**Reference mapping students are held to:**

| Data | Expected choice |
|---|---|
| One categorical variable | Bar chart (pie only if binary) |
| One numerical variable, many observations | Histogram |
| One numerical variable, few observations | Boxplot (+ stripplot) |
| One numerical variable over time | Line plot |
| Numerical across categories | Grouped boxplot |
| Two numerical | Scatterplot |
| Panel (entity × time) | Multi-line or faceted plot |

**Not yet:** Pie chart for a multi-category variable; histogram for a time series; bar chart for two numerical variables.

### A3. Draw a correct figure from a data table

**Tested by:** ME1 Q1–Q6 (part b, "draw or describe"); ME1 Demo Bank Q5, Q4b

**Pass criteria (all required):**
1. Correct chart type for the data
2. Both axes labeled with the right variables
3. Shape is faithful to the data shown (right direction, right relative magnitudes)

**Not yet:** Unlabeled axes; a sketch that contradicts the table.

> Students may "draw or describe." A precise description earns the pass —
> this spec is about knowing what the figure *is*, not draftsmanship.

### A4. Summarize a distribution numerically

**Tested by:** HW 1.1 Q6–Q7, HW 1.2 Q1–Q2

**Pass criteria (all required):**
1. Computes or reads center (mean or median) and spread (SD or IQR)
2. Reads quartiles off a boxplot correctly
3. Describes shape in words (symmetric, skewed, outliers)

**Not yet:** Reports mean without spread; misreads the box as the range.

### A5. Transform a variable and say why ★

**Tested by:** HW 1.3 Q1–Q2 (real price adjustment, growth rates); HW 1.5 Q1

**Pass criteria (all required):**
1. Applies the right transformation (inflation adjustment, per capita, growth rate, difference)
2. States what question the transformation makes answerable

**Not yet:** Transforms without justification; compares nominal values across decades.

> Assessed only on homework, never on an exam. If you want this on ME1,
> it needs a question. Otherwise treat it as homework-certified.

---

## Bundle B — Relationships & Transformation
*Assessed on ME2 (Versions A/B + Demo + Bank) and HW 2.1–2.5*

### B1. Choose and draw a Part 2 visualization

**Tested by:** ME2 Q1 (a, b, c across three datasets)

**Pass criteria (all required):**
1. Identifies variable types for each dataset
2. Two numerical → scatterplot; one numerical + one categorical → grouped boxplot; two numerical + one categorical → scatter colored by category
3. Draws each with labeled axes

**Not yet:** Any of the three mismatched to its data.

> Three datasets in one question. Require all three; the whole point is
> discriminating between the three cases.

### B2. Diagnose and fix a misleading figure

**Tested by:** ME2 Q2 ("Fix the Figure", three figures); ME2 Bank Q1b, Q5b

**Pass criteria (all required):**
1. Names the problem (skew compressing the data, wrong chart type, unreadable scale)
2. Names the fix (log scale, different chart, filtering)
3. Draws the improved version

**Not yet:** "It looks bad" without naming the cause; a redraw that doesn't fix the stated problem.

### B3. Interpret log scales

**Tested by:** ME2 Q4 (a, b, c); ME2 Demo Q3

**Pass criteria (all required):**
1. One log10 unit = ×10; one log2 unit = ×2
2. Computes a multi-unit jump (4 units on log2 = ×16)
3. Compares two logged values (3 units apart on log10 = 1,000×)

**Not yet:** Reads a log unit as an addition rather than a multiplication.

> Pure computation, multiple choice. All three sub-parts required — one
> right answer out of three is guessing.

### B4. Filter data to reveal a pattern

**Tested by:** ME2 Q3 ("Investigate and Visualize"); ME2 Bank Q1–Q3 (filtering); HW 2.3

**Pass criteria (all required):**
1. Identifies which rows don't belong given the question (e.g., Social members who never use equipment)
2. States the filter condition
3. Describes how the figure changes after filtering

**Not yet:** Plots everything and calls the result uninformative; filters on the wrong variable.

> The exam framing is deliberately indirect — students must notice the
> data problem themselves. That noticing is the skill.

### B5. Read a scatterplot split by category

**Tested by:** ME2 Q5 (a, b, c)

**Pass criteria (all required):**
1. Reads the trend for each group separately
2. Compares groups at a specific x value
3. Describes how the relationship differs between groups

**Not yet:** Reports one overall trend and ignores the split.

> This is the visual precursor to interaction models in Bundle E. Worth
> saying so to students explicitly.

---

## Bundle C — Inference
*Assessed on ME3 (S26 + Demo) and HW 3.1–3.4*

### C1. Describe a sampling distribution

**Tested by:** ME3 Q1 (a, b, c at n=1, 49, 144); ME3 Demo Q1

**Pass criteria (all required):**
1. Center: the population mean μ, at every n
2. Spread: the standard error σ/√n, computed correctly
3. Shape: approximately normal for large n, whatever the population shape

**Not yet:** Says the sampling distribution has spread σ; says the shape matches the population at large n.

> Asked at three sample sizes including n=1. The n=1 case is the
> discriminator — a student who says "normal" there hasn't understood.

### C2. Apply the Central Limit Theorem to a skewed population

**Tested by:** ME3 Q2 (a, b, c); ME3 Demo Q2, Q3; HW 3.2 Q2

**Pass criteria (all required):**
1. Describes the histogram of many sample means as approximately normal
2. States that a smaller n gives a wider distribution
3. Judges whether one observed mean is surprising, using the SE

**Not yet:** Says the histogram of sample means looks like the (skewed) population.

### C3. Construct and interpret a confidence interval

**Tested by:** ME3 Q3b; ME3 Demo Q5 (a, b, c); HW 3.3 Q1–Q2

**Pass criteria (all required):**
1. Computes x̄ ± 2·SE with the right SE
2. States both bounds
3. Uses it to reach a reject / fail-to-reject conclusion when asked

**Not yet:** Uses σ instead of SE; interprets the interval as containing 95% of the data.

### C4. Describe the null sampling distribution and visualize a p-value

**Tested by:** ME3 Q3a, Q3c; ME3 Demo Q4a

**Pass criteria (all required):**
1. Centers the null distribution on the hypothesized value, **not** the sample mean
2. Uses the correct standard error for its spread
3. Shades the tail region(s) corresponding to the p-value

**Not yet:** Centers on x̄ (the single most common error — "the centerpoint flip" from 3.3); shades one tail on a two-tailed test without saying so.

### C5. Interpret a p-value in words

**Tested by:** ME3 Q4; ME3 Demo Q4b; ME4 Demo Q4a; HW 3.3 Q3

**Pass criteria (all required):**
1. Frames it as a probability of data at least this extreme
2. Conditions on the null being true
3. Avoids claiming the probability that the null is true

**Not yet:** "There's a 12% chance the null is true"; "12% chance the result is due to random noise."

> Assessed on both ME3 and ME4. Two independent demonstrations, so this
> can be a strict spec.

---

## Bundle D — The Bivariate Model
*Assessed on ME4 (S26 + Demo, with a full spec-style rubric) and HW 4.1–4.4*

### D1. Write a regression model for a research question

**Tested by:** ME4 Q1a, Q2a; ME4 Demo Q1a, Q2a

**Pass criteria (all required):**
1. Correct outcome on the left
2. Correct predictor on the right with a coefficient
3. Error term present

**Not yet:** Outcome and predictor flipped; no error term.

> The S26 rubric gives 3/5 for a flipped model ("structure right,
> concept wrong"). Under specs that's a **not yet** — but it's the
> clearest case where you may want a partial tier.

### D2. Sketch the model's visualization

**Tested by:** ME4 Q1b, Q3a; ME4 Demo Q1b, Q2b

**Pass criteria (all required):**
1. Scatterplot with fitted line for a numerical predictor; two group means (or boxplots) for a binary predictor
2. Predictor on x, outcome on y
3. Axes labeled

**Not yet:** Omits the fitted line ("visualization of this model" implies it); wrong chart type for the predictor type.

### D3. Interpret a coefficient in context

**Tested by:** ME4 Q1c, Q3b, Q3c; ME4 Demo Q3b, Q3c; HW 4.1 Q3, HW 4.2 Q2

**Pass criteria (all required):**
1. States the one-unit change in x
2. States direction **and** magnitude of the change in y
3. Uses variable names and units — not "x" and "y"

**Not yet:** "They are positively related" (no magnitude); "0.48 higher" (no unit of x).

> Also requires interpreting the **intercept** in context where asked
> (ME4 Q3b). Students often skip it or describe it as meaningless — it
> should be read as the predicted value at x = 0.

### D4. Work with a binary predictor

**Tested by:** ME4 Q2b, Q2c, Q2d; ME4 Demo Q6

**Pass criteria (all required):**
1. β₀ = mean of the reference group
2. β₁ = difference between groups
3. Correctly recomputes both when the coding is **flipped** (ME4 Q2d)

**Not yet:** Gives β₀ as the overall mean; can't handle the recoding.

> The recoding sub-question is the real test. It separates memorized
> definitions from understanding.

### D5. Diagnose a residual plot

**Tested by:** ME4 Q5 (a, b); ME4 Demo Q5; HW 4.3 Q2–Q3

**Pass criteria (all required):**
1. Names the violated assumption from the pattern (fan → homoskedasticity; curve → linearity; wave/lag → independence)
2. Names a defensible fix (log transform, different specification, differencing)

**Not yet:** Names the wrong assumption; "the model is bad."

### D6 ★. Draw the null sampling distribution for a slope

**Tested by:** ME4 Q4; ME4 Demo Q5

**Pass criteria (all required):**
1. Centered at β₁ = 0
2. Spread equal to the reported standard error
3. Observed coefficient marked, p-value region shaded

**Not yet:** Centered on the observed coefficient.

> Same conceptual move as C4, one level up. Consider whether passing C4
> should exempt a student here, or whether the repetition is the point.

---

## Bundle E — Controls & Interactions
*Assessed on ME5 (F25 + S26 + Demo) and HW 5.1–5.4. Your existing
`ME_5_F26_Rubric.md` already drafts these; reproduced here with the
numbering aligned to the other bundles.*

### E1. Select the correct model for a research question

**Tested by:** ME5 Q1a (F25 and S26)

**Pass criteria:**
- "Holding constant" / "controlling for" → both predictors as separate terms, no interaction
- "Differs by" / "allowing the effect to vary" → interaction term present

**Not yet:** Wrong model.

> Recognition task, no partial credit. **Single MC question — one lucky
> guess passes.** Flagged in your F26 notes; worth a second question or
> a one-line justification.

### E2. Interpret a coefficient holding a control constant

**Tested by:** ME5 Q1b, Q2b, Q3c

**Pass criteria (all required):**
1. States the one-unit (or group) change in x
2. States direction and magnitude of the change in y
3. Uses "holding constant," "comparing two units with equal…," or equivalent

**Not yet:** A correct Bundle D interpretation with no control language.

> **Must be demonstrated twice** across the exam. This is the bright
> line for Part 5 and the core skill of the bundle.

### E3. Write a multiple regression model

**Tested by:** ME5 Q2a

**Pass criteria (all required):**
1. Correct outcome on the left
2. Both predictors with separate coefficients
3. Error term present

**Not yet:** Missing a predictor; an interaction term where the question said "controlling for."

### E4. Predict from a fitted model

**Tested by:** ME5 Q3a, Q3b

**Pass criteria (all required):**
1. Plugs values into all terms, including the binary predictor
2. Correct answer, or correct setup with a minor arithmetic slip

**Must pass both sub-parts.**

**Not yet:** Drops the binary term; fundamentally wrong setup.

> Watch for units (mileage in thousands: 60 vs 60,000). Your F26 notes
> leave this open — a units error is arguably a pass-with-note rather
> than a not-yet, since the model reasoning is intact.

### E5. Compute and interpret an interaction

**Tested by:** ME5 Q4a, Q4b, Q4c

**Pass criteria (all required):**
1. Reference-group effect = β₁
2. Other-group effect = β₁ + β₃
3. Identifies β₃ as the *difference* in effects

**Not yet:** Same effect for both groups; gives β₃ as the full effect for the interacted group.

> All three must be consistent — right computation with the wrong
> interpretation suggests arithmetic luck.

### E6 ★. Explain why a control is needed

**Tested by:** ME5 Q2c

**Pass criteria (all required):**
1. States that the control relates to **both** predictor and outcome
2. Explains how omitting it biases the estimate

**Not yet:** "To be more accurate"; "to improve the model."

> The one spec that asks *why* rather than *how*. Currently the advanced
> tier.

---

## Bundle P — The Project
*Assessed by the final report, slides, and replication folder*

### P1. Pose an answerable question and match data to it
### P2. Apply an appropriate method and justify the choice
### P3. Interpret results correctly, including limitations
### P4. Communicate in a written report and a short presentation

> These are held to the existing project rubric rather than restated as
> specs. Flagged as a gap below — if the whole course moves to specs,
> the project needs the same treatment, and it's the one assessment
> where **code fluency** is actually certified.

---

## Assessed but not on any MiniExam

Practiced and graded on homework only. Each is a candidate for either an
exam question or explicit "homework-certified" status:

| Skill | Where |
|---|---|
| Transformations: real prices, per capita, growth rates | HW 1.3, 1.5 |
| Panel data: multi-line plots, faceting, groupby summaries | HW 1.4 |
| Geographic data and maps | HW 2.5 |
| Reshaping: melt / pivot | HW 1.5 optional |
| Time-series model comparison: levels vs differences vs growth | HW 4.4 |
| Model comparison and causal language | HW 5.4 |
| Data cleaning: missing values, dates, strings | HW 2.1 (cleaning) |
| All code fluency: pandas, seaborn, statsmodels | every HW; certified by P |

---

## Taught but never assessed

Neither exams nor homework test these. They complete the toolkit or
serve the project, and naming them keeps the specs honest:

Anscombe's Quartet · bubble/size encoding · merging datasets ·
PDF/CDF computation · MSE mechanics · deseasonalization ·
R² and the F-statistic · Simpson's Paradox as such (the *tool* is
assessed in E2; the paradox itself is not).

---

## Decisions to make before F26

Carried forward from your ME5 draft, plus what this audit surfaced.

1. **Reattempt policy.** The central unanswered question — specs only work if "not yet" can become "pass." Ties to the existing 2-of-3 gate and TA makeup policy.

2. **Bundle pass threshold.** 4 of 5 is drafted for ME5. Applying it uniformly means a student can skip one spec per bundle permanently. Are some specs non-negotiable? A1, C4, D3, and E2 are the load-bearing ones.

3. **Single-question specs are fragile.** E1 (one MC), D6, and B3 rest on one question each. A lucky guess passes. Either add a second question or require a one-line justification.

4. **Partial structure inside a spec.** The ME4 rubric awards 3/5 for a flipped model — real information that pure pass/not-yet discards. Consider a "pass with note" state for errors that are mechanical rather than conceptual (flipped axes, unit slips).

5. **Two tiers or one?** Five ★ specs are marked (A5, D6, E6). A standard/advanced split rewards depth without penalizing competence — but doubles the bookkeeping.

6. **The project needs specs.** It's 4 broad criteria against a holistic rubric while everything else becomes granular. It's also the only place code is assessed.

7. **Repeated specs across bundles.** C4 and D6 are the same skill at different levels; C5 is assessed on both ME3 and ME4. Decide whether a later pass supersedes an earlier not-yet.

---

*Draft, 2026-08-21. Audited from all MiniExam versions and demos, the
ME1/ME2 question banks, the ME4 S26 and ME5 F25/S26/F26 rubrics, 26
homework assignments, and the project guidelines and rubric. Companion:
`Course_Specs.md` (full coverage map, including unassessed material).*
