# Homework 3.1 | Gradescope

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

## Q1: `Working with a Normal Distribution`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The wait times (in minutes) at a restaurant follow a normal distribution with mean 12 minutes and standard deviation 2.5 minutes. Use stats.norm.cdf() and stats.norm.ppf() for the questions marked "use python".
```

### Q1.1: `What is the population mean wait time?`

```
[____](=12+-0)
```

### Q1.2: `What is the population variance of the wait time?`

```
[____](=6.25+-0)
```

### Q1.3: `What is the wait time that is longer than exactly 77 percent of wait times? Round to two decimal places.`

```
[____](=13.85+-0.01)
```

### Q1.4: `What is the probability that a wait time will be greater than 10 minutes? Round to three decimal places.`

```
[____](=0.788+-0.001)
```

### Q1.5: `What is the probability that the wait time will be between 10 and 14 minutes? Round to three decimal places.`

```
[____](=0.576+-0.001)
```

### Q1.6: `What is the probability that the wait time will be less than 7 or greater than 17 minutes? Round to three decimal places.`

```
[____](=0.046+-0.001)
```

## Q2: `Sample vs. Population`

```
The restaurant's population parameters are a mean of 12 and a standard deviation of 2.5. Draw samples from this known population with np.random.normal(12, 2.5, n) and compare the sample statistics to the population parameters.
```

### Q2.1: `How do the sample mean and sample standard deviation of your n = 10 sample compare to the population mean and standard deviation?`

```
(x) They are near 12 and 2.5 but not equal, and a different sample would give different values
( ) They are exactly 12 and 2.5
( ) They have no connection to 12 and 2.5
```

### Q2.2: `How do the sample statistics change as n increases from 10 to 100 to 1000?`

```
(x) The sample mean and standard deviation tend to land closer to 12 and 2.5
( ) The sample mean gets closer to 12, but the sample standard deviation shrinks toward 0
( ) The sample mean and standard deviation move further from 12 and 2.5
( ) They do not change in any systematic way
```

### Q2.3: `Plot a histogram of your n = 1000 sample with the population PDF overlaid. Upload your figure.`

```
|files|
```

### Q2.4: `How well does the sample histogram approximate the population?`

```
(x) Closely: it has the same center, spread, and bell shape, with bars wobbling a little above and below the curve
( ) Poorly: the histogram is skewed while the population curve is symmetric
( ) Perfectly: every bar touches the curve exactly
```

### Q2.5: `In your own words, what is the relationship between a sample and a population? Why do larger samples give us more information about the population?`

```
|____|
```

## Answer check

Computed with `scipy.stats.norm` for a mean of 12 and a standard deviation of 2.5. Q1.3: `norm.ppf(0.77, 12, 2.5)` = 13.847. Q1.4: 1 − `norm.cdf(10)` = 0.7881. Q1.5: `norm.cdf(14)` − `norm.cdf(10)` = 0.5763. Q1.6: `norm.cdf(7)` + 1 − `norm.cdf(17)` = 0.0455 (7 and 17 are exactly two standard deviations out). The tolerance on Q1.6 accepts 0.045 to 0.047, so 0.0455 rounded either way is accepted. Q2 is a simulation, so there is no fixed number to key. A sample of 10 has a sample mean between about 9.6 and 14.4 in 99.8 percent of draws, so Q2.1 keys "near but not equal." The Q2.2 distractor about the standard deviation shrinking toward 0 catches students confusing the sample standard deviation with the standard error, which is the topic of Homework 3.2.
