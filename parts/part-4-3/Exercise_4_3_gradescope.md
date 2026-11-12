# Exercise 4.3 | Gradescope

This is an instructor-facing document to make it easy to enter questions into Gradescope. This sheet is the selection form students submit on Gradescope after completing their work in a notebook, taken from the Exercise notebook. 

- Each `## QN` is a parent question. Put its title in the title field and paste its block into the Description box. A parent question can only hold description text; students answer the sub-questions.

- Each `### QN.M` under it is a sub-question. Put its title in the sub-question’s title field and paste its block into the **Problem** box.

- Ignore points. Each sub-question is worth 1 point by default on Gradescope.

Gradescope parses the code directly. Every input field must sit on its own line with no text before or after it, and a question can hold several fields:

- Text is Markdown, and LaTeX goes between `$$`. Images can be inserted with **Insert Image** or as a Markdown link `![alt](url)` to a file on the course site.
- Multiple choice: consecutive `( )` lines become a multiple-choice field, with `(x)` marking the correct answer. A blank line between choices starts a new group.
- Select all: consecutive `[ ]` lines become a select-all field, with `[x]` marking each correct answer. Students must mark every correct answer to get the point.
- Short answer: `[____](answer)` gives a one-line text box, autograded against the answer in parentheses. For numbers, `[____](=2+-0)` accepts any equivalent of 2 and `[____](=2+-0.2)` accepts anything from 1.8 to 2.2. Leave the parentheses empty to grade by hand.
- Free response: `|____|` gives a multi-paragraph text box. Any question with one is graded by hand.
- File uploads: `|files|` lets students upload any file type (a PNG of a figure, a notebook, a PDF). Uploads can be viewed and graded but not annotated.

## Q1: `Assumption 1: Linearity`

```
Complete Questions 1–3 in the Exercise 4.3 notebook. The data are 2024 observations, one per country, with life evaluation on a 0–10 scale and GDP per capita. Fit the model in dollars (Life_Evaluation ~ GDP_Per_Cap) and the log model (Life_Evaluation ~ log_GDP_PerCap), and make a residual plot for each.
```

### Q1.1: `What does the residual plot for the model in dollars show?`

```
(x) A clear pattern: most countries are bunched at low predictions, and the residuals rise and then fall as the prediction grows
( ) Random scatter around zero with an even spread
( ) Every residual is positive
( ) Only two predictions, one for each group
```

### Q1.2: `Which assumption does the model in dollars violate most clearly?`

```
(x) Linearity: a straight line in dollars does not describe the relationship
( ) Independence: the countries are listed in alphabetical order
( ) Normality: the outcome is measured on a 0–10 scale
( ) None: the slope's p-value is below 0.05, so the model is valid
```

### Q1.3: `Did the log transformation fix the pattern?`

```
(x) Yes: the residuals from the log model scatter around zero with no curve
( ) No: the residual plot looks the same
( ) No: the curve is now stronger
( ) It cannot be checked, because the log model has a different predictor
```

### Q1.4: `What is the mean of the residuals from the log model?`

```
Round to three decimal places.
[____](=0+-0.001)
```

### Q1.5: `Which country has the most negative residual in the log model, and what does that mean?`

```
(x) Afghanistan: its life evaluation is about 2.5 points lower than the model predicts for its GDP per capita
( ) Afghanistan: its GDP per capita is about 2.5 log points lower than the model predicts
( ) Nicaragua: its life evaluation is about 1.5 points lower than the model predicts
( ) Finland: it has the highest life evaluation in the data
```

## Q2: `Assumption 2: Homoskedasticity`

```
Complete Questions 4–5 in the notebook, using the log model. Round numerical answers to three decimal places.
```

### Q2.1: `What is the standard deviation of the residuals for countries with below-median predictions?`

```
[____](=0.826+-0.002)
```

### Q2.2: `What is the standard deviation of the residuals for countries with above-median predictions?`

```
[____](=0.527+-0.002)
```

### Q2.3: `What does this say about the spread of the residuals?`

```
(x) The spread is larger among countries with low predicted life evaluation, so the residuals are somewhat heteroskedastic
( ) The spread is the same everywhere, so the residuals are homoskedastic
( ) The spread is larger among countries with high predicted life evaluation
( ) The spread cannot differ, because the residuals have mean zero
```

### Q2.4: `What is the robust (HC3) standard error on the slope?`

```
[____](=0.091+-0.001)
```

### Q2.5: `What changes when the log model is refit with robust standard errors?`

