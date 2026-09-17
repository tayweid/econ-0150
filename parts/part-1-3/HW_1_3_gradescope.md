# Homework 1.3 | Gradescope

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

## Q1: `US Economic Growth`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The dataset us_real_gdp.csv contains annual US Real GDP (in trillions of dollars) from 1970 to 2024.
```

### Q1.1: `What is the data structure of this dataset?`

```
( ) Cross-sectional — many entities at one point in time
(x) Timeseries — one entity observed over many time periods
( ) Panel — many entities observed over many time periods
( ) Categorical — the values are labels rather than numbers
```

### Q1.2: `Create a line graph of US Real GDP over time. Roughly what are the first and last values?`

```
( ) About 1 trillion in 1970 and about 5 trillion in 2024
(x) About 5 trillion in 1970 and about 23 trillion in 2024
( ) About 23 trillion in 1970 and about 5 trillion in 2024
( ) About 10 trillion in every year
```

### Q1.3: `Describe the overall trend. Are there any periods where the trend changes noticeably?`

```
Select all that apply.
[x] The overall trend is upward.
[x] There are visible dips around 2008-2009 and 2020.
[x] Growth resumes after each dip.
[ ] The overall trend is downward.
[ ] The series is flat until 2000 and then jumps.
```

## Q2: `US Economic Growth Rates`

```
Use the same us_real_gdp.csv dataset to create a new column with the annual growth rate of Real GDP: this year's GDP minus last year's, divided by last year's. (Hint: gdp['Real_GDP'].pct_change())
```

### Q2.1: `Create a line graph of the growth rate over time. How does it differ from the line graph of GDP itself?`

```
(x) The growth rate bounces around a level near 3% with no upward trend, and dips below zero in a few years
( ) The growth rate rises steadily just like GDP does
( ) The growth rate is always negative
( ) The two graphs look identical
```

### Q2.2: `In which years did the US economy shrink (negative growth)?`

```
Select every year with negative growth.
[x] 1974
[x] 1975
[x] 1980
[x] 1982
[x] 1991
[ ] 2001
[ ] 2008
[x] 2009
[x] 2020
```

### Q2.3: `What is the average growth rate over this period?`

```
( ) About 0.5% per year
(x) About 2.8% per year
( ) About 7% per year
( ) About 23% per year
```

## Q3: `Seasonal Patterns in Coffee Prices`

```
The dataset Monthly_Coffee_Prices_dated.csv contains monthly coffee prices from 1973 to 2024, with a column for the month.
```

### Q3.1: `Create a multi-boxplot of coffee prices grouped by month. What does each box represent?`

```
(x) The distribution of prices in that calendar month across all years in the data
( ) The price in that month of a single year
( ) The average price for each year
( ) The change in price from the previous month
```

### Q3.2: `Which month has the highest median price?`

```
( ) January
( ) April
(x) May
( ) November
```

### Q3.3: `Which month shows the most price variability (largest range)?`

```
(x) April
( ) May
( ) November
( ) December
```

### Q3.4: `Based on your multi-boxplot, is there a clear seasonal pattern in coffee prices?`

```
( ) Yes — summer months are consistently far more expensive than winter months
(x) No — the medians and spreads are similar across months, so month-to-month differences are small compared with year-to-year swings
( ) Yes — prices are only ever high in December
( ) The boxplot cannot say anything about seasonality
```

## Q4: `Choosing the Right Visualization`

```
You've now created line graphs (Q1-Q2) and a multi-boxplot (Q3).
```

### Q4.1: `If you wanted to know whether coffee prices are higher today than in 2000, which visualization would you use?`

```
(x) A line graph of price over time
( ) A multi-boxplot grouped by month
( ) A histogram of prices
( ) A bar chart of months
```

### Q4.2: `If you wanted to know whether coffee prices tend to be higher in certain months, which visualization would you use?`

```
( ) A line graph of price over time
(x) A multi-boxplot grouped by month
( ) A histogram of prices
( ) A pie chart of months
```
