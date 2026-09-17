# Homework 1.4 | Gradescope

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

## Q1: `Numerical Variables in Panel`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The following data on hours worked is available from Our World in Data. This question is aimed at practicing the skill of making comparisons of numerical timeseries variables displayed visually.

![Average annual hours worked by country](https://econ-0150.tayweid.io/parts/part-1-4/i/hw_01.png)
```

### Q1.1: `In which country did people work the most on average?`

```
(x) South Korea
( ) United States
( ) Norway
```

### Q1.2: `When did Norwegians work less than Americans?`

```
( ) Before 1963
( ) During 1963
(x) After 1963
( ) Never
```

### Q1.3: `When was the largest difference between the longest and the shortest annual working time?`

```
( ) 1960s
(x) 1980s
( ) 2000s
( ) 2010s
```

### Q1.4: `In the 1980s, roughly how many times more did an average South Korean work than an average Norwegian?`

```
(x) 2x
( ) 3x
( ) 4x
( ) 5x
```

### Q1.5: `Use working_north_america.csv to create a multiple line plot of average annual hours worked for the United States, Canada, and Mexico, 1956-2017. What does it show?`

```
Select all that apply.
[x] Mexico is above the other two countries in every year.
[x] Canada and the United States are close together and cross each other several times.
[x] All three countries work fewer hours in 2017 than in 1956.
[ ] The United States is above Mexico for most of the period.
[ ] Canada's hours rise steadily over the period.
```

## Q2: `Multi-Country Coffee Production`

```
Use selected_coffee_prod_in_years.csv, which provides coffee production (tonnes) for seven countries between 1961 and 2023.
```

### Q2.1: `Plot a line graph of global coffee production over time (the total across all countries for each year). Describe the trend.`

```
( ) Total production is roughly flat from 1961 to 2023.
(x) Total production rises over the period, from about 3 million tonnes to nearly 8 million, with year-to-year variation.
( ) Total production falls steadily after 1990.
( ) Total production spikes once in the 1970s and then returns to its 1961 level.
```

### Q2.2: `Plot a line graph of coffee production for each country over time, all countries in a single figure. Which country is the largest producer in every year?`

```
(x) Brazil
( ) Colombia
( ) Vietnam
( ) Indonesia
```

### Q2.3: `Create a faceted line plot with each country in its own panel. Which country shows the most dramatic growth, going from almost nothing in 1961 to the second-largest producer by 2023?`

```
( ) Honduras
( ) India
(x) Vietnam
( ) Mexico
```

### Q2.4: `Compare your multi-line plot (b) with your faceted plot (c).`

```
Select the statements that are true.
[x] The faceted plot makes it easier to see each country's own trend, because each panel has its own scale.
[x] The multi-line plot makes it easier to compare countries against each other, because they share one set of axes.
[x] In the multi-line plot, Brazil's scale squashes the smaller producers toward the bottom of the figure.
[ ] The faceted plot is better for comparing the level of production across countries.
[ ] The two figures show different data.
```

### Q2.5: `Choose one of the top coffee-producing countries and plot its production over time. Describe the pattern and propose a possible explanation.`

```
Select the country you plotted, then describe the pattern in one or two sentences and propose a possible explanation (e.g., conflict, policy changes, new entrants to the market).
( ) Brazil
( ) Colombia
( ) Vietnam
( ) Indonesia
( ) Another country from the dataset

|____|
```
