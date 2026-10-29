# Homework 3.4 | Gradescope

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

## Q1: `Study Hours`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

An economics professor claims that students spend 6 hours per week on average studying for their economics class. You survey 20 students and record the number of hours they reported studying per week (the list is in the handout and the notebook). Use an intercept-only regression (GLM) model to test the professor's claim. The p-value on the intercept tests whether the population mean is zero, so first subtract 6 from each student's hours; the notebook includes this step.
```

### Q1.1: `What is the estimated difference in study hours from 6 hours?`

```
The intercept of the model (three decimal places)
[____](=0.21+-0.001)
```

### Q1.2: `What is the intercept's p-value?`

```
Round to two decimal places.
[____](=0.41+-0.01)

At α = 0.05, what do you conclude about the professor's claim?
(x) Fail to reject the null: the data are consistent with an average of 6 hours per week
( ) Reject the null: students study significantly more than 6 hours per week
( ) Reject the null: students study significantly less than 6 hours per week
( ) The test cannot be run because the sample mean is not zero
```

### Q1.3: `In your own words, what does the p-value in this model represent?`

```
|____|
```

## Q2: `Pennsylvania Household Income`

```
According to USAFacts, the median household income in Pennsylvania was reported to be $73,824 in 2023. The Homework 3.4 Notebook loads a sample of median household incomes for 30 Pennsylvania counties. Use this sample to test whether the average median household income in these counties differs from the statewide figure. As in Q1, subtract 73,824 from each county's median income before fitting the intercept-only model.
```

### Q2.1: `Use an intercept-only model to test whether the average median household income in the sample differs from $73,824. Report the sample mean, the standard error, and the p-value.`

```
Sample mean median household income, in dollars (nearest dollar)
[____](=65700+-1)

Intercept: the mean difference from 73,824, in dollars (nearest dollar)
[____](=-8124+-1)

Standard error, in dollars (nearest dollar)
[____](=1905+-1)

Two-sided p-value (four decimal places; the coefficient table shows 0.000)
[____](=0.0002+-0.0002)
```

### Q2.2: `Based on your results, does the sample provide evidence that the average county median income is different from the statewide figure? Briefly interpret your results in words.`

```
Does the sample provide evidence that the average county median income differs from $73,824?
(x) Yes: the sample average is about $8,100 lower, more than four standard errors from zero, so the difference is very unlikely to be sampling noise
( ) No: the p-value is above 0.05
( ) No: a sample of 30 counties is too small to test anything
( ) Yes, but only because the standard error is large

Briefly interpret your results in words.
|____|
```

## Answer check

Verified with statsmodels intercept-only OLS fits on the handout's 20 study-hour values and the 30 rows of data/pa_sample_30.csv:

- Q1: sample mean 6.21 hours; intercept on the difference 0.2100; standard error 0.2491; t = 0.843 with 19 degrees of freedom; two-sided p = 0.4097. Fitting the raw hours instead (no subtraction) gives an intercept of 6.21 with p ≈ 6 × 10⁻¹⁶, which tests the wrong null (mean = 0).
- Q2: sample mean $65,699.87; intercept −8,124.13; standard error 1,905.33; t = −4.264 with 29 degrees of freedom; two-sided p = 0.000195. The coefficient table prints 0.000, so the tolerance accepts anything from 0 to 0.0004.
- The county average sits below the statewide household median because the statewide figure weights by households, so the populous suburban counties count more, while the county average weights every county equally.
