## ME5 | Spec-Based Rubric | Fall 2026 (Draft)

This is a draft spec-based rubric for ME5. Each question maps to a skill. Each skill has required elements. All elements present = pass. Missing any = not yet.

**Exam-level pass:** 4 of 5 specs pass.

---

##### Spec 1: Select the correct model for a research question

**Tested by:** Q1a

**Pass criteria:**
- Student circles the model that matches the research question
- For "holding constant" or "controlling for" language: model must include both the main predictor and the control as separate terms (no interaction)
- For "differs by" or "allowing the effect to vary" language: model must include the interaction term

**Not yet:** Wrong model selected.

> No partial credit. This is a recognition task.

---

##### Spec 2: Interpret a coefficient with "holding constant" language

**Tested by:** Q1b, Q2b, Q3c

**Pass criteria (all three required):**
1. States the one-unit (or group) change in x
2. States the direction and magnitude of the change in y
3. Uses "holding constant," "comparing two [units] with equal [control]," or equivalent

**Not yet if missing any of:**
- No mention of the change in x (just says "related to" or "associated with")
- No magnitude (just direction)
- No "holding constant" language (a correct Part 4 interpretation is not yet for this spec)

**Assessed across multiple questions.** Student must demonstrate this skill at least twice (e.g., Q1b + Q3c, or Q1b + Q2b). A single instance could be lucky phrasing. Two confirms understanding.

> This is the core Part 5 skill. The "holding constant" element is the bright line between pass and not yet.

---

##### Spec 3: Write a multiple regression model

**Tested by:** Q2a

**Pass criteria (all three required):**
1. Correct outcome variable on the left
2. Both predictors on the right with separate coefficients
3. Error term present

**Not yet if:**
- Outcome and predictor are flipped
- Missing one predictor
- Includes an interaction term when the question says "controlling for"

> Accept any reasonable variable names. Accept β or b notation.

---

##### Spec 4: Make predictions from regression output

**Tested by:** Q3a, Q3b

**Pass criteria:**
- Correct setup: plugs in the right values for all terms (intercept + numerical predictor + binary predictor)
- Correct answer (or correct setup with minor arithmetic error)

**Not yet if:**
- Missing a term (e.g., forgets the binary predictor)
- Fundamentally wrong setup

**Must pass both sub-parts.** Getting one prediction right but not the other suggests the student doesn't reliably understand how to use the model.

> Common mistake to watch for: mileage in thousands. A student who plugs in 60,000 instead of 60 has a units error, not a conceptual error. This is not yet for the spec, but note it as a minor issue rather than a fundamental misunderstanding.

---

##### Spec 5: Compute and interpret interaction effects

**Tested by:** Q4a, Q4b, Q4c

**Pass criteria (all three required):**
1. Correctly identifies the effect for the reference group (β₁ alone)
2. Correctly computes the effect for the other group (β₁ + β₃)
3. Correctly identifies what the interaction coefficient means (the difference in effects between groups)

**Not yet if any of:**
- Gives the same effect for both groups (ignores interaction)
- Gives β₃ as the full effect for the interacted group (instead of β₁ + β₃)
- Picks the wrong MC answer

> Parts (a) and (b) are the computation. Part (c) is the interpretation. A student who computes correctly but picks the wrong MC answer may have gotten lucky on the computation. All three must be consistent to pass.

---

##### Spec 6 (optional/advanced): Explain why a control variable is needed

**Tested by:** Q2c

**Pass criteria:**
- Student identifies that the control variable is related to both the predictor and the outcome
- Explains how this could bias the estimate without the control

**Not yet if:**
- Just says "to be more accurate" or "to get a better model"
- Doesn't connect the control to both variables

> This could be a separate spec or folded into Spec 3 as an advanced tier. If using a two-tier system (standard/advanced), this is the advanced component.

---

## Summary

| Spec | Skill | Tested by |
|------|-------|-----------|
| 1 | Select the correct model | Q1a |
| 2 | Interpret with "holding constant" | Q1b, Q2b, Q3c |
| 3 | Write a multiple regression model | Q2a |
| 4 | Make predictions from output | Q3a, Q3b |
| 5 | Compute and interpret interactions | Q4a, Q4b, Q4c |
| 6 | Explain why controls are needed (advanced) | Q2c |

**Standard pass:** Specs 1-5 pass (4 of 5 required).

**Advanced pass:** Standard pass + Spec 6 passes.

---

## Migration Notes

Things to decide before F26:
- **Reattempt policy:** If a student doesn't pass, what's the reattempt process? (Ties into the 2-of-3 gate and TA makeup policy from earlier this semester.)
- **Spec 2 threshold:** Requiring "holding constant" twice is stricter than the current rubric. Is that the right bar?
- **Spec 4 units error:** Is a units error (60,000 vs 60) a not-yet or a pass-with-note? Current draft says not yet, but it's a judgment call.
- **MC-only specs:** Spec 1 is a single MC question. One lucky guess = pass. Consider adding a second model selection question or requiring a brief justification.
- **Weighting:** In a pure spec system, all specs are equal. But Spec 2 (interpret with holding constant) is arguably the most important Part 5 skill. Should it carry more weight, or is the "must demonstrate twice" requirement sufficient?
