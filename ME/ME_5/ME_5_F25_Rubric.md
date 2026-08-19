## ME5 | Rubric | Fall 2025

**Total: 100 points**

---

##### ACC — 20 pts

---

##### Q1. Model Selection with Controls (Study Hours / Scores / GPA) — 20 pts

**Spec:** Student selects the correct model for a "controlling for" question and interprets the main coefficient with "holding constant" language.

##### a) Which regression model? — 9 pts

**Correct:** C) `score = β₀ + β₁·hours + β₂·GPA + ε`

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| C | 9 | Correct |
| A | 3 | Simple regression. Knows hours is the predictor but ignores the control |
| D | 5 | Interaction model. Recognizes both variables but misreads "controlling for" as "allowing the effect to differ" |
| B | 0 | Wrong predictor entirely |

##### b) Interpret the coefficient on `hours` — 11 pts

**Spec:** Student states the one-unit change interpretation with "holding constant" language in context.

**Correct:** The additional score associated with each additional hour of study, comparing two students with equal GPA.

| Element | Pts |
|---------|-----|
| Mentions "additional score" (direction + magnitude of change in y) | 3 |
| Mentions "each additional hour of study" (one-unit change in x) | 3 |
| Mentions "comparing two students with equal GPA" (holding constant) | 3 |
| Anything written (baseline) | 2 |

---

##### Q2. Binary Predictor with Control (Remote Work / Productivity / Experience) — 20 pts

**Spec:** Student writes a correct multiple regression model with a binary predictor and a control, interprets the binary coefficient with "holding constant" language, and explains why the control is needed.

**Correct model:** `productivity = β₀ + β₁·remote + β₂·experience + ε`

##### a) Write the regression model — 8 pts

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| productivity = β₀ + β₁·remote + β₂·experience + ε | 8 | Correct |
| y = β₀ + β₁·x₁ + β₂·x₂ + ε | 5 | Structure correct, no context |
| Flipped outcome | 4 | Structure right, conceptual error about which is outcome |
| Missing one predictor | 4 | Partial model |
| Missing error term but otherwise correct | 7 | Minor omission |
| Includes interaction (remote × experience) | 5 | Overcomplicated |
| Blank | 0 | |

##### b) Interpret the coefficient on `remote` — 6 pts

**Spec:** Student interprets β₁ as the difference in average productivity between remote and in-office workers, holding experience constant.

**Correct:** The difference in average productivity between remote and in-office workers, comparing two workers with equal experience.

| Element | Pts |
|---------|-----|
| Mentions "difference in average productivity" | 2 |
| Mentions "remote and in-office workers" | 2 |
| Mentions "comparing two workers with equal experience" (holding constant) | 2 |

##### c) Why control for experience? — 6 pts

**Spec:** Student identifies that experience is correlated with both remote work and productivity (confounding).

**Correct:** Those with more experience may be more productive AND more likely to want to work from the office.

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| Identifies that experience is related to both remote status and productivity | 6 | Correct |
| Something generally in the right direction | 3 | Partial |
| Blank | 0 | |

---

##### Q3. Reading Regression Output (Apartments / Sqft + Pets) — 20 pts

**Spec:** Student makes predictions from a multiple regression output with a numerical and binary predictor, and interprets the binary coefficient.

##### a) Predicted rent: 900 sqft, no pets — 6 pts

**Correct:** RENT = 250 + 0.8 × 900 = $970 per month

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| $970 with work shown | 6 | Correct |
| $970 without work | 5 | Correct but no verification |
| Arithmetic error but correct setup (all terms present) | 4 | Right method, execution error |
| Missing a term | 2 | |
| Blank | 0 | |

##### b) Predicted rent: 900 sqft, allows pets — 6 pts

**Correct:** RENT = 970 + 150 = $1,120 per month

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| $1,120 with correct setup | 6 | Correct |
| Correct setup but with math error | 5 | |
| Incorrect setup | 3 | |
| Blank | 0 | |

##### c) Interpret coefficient on `pets_allowed` (150) — 8 pts

**Spec:** Student interprets 150 as the difference in average rent between pet-friendly and non-pet-friendly apartments, holding sqft constant.

**Correct:** The extra average cost for an apartment that allows pets.

| Element | Pts |
|---------|-----|
| Mentions "extra (average) cost" | 3 |
| Mentions "allows pets" | 3 |
| Anything written (baseline) | 2 |

---

##### Q4. Interaction Model (Training × Degree / Performance) — 20 pts

**Spec:** Student computes group-specific effects from an interaction model and correctly identifies the meaning of the interaction coefficient.

**Coefficients:** β₀ = 50, β₁ = 2.0, β₂ = 10, β₃ = 0.8

##### a) Effect for employees without a degree — 6 pts

**Correct:** β₁ = 2

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| β₁ or 2 | 6 | Correct |
| Incorrect | 2 | |
| Blank | 0 | |

##### b) Effect for employees with a degree — 6 pts

**Correct:** β₁ + β₃ = 2 + 0.8 = 2.8

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| β₁ + β₃ or 2.8 | 6 | Correct |
| β₃ or 0.8 (interaction only) | 3 | Thinks interaction IS the full effect |
| Anything else | 2 | |
| Blank | 0 | |

##### c) Interaction coefficient MC (circle one) — 8 pts

**Correct:** B) An additional hour of training increases performance by 0.8 more for employees with degrees than those without

| Answer | Pts | Reasoning |
|--------|-----|-----------|
| B | 8 | Correct |
| A | 3 | Confuses interaction (β₃) with fixed effect (β₂) |
| C | 2 | Multiplicative misinterpretation |
| D | 0 | Confuses interaction with total effect |

---

## Summary: Point Distribution

| Section | Topic | Pts |
|---------|-------|-----|
| ACC | Academic conduct code | 20 |
| Q1 | Model selection + holding constant | 20 |
| Q2 | Binary predictor with control | 20 |
| Q3 | Reading regression output | 20 |
| Q4 | Interaction model | 20 |
| **Total** | | **100** |
