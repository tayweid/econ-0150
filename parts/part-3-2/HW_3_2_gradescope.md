# Homework 3.2 | Gradescope

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

## Q1: `The Central Limit Theorem with a Normal Population`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The wait times (in minutes) at a restaurant follow a normal distribution with mean 12 minutes and standard deviation 2.5 minutes. In this question you will explore what happens to the distribution of sample means as the sample size increases.
```

### Q1.1: `Take 1,000 samples of size n = 5 from this distribution. Compute the mean of each sample and plot a histogram of the 1,000 sample means. Upload your figure.`

```
|files|
```

### Q1.2: `Repeat Q1.1 for sample sizes n = 30 and n = 100. Plot all three histograms. Describe how the distribution of sample means changes as n increases.`

```
Upload your figure with all three histograms.
|files|

How does the distribution of sample means change as n increases?
(x) It stays centered at 12 and gets narrower
( ) It stays centered at 12 and gets wider
( ) Its center moves away from 12
( ) It becomes skewed to the right
```

### Q1.3: `Compute the standard deviation of the sample means for each sample size. Round to two decimal places.`

```
n = 5
[____](=1.12+-0.1)

n = 30
[____](=0.46+-0.04)

n = 100
[____](=0.25+-0.02)
```

### Q1.4: `Compute the standard error σ/√n for each sample size, using σ = 2.5. Round to three decimal places. Compare these values to the standard deviations you computed in Q1.3.`

```
n = 5
[____](=1.118+-0.001)

n = 30
[____](=0.456+-0.001)

n = 100
[____](=0.25+-0.001)

Compared to these standard errors, your standard deviations from Q1.3 are:
(x) Very close at every sample size
( ) Close to σ = 2.5 at every sample size
( ) Close only for n = 5
```

### Q1.5: `In your own words, why does the spread of the sampling distribution decrease as n increases?`

```
|____|
```

## Q2: `The Central Limit Theorem with a Skewed Population`

```
Wait times at a busy food truck follow an exponential distribution with a mean of 5 minutes. This distribution is skewed right: most waits are short, but some are very long. Use np.random.exponential(5, size=n) to draw n observations from this population.
```

### Q2.1: `Draw 10,000 observations from this population and plot the histogram. Describe the shape. Is it normal?`

```
Upload your figure.
|files|

Describe the shape. Is it normal?
(x) Not normal: it peaks near zero with a long tail to the right
( ) Not normal: it peaks at the high end with a long tail to the left
( ) Approximately normal and centered at 5
( ) Roughly flat between 0 and 10
```

### Q2.2: `Take 1,000 samples of size n = 5 from this population. Compute the mean of each sample and plot a histogram of the sample means. Upload your figure.`

```
|files|
```

### Q2.3: `Repeat Q2.2 for n = 30. Plot the histogram and describe how the shape changed compared to n = 5.`

```
Upload your figure.
|files|

How did the shape change compared to n = 5?
(x) At n = 5 it is still skewed right; at n = 30 it is close to a symmetric bell and narrower
( ) Both are as skewed as the population
( ) At n = 5 it is already perfectly normal, and n = 30 looks the same
( ) It becomes more skewed as n increases
```

### Q2.4: `For both n = 5 and n = 30, compare the standard deviation of the sample means to the standard error σ/√n. For the exponential distribution, the population standard deviation equals the mean, so σ = 5.`

```
Standard deviation of your sample means, n = 5 (two decimal places)
[____](=2.24+-0.25)

Standard deviation of your sample means, n = 30 (two decimal places)
[____](=0.91+-0.1)

Compared to the standard errors σ/√n, these standard deviations are:
(x) Close at both sample sizes, even though the population is not normal
( ) Far apart, because σ/√n only works for normal populations
( ) Close only for n = 30
```

### Q2.5: `In your own words, what does the Central Limit Theorem guarantee about the shape of the sampling distribution, regardless of the population shape?`

```
|____|
```

## Q3: `The Central Limit Theorem with a Bimodal Population`

```
A coffee shop has two types of customers: those who order just a drink (mean spending of 4 dollars, standard deviation 1) and those who order a drink plus food (mean spending of 12 dollars, standard deviation 1.5). About half of customers fall into each group. Use the bimodal_sample(n) function from the homework to draw n observations from this population.
```

### Q3.1: `Draw 10,000 observations from this population and plot the histogram. Describe the shape. How many peaks does it have?`

```
Upload your figure.
|files|

