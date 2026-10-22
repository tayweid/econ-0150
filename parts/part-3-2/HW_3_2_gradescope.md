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

The wait times (in minutes) at a restaurant follow a normal distribution with mean 12 minutes and standard deviation 2.5 minutes. Take 1,000 samples of each size and compute the mean of each sample.
```

### Q1.1: `Plot the histograms of the 1,000 sample means for n = 5, n = 30, and n = 100. Upload your figure.`

```
|files|
```

### Q1.2: `How does the distribution of sample means change as n increases?`

```
(x) It stays centered at 12 and gets narrower
( ) It stays centered at 12 and gets wider
( ) Its center moves away from 12 as n increases
( ) It becomes skewed to the right
```

### Q1.3: `What is the standard deviation of your 1,000 sample means for n = 5? Round to two decimal places.`

```
[____](=1.12+-0.1)
```

### Q1.4: `What is the standard deviation of your 1,000 sample means for n = 30? Round to two decimal places.`

```
[____](=0.46+-0.04)
```

### Q1.5: `What is the standard deviation of your 1,000 sample means for n = 100? Round to two decimal places.`

```
[____](=0.25+-0.02)
```

### Q1.6: `How do the standard deviations of your sample means compare to the standard errors σ/√n (1.118, 0.456, and 0.250)?`

```
(x) They are very close to the standard errors for every sample size
( ) They are all close to σ = 2.5, not to the standard errors
( ) They match the standard error for n = 5 but not for larger samples
```

### Q1.7: `In your own words, why does the spread of the sampling distribution decrease as n increases?`

```
|____|
```

## Q2: `The Central Limit Theorem with a Skewed Population`

```
Wait times at a busy food truck follow an exponential distribution with a mean of 5 minutes and a standard deviation of 5 minutes. Draw from it with np.random.exponential(5, size=n).
```

### Q2.1: `Plot the histogram of 10,000 observations from this population. Upload your figure.`

```
|files|
```

### Q2.2: `Describe the shape of the population. Is it normal?`

```
(x) Not normal: it peaks near zero with a long tail to the right
( ) Not normal: it peaks at the high end with a long tail to the left
( ) Approximately normal and centered at 5
( ) Roughly flat between 0 and 10
```

### Q2.3: `Plot the histograms of the 1,000 sample means for n = 5 and n = 30. Upload your figure.`

```
|files|
```

### Q2.4: `How did the shape of the sampling distribution change from n = 5 to n = 30?`

```
(x) At n = 5 it is still skewed right; at n = 30 it is close to a symmetric bell and narrower
( ) Both are as skewed as the population
( ) At n = 5 it is already perfectly normal, and n = 30 looks the same
( ) It becomes more skewed as n increases
```

### Q2.5: `What is the standard deviation of your 1,000 sample means for n = 5? Round to two decimal places.`

```
[____](=2.24+-0.25)
```

### Q2.6: `What is the standard deviation of your 1,000 sample means for n = 30? Round to two decimal places.`

```
[____](=0.91+-0.1)
```

### Q2.7: `How do these compare to the standard errors σ/√n (2.236 and 0.913)?`

```
(x) They are close, so the standard error formula works even though the population is not normal
( ) They are far apart, because the formula only works for normal populations
( ) They are both close to σ = 5
```

### Q2.8: `In your own words, what does the Central Limit Theorem guarantee about the shape of the sampling distribution, regardless of the population shape?`

```
|____|
```

## Q3: `The Central Limit Theorem with a Bimodal Population`

```
A coffee shop has two types of customers: about half order just a drink (mean spending 4 dollars, standard deviation 1) and half order a drink plus food (mean spending 12 dollars, standard deviation 1.5). Use the bimodal_sample(n) function from the homework to draw from this population.
```

### Q3.1: `Plot the histogram of 10,000 observations from this population. Upload your figure.`

```
|files|
```

### Q3.2: `How many peaks does the population have?`

```
( ) One
(x) Two
( ) Three
( ) None: it is flat
```

### Q3.3: `Plot the histograms of the 1,000 sample means for n = 5 and n = 30. Upload your figure.`

```
|files|
```

### Q3.4: `How did the shape change compared to the population and from n = 5 to n = 30?`

```
(x) The two peaks are replaced by values centered near 8; at n = 5 it is wide and lumpy, and at n = 30 it is a smooth, narrow bell
( ) The sample means keep two peaks, at 4 and 12, at both sample sizes
( ) The sample means pile up near 4, the more common purchase
( ) The shape is the same as the population at both sample sizes
```

### Q3.5: `What is the standard deviation of your 10,000 population observations? Round to two decimal places.`

```
[____](=4.2+-0.06)
```

### Q3.6: `What is the standard deviation of your 1,000 sample means for n = 5? Round to two decimal places.`

```
[____](=1.88+-0.15)
```

### Q3.7: `What is the standard deviation of your 1,000 sample means for n = 30? Round to two decimal places.`

```
[____](=0.77+-0.07)
```

### Q3.8: `Across the normal, skewed, and bimodal populations, what happened to the sampling distribution of the mean as n increased? What does this tell you about how general the Central Limit Theorem is?`

```
|____|
```

## Answer check

The standard deviations in Q1, Q2, and Q3 come from each student's own simulation, so the keys are the theoretical values with tolerances set by simulating 3,000 students (each running the homework's 1,000 samples). Every tolerance covers at least the middle 99.8 percent of those simulated answers:

| Field | Key | Accepted | Middle 99.8% of simulated answers |
|---|---|---|---|
| Q1.3 (normal, n = 5) | 2.5/√5 = 1.118 | 1.02 to 1.22 | 1.04 to 1.19 |
| Q1.4 (normal, n = 30) | 2.5/√30 = 0.456 | 0.42 to 0.50 | 0.42 to 0.49 |
| Q1.5 (normal, n = 100) | 2.5/√100 = 0.250 | 0.23 to 0.27 | 0.23 to 0.27 |
| Q2.5 (exponential, n = 5) | 5/√5 = 2.236 | 1.99 to 2.49 | 2.06 to 2.44 |
| Q2.6 (exponential, n = 30) | 5/√30 = 0.913 | 0.81 to 1.01 | 0.85 to 0.99 |
| Q3.5 (bimodal population) | √17.625 = 4.198 | 4.14 to 4.26 | 4.16 to 4.23 |
| Q3.6 (bimodal, n = 5) | 4.198/√5 = 1.877 | 1.73 to 2.03 | 1.76 to 1.99 |
| Q3.7 (bimodal, n = 30) | 4.198/√30 = 0.766 | 0.70 to 0.84 | 0.71 to 0.82 |

The bimodal population's variance is the average within-group variance plus the variance of the group means: 0.5(1²) + 0.5(1.5²) + 4² = 17.625, so σ ≈ 4.20. The earlier solutions said "approximately 4.3"; that was wrong. Q3.4: at n = 5 the sample means look lumpy because a sample of five has 0 to 5 food customers, which puts bumps near 5.6, 7.2, 8.8, and 10.4 dollars. The solution notebook uses `np.random.seed(150)`, giving 1.149, 0.469, 0.246 (Q1), 2.134, 0.907 (Q2), and 4.208, 1.877, 0.756 (Q3), all inside the accepted ranges.
