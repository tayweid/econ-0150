# Homework 1.5 | Gradescope

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

## Q1: `Transforming Marriage Rates`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The following questions are based on crude marriage rates in marriage_rates.csv — numbers of marriages per one thousand inhabitants — in 1990 and 2019. Each row represents a different European country.
```

### Q1.1: `Create a multi-boxplot comparing marriage rates in 1990 vs 2019. Did marriage rates generally increase or decrease?`

```
( ) Increased — the 2019 box sits above the 1990 box
(x) Decreased — the 2019 box sits below the 1990 box, with the median falling from about 6.5 to about 4.9
( ) Stayed about the same — the two boxes overlap almost completely
( ) The boxplots cannot tell us
```

### Q1.2: `Compute the absolute change (2019 minus 1990). Which country has the largest absolute change?`

```
(x) Iceland
( ) Hungary
( ) Portugal
( ) Sweden
```

### Q1.3: `Compute the relative change (absolute change divided by the 1990 value). Which country has the largest relative change?`

```
(x) Iceland
( ) Hungary
( ) Portugal
( ) Czechia
```

### Q1.4: `Create a scatterplot of 1990 (x-axis) vs 2019 (y-axis) with a 45-degree line. Which countries are above the line, and what does that mean?`

```
Select all that apply.
[x] Iceland is above the line.
[x] Hungary is above the line.
[x] Being above the line means the country's marriage rate was higher in 2019 than in 1990.
[ ] Portugal is above the line.
[ ] Being above the line means the country's marriage rate is above the European average.
```

## Q2: `Optional: Comparing Coffee Production Across Time`

```
Optional. Use coffee_prod_in_years.csv, which provides coffee production for 76 countries between 1961 and 2023 in long format. Reshape it to wide format with pivot() before comparing years.
```

### Q2.1: `Reshape to wide format and scatter 1961 (x-axis) vs 2023 (y-axis) with a 45-degree line. Which countries stand out as outliers?`

```
Select all that apply.
[x] Brazil — by far the largest producer in both years, far to the upper right
[x] Vietnam — almost no production in 1961 but among the largest producers in 2023, far above the line
[ ] Angola — the largest producer in 2023
[ ] Colombia — the only country below the line
```

### Q2.2: `How many countries increased their coffee production between 1961 and 2023, and how many decreased?`

```
( ) 31 increased, 45 decreased
(x) 45 increased, 31 decreased
( ) 76 increased, 0 decreased
( ) 38 increased, 38 decreased
```

### Q2.3: `Which figure better helps you understand patterns in coffee production: the HW 1.4 multi-line plot or the 1961 vs 2023 scatter?`

```
There is no single right answer — select the statements that correctly describe what each figure shows.
[x] The scatter summarizes the change for every country in one figure, but only compares two years.
[x] The multi-line plot shows the full path over time, but becomes crowded with many countries.
[x] The scatter's 45-degree line makes it immediate to see who increased and who decreased.
[ ] The multi-line plot shows which countries increased more clearly than the scatter does.
[ ] The two figures always lead to the same conclusion, so the choice does not matter.

|____|
```