How many peaks does it have?
( ) One
(x) Two
( ) Three
( ) None: it is flat
```

### Q3.2: `Take 1,000 samples of size n = 5 from this population. Compute the mean of each sample and plot a histogram of the sample means. Upload your figure.`

```
|files|
```

### Q3.3: `Repeat Q3.2 for n = 30. Plot the histogram and describe how the shape changed compared to the population and to n = 5.`

```
Upload your figure.
|files|

How did the shape change?
(x) The two peaks are gone: at n = 5 the means center near 8 but are wide and lumpy, and at n = 30 they form a smooth, narrow bell
( ) The sample means keep two peaks, at 4 and 12, at both sample sizes
( ) The sample means pile up near 4, the more common purchase
( ) The shape is the same as the population at both sample sizes
```

### Q3.4: `Compute the standard deviation of your 10,000 population observations and use it as σ. Then compare the standard deviation of your sample means (for n = 5 and n = 30) to the standard error σ/√n.`

```
Standard deviation of your 10,000 population observations (two decimal places)
[____](=4.2+-0.06)

Standard deviation of your sample means, n = 5 (two decimal places)
[____](=1.88+-0.15)

Standard deviation of your sample means, n = 30 (two decimal places)
[____](=0.77+-0.07)

Compared to the standard errors σ/√n, these standard deviations are:
(x) Close at both sample sizes
( ) Far apart, because σ/√n only works for normal populations
( ) Close to σ itself at both sample sizes
```

### Q3.5: `Across all three questions, you started with a normal population, a skewed population, and a bimodal population. What happened to the sampling distribution of the mean in each case as n increased? What does this tell you about how general the Central Limit Theorem is?`

```
|____|
```

## Answer check

One sub-question per handout part, in the handout’s order (a) to e) are .1 to .5 in each question). Parts that ask for several things (a figure and a description, or several numbers) hold several answer fields in one sub-question.

The standard deviations in Q1.3, Q2.4, and Q3.4 come from each student’s own simulation, so the keys are the standard errors σ/√n with tolerances set by simulating 3,000 students (each running the homework’s 1,000 samples). Every tolerance covers at least the middle 99.8 percent of those simulated answers:

| Field | Key | Accepted | Middle 99.8% of simulated answers |
| --- | --- | --- | --- |
| Q1.3, n = 5 | 2.5/√5 = 1.118 | 1.02 to 1.22 | 1.04 to 1.19 |
| Q1.3, n = 30 | 2.5/√30 = 0.456 | 0.42 to 0.50 | 0.42 to 0.49 |
| Q1.3, n = 100 | 2.5/√100 = 0.250 | 0.23 to 0.27 | 0.23 to 0.27 |
| Q2.4, n = 5 | 5/√5 = 2.236 | 1.99 to 2.49 | 2.06 to 2.44 |
| Q2.4, n = 30 | 5/√30 = 0.913 | 0.81 to 1.01 | 0.85 to 0.99 |
| Q3.4, population | √17.625 = 4.198 | 4.14 to 4.26 | 4.16 to 4.23 |
| Q3.4, n = 5 | 4.198/√5 = 1.877 | 1.73 to 2.03 | 1.76 to 1.99 |
| Q3.4, n = 30 | 4.198/√30 = 0.766 | 0.70 to 0.84 | 0.71 to 0.82 |

Q1.4’s standard errors are exact: 2.5/√5 = 1.118, 2.5/√30 = 0.456, 2.5/√100 = 0.250, accepted to ±0.001.

The bimodal population’s variance is the average within-group variance plus the variance of the group means: 0.5(1²) + 0.5(1.5²) + 4² = 17.625, so σ ≈ 4.20. The earlier solutions said “approximately 4.3”; that was wrong. Q3.3: at n = 5 the sample means look lumpy because a sample of five has 0 to 5 food customers, which puts bumps near 5.6, 7.2, 8.8, and 10.4 dollars. The solution notebook uses `np.random.seed(150)`, giving 1.149, 0.469, 0.246 (Q1.3), 2.134, 0.907 (Q2.4), and 4.208, 1.877, 0.756 (Q3.4), all inside the accepted ranges.
