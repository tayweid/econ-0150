# Homework 3.3 | Gradescope

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

## Q1: `Known μ and σ`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

A university runs a campus wellness program designed to reduce student anxiety. Anxiety is measured on a 0–21 scale for the same students before and after the program. For each student, we compute the paired difference: after minus before. A negative difference means the student's anxiety decreased.

Suppose we know the population of paired differences has mean μ = -3 and standard deviation σ = 5 and we have a sample of n = 25 students.
```

### Q1.1: `Compute the standard error (SE) of the sample mean. Then compute the probability that the sample mean falls within 1 SE of μ.`

```
Standard error
[____](=1+-0)

Probability the sample mean falls within 1 SE of μ (three decimal places)
[____](=0.683+-0.002)
```

### Q1.2: `Construct a 1 SE confidence interval centered on μ. Then simulate 1,000 samples of size n = 25 from this population. What fraction of the 1,000 sample means fall inside the confidence interval?`

```
Lower end of the interval
[____](=-4+-0)

Upper end of the interval
[____](=-2+-0)

Fraction of your 1,000 sample means inside the interval (three decimal places)
[____](=0.683+-0.06)

How does this fraction compare to the probability you computed in Q1.1?
(x) Close to it: the simulation matches the normal probability, apart from random noise
( ) About half of it
( ) Much larger, close to 0.95
( ) Unrelated: the simulation and the probability measure different things
```

## Q2: `Testing a Model`

```
In practice we don't know σ or μ. Instead of constructing confidence intervals centered on μ using σ, we center them on the sample mean and swap in the sample standard deviation S for σ. This swap introduces extra uncertainty which we account for using the t-distribution. Use this to test whether the wellness program actually works.
```

### Q2.1: `A university runs the program on n = 25 students and finds a sample mean of -2.8 and S = 4.6. State the null hypothesis for testing whether the program has any effect on anxiety.`

```
(x) The population mean paired difference is zero: the program has no effect on anxiety
( ) The sample mean paired difference is zero
( ) The population mean paired difference is -2.8
( ) The population mean paired difference is less than zero: the program reduces anxiety
```

### Q2.2: `Compute the probability of seeing a sample as extreme as this sample mean given the null hypothesis (two-sided).`

```
Standard error S/√n (two decimal places)
[____](=0.92+-0.01)

Two-sided p-value (three decimal places)
[____](=0.006+-0.001)

At α = 0.05, what do you conclude?
(x) Reject the null: a 2.8-point drop would be surprising if the program had no effect
( ) Fail to reject the null: a 2.8-point drop is unsurprising if the program had no effect
( ) Accept the null: the program has no effect
```

### Q2.3: `A large national study of a similar program surveys n = 2,000 students and finds a sample mean of -0.3 and S = 5. Compute the p-value.`

```
Standard error S/√n (two decimal places)
[____](=0.11+-0.01)

Two-sided p-value (three decimal places)
[____](=0.007+-0.001)
```

### Q2.4: `A clinician considers a drop of at least 2 points on the anxiety scale to be meaningful. The first study found a 2.8-point drop. The second found a 0.3-point drop. Which result is practically significant? What does this tell you about the difference between statistical significance and practical significance?`

```
Which result is practically significant?
(x) Only the first study (2.8-point drop, n = 25)
( ) Only the second study (0.3-point drop, n = 2,000)
( ) Both studies, because both p-values are below 0.05
( ) Neither study

In your own words, what does this tell you about the difference between statistical significance and practical significance?
|____|
```

## Q3: `Interpreting p-Values`

```
A researcher studying the effect of a new teaching method on exam scores conducts a hypothesis test and reports a p-value of 0.032.
```

### Q3.1: `In your own words, what does this p-value tell us?`

```
|____|
```

### Q3.2: `If the researcher used a significance level of α = 0.05, would they reject the null hypothesis? What if they used α = 0.01?`

```
At α = 0.05:
(x) Reject the null hypothesis
( ) Fail to reject the null hypothesis

At α = 0.01:
( ) Reject the null hypothesis
(x) Fail to reject the null hypothesis
```

### Q3.3: `For each of the following statements, say whether it is true or false and explain your reasoning.`

```
A p-value of 0.10 means there is a 10% chance that the null hypothesis is true.
( ) True
(x) False

If we fail to reject the null hypothesis, we have proven that it is true.
( ) True
(x) False

A small p-value indicates that our observed result would be unlikely if the null hypothesis were true.
(x) True
( ) False

Explain your reasoning for each statement.
|____|
```

## Answer check

Verified with scipy for the handout's numbers:

- Q1.1: SE = 5/√25 = 1 exactly; P(μ − SE ≤ x̄ ≤ μ + SE) = 0.6827.
- Q1.2: interval [−4, −2]. Across 3,000 simulated students each drawing 1,000 samples, the fraction inside averaged 0.683 with a standard deviation of 0.015 (range 0.629 to 0.737), so ±0.06 covers about four standard deviations.
- Q2.2: SE = 4.6/5 = 0.92; t = −3.04 with 24 degrees of freedom; two-sided p = 0.0056.
- Q2.3: SE = 5/√2000 = 0.112; t = −2.68 with 1,999 degrees of freedom; two-sided p = 0.0074.
- Q2.4: only the 2.8-point drop clears the 2-point threshold. Both p-values are below 0.01, so both are statistically significant; the contrast is the point of the question.
- Q3.2: 0.032 < 0.05 but 0.032 > 0.01.
- Q3.3: false, false, true.
