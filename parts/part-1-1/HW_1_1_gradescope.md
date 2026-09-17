# Homework 1.1 | Gradescope

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

## Q1: `Data Selection`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

Lets use the class survey dataset to understand who is in our class!
```

### Q1.1: `Who collected this data?`

```
(x) Taylor, in class
( ) Pitt's Office of Institutional Research
( ) The U.S. Census Bureau
( ) A national survey of college students
```

### Q1.2: `How was this data collected?`

```
(x) With an online survey form filled out in class
( ) From registrar records
( ) By randomly sampling Pitt undergraduates
( ) By scraping public social media profiles
```

### Q1.3: `What does this data miss?`

```
Select all that apply.
[x] Students who were absent or chose not to respond
[x] Students in the other sections of ECON 0150
[x] Anything about prior coursework or programming experience
[ ] The major of each student who responded
[ ] The favorite color of each student who responded
```

## Q2: `Data Diagram`

```
Diagram the class survey dataset before summarizing any of it.
```

### Q2.1: `What is the index variable?`

```
(x) Entry — each row is one student's set of responses
( ) When is your birthday?
( ) What is your (primary) major?
( ) The dataset has no index variable
```

### Q2.2: `What is the data structure?`

```
(x) Cross-sectional
( ) Timeseries
( ) Panel, long format
( ) Panel, wide format
```

### Q2.3: `How many (meaningful) variables does the dataset contain?`

```
( ) 13
(x) 12
( ) 11
( ) 50
```

## Q3: `Variable Types`

```
What is each of the following variable's type? Choose from: Binary Categorical, Nominal Categorical, Ordinal Categorical, Discrete Numerical, Continuous Numerical.
```

### Q3.1: `"What is your favorite color?"`

```
( ) Binary Categorical
(x) Nominal Categorical
( ) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

### Q3.2: `"Approximately how many miles away from Pittsburgh is your hometown?"`

```
( ) Binary Categorical
( ) Nominal Categorical
( ) Ordinal Categorical
( ) Discrete Numerical
(x) Continuous Numerical
```

### Q3.3: `"What is your (primary) major?"`

```
( ) Binary Categorical
(x) Nominal Categorical
( ) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

### Q3.4: `"How much did you like your statistics class?"`

```
( ) Binary Categorical
( ) Nominal Categorical
(x) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

### Q3.5: `"How excited are you for this class?"`

```
( ) Binary Categorical
( ) Nominal Categorical
(x) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

### Q3.6: `"Do you feel confident in Excel?"`

```
(x) Binary Categorical
( ) Nominal Categorical
( ) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

## Q4: `Summarize 'Do you feel confident in Excel?'`

```
Summarize the variable 'Do you feel confident in Excel?'. Build the figure in your notebook first, then answer.
```

### Q4.1: `Which visualization is appropriate for this variable?`

```
(x) A bar chart of the two response counts
( ) A histogram of the responses
( ) A boxplot with a stripplot
( ) A line plot of the responses over time
```

### Q4.2: `How many students in the class feel confident in Excel?`

```
( ) 13
( ) 27
(x) 37
( ) 50
```

## Q5: `Summarize 'What is your major?'`

```
Summarize the variable 'What is your (primary) major?'. Build the figure in your notebook first, then answer.
```

### Q5.1: `This variable has many more categories. Which visualization handles that best?`

```
(x) A bar chart drawn horizontally, so the major labels stay readable
( ) A vertical bar chart with the major labels overlapping
( ) A pie chart with one slice per major
( ) A histogram of majors
```

### Q5.2: `How many students in the dataset are not economics majors?`

```
( ) 13
( ) 23
(x) 27
( ) 37
```
