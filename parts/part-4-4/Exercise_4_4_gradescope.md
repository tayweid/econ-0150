# Exercise 4.4 | Gradescope

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
Complete Question 1 in the Exercise 4.4 notebook. The data are quarterly observations for the United States from 1948 through 2019, with real GDP in billions of dollars and the unemployment rate in percentage points.
```

### Q1.1: `How does each series move over time?`

```
(x) GDP trends steadily upward; unemployment rises and falls in cycles with no long-run trend
( ) Both GDP and unemployment trend steadily upward
( ) GDP rises and falls in cycles with no trend; unemployment trends steadily upward
( ) Neither series shows any pattern over time
```

## Q2: `Model 1 | Levels`

```
Complete Questions 2–3 in the notebook. Fit the levels model gdp ~ unemployment and check its residuals. Round numerical answers to three decimal places.
```

### Q2.1: `What is the estimated slope?`

```
[____](=479.649+-0.01)
```

### Q2.2: `Does the sign of the slope agree with Okun's Law?`

```
(x) No: the slope is positive, saying GDP is higher when unemployment is higher
( ) Yes: the slope is negative, saying GDP is lower when unemployment is higher
( ) Yes: the slope is positive, which is what Okun's Law predicts
( ) It cannot be told from the coefficient table
```

### Q2.3: `What is the correlation between each residual and the residual of the quarter before?`

```
[____](=0.999+-0.001)
```

### Q2.4: `What do the residual plots and this correlation tell you about the levels model?`

```
(x) The residuals are almost perfectly autocorrelated, so the independence assumption fails and the standard errors and p-values cannot be trusted
( ) The residuals are independent, so the model's p-values can be trusted
( ) The residuals are normally distributed, so the model is valid
( ) The model fits almost perfectly, because the correlation is close to 1
```

## Q3: `Model 2 | First Differences (Y)`

```
Complete Question 4 in the notebook. Fit gdp_diff ~ unemployment. Round numerical answers to three decimal places.
```

### Q3.1: `What is the lagged residual correlation for Model 2?`

```
[____](=0.424+-0.001)
```

### Q3.2: `How does it compare with Model 1?`

```
(x) Much lower than in Model 1, but still clearly positive: differencing GDP reduced the autocorrelation without eliminating it
( ) About the same as in Model 1
( ) Higher than in Model 1
( ) Exactly zero: differencing GDP eliminated the autocorrelation
```

## Q4: `Model 3 | First Differences (X, Y)`

```
Complete Question 5 in the notebook. Fit gdp_diff ~ unemployment_diff. Round numerical answers to three decimal places.
```

### Q4.1: `What is the estimated intercept?`

```
[____](=65.599+-0.01)
```

### Q4.2: `What is the estimated slope?`

```
[____](=-80.250+-0.01)
```

### Q4.3: `What is the lagged residual correlation for Model 3?`

```
[____](=0.256+-0.001)
```

### Q4.4: `Which sentence correctly interprets the intercept?`

```
(x) In a quarter when the unemployment rate does not change, GDP rises by about $66 billion on average
( ) When the unemployment rate is zero, GDP is about $66 billion
( ) GDP rises by about $66 billion for each one-point rise in the unemployment rate
( ) GDP grows by about 66 percent per quarter
```

### Q4.5: `Which sentence correctly interprets the slope?`

```
(x) A quarter in which the unemployment rate rises by one percentage point is associated with a change in GDP about $80 billion lower
( ) A one percentage point higher unemployment rate is associated with GDP that is $80 billion lower in total
( ) A one percent rise in the unemployment rate is associated with 80 percent lower GDP
( ) GDP falls by $80 billion every quarter
```

### Q4.6: `Does the sign of the slope agree with Okun's Law now?`

```
(x) Yes: quarters in which unemployment rises are quarters in which GDP grows less
( ) No: the slope is still positive
( ) No: the slope is not statistically different from zero
```

## Q5: `Model 4 | Growth Rates`

```
Complete Question 6 in the notebook. Fit gdp_growth ~ unemployment_growth, with growth rates calculated by pct_change (0.01 is growth of 1 percent).
```

### Q5.1: `What is the estimated intercept?`

```
Round to four decimal places.
[____](=0.0081+-0.0001)
```

### Q5.2: `What is the estimated slope?`

```
Round to three decimal places.
[____](=-0.064+-0.001)
```

### Q5.3: `What is the lagged residual correlation for Model 4?`

```
Round to three decimal places.
[____](=0.134+-0.001)
```

### Q5.4: `What does the intercept say about GDP growth in a quarter when the unemployment rate does not change?`

```
(x) GDP grows by about 0.8 percent in that quarter, on average
( ) GDP grows by about 8 percent in that quarter, on average
( ) GDP grows by about $0.008 billion in that quarter, on average
( ) GDP does not grow
```

## Q6: `Comparing the Models`

```
Complete Questions 7–8 in the notebook.
```

### Q6.1: `Which model has the least autocorrelation in its residuals?`

```
(x) Model 4, growth rates
( ) Model 3, first differences of X and Y
( ) Model 2, first differences of Y
( ) Model 1, levels
```

### Q6.2: `Did differencing or growth rates eliminate the autocorrelation?`

```
(x) No: each step reduced it, from 0.999 to 0.424 to 0.256 to 0.134, but some remains
( ) Yes: it is exactly zero in Model 4
( ) No: it is about the same in all four models
( ) Yes: it is negative in Model 4
```

### Q6.3: `What relationship does the plot of GDP growth against the change in unemployment show?`

```
(x) Negative: quarters in which unemployment rises more tend to have lower GDP growth
( ) Positive: quarters in which unemployment rises more tend to have higher GDP growth
( ) No visible relationship
( ) A U shape
```

## Answer check

Verified by running the notebook's code with the solutions against `data/okun.csv` (287 quarters, 1948 Q2 through 2019 Q4). Each differencing step drops one row, so the models use 287, 286, 285, and 284 observations.

- Model 1 (levels): intercept 6707.741; slope 479.649 (standard error 197.436, p = 0.016); R² 0.020; lagged residual correlation 0.9990.
- Model 2 (gdp_diff ~ unemployment): intercept 60.545; slope 0.847 (standard error 2.713, p = 0.755); lagged residual correlation 0.4241.
- Model 3 (gdp_diff ~ unemployment_diff): intercept 65.599 (standard error 3.969); slope −80.250 (standard error 9.335, t = −8.597, p ≈ 5.7 × 10⁻¹⁶); R² 0.207; lagged residual correlation 0.2561.
- Model 4 (growth rates): intercept 0.008059; slope −0.064436 (standard error 0.006, t = −11.321, p ≈ 9.6 × 10⁻²⁵); R² 0.312; lagged residual correlation 0.1336. Mean quarterly GDP growth in this sample is 0.79 percent.
- Okun's Law plot: the correlation between unemployment_diff and gdp_growth is −0.581.

The data file also carries precomputed unemployment_diff, gdp_diff, and gdp_growth columns, with gdp_growth in percent rather than as a fraction. The notebook drops them on load and builds each variable itself, so the answers above are in the notebook's units. The Model 4 slope is in fractional growth terms: a quarter in which the unemployment rate rises by 10 percent of its level (for example from 5.0 to 5.5) is associated with GDP growth about 0.64 percentage points lower.
