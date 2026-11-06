# Exercise 4.1 | Gradescope

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

## Q1: `Explore the Data`

```
Complete Question 1 in the Exercise 4.1 notebook. The data are 2024 observations, one per country, with life evaluation on a 0–10 scale and log10 GDP per capita.
```

### Q1.1: `What relationship does the scatter plot show?`

```
(x) Positive: countries with higher log GDP per capita tend to report higher life evaluation
( ) Negative: countries with higher log GDP per capita tend to report lower life evaluation
( ) No visible relationship
( ) A U shape: life evaluation is highest at the lowest and highest incomes
```

## Q2: `Fitting the Model`

```
Complete Questions 2–4 in the notebook. Fit the bivariate GLM Life_Evaluation ~ log_GDP_PerCap using statsmodels and inspect its coefficient table. Round numerical answers to three decimal places.
```

### Q2.1: `What is the estimated intercept?`

```
[____](=-0.250+-0.001)
```

### Q2.2: `What is the estimated slope?`

```
[____](=1.515+-0.001)
```

### Q2.3: `Is the slope positive or negative?`

```
(x) Positive
( ) Negative
( ) Zero
```

### Q2.4: `What is the p-value on the slope?`

```
(x) Less than 0.001 (the table shows 0.000)
( ) About 0.05
( ) About 0.49
( ) About 16.2
```

### Q2.5: `What null hypothesis does the slope p-value test?`

```
(x) The population slope is zero: log GDP per capita has no linear relationship with life evaluation
( ) The sample slope is zero
( ) The intercept is zero: a country with log GDP per capita of 0 has life evaluation 0
( ) Every wealthier country is happier than every poorer country
```

## Q3: `Predictions`

```
Complete Questions 5–6 in the notebook. Use the estimated intercept and slope to predict life evaluation. Round numerical answers to three decimal places.
```

### Q3.1: `What is the predicted life evaluation when log10 GDP per capita is 3 (GDP per capita of $1,000)?`

```
[____](=4.293+-0.002)
```

### Q3.2: `What is the predicted life evaluation when log10 GDP per capita is 4 (GDP per capita of $10,000)?`

```
[____](=5.808+-0.002)
```

### Q3.3: `How much higher is the second prediction than the first?`

```
[____](=1.515+-0.002)
```

### Q3.4: `How does that difference compare with the slope?`

```
(x) It equals the slope: moving x up by one unit moves the prediction by the slope
( ) It equals the intercept
( ) It is ten times the slope, because GDP per capita is ten times larger
( ) It is unrelated to the slope
```

## Q4: `Interpretation`

```
Complete Questions 7–8 in the notebook.
```

### Q4.1: `Which sentence correctly interprets the slope?`

```
(x) For every one-unit increase in log10 GDP per capita, predicted life evaluation increases by about 1.51 points
( ) For every $1 increase in GDP per capita, predicted life evaluation increases by about 1.51 points
( ) For every one-point increase in life evaluation, log10 GDP per capita increases by about 1.51
( ) Wealthier countries are about 1.51 times happier than poorer countries
```

### Q4.2: `What does a one-unit increase in log10 GDP per capita mean for actual GDP per capita?`

```
(x) GDP per capita is multiplied by 10
( ) GDP per capita increases by $1
( ) GDP per capita increases by $10
( ) GDP per capita increases by 10%
```

## Answer check

Verified by running the notebook's code with the solutions against `data/Life_Evaluation_GDP_PerCap.csv`, 2024 rows only:

- 147 countries in 2024; one is missing GDP per capita, so the fit uses 146 observations.
- Intercept: −0.2501630; standard error 0.3639646; t = −0.687; p = 0.493.
- Slope: 1.5145335; standard error 0.0933445; t = 16.225 with 144 degrees of freedom; two-sided p ≈ 2.55 × 10⁻³⁴. The table rounds it to 0.000; it is not exactly zero.
- Predictions: 4.2934374 at x = 3 and 5.8079709 at x = 4; the difference is the slope, 1.5145335.
- Correlation 0.804; R² 0.646. Log10 GDP per capita ranges from 2.65 to 5.08, so x = 3 and x = 4 are both inside the data.

The prediction tolerances are ±0.002 so that students who plug in the table's four-decimal coefficients (−0.2502 and 1.5145, giving 4.2933 and 5.8078) are also marked correct. The slope describes an association in observational country-level data, not a causal effect of income on happiness.
