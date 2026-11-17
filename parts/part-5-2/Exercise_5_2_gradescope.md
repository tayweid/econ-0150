# Exercise 5.2 | Gradescope

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

## Q1: `Model 3: Differential Returns to Education`

```
Complete Question 1 in the Exercise 5.2 notebook. Fit the model LNINC ~ EDU + EDU:MALE.
```

### Q1.1: `What is the estimated coefficient on EDU:MALE?`

```
Round to three decimal places.
[____](=0.034+-0.001)
```

## Q2: `Model 4: Full Model`

```
Complete Question 2 in the notebook. Fit the model LNINC ~ EDU + MALE + EDU:MALE.
```

### Q2.1: `What is the estimated coefficient on EDU:MALE?`

```
Round to three decimal places.
[____](=0.015+-0.001)
```

## Answer check

Verified by running the notebook's code with the solutions against `data/usa_00041_sample.csv` (1,000 rows, 482 male), with `LNINC` the natural log of `INCTOT`:

- Model 3: intercept 7.2049, EDU 0.2111, EDU:MALE 0.0344 (standard error 0.004, p < 0.001).
- Model 4: intercept 7.0736, EDU 0.2203, MALE 0.2731 (p = 0.493), EDU:MALE 0.0149 (standard error 0.029, p = 0.604).
