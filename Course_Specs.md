# ECON 0150 | Economic Data Analysis | Course Specifications

A concept-by-concept map of what the course teaches, how it builds, what students practice, and what is assessed. Written in the spirit of spec-based grading: every unit is described as a set of skills a student can demonstrate, each tagged with where it is practiced and where it is assessed.

**Audiences.** Students: use this to see exactly what you are expected to be able to do at each point in the course. Instructors: use this as the authoritative statement of coverage and assessment — what a MiniExam may ask is bounded by the skills tagged to it here.

**Tags.** Each skill carries the places it appears:

| Tag | Meaning |
| --- | --- |
| `E` | practiced in the in-class exercise (supported) |
| `HW` | practiced independently on homework |
| `ME1`–`ME5` | assessed on that MiniExam |
| `FP` | assessed in the final project |
| `—` | taught and practiced, not directly assessed |

Assessment tags reflect what recent exam versions actually asked (F25/S26 exams and rubrics), not aspirations.

---

## The Spine of the Course

Every unit adds to one of four accumulating **building blocks**:

- **Variables** — what kind of values? *(categorical: binary, nominal, ordinal; numerical: discrete, continuous)*
- **Structures** — how is the data organized? *(cross-section, time series, panel long/wide, geographic)*
- **Operations** — what do I do to it? *(count, bin, summarize, transform, filter, group, reshape, merge, clean)*
- **Visualizations** — how do I show it? *(bar, pie, histogram, boxplot, line, scatter, and their multiples)*

And every figure is built by the same three-step pattern:

> **SELECT** the subset → **TRANSFORM** to summarize or reshape → **ENCODE** values as visual elements.

The course then makes one long move: **Parts 1–2 teach students to *****see***** data; Parts 3–5 teach them to *****test***** what they see**, using a single expanding tool — the general linear model — rather than a zoo of disconnected tests. Each EDA skill has a modeling twin:

| You learn to see it with… | …then test it with |
| --- | --- |
| Boxplots by category (2.2) | Two-sample t-test / binary-predictor GLM (4.2) |
| Scatterplots (2.1) | Bivariate regression (4.1) |
| Scatter colored by category (2.3) | Regression with categorical controls (5.1) |
| One histogram (1.2) | Intercept-only GLM (3.4) |

---

## Part 0 | Framework

*What is data, and what tools do we need?* One block, week 1. Motivated by Card & Krueger's minimum-wage study, which returns as the running example in 1.4 and 3.3.

| # | Skill — the student can… | Practice | Assessed |
| --- | --- | --- | --- |
| 0.1 | State that data is a realization of an underlying random process, and that analysis targets the process, not the sample | E | ME3 (implicitly) |
| 0.2 | Write data in `x_it` notation and distinguish substantive variables from index variables | E, HW | ME1 |
| 0.3 | Classify a dataset's structure: cross-section, time series, panel, geographic | E, HW | ME1 |
| 0.4 | Classify each variable's type: binary / nominal / ordinal categorical; discrete / continuous numerical | E, HW | ME1 |
| 0.5 | Describe the SELECT → TRANSFORM → ENCODE pattern for constructing a figure | E | — |

---

## Part 1 | Exploring Variables

*What does one variable look like?* One substantive variable at a time, walked across data structures: cross-section → time series → panel.

### 1.1 Cross-Sectional Categorical Data

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 1.1.1 | Summarize a categorical variable with counts and proportions (`value_counts`) | E, HW | ME1 |
| 1.1.2 | Choose and construct the right display: bar chart for nominal/ordinal, pie only for binary | E, HW | ME1 |
| 1.1.3 | Apply figure hygiene: remove clutter, order categories by size | E, HW | ME1 (via drawing) |
| 1.1.4 | Collapse a nominal variable into a binary one (e.g., CA vs. Other) and display it as percentages | E | — |

