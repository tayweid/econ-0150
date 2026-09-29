# Homework 2.1 | Gradescope

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

## Q1: `Bike Rentals and Weather`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

In the following questions, we'll analyze a data set that includes the monthly number of bike rentals in London as well as monthly weather data: minimum and maximum temperature in degrees Celsius, rain in millimeters, and hours of sunshine.

![Bike rentals vs. maximum temperature, sunshine, and rain](https://econ-0150.tayweid.io/parts/part-2-1/i/hw_01.png)
```

### Q1.1: `How much did it rain in the month with the largest number of bike rentals?`

```
(x) 7.6 mm
( ) 27.6 mm
( ) 137.6 mm
( ) 157.6 mm
```

### Q1.2: `When were bikes most popular?`

```
(x) In very sunny months
( ) In moderately sunny months
( ) In cloudy months
( ) Sunshine and bike rentals were not strongly related
```

### Q1.3: `In months with what maximum temperatures were bikes most popular?`

```
( ) Between 5 C and 10 C
( ) Between 15 C and 20 C
(x) Between 25 C and 30 C
( ) Maximum temperature and bike rentals were not strongly related
```

## Q2: `Coffee Production and Agricultural Employment`

```
The dataset coffee_prod_agr.csv provides information on coffee production and employment in agriculture across 76 countries in 2023, merged from data available at Our World In Data (https://ourworldindata.org/grapher/coffee-production-by-region?tab=table) and The World Bank (https://data.worldbank.org/indicator/SL.AGR.EMPL.ZS).
```

### Q2.1: `Briefly describe the organizations that collected the data reported in each source.`

```
|____|
```

### Q2.2: `Identify one potential limitation in the data.`

```
|____|
```

### Q2.3: `Create Log_Coffee_Prod and scatter Employment_in_agriculture against it. Upload your figure.`

```
|files|
```

### Q2.4: `Describe the relationship: positive, negative, or unclear?`

```
(x) Weakly positive: countries with more agricultural employment tend to produce somewhat more coffee, but the points are widely scattered
( ) Strongly positive: the points fall close to an upward-sloping line
( ) Negative: countries with more agricultural employment produce less coffee
( ) No relationship: the points show no pattern at all
```

### Q2.5: `Why might we see this relationship between log coffee production and employment in agriculture?`

```
|____|
```

## Answer check

Computed from `data/coffee_prod_agr.csv` (76 countries, all 2023; Dominica has no agricultural employment value, so the scatter shows 75 points). The correlation between `Employment_in_agriculture` and `Log_Coffee_Prod` is 0.28: weakly positive. A student who answers "unclear" in the notebook has a defensible reading; Q2.4 keys the weak positive choice. Q1 answers are read off `i/hw_01.png`: the highest-rental month (about 1,320 thousand) sits at about 7.6 mm of rain, rentals peak in the sunniest months, and the top rentals occur at 25-30 C maximum temperatures.
