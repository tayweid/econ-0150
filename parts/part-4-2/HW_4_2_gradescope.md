# Homework 4.2 | Gradescope

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

## Q1: `Mental Health and Income Group`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The 2011 Behavioral Risk Factor Surveillance System (BRFSS) data include MENTHLTH (days of poor mental health in the past 30 days) and INCOME2 (income category: 1 = less than $10,000, ..., 8 = $75,000 or more). The Homework 4.2 Notebook loads the data and, as in Exercise 4.2, drops respondents with a missing income or mental health response. Create a binary variable under_10k equal to 1 if INCOME2 == 1 and 0 otherwise, then estimate the linear model

$$MENTHLTH_i = \beta_0 + \beta_1 \cdot under\_10k_i + \varepsilon_i$$
```

### Q1.1: `Report the estimated intercept. What does it represent in context?`

```
Intercept $$\hat\beta_0$$ (three decimal places)
[____](=3.195+-0.003)

What does it represent?
(x) The average number of poor mental health days among respondents with household income of $10,000 or more
( ) The average number of poor mental health days among respondents with household income under $10,000
( ) The average number of poor mental health days across all respondents
( ) The predicted number of poor mental health days for a respondent with zero income
```

### Q1.2: `Report the estimated slope. What does it represent in context?`

```
Slope $$\hat\beta_1$$ (three decimal places)
[____](=4.834+-0.003)

What does it represent?
(x) The difference in average poor mental health days between respondents under $10,000 and everyone else
( ) The average number of poor mental health days among respondents under $10,000
( ) The change in poor mental health days for each additional $10,000 of income
( ) The share of respondents with household income under $10,000
```

## Q2: `Reading Regression Output`

```
A researcher wants to test whether having a college degree is associated with higher hourly wages. They code a binary variable college equal to 1 if the worker has a college degree and 0 otherwise, then estimate

$$wage_i = \beta_0 + \beta_1 \cdot college_i + \varepsilon_i$$

Their regression output is in the handout and the notebook: the Intercept row shows coef 18.42, std err 0.310, t 59.419, p 0.000; the college row shows coef 9.65, std err 0.440, t 21.932, p 0.000.
```

### Q2.1: `Interpret the intercept coefficient (18.42) in context.`

```
(x) Workers without a college degree earn $18.42 per hour on average
( ) Workers with a college degree earn $18.42 per hour on average
( ) All workers in the sample earn $18.42 per hour on average
( ) A worker with zero years of schooling is predicted to earn $18.42 per hour
```

### Q2.2: `Interpret the slope coefficient (9.65) in context.`

```
(x) Workers with a college degree earn $9.65 more per hour on average than workers without one
( ) Workers with a college degree earn $9.65 per hour on average
( ) Each additional year of college raises the hourly wage by $9.65
( ) Workers with a college degree earn 9.65% more than workers without one
```

### Q2.3: `What is the null hypothesis being tested for the college coefficient?`

```
(x) $$\beta_1 = 0$$: workers with and without a college degree have the same average wage
( ) $$\beta_1 = 9.65$$
( ) $$\beta_0 = 0$$: workers without a college degree earn nothing
( ) $$\beta_1 > 0$$: college graduates earn more
```

### Q2.4: `Interpret the p-value in words.`

```
|____|
```

## Answer check

Verified with a statsmodels OLS fit on data/BRFSS_cleaned.csv after dropping rows with a missing INCOME2 or MENTHLTH (206,739 of 243,402 rows remain):

- Q1: intercept 3.1948 (standard error 0.017), the mean of the 195,920 respondents at \$10,000 or more; slope 4.8339 (standard error 0.075, t = 64.596, p prints as 0.000); the 10,819 respondents under \$10,000 average 8.0287 days.
- Skipping the drop codes the 33,525 missing-income respondents as under_10k = 0 and gives an intercept of 3.1877 and a slope of 4.8410. Both fall outside the ±0.003 tolerances, so widen them to ±0.01 to accept either version.