### 1.2 Cross-Sectional Numerical Data

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 1.2.1 | Construct a histogram; choose bin widths that balance resolution against noise | E, HW | ME1 |
| 1.2.2 | Describe a distribution's shape, center, and spread; compute mean and standard deviation | E, HW | ME3 (reused) |
| 1.2.3 | Construct a boxplot (+ stripplot) and read the five-number summary / quartiles | E, HW | ME1 |
| 1.2.4 | Choose histogram vs. boxplot based on sample size and purpose | E | ME1 |

### 1.3 Time Series Data

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 1.3.1 | Construct a line plot for a t-indexed variable; identify trends and subtrends | E, HW | ME1 |
| 1.3.2 | Adjust a nominal series for inflation using the CPI (real vs. nominal) | E, HW | — |
| 1.3.3 | Detect seasonality with monthly multi-boxplots | E, HW | — |
| 1.3.4 | Recognize that a time-series plot is still univariate analysis: time is scaffolding, not a substantive variable | E | ME1 |

### 1.4 Panel Data (Long Format)

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 1.4.1 | Recognize long-format panel data: both `i` and `t` active, one row per entity-period | E, HW | ME1 |
| 1.4.2 | Use `groupby` to build summary tables across entities or periods | E, HW | ME2 |
| 1.4.3 | Compare entities over time with multi-line plots | E, HW | ME1 |
| 1.4.4 | Compare distributions across groups with faceted histograms / small multiples | E, HW | — |

### 1.5 Panel Data (Wide Format)

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 1.5.1 | Recognize wide format and explain that wide and long are the same data | E, HW | — |
| 1.5.2 | Compare distributions across years with multi-boxplots | E, HW | — |
| 1.5.3 | Track entity changes between periods with a scatterplot against a 45° line | E, HW | — |
| 1.5.4 | Reshape between formats with `melt` and `pivot` *(optional unit)* | E | — |
| 1.5.5 | Count subsets with basic filtering (previewing 2.3) | E, HW | ME2 |

**End of Part 1 toolkit** — variables: categorical (binary, nominal, ordinal), numerical · structures: cross-section, time series, panel (long & wide) · operations: count, bin, mean, SD, quartiles, real-price transform, groupby, filter · visualizations: bar, pie, histogram, boxplot, stripplot, line, multi-boxplot, multi-line, facets, scatterplot w/ 45° line.

### MiniExam 1 — data dimensions and visualization choice

Format: six small data tables. For each, the student **identifies the data structure, the variable type(s), and the number of variables, then draws or describes an appropriate visualization.** This is the capstone of skills 0.2–0.4 and the visualization-choice skills of 1.1–1.4. Everything on ME1 is table → dimensions → picture; no code.

---

## Part 2 | Exploring Relationships

*How do variables relate?* A second substantive variable arrives, plus the operations for preparing data: filtering and log transformation.

### 2.1 Numerical × Numerical

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 2.1.1 | Construct a scatterplot for two numerical variables; describe direction, form, strength | E, HW | ME2 |
| 2.1.2 | Apply log transformation to deskew a variable; know when to log one axis vs. both | E, HW | ME2 |
| 2.1.3 | Interpret log-scaled axes: one log2 unit = doubling; one log10 unit = tenfold; compare two values on a log scale | E, HW | ME2 |
| 2.1.4 | Encode a third variable with size (bubble chart) or color | E | — |
| 2.1.5 | Explain Anscombe's Quartet: identical summary statistics can hide different data — always visualize | E | — |

### 2.2 Numerical × Categorical

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 2.2.1 | Compare a numerical variable across categories with grouped boxplots | E, HW | ME2 |
| 2.2.2 | Compute grouped statistics (count, mean, sum by category) and predict the shape of the output (rows, groups) | E, HW | ME2 |
| 2.2.3 | Diagnose a compressed or misleading figure (skew, zeros) and fix it by filtering or logging | E, HW | ME2 |
| 2.2.4 | Reason about overlapping group distributions: seeing a difference is not the same as the difference being real *(bridge to Part 3)* | E | — |

