# ME4 Rubric | Spring 2026

**Total: 100 points**

---

## Q1. Numerical Predictor (Gini / Depression) — 20 pts

**Correct model:** depression_rate = β₀ + β₁ × gini + ε

### a) Write the model — 5 pts

**Spec:** Student places the correct outcome on the left, correct predictor on the right, with proper model structure.

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| depression_rate = β₀ + β₁ × gini + ε | 5 | Correct |
| y = β₀ + β₁ × x + ε | 3 | Structure correct, no context — knows the framework but didn't apply it |
| gini = β₀ + β₁ × depression_rate + ε | 3 | Flipped x and y — structure is right, conceptual error about which is outcome |
| depression_rate = β₀ + β₁ × gini (no ε) | 4 | Minor — the blank literally has a slot for ε |
| Anything else or blank | 0 | |

> **Edge case:** Some students write "depression" or "dep_rate" instead of "depression_rate." Accept any reasonable variable name that clearly refers to the right variable.

### b) Sketch the visualization — 5 pts

**Spec:** Student chooses scatterplot (correct for two numerical variables) with the predictor on x and outcome on y.

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| Scatter + regression line, gini on x, depression_rate on y, axes labeled | 5 | Correct |
| Scatter + line but missing axis labels | 4 | Right idea, minor omission |
| Scatter only (no regression line) | 3 | Shows the data but "visualization of this model" implies the fitted line |
| Scatter + line but axes flipped | 3 | Consistent with flipped model in (a) |
| Bar chart, box plot, histogram | 1 | Wrong chart type — doesn't recognize two numerical variables → scatter |
| Blank | 0 | |

### c) Interpret β₁ = 0.48 — 5 pts

**Spec:** Student demonstrates they understand β₁ as the predicted change in y per one-unit change in x, stated in context.

A complete interpretation must include:
1. **One-unit change in x**: mentions a one-point increase in the Gini coefficient
2. **Direction + magnitude of change in y**: depression rate increases by 0.48
3. **Context**: uses variable names or units (cases per 1,000)

| Answer | Pts | What's present |
|--------|-----|---------------|
| "A one-point increase in the Gini coefficient is associated with 0.48 more depression cases per 1,000 residents" | 5 | All three elements |
| "For each unit increase in gini, depression rate increases by 0.48" | 4 | Elements 1-2, weak context |
| "Higher inequality is associated with higher depression" | 2 | Direction only — no magnitude, no "per unit" |
| "A one-unit increase in depression rate increases gini by 0.48" | 1 | Backwards — x and y reversed |
| "48% of depression is explained by inequality" | 0 | Confuses β₁ with R² |
| Blank | 0 | |

> **Common edge cases:**
> - **Causal language** ("causes" instead of "associated with"): Do NOT deduct in this course. Students aren't expected to distinguish association from causation in Part 4.
> - **"For every 1% increase in inequality..."**: Accept — reasonable interpretation of the 0-100 Gini scale.
> - **Percentage interpretation** ("increases by 48%"): Deduct to 2 pts. Confuses 0.48 with a percentage.

### d) Null hypothesis — 5 pts

**Spec:** Student identifies β₁ = 0 as the default null.

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| β₁ = 0 or H₀: β₁ = 0 | 5 | Correct |
| "No relationship" or "gini has no effect" (in words only) | 3 | Correct idea, but question has a fill-in blank — symbolic expected |
| β₁ ≠ 0 | 1 | Wrote the alternative hypothesis |
| β₀ = 0 or β₁ = 0.48 or anything else | 0 | |

---

## Q2. Binary Predictor (Tutoring / Scores) — 20 pts

**Correct model:** scores = β₀ + β₁ × tutoring + ε
**Key rule:** β₀ = mean of group coded 0. β₁ = difference (group 1 minus group 0).

### a) Write the model — 5 pts

Same grading structure as Q1a.

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| scores = β₀ + β₁ × tutoring + ε | 5 | Correct |
| y = β₀ + β₁ × x + ε | 3 | Structure correct, no context |
| tutoring = β₀ + β₁ × scores + ε | 3 | Flipped |
| Blank or wrong structure | 0 | |

### b) β₀ = ? — 5 pts

**Spec:** Student knows β₀ is the mean of the group coded 0 (no tutoring = 72).

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| 72 | 5 | Correct — mean of the tutoring=0 group |
| 78 | 2 | Most common error. Student thinks β₀ is the tutoring group, or "the first number mentioned." Shows they know β₀ is a group mean, just the wrong one |
| 75 | 0 | Averaged the two means — doesn't understand binary model |
| 6 | 0 | Confused β₀ with β₁ |

