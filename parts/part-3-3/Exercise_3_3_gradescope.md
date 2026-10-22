# Exercise 3.3 | Gradescope

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

## Q1: `Confidence Intervals with Known Mean and Standard Deviation`

```
Work through the questions in the Exercise 3.3 notebook first, then enter your answers here. Suppose we know that the true effect of the NJ minimum wage on employment is $$\mu = 0$$ FTE and the population standard deviation is $$\sigma = 9.8$$ FTE. Card and Krueger surveyed $$n = 331$$ restaurants.
```

### Q1.1: `What is the standard error of the sample mean? Round to two decimals.`

```
[____](=0.54+-0.01)
```

### Q1.2: `What is the probability that the sample mean falls within 1 × SE of μ? Round to two decimals.`

```
[____](=0.68+-0.01)
```

### Q1.3: `What is the probability that the sample mean falls within 2 × SE of μ? Round to two decimals.`

```
[____](=0.95+-0.01)
```

## Q2: `Simulating Confidence Intervals`

```
Draw a sample of 331 restaurants from the population in the notebook. Your sample is random, so your sample mean will differ from your classmates'.
```

### Q2.1: `What is the interval μ ± 1 × SE? Round to two decimals.`

```
Lower bound:
[____](=-0.54+-0.01)

Upper bound:
[____](=0.54+-0.01)
```

### Q2.2: `What is your sample mean? Round to two decimals.`

```
[____](=0+-2.7)
```

### Q2.3: `Did your sample mean fall within μ ± 1 × SE? Enter 1 for yes and 0 for no.`

```
[____](=0.5+-0.5)
```

### Q2.4: `Did your sample mean fall within μ ± 2 × SE? Enter 1 for yes and 0 for no.`

```
[____](=0.5+-0.5)
```

## Q3: `Class Data`

```
Everyone in the class drew their own sample of 331 restaurants.
```

### Q3.1: `About what fraction of the class should have a sample mean within μ ± 2 × SE?`

```
( ) About 50%
( ) About 68%
(x) About 95%
( ) 100%
```

## Answer check

Computed by running the Exercise 3.3 notebook. SE = 9.8 / √331 = 0.539. Within 1 × SE: 0.683; within 2 × SE: 0.954. The interval μ ± 1 × SE is [−0.54, 0.54].

Q2.2 to Q2.4 depend on each student's random draw, so they are graded for completion. Q2.2 accepts −2.7 to 2.7, which is 5 standard errors on either side of μ = 0: it accepts any honest draw and rejects common slips like entering σ or the sum instead of the mean. Q2.3 and Q2.4 accept 0 or 1 (the range also lets 0.5 through). Their Gradescope averages are the class fractions from the notebook's Class Data cell, so expect about 0.68 and 0.95.