### 2.3 Filtering & Encoding Categories

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 2.3.1 | Filter rows by category and by inequality | E, HW | ME2 |
| 2.3.2 | Combine filters with AND / OR / NOT and predict which rows survive | E, HW | ME2 |
| 2.3.3 | Encode a categorical variable in a scatterplot with color or shape | E | ME2 |
| 2.3.4 | Read a color-coded scatterplot: identify separate trends per group and describe how the relationship differs | E, HW | ME2 |

### Additional Part 2 material (taught some semesters)

- **Merging** — join two datasets on a shared key (elections + income by county). Practiced when taught; not currently assessed.
- **Geographic data** — maps, location as index (restaurant zipcodes; city temperature/population). Practiced when taught; not currently assessed.
- **Data cleaning** — string parsing, type conversion, missing values (survey data). Practiced when taught; feeds the final project.

### MiniExam 2 — relationships, transformation, and subsetting

Across versions, ME2 asks students to: **choose the right visualization from variable types; sketch scatterplots, grouped boxplots, and scatter-by-category; diagnose and fix a skewed figure with logs; interpret log2/log10 scales; predict the output of grouped aggregations; and apply compound filters to a data table.** Skills listed as `E`-only above (bubble charts, Anscombe, merging, maps) are deliberately excluded.

---

## Part 3 | Univariate GLM

*What can we infer about the population?* From description to inference: the sample/population distinction, the CLT, confidence intervals, hypothesis tests — converging on the simplest possible model.

### 3.1 Random Variables

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 3.1.1 | Distinguish sample statistics from population parameters | E, HW | ME3 |
| 3.1.2 | Describe a distribution by location (mean, median) and dispersion (SD, IQR) and choose measures appropriate to skew | E, HW | ME3 |
| 3.1.3 | Read a PDF and a CDF; compute probabilities from a known distribution | E, HW | — |

### 3.2 Sampling & the Central Limit Theorem

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 3.2.1 | State the CLT: the sample mean is approximately normal around μ with spread σ/√n, regardless of the population's shape | E, HW | ME3 |
| 3.2.2 | Compute the standard error and predict how the sampling distribution changes with n | E, HW | ME3 |
| 3.2.3 | Apply the CLT to a *skewed* population: describe the histogram of many sample means | E, HW | ME3 |
| 3.2.4 | Judge whether one observed sample mean is surprising given a sampling distribution | E, HW | ME3 |

### 3.3 Confidence Intervals & Hypothesis Testing

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 3.3.1 | Construct a confidence interval as x̄ ± 2·SE and interpret it as a statement about the estimate, not the parameter | E, HW | ME3 |
| 3.3.2 | Describe the sampling distribution *under the null hypothesis* (the centerpoint flip: center on H₀, not on x̄) | E, HW | ME3 |
| 3.3.3 | Use S for unknown σ and explain why the t-distribution replaces the normal | E, HW | — |
| 3.3.4 | Compute a t-statistic; visualize and interpret a p-value on the null sampling distribution | E, HW | ME3 |
| 3.3.5 | Interpret a p-value in one plain-English sentence, and distinguish statistical from practical significance | E, HW | ME3 |

### 3.4 The Simplest GLM

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 3.4.1 | Write the intercept-only model y = β₀ + ε and identify β̂₀ as the sample mean | E, HW | ME4 (as the base case) |
| 3.4.2 | Explain the mean as the MSE-minimizing line; compute MSE for a candidate line | E, HW | — |
| 3.4.3 | Fit the model in code (`smf.ols('y ~ 1')`), read the output, and recognize the one-sample t-test inside it | E, HW | ME4 (output reading) |

### MiniExam 3 — sampling and inference

Recent versions ask students to: **give the sampling distribution of the mean at several n (including n=1); describe the histogram of 10,000 sample means from a skewed population and how it changes with n; judge whether an observed mean is surprising; describe the null sampling distribution; build a 2-SE confidence interval; visualize a p-value on a sketch of the null distribution; and interpret a p-value in one sentence.** No code; reasoning and sketching only.

---

## Part 4 | Bivariate GLM

*How does y change with x?* One predictor — numerical, then categorical — then the assumptions that make the machinery trustworthy, and the one place they reliably fail: time series.