> **Consistency note:** If a student answers 78 here AND -6 in part (c), they have a consistent (but wrong) mental model where they think the tutoring group is coded 0. Grade each part independently per the table, but note the consistency — it tells you the student understands the structure but confused the groups.

### c) β₁ = ? — 5 pts

**Spec:** Student knows β₁ is the difference between group means (group 1 minus group 0).

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| 6 | 5 | Correct (78 - 72) |
| -6 | 3 | Correct magnitude, wrong sign. Could be consistent with flipping groups in (b). Shows they understand β₁ is a difference |
| 78 or 72 | 0 | Confused β₁ with a group mean |
| 150 | 0 | Added means |

### d) Flipped coding: β₀ = ? — 5 pts

**Spec:** Student demonstrates that β₀ depends on which group is coded 0. When coding flips, β₀ changes to the other group's mean.

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| 78 | 5 | Correct — now the tutoring group is coded 0, so β₀ = their mean |
| 72 | 1 | Doesn't understand that flipping changes β₀. Likely memorized the answer from (b) |
| -6 or 6 | 0 | Confused β₀ with β₁ |

> **This is the most conceptually demanding sub-part.** A student who gets (b), (c), AND (d) correct has fully internalized how binary coding maps to coefficients. A student who gets (b) and (c) right but (d) wrong may have memorized the procedure without understanding.

---

## Q3. Reading Regression Output (PM2.5 / Admissions) — 30 pts

### a) Sketch the fitted model — 6 pts

