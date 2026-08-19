# Homework 4.1–4.4 Revision Plan

Align homeworks with MiniExam 4 skills. Each homework should prepare students for the exam questions that correspond to that unit.

---

## HW 4.1 — Numerical Predictors

**Currently covers:** Fit regression (BMI ~ unemployment, MENTHLTH ~ unemployment), interpret β₁.

**Add:**
- Q: "What is the null hypothesis for β₁?"
- Q: "What does the p-value for β₁ tell us? Write a complete interpretation."
- Q: Give a pre-made regression output table (different dataset) and ask students to interpret β₀, β₁, and the p-value without running code.
- Q: "Sketch or describe what the sampling distribution of β₁ would look like under the null hypothesis. Where would our observed β₁ fall?"

**Rationale:** ME_4 Q1d (null hypothesis), Q3b (interpret β₁), Q4 (draw sampling distribution), Q5d (p-value interpretation).

---

## HW 4.2 — Categorical Predictors

**Currently covers:** Create binary variable, fit regression (MENTHLTH ~ under_10k), interpret results. Partially built (over_75k section is commented out).

**Fix:**
- Complete the over_75k question (currently just a commented-out line).
- Add explicit questions: "What does β₀ represent?" and "What does β₁ represent?"
- Q: Give a pre-made regression output table with a binary predictor. Ask students to interpret β₀, β₁, and the p-value.
- Q: "If group A has mean 3.2 and group B has mean 2.9, and we code group A as 1 and group B as 0, what would β₀ and β₁ equal?"

**Rationale:** ME_4 Q1a-c (write model, identify β₀ and β₁ from group means), Q5a-c (interpret output table with binary predictor), Q6 in Demo (β₀ and β₁ from group means).

---

## HW 4.3 — Model Assumptions

**Currently covers:** Scatterplot, log transformation, fit regression, interpret coefficients and p-value. This is essentially a 4.1-style homework — no diagnostics.

**Restructure to actually cover 4.3 material.** Keep the existing model-fitting as setup, then add diagnostics:

- Keep Q1 (final project groups) and the existing model-fitting questions (a–e) as Part 1.
- Add Part 2: Diagnostics
  - Q: "Extract the residuals and predicted values from your model."
  - Q: "Create a residual plot (predicted values on x-axis, residuals on y-axis). Does the model appear to violate the linearity assumption?"
  - Q: "Does the residual plot show signs of heteroskedasticity? Explain."
  - Q: "Create a histogram of the residuals. Do they appear roughly normal?"
  - Q: "Create a lagged residual plot. Does this model appear to violate the independence assumption?"
  - Q: "Re-fit the model using robust standard errors (`cov_type='HC3'`). How do the standard errors and p-values change?"
- Q: Give a pre-made residual plot showing clear heteroskedasticity. Ask students to identify the problem and name the assumption violated.

**Rationale:** ME_4 Q5e (sketch heteroskedasticity in a residual plot). This is the biggest gap — the exam tests diagnostics but no homework practices it.

---

## HW 4.4 — The Problem of Timeseries

**Currently:** Empty (just imports).

**Build from scratch using Okun's Law data** (already used in Exercise 4.4):

- Q1: Load `okun.csv`. Create a scatterplot of GDP vs unemployment. Fit a levels model: `gdp ~ unemployment`. Interpret β₁.
- Q2: Create a residual plot. Does the model look well-specified?
- Q3: Create a lagged residual plot. Does the model show autocorrelation?
- Q4: Create first-differenced variables (`gdp_diff`, `unemployment_diff`). Fit the differenced model: `gdp_diff ~ unemployment_diff`. Interpret β₁.
- Q5: Create a residual plot and lagged residual plot for the differenced model. Did differencing fix the autocorrelation?
- Q6: Interpret the difference between the levels and differenced results. Why does the levels model give a misleading positive coefficient?

**Rationale:** ME_4 doesn't test timeseries heavily, but the diagnostics skills (residual plots, lag plots) reinforce 4.3 material. Students also need this for the final project.

---

## Summary of Changes

| Homework | Current State | Work Needed |
|----------|--------------|-------------|
| HW 4.1 | Mostly complete | Add 3–4 conceptual questions (null hypothesis, p-value interpretation, sampling distribution, read output table) |
| HW 4.2 | Partially built | Complete the over_75k question, add β₀/β₁ interpretation questions, add output table reading |
| HW 4.3 | Wrong content (no diagnostics) | Add Part 2 with residual plot, heteroskedasticity check, histogram, lag plot, robust SE |
| HW 4.4 | Empty | Build from scratch using Okun's Law data |

## Exam Skill Coverage After Changes

| ME_4 Skill | Practiced In |
|------------|-------------|
| Write regression model | HW 4.1, 4.2, 4.3, 4.4 |
| Interpret β₀, β₁ | HW 4.1, 4.2, 4.3, 4.4 |
| State null hypothesis | HW 4.1 (new) |
| Interpret p-value | HW 4.1 (new), 4.3 |
| Sampling distribution concept | HW 4.1 (new) |
| Read regression output table | HW 4.1 (new), 4.2 (new) |
| Residual plot | HW 4.3 (new), 4.4 (new) |
| Identify heteroskedasticity | HW 4.3 (new) |
| Robust standard errors | HW 4.3 (new) |
| Differencing / autocorrelation | HW 4.4 (new) |
| Sketching models | Not directly practicable in notebooks — covered in exercises (in-class) |
