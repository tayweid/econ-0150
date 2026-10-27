# Exercise 3.4 | Gradescope

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
Complete Questions 1–2 in the Exercise 3.4 notebook. The 30 observations are paired wait time differences (afternoon minus morning), in minutes. Round numerical answers to three decimal places.
```

### Q1.1: `What is the sample mean difference in minutes?`

```
[____](=2.047+-0.001)
```

### Q1.2: `What is the sample standard deviation in minutes?`

```
Use the sample standard deviation, with ddof=1.
[____](=0.477+-0.001)
```

### Q1.3: `Where is the histogram centered?`

```
( ) Near zero minutes
(x) Near positive two minutes: afternoon waits tend to be longer
( ) Near negative two minutes: morning waits tend to be longer
( ) Near positive thirty minutes
```

## Q2: `Choosing the Best Prediction`

```
Complete Questions 3–5 in the notebook. Predict each observation using a single number b and calculate the mean squared error. MSE is measured in squared minutes. Round numerical answers to three decimal places.
```

### Q2.1: `What is the MSE when b = 2.5?`

```
[____](=0.425+-0.001)
```

### Q2.2: `What is the MSE when b = 1.5?`

```
[____](=0.519+-0.001)
```

### Q2.3: `What is the MSE when b is the sample mean?`

```
Use the unrounded sample mean in your calculation.
[____](=0.220+-0.001)
```

### Q2.4: `Which prediction gives the smallest MSE?`

```
( ) b = 2.5
( ) b = 1.5
(x) b = the sample mean
( ) All three have the same MSE
```

## Q3: `Fitting the Model`

```
Complete Questions 6–7 in the notebook. Fit the intercept-only model using statsmodels and inspect its coefficient table.
```

### Q3.1: `What is the estimated intercept?`

```
Round to three decimal places.
[____](=2.047+-0.001)
```

### Q3.2: `How does the intercept compare with the sample mean?`

```
(x) They are equal, apart from numerical rounding
( ) The intercept is the sample standard deviation
( ) The intercept is the mean squared error
( ) The intercept must be zero because there are no predictors
```

### Q3.3: `What null hypothesis does the intercept p-value test?`

```
(x) The population mean afternoon-minus-morning wait time difference is zero
( ) The sample mean difference is zero
( ) The population standard deviation of the differences is zero
( ) Every afternoon wait is longer than its paired morning wait
```

## Answer check

Verified using the notebook's 30 observations and a statsmodels intercept-only OLS fit:

- Mean: 2.0466666667 minutes; sample standard deviation: 0.4768671711 minutes.
- MSE at 2.5: 0.4253333333; at 1.5: 0.5186666667; at the mean: 0.2198222222 squared minutes.
- Intercept: 2.0466666667; standard error: approximately 0.0870636; t = 23.50770967 with 29 degrees of freedom.
- Two-sided p-value: approximately 1.9722 × 10⁻²⁰. The one-sample t-test against zero gives the same statistic and p-value.
- 95% confidence interval: approximately [1.869, 2.225] minutes.

The notebook uses 1/n for MSE and 1/(n−1) for sample variance; these quantities differ. The inference assumes independent pairs and a suitable sampling model. The result describes a mean difference, not a causal effect or a claim about every visit. The coefficient table rounds the p-value to 0.000; the p-value is not exactly zero.