**Spec:** Student reads the output, identifies this as a numerical predictor model, draws a scatter with regression line, and labels with fitted values.

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| Scatter + upward line + labels (β₀ = 35.2 at intercept, slope = 2.15 annotated) | 6 | Correct |
| Scatter + upward line + one label only | 5 | Minor omission |
| Scatter + upward line but no value labels | 4 | Right structure, didn't follow the "label using fitted values" instruction |
| Scatter + line but downward slope | 3 | Conceptual error — β₁ is positive (2.15) so slope goes up |
| Scatter only, no line | 3 | Didn't show the model, just the data |
| Axes flipped | 3 | PM2.5 should be on x (it's the predictor in the output) |
| Bar chart or other wrong type | 1 | |
| Blank | 0 | |

### b) Interpret intercept (35.20) — 8 pts

**Spec:** Student explains what β₀ means: the predicted value of y when x = 0.

A complete interpretation must include:
1. **When x = 0**: when PM2.5 concentration is zero
2. **Predicted y**: the expected/predicted admission rate
3. **Context**: uses variable names and/or units

| Answer | Pts | What's present |
|--------|-----|---------------|
| "When PM2.5 is 0, the predicted admission rate is 35.2 per 100,000" | 8 | All three |
| "When PM2.5 is 0, admissions are 35.2" | 7 | Elements 1-2, light on units |
| "The baseline admission rate is 35.2" | 5 | Element 2-3 but doesn't specify "when x = 0" |
| "When x = 0, y = 35.2" | 4 | Elements 1-2, no context |
| "The average admission rate is 35.2" | 3 | Confuses intercept with overall mean |
| "For each unit increase in PM2.5, admissions increase by 35.2" | 0 | Gave the slope interpretation — fundamentally wrong |
| Blank | 0 | |

> **Edge case:** A student who notes "a PM2.5 of 0 may not be realistic, so this is an extrapolation" deserves bonus recognition — this shows deeper understanding. Don't deduct for this caveat.

### c) Interpret slope (2.15) — 8 pts

**Spec:** Same structure as Q1c. Student explains what β₁ means: the predicted change in y per one-unit change in x.

| Answer | Pts | What's present |
|--------|-----|---------------|
| "Each one-unit increase in PM2.5 is associated with 2.15 more admissions per 100,000" | 8 | All elements |
| "For each unit increase in PM2.5, admissions increase by 2.15" | 7 | Missing units but otherwise correct |
| "As PM2.5 increases by 1, hospital admissions increase by 2.15" | 6 | Correct structure, light on context |
| "Higher PM2.5 leads to more admissions" | 3 | Direction only, no magnitude or "per unit" |
| Backwards (PM2.5 increases by 2.15 per admission) | 1 | x and y reversed |
| Blank | 0 | |

### d) P-value multiple choice — 8 pts

**Correct:** "If air quality has no effect on admissions, 0.1% of samples would have a coefficient this far from zero" (Option 1)

| Answer | Pts |
|--------|-----|
| Option 1 (correct) | 8 |
| Any other option | 0 |

> **Why each distractor is wrong** (for your reference when students ask):
> - Option 2 ("where air quality truly matters"): Assumes alternative is true. P-value is computed under the NULL.
> - Option 3 ("0.1% of the difference is due to chance"): Nonsensical — p-value isn't a proportion of the effect.
> - Option 4 ("99.9% probability true coeff is at least 2.15"): Classic inverse probability error — p-value ≠ P(H₀|data).
> - Option 5 ("0.1% margin of error"): Confuses p-value with margin of error.

---

## Q4. Sampling Distribution Drawing — 15 pts

**Spec:** Student can draw the null sampling distribution, locate their observed statistic, and identify the p-value as tail area(s).

### Checklist (3 pts each):

| Element | 3 pts | 1-2 pts | 0 pts |
|---------|-------|---------|-------|
| **1. Bell curve** | Symmetric, unimodal curve drawn | Recognizable but lopsided or very flat | No curve |
| **2. Centered at 0** | Curve clearly centered on 0 (the null) | Center unclear or unlabeled | Centered on 2.15 or other wrong value |
| **3. X-axis labeled** | Labeled as β₁, "slope," or "coefficient" | Has tick marks but no label | No axis information |
| **4. Observed value marked** | 2.15 marked with line/arrow on right side | A value marked but wrong (e.g., 0.620) | Nothing marked |
| **5. Tails shaded** | Both tails shaded beyond ±2.15 | One tail shaded (partial understanding of two-sided test) | Area between 0 and 2.15 shaded, or nothing shaded |

### Critical errors (cap the score):

- **Centered on 2.15 instead of 0**: Maximum 6 pts total regardless of other elements. This shows the student doesn't understand that the null distribution is centered at the null value. Everything else may be "right" relative to their wrong center, but the core concept is wrong.

- **Shades area between 0 and 2.15**: Maximum 8 pts. Student confuses the p-value region (tails) with the "distance from null" region.

- **Only one tail shaded**: No cap, but Element 5 gets 2 pts instead of 3. This is a minor conceptual gap (one-sided vs two-sided).

---

## Q5. Residual Plot Interpretation — 15 pts

### a) Which assumption is violated? — 8 pts

**Spec:** Student correctly identifies the fan-shaped pattern as a violation of homoskedasticity (constant variance).

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| "Homoskedasticity" or "constant variance" or "equal variance" | 8 | Correct — names the assumption |
| "Heteroskedasticity" | 8 | Also correct — names the violation (same concept) |
| "The variance is not constant" or "spread changes" | 6 | Describes the violation correctly but doesn't use the term |
| "Linearity" | 0 | Fan shape ≠ curvature. Linearity violations show U-shaped or curved residuals |
| "Normality" | 0 | Fan shape is about variance, not distributional shape |
| "Independence" | 0 | Independence violations show up in lag plots, not standard residual plots |

> **Why 8 pts:** This question is testing recognition of a specific visual pattern and its connection to a specific assumption. It's more discriminating than it looks — students frequently confuse the four assumptions. Getting this right means the student can read a residual plot.

### b) Name one approach to address this — 7 pts

**Spec:** Student names a valid remediation for heteroskedasticity.

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| "Use robust standard errors" or "HC3" or "heteroskedasticity-consistent SEs" | 7 | Correct — directly addresses the problem |
| "Log transform the dependent variable" or "take the log of y" | 7 | Correct — stabilizes variance |
| "Weighted least squares" or "WLS" | 7 | Correct — weights observations by inverse variance |
| "Transform the data" (no specifics) | 4 | Right direction but vague — which transformation? |
| "Remove outliers" | 2 | Fan shape is systematic, not driven by outliers. But shows awareness something is wrong |
| "Collect more data" | 0 | Doesn't fix a structural problem |
| "Add more variables" | 2 | Might help indirectly but doesn't directly address heteroskedasticity |
| Blank | 0 | |

---

## Summary: Point Distribution

| Question | Topic | Pts | Sub-parts |
|----------|-------|-----|-----------|
| Q1 | Numerical predictor | 20 | 5 + 5 + 5 + 5 |
| Q2 | Binary predictor | 20 | 5 + 5 + 5 + 5 |
| Q3 | Regression output | 30 | 6 + 8 + 8 + 8 |
| Q4 | Sampling distribution | 15 | Checklist (5 × 3) |
| Q5 | Residual plot | 15 | 8 + 7 |
| **Total** | | **100** | |

---

## Proposed Exam Edits

1. **Q1 stem typo**: "normalized to a between 0-100" → "normalized to between 0-100"
2. **Q3c spacing**: "coefficient(2.15)" → "coefficient (2.15)"
3. **Consider adding Q5c**: "Does this violation affect the estimated coefficients (β₀ and β₁), or does it affect the standard errors and p-values?" — this was tested on HW 4.3 and is a high-value conceptual question. Would make Q5 a stronger question. (Optional — only if you want Q5 to carry more weight.)
