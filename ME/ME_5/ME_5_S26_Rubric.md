## ME5 | Rubric | Spring 2026

**Total: 100 points**

---

##### ACC — 20 pts

---

##### Q1. Model Selection with Controls — 20 pts

**Spec:** Pick the right model and interpret the coefficient with "holding constant."

##### a) Which regression model? — 9 pts

**Correct:** C) `employment = β₀ + β₁·min_wage + β₂·cost_of_living + ε`

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| C | 9 | Correct |
| A | 3 | Simple regression. Knows min_wage is the predictor but ignores the control |
| D | 5 | Interaction model. Has both variables but misreads "holding constant" as "differs by" |
| B | 0 | Wrong predictor entirely |

##### b) Interpret the coefficient on `min_wage` — 11 pts

**Spec:** One-unit change, in context, with "holding constant."

**Correct:** The change in employment associated with each additional unit of minimum wage, comparing two states with equal cost of living.

| Element | Pts |
|---------|-----|
| Mentions "change in employment" (direction + magnitude of change in y) | 3 |
| Mentions "each additional unit of minimum wage" (one-unit change in x) | 3 |
| Mentions "comparing states with equal cost of living" (holding constant) | 3 |
| Anything written (baseline) | 2 |

> **Bright line:** The "holding constant" element is what separates Part 5 from Part 4. A student who writes a correct Part 4 interpretation (no "holding constant") gets 8/11. The 3-point gap tests whether they understand what multiple regression does.

---

##### Q2. Binary Predictor with Control — 20 pts

**Spec:** Write the model, interpret the binary coefficient with "holding constant," and explain why we need the control.

**Correct model:** `uninsured_rate = β₀ + β₁·expansion + β₂·poverty_rate + ε`

##### a) Write the regression model — 8 pts

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| uninsured_rate = β₀ + β₁·expansion + β₂·poverty_rate + ε | 8 | Correct |
| y = β₀ + β₁·x₁ + β₂·x₂ + ε | 5 | Structure correct, no context |
| Flipped outcome | 4 | Right structure, wrong variable on the left |
| Missing one predictor | 4 | Partial model |
| Missing error term but otherwise correct | 7 | Minor omission |
| Includes interaction (expansion × poverty_rate) | 5 | Overcomplicated |
| Blank | 0 | |

##### b) Interpret the coefficient on `expansion` — 6 pts

**Spec:** β₁ is the difference between expansion and non-expansion counties, holding poverty constant.

**Correct:** The difference in average uninsured rate between expansion and non-expansion counties, comparing two counties with equal poverty rates.

| Element | Pts |
|---------|-----|
| Mentions "difference in average uninsured rate" | 2 |
| Mentions "expansion and non-expansion counties" | 2 |
| Mentions "comparing counties with equal poverty rate" (holding constant) | 2 |

##### c) Why control for poverty rate? — 6 pts

**Spec:** Poverty is correlated with both expansion and uninsured rate, so it confounds.

**Correct:** Poorer counties may have higher uninsured rates AND be less likely to adopt expansion (or vice versa).

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| Identifies that poverty is related to both variables | 6 | Correct |
| Something generally in the right direction | 3 | Partial |
| Blank | 0 | |

---

##### Q3. Reading Regression Output (Used Cars / Mileage + Accident) — 20 pts

**Spec:** Make predictions from the output and interpret the binary coefficient.

> **Grader note:** Mileage is in thousands of miles, so 60,000 miles = 60. Many students will plug in 60,000 and get a huge negative number. Units error, not conceptual. See partial credit below.

##### a) Predicted price: 60k miles, no accident — 6 pts

**Correct:** PRICE = 22000 + (-120) × 60 + (-3200) × 0 = 22000 - 7200 = $14,800

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| $14,800 with work shown | 6 | Correct |
| $14,800 without work | 5 | Correct but no verification |
| Arithmetic error but correct setup (all terms present) | 4 | Right method, execution error |
| Uses 60,000 instead of 60 (wrong units) | 3 | Correct setup, didn't read "thousands of miles" |
| Missing a term | 2 | |
| Blank | 0 | |

##### b) Predicted price: 60k miles, with accident — 6 pts

**Correct:** PRICE = 22000 + (-120)(60) + (-3200)(1) = 22000 - 7200 - 3200 = $11,600. Or equivalently: 14,800 - 3,200 = $11,600 (building on part a).

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| $11,600 with correct setup | 6 | Correct |
| Correct setup but with math error | 5 | |
| Incorrect setup | 3 | |
| Blank | 0 | |

##### c) Interpret coefficient on `accident` (-3200) — 8 pts

**Spec:** -3200 is the price difference between accident and no-accident cars, holding mileage constant.

**Correct:** The extra average cost of a car with an accident history (compared to one without), holding mileage constant.

| Element | Pts |
|---------|-----|
| Mentions "extra (average) cost" or "lower price" (direction) | 3 |
| Mentions "accident history" (context) | 3 |
| Anything written (baseline) | 2 |

---

##### Q4. Interaction Model (Study Hours × Tutoring / Exam Scores) — 20 pts

**Spec:** Compute the effect for each group and interpret the interaction coefficient.

**Coefficients:** β₀ = 65, β₁ = 2.5, β₂ = 4, β₃ = 1.5

##### a) Effect for non-tutored students — 6 pts

**Correct:** β₁ = 2.5

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| β₁ or 2.5 | 6 | Correct |
| Incorrect | 2 | |
| Blank | 0 | |

##### b) Effect for tutored students — 6 pts

**Correct:** β₁ + β₃ = 2.5 + 1.5 = 4.0

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| β₁ + β₃ or 4.0 | 6 | Correct |
| β₃ or 1.5 (interaction only) | 3 | Thinks interaction IS the full effect |
| Anything else | 2 | |
| Blank | 0 | |

##### c) Interaction coefficient MC (circle one) — 8 pts

**Correct:** B) An additional hour of studying increases exam scores by 1.5 more for tutored students than non-tutored students

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| B | 8 | Correct |
| A | 3 | Confuses interaction (β₃) with fixed effect (β₂) |
| C | 2 | Reads 1.5 as a multiplier, not an additive difference |
| D | 2 | Confuses interaction with full effect for the tutored group |