```
(x) The coefficients are identical; the slope's standard error moves slightly, from 0.093 to 0.091, and the slope is still clearly different from zero
( ) The slope changes from 1.515 to 0.091
( ) The slope is no longer statistically significant
( ) Nothing at all changes, including the standard errors
```

## Q3: `Assumptions 3 and 4: Independence and Normality`

```
Complete Questions 6–7 in the notebook, using the log model.
```

### Q3.1: `What does the lagged residual plot show?`

```
(x) No pattern: a country's residual tells us nothing about the residual of the next country in the alphabet
( ) A strong upward diagonal: neighboring rows have similar residuals
( ) A strong downward diagonal: neighboring rows have opposite residuals
( ) A U shape
```

### Q3.2: `Why would we expect a pattern if the rows were the same country in consecutive years?`

```
(x) A country that is above the line one year tends to be above it the next year too, so neighboring residuals would be similar
( ) Because there would be more rows
( ) Because GDP per capita is measured in dollars
( ) We would not: observations are always independent
```

### Q3.3: `What does the histogram of residuals show?`

```
(x) Roughly bell-shaped and centered at zero, with a longer left tail from a few countries far below the line
( ) Perfectly symmetric
( ) Flat: every residual value is equally common
( ) Two separate peaks
```

### Q3.4: `With 146 countries, how much should a modest departure from normality worry us?`

```
(x) Not much: by the Central Limit Theorem the sampling distribution of the slope is still approximately normal in a sample this large
( ) A lot: the coefficients are biased whenever the residuals are not exactly normal
( ) A lot: the model cannot be estimated
( ) Not at all, at any sample size
```

## Q4: `A Binary Predictor`

```
Complete Question 8 in the notebook, using the income and mental health model from Exercise 4.2 (MENTHLTH ~ low_income). Round numerical answers to three decimal places.
```

### Q4.1: `What is the standard deviation of the residuals for households at $35,000 or more (low_income = 0)?`

```
[____](=6.179+-0.002)
```

### Q4.2: `What is the standard deviation of the residuals for households below $35,000 (low_income = 1)?`

```
[____](=9.327+-0.002)
```

### Q4.3: `Which assumption does this model violate?`

```
(x) Homoskedasticity: the residuals are much more spread out in the lower-income group
( ) Linearity: a binary predictor cannot be fit with a line
( ) Independence: there are only two predictions
( ) None of them
```

### Q4.4: `What is the robust (HC3) standard error on low_income?`

```
[____](=0.037+-0.001)
```

### Q4.5: `Does the conclusion change with robust standard errors?`

```
(x) No: the standard error rises slightly, from 0.034 to 0.037, and the difference between the groups is still far from zero
( ) Yes: the difference between the groups is no longer statistically significant
( ) Yes: the estimated difference between the groups changes
( ) No: robust standard errors are always identical to the usual ones
```

## Answer check

Verified by running the notebook's code with the solutions against `data/Life_Evaluation_GDP_PerCap.csv` (2024 rows, 146 countries after dropping the one missing GDP per capita) and `data/BRFSS_cleaned.csv` (206,739 complete responses):

- Model in dollars: intercept 5.0195, slope 3.317 × 10⁻⁵, R² 0.408. Two thirds of countries have a prediction below 5.5. Mean residual by third of the predictions: −0.587, 0.385, 0.210, and the richest countries fall well below the line. The most negative residual is Afghanistan at −3.674.
- Log model: intercept −0.2502, slope 1.5145 (standard error 0.0933), R² 0.646. Mean residual by third of the predictions: −0.042, 0.087, −0.043. Residual mean is 0 to 15 decimal places. Most negative residual: Afghanistan, −2.535; most positive: Nicaragua, 1.480.
- Residual standard deviation: 0.8261 for the 73 countries with below-median predictions, 0.5268 for the 73 above.
- HC3 standard errors: intercept 0.3806, slope 0.0915 (z = 16.560). The usual slope standard error is 0.0933.
- Lagged residuals: correlation −0.010 (p = 0.90).
- Residual skewness −0.656; 95.2% of residuals are within two standard deviations of zero.
- BRFSS model: intercept 2.4279, slope 2.6593. Residual standard deviation 6.1791 for the 127,450 respondents at $35,000 or more and 9.3270 for the 79,289 below. Standard error on low_income: 0.0341 usual, 0.0374 with HC3 (z = 71.154).

Q1.4 accepts 0 and tiny floating-point values such as 1.7e-15. Robust standard errors moved the slope's standard error down slightly in the happiness model and up slightly in the BRFSS model; neither conclusion changes.