### 4.1 Numerical Predictors

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 4.1.1 | Write the bivariate model y = β₀ + β₁x + ε with the correct outcome and predictor for a stated question | E, HW | ME4 |
| 4.1.2 | Sketch the model's visualization: scatterplot, predictor on x, fitted line | E, HW | ME4 |
| 4.1.3 | Interpret β̂₁ in context: predicted change in y per one-unit change in x (direction, magnitude, units) | E, HW | ME4 |
| 4.1.4 | Generate predictions from a fitted model | E, HW | ME5 (reused) |
| 4.1.5 | Explain the slope's sampling distribution: β̂₁ varies from sample to sample around β₁ | E | ME4 (drawing) |

### 4.2 Categorical Predictors

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 4.2.1 | Write and fit a model with a binary predictor; interpret β̂₀ as the base-group mean and β̂₁ as the group difference | E, HW | ME4 |
| 4.2.2 | Recognize that a binary-predictor GLM *is* the two-sample t-test | E, HW | ME4 |
| 4.2.3 | Read a full regression output: coefficient, standard error, t-statistic, p-value, confidence interval — and state the conclusion | E, HW | ME4 |

### 4.3 Model Assumptions

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 4.3.1 | Name the four assumptions: linearity, homoskedasticity, independence, normality | E, HW | ME4 |
| 4.3.2 | Compute residuals and construct a residual-vs-fitted plot | E, HW | — |
| 4.3.3 | Diagnose violations from a residual plot (curvature → non-linearity; funnel → heteroskedasticity; waves/lag pattern → dependence) | E, HW | ME4 |
| 4.3.4 | Propose the standard fixes: log transforms for non-linearity/heteroskedasticity | E | — |

### 4.4 The Problem of Time Series

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 4.4.1 | Explain autocorrelation as the failure of independence in t-indexed data | E, HW | ME4 (residual reading) |
| 4.4.2 | Compare model specifications for trending data: levels → first differences → growth rates | E, HW | — |
| 4.4.3 | Read a lagged residual plot to check whether differencing removed the dependence | E | ME4 |

### MiniExam 4 — the bivariate model end to end

Recent versions (per the S26 rubric): **Q1 write, sketch, and interpret a numerical-predictor model; Q2 the same for a binary predictor; Q3 read a regression output (coefficient, SE, t, p, CI, conclusion); Q4 draw the sampling distribution of an estimate; Q5 interpret residual plots, including a lagged residual plot.** Partial credit follows explicit per-answer specs; interpretation questions require the one-unit change, the direction/magnitude, and the context to earn full marks.

---

## Part 5 | Multivariate GLM

*How does y change with x, holding z constant?* Confounding is the motivation; controls, interactions, and model selection are the tools.

### 5.0 Causality (bridge)

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 5.0.1 | Distinguish correlation from causation; give the three standard failure modes: common cause, reverse causality, selection | E | ME5 (via "why control?") |
| 5.0.2 | Explain a spurious correlation by naming the lurking variable (ice cream & drowning) | E | — |
| 5.0.3 | Explain what controls can and cannot buy you: conditioning ≠ causal identification | E | — |

### 5.1 Categorical Controls

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 5.1.1 | Explain Simpson's Paradox: a relationship can reverse when a grouping variable is conditioned on | E | — |
| 5.1.2 | Write and fit a model with a categorical control (fixed effects / multiple intercepts) | E, HW | ME5 |
| 5.1.3 | Interpret a coefficient "holding the control constant," in one sentence, in context | E, HW | ME5 |
| 5.1.4 | Explain *why* a specific control belongs in a specific model (what confound it absorbs) | E, HW | ME5 |
| 5.1.5 | Deseasonalize a series with month fixed effects *(taught some semesters)* | E | — |

### 5.2 Interactions

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 5.2.1 | Write a model where the slope differs by group: y = β₀ + β₁x + β₂D + β₃(x·D) + ε | E, HW | ME5 |
| 5.2.2 | Compute the slope for each group (β₁ vs. β₁+β₃) and predicted values for either group | E, HW | ME5 |
| 5.2.3 | Interpret the interaction coefficient: the *difference* in slopes between groups | E, HW | ME5 |
| 5.2.4 | Interpret coefficients when the outcome is logged (≈ percent effects) | E, HW | — |

