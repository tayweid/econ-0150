# Homework 4.4 | Gradescope

This is an instructor-facing document to make it easy to enter questions into Gradescope. This sheet is the selection form students submit on Gradescope after completing their work in a notebook, taken from the Homework file. 

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

## Q1: `Okun's Law: Levels Model`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and fitting each model, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

Okun's Law is a well-known empirical relationship in macroeconomics: when unemployment rises, GDP tends to grow more slowly, and vice versa. The Homework 4.4 Notebook loads okun.csv, quarterly US data from 1948–2019, with gdp (real GDP, billions of 2017 dollars), unemployment (unemployment rate, %), gdp_diff, unemployment_diff, and gdp_growth (quarter-over-quarter GDP growth in percent, so 1.5 means 1.5%).
```

### Q1.1: `Create a scatterplot with unemployment on the x-axis and gdp on the y-axis.`

```
Upload your figure.
|files|
```

### Q1.2: `Fit a linear regression model: gdp ~ unemployment. Report the estimated coefficients and p-values. Interpret the slope: what does the sign suggest about the relationship between unemployment and GDP?`

```
Intercept (two decimal places)
[____](=6707.74+-0.01)

Slope (two decimal places)
[____](=479.65+-0.01)

p-value on the intercept (three decimal places)
[____](=0+-0.001)

p-value on the slope (three decimal places)
[____](=0.016+-0.001)

What does the sign of the slope suggest?
(x) Positive: higher unemployment goes with higher GDP, the opposite of Okun's Law
( ) Negative: higher unemployment goes with lower GDP, as Okun's Law predicts
( ) Zero: unemployment and GDP are unrelated
```

### Q1.3: `Create a residual plot (predicted values on x-axis, residuals on y-axis). Does the model look well-specified?`

```
Upload your figure.
|files|

(x) No: the residuals fall in bands with clear structure, not random scatter around zero
( ) Yes: the residuals scatter randomly around zero
( ) Yes: every residual is close to zero
```

### Q1.4: `Create a lagged residual plot. Does the model show autocorrelation? What does this mean for the reliability of the regression results?`

```
Upload your figure.
|files|

(x) Yes, very strong: each residual is nearly identical to the one before it, so the standard errors and p-values cannot be trusted
( ) Yes, but weak: the results are still reliable
( ) No: the residuals are independent, so the results are reliable
```

## Q2: `Okun's Law: GDP Growth and Unemployment Changes`

```
The levels model in Q1 regresses the level of GDP on the level of unemployment. But GDP trends upward over time while unemployment fluctuates around a stable mean, and that trend can create a spurious relationship. Okun's Law is typically stated in terms of GDP growth and changes in unemployment: when unemployment rises, GDP growth slows. Use the gdp_growth and unemployment_diff columns provided in the dataset.
```

### Q2.1: `Create a scatterplot with unemployment_diff on the x-axis and gdp_growth on the y-axis. How does this scatterplot compare to the one in Q1(a)?`

```
Upload your figure.
|files|

(x) It is a single cloud with a clear downward slope, where Q1(a) showed stacked bands with no clear overall relationship
( ) It looks the same as Q1(a)
( ) It shows a clear upward slope, where Q1(a) sloped downward
```

### Q2.2: `Fit the Okun's Law model: gdp_growth ~ unemployment_diff. Report the estimated coefficients and p-values. How does the sign of the slope compare to Q1(b)? Interpret the slope in context.`

```
Intercept (three decimal places)
[____](=0.788+-0.001)

Slope (three decimal places)
[____](=-1.261+-0.001)

p-value on the intercept (three decimal places)
[____](=0+-0.001)

p-value on the slope (three decimal places)
[____](=0+-0.001)

How does the sign compare, and what does the slope mean?
(x) It flipped to negative: a quarter in which unemployment rises one percentage point has GDP growth about 1.26 percentage points lower
( ) It is still positive: a quarter in which unemployment rises one percentage point has GDP growth about 1.26 percentage points higher
( ) It flipped to negative: a one percentage point higher unemployment rate lowers the level of GDP by $1.26 billion
```

### Q2.3: `Create a residual plot for the Okun's Law model. Compare it to the residual plot from Q1(c). Which model appears better specified? Describe the differences you see.`

```
Upload your figure.
|files|

Describe the differences you see.
|____|
```

### Q2.4: `Create a lagged residual plot for the Okun's Law model. Compare it to the lagged residual plot from Q1(d). Which model shows less autocorrelation? How can you tell from the plot?`

```
Upload your figure.
|files|

(x) The Okun's Law model: its lag plot is a round cloud, while the levels model's is a tight diagonal line
( ) The levels model: its lag plot is a tight diagonal line, while the Okun's Law model's is a round cloud
( ) Neither: the two lag plots look the same
```

### Q2.5: `Compare the levels model (Q1) and the Okun's Law model (Q2). Which result is more consistent with economic theory? Why does the levels model give a misleading result?`

```
|____|
```

## Answer check

Verified by running the solutions notebook against `data/okun.csv` (287 quarters, 1948 Q2 through 2019 Q4), using the gdp_growth and unemployment_diff columns provided in the file:

- Q1 (gdp ~ unemployment): intercept 6707.741 (standard error 1179.511, p ≈ 3 × 10⁻⁸); slope 479.649 (standard error 197.436, t = 2.429, p = 0.0157); R² 0.020. Lagged residual correlation 0.999.
- Q2 (gdp_growth ~ unemployment_diff): intercept 0.7879 (standard error 0.045); slope −1.2613 (standard error 0.107, t = −11.834, p ≈ 1.5 × 10⁻²⁶); R² 0.329. Lagged residual correlation 0.112.
- The provided gdp_growth column is in percent. A student who instead computes growth with pct_change(), as in Exercise 4.4, gets a fraction and loses the first quarter: intercept 0.0078 and slope −0.0128 on 286 quarters. Those answers are marked wrong by the tolerances above; the handout tells students to use the provided columns.
