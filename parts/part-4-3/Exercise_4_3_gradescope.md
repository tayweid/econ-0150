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

## Q1: `General Linear Model`

```
Complete Questions 1–2 in the Exercise 4.3 notebook. Fit the model from Exercise 4.1, Life_Evaluation ~ log_GDP_PerCap, on the 2024 observations, then calculate its residuals and predictions.
```

### Q1.1: `What is the estimated slope?`

```
Round to three decimal places.
[____](=1.515+-0.001)
```

## Q2: `Assumptions 1 and 2: Residual Plot`

```
Complete Question 3 in the notebook.
```

### Q2.1: `Linearity: is there a curve in the residuals?`

```
(x) No: the residuals scatter around zero across the whole range of predictions
( ) Yes: the residuals form a clear U shape
( ) Yes: the residuals rise steadily with the predictions
( ) It cannot be checked with a residual plot
```

### Q2.2: `Homoskedasticity: is the spread of the residuals about the same everywhere?`

```
(x) Roughly, though the residuals are somewhat less spread out at the highest predictions
( ) No: the spread grows dramatically as the predictions grow
( ) No: every residual is the same size
( ) It cannot be checked with a residual plot
```

## Q3: `Assumption 3: Lagged Residual Plot`

```
Complete Question 4 in the notebook.
```

### Q3.1: `What does the lagged residual plot show?`

```
(x) No pattern: a residual tells us nothing about the residual of the row before it
( ) A strong upward diagonal: neighboring rows have similar residuals
( ) A strong downward diagonal: neighboring rows have opposite residuals
( ) A U shape
```

## Q4: `Assumption 4: Normality of Residuals`

```
Complete Question 5 in the notebook.
```

### Q4.1: `What does the histogram of residuals show?`

```
(x) Roughly bell-shaped and centered at zero, with a longer left tail from a few countries far below the line
( ) Perfectly symmetric
( ) Flat: every residual value is equally common
( ) Two separate peaks
```

## Answer check

Verified by running the notebook's code with the solutions against `data/Life_Evaluation_GDP_PerCap.csv`, 2024 rows only (146 countries with GDP per capita):

- Model: intercept −0.2502, slope 1.5145 (standard error 0.0933), as in Exercise 4.1.
- Linearity: mean residual by third of the predictions is −0.042, 0.087, −0.043, so there is no curve.
- Homoskedasticity: the residual standard deviation is 0.826 for the 73 countries with below-median predictions and 0.527 for the 73 above.
- Independence: the correlation between each residual and the one before it is −0.010. The rows are countries in alphabetical order.
- Normality: residual skewness −0.656. The most negative residual is Afghanistan at −2.535; the most positive is Nicaragua at 1.480.