### 5.3 Numerical Controls

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 5.3.1 | Fit multiple regression with several numerical predictors | E, HW | ME5 |
| 5.3.2 | Interpret each coefficient "holding the others constant" | E, HW | ME5 |
| 5.3.3 | Compare separate bivariate models to one joint model and explain why coefficients change | E, HW | — |
| 5.3.4 | Check residual diagnostics on a multivariate model | E, HW | — |

### 5.4 Model Selection *(taught some semesters)*

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 5.4.1 | Interpret R² as proportion of variation explained — and why it cannot fall when variables are added | E | — |
| 5.4.2 | Explain overfitting: adding noise variables raises R² | E | — |
| 5.4.3 | Use the F-statistic to test a model against noise / test the full model | E | — |

### MiniExam 5 — models with controls

Recent versions ask students to: **choose or write the regression that answers a stated question with a control; interpret a coefficient holding the control constant; explain in words why the control belongs; compute predictions from a fitted model with a binary predictor; interpret a binary coefficient; and work an interaction model — the per-group slopes and the meaning of the interaction term.** All reasoning from provided output; no code.

---

## Part 6 | Communicating with Data

*How do I tell someone what I found?* Workflow and communication, assessed through the final project rather than a MiniExam.

| # | Skill | Practice | Assessed |
| --- | --- | --- | --- |
| 6.1 | Take a question from raw data to model to interpretation in one reproducible notebook | E | FP |
| 6.2 | Clean real data: parse strings, convert types, handle missing values | E, HW | FP |
| 6.3 | Choose the figures that carry the argument, styled for an audience | E | FP |
| 6.4 | Write a 1–2 page report: question, data, method, findings, caveats | — | FP |
| 6.5 | Present the analysis in 1–2 slides / ~3 minutes | — | FP |

**Final project.** Staged across the semester (a checkpoint per part), ending in a written report, slides, and a replication folder (notebook + data). Graded on rubric: question, appropriate methods, correct interpretation, communication quality. Exemplars are published on the course site as anonymized replication sets.

---

## Assessment Map at a Glance

| Assessment | After | What it certifies the student can do |
| --- | --- | --- |
| **ME1** | Part 1 | Look at a raw table → name its structure, variables, and types → choose and draw the right picture |
| **ME2** | Part 2 | Prepare data (filter, log) and read/draw relationship figures; predict grouped-aggregation output |
| **ME3** | Part 3 | Reason about sampling distributions; build CIs; describe the null; visualize and interpret p-values |
| **ME4** | Part 4 | Write, sketch, and interpret bivariate models; read regression output; diagnose residual plots |
| **ME5** | Part 5 | Write and interpret models with controls and interactions; explain why controls belong |
| **Final project** | Part 6 | The full pipeline: question → data → model → interpretation → communication |

MiniExams are on paper, no computer. Code fluency (pandas, seaborn, statsmodels) is practiced in every exercise and homework and certified by the final project, not by the exams. The exams certify the *reasoning*: choosing tools, reading output, and interpreting results in plain English.

### Deliberately taught-but-not-assessed

These appear in class because they complete the toolkit or serve the project, and are intentionally left off exams: reshaping (melt/pivot), merging datasets, geographic mapping, bubble/size encoding, Anscombe's Quartet, CDF/PDF computation, MSE mechanics, time-series model comparison (levels vs. differences vs. growth rates), deseasonalization, R²/F-statistic model selection, and all code syntax.

---

*Maintained in *`ECON_0150/Course_Specs.md`*. Companion documents: *`course-content.yml`* (site structure), *`parts/Course_Outline.md`* on the site (student-facing outline), *`ME/ME_2/ME_2_Skillset.md`* (per-exam skill lists, ME2 pilot). Sources audited 2026-08-19: all 35 concept decks, 51 notes/homework files, and the F25/S26 MiniExams with rubrics.*
