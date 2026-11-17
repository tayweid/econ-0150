# Exercise 5.1 | Gradescope

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

## Q1: `Model 1: Basic Gender Wage Gap`

```
Complete Question 1 in the Exercise 5.1 notebook. Fit the model INCLOG10 ~ MALE.
```

### Q1.1: `What is the estimated coefficient on MALE?`

```
Round to three decimal places.
[____](=0.159+-0.001)
```

## Q2: `Model 2: Education + Gender Wage Gap`

```
Complete Question 2 in the notebook. Fit the model INCLOG10 ~ EDU + MALE.
```

### Q2.1: `What is the estimated coefficient on MALE?`

```
Round to three decimal places.
[____](=0.207+-0.001)
```

## Answer check

Verified by running the notebook's code with the solutions against `data/usa_00041_sample.csv` (1,000 rows, 482 male):

- Model 1: intercept 4.4040, MALE 0.1593 (standard error 0.030, p < 0.001).
- Model 2: intercept 3.0302, EDU 0.0987, MALE 0.2072 (standard error 0.027, p < 0.001).
