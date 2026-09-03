# Gradescope build sheet — HW 1.1

Instructor-facing. The homework file is free response worked in the notebook; this sheet is the selection form students submit. It mirrors the Online Assignment editor's structure: each `## Question N` is a parent question — put its title in the title field and paste its **Description** block into the Description box. Each `### Question N.M` under it is a sub-question — put its title in the sub-question's title field and paste its block into the **Problem** box. Parent points are the sum of their sub-questions. Gradescope parses the typed syntax directly: consecutive `( )` lines become a multiple-choice field and consecutive `[ ]` lines a select-all field, with `(x)`/`[x]` marked correct.

**Assignment settings:** Online Assignment · name: `HW 1.1` · due Friday, Sept. 4, 5:00 PM. 5 parent questions, 16 sub-questions at 1 pt each. Select-all fields keep default (strict) scoring — completion-graded anyway.

Answer check, from `Survey_26F.csv` (50 students, 13 columns): `Entry` is the index, leaving 12 meaningful variables. 37 students feel confident in Excel (13 do not). 23 of the 50 are economics majors, so 27 are not. Q1.3 and Q3 answers follow `Homework_1_1_sols.ipynb`.

---

## Question 1 — title: `Data Selection` · 3 pts

Description:

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

Lets use the class survey dataset to understand who is in our class!
```

### Question 1.1 — title: `Who collected this data?` · 1 pt

```
(x) Taylor, in class
( ) Pitt's Office of Institutional Research
( ) The U.S. Census Bureau
( ) A national survey of college students
```

### Question 1.2 — title: `How was this data collected?` · 1 pt

```
(x) With an online survey form filled out in class
( ) From registrar records
( ) By randomly sampling Pitt undergraduates
( ) By scraping public social media profiles
```

### Question 1.3 — title: `What does this data miss?` · 1 pt

```
Select all that apply.
[x] Students who were absent or chose not to respond
[x] Students in the other sections of ECON 0150
[x] Anything about prior coursework or programming experience
[ ] The major of each student who responded
[ ] The favorite color of each student who responded
```

---

## Question 2 — title: `Data Diagram` · 3 pts

Description:

```
Diagram the class survey dataset before summarizing any of it.
```

### Question 2.1 — title: `What is the index variable?` · 1 pt

```
(x) Entry — each row is one student's set of responses
( ) When is your birthday?
( ) What is your (primary) major?
( ) The dataset has no index variable
```

### Question 2.2 — title: `What is the data structure?` · 1 pt

```
(x) Cross-sectional
( ) Timeseries
( ) Panel, long format
( ) Panel, wide format
```

### Question 2.3 — title: `How many (meaningful) variables does the dataset contain?` · 1 pt

```
( ) 13
(x) 12
( ) 11
( ) 50
```

---

## Question 3 — title: `Variable Types` · 6 pts

Description:

```
What is each of the following variable's type? Choose from: Binary Categorical, Nominal Categorical, Ordinal Categorical, Discrete Numerical, Continuous Numerical.
```

### Question 3.1 — title: `"What is your favorite color?"` · 1 pt

```
( ) Binary Categorical
(x) Nominal Categorical
( ) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

### Question 3.2 — title: `"Approximately how many miles away from Pittsburgh is your hometown?"` · 1 pt

```
( ) Binary Categorical
( ) Nominal Categorical
( ) Ordinal Categorical
( ) Discrete Numerical
(x) Continuous Numerical
```

### Question 3.3 — title: `"What is your (primary) major?"` · 1 pt

```
( ) Binary Categorical
(x) Nominal Categorical
( ) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

### Question 3.4 — title: `"How much did you like your statistics class?"` · 1 pt

```
( ) Binary Categorical
( ) Nominal Categorical
(x) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

### Question 3.5 — title: `"How excited are you for this class?"` · 1 pt

```
( ) Binary Categorical
( ) Nominal Categorical
(x) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

### Question 3.6 — title: `"Do you feel confident in Excel?"` · 1 pt

```
(x) Binary Categorical
( ) Nominal Categorical
( ) Ordinal Categorical
( ) Discrete Numerical
( ) Continuous Numerical
```

---

## Question 4 — title: `Summarize 'Do you feel confident in Excel?'` · 2 pts

Description:

```
Summarize the variable 'Do you feel confident in Excel?'. Build the figure in your notebook first, then answer.
```

### Question 4.1 — title: `Which visualization is appropriate for this variable?` · 1 pt

```
(x) A bar chart of the two response counts
( ) A histogram of the responses
( ) A boxplot with a stripplot
( ) A line plot of the responses over time
```

### Question 4.2 — title: `How many students in the class feel confident in Excel?` · 1 pt

```
( ) 13
( ) 27
(x) 37
( ) 50
```

---

## Question 5 — title: `Summarize 'What is your major?'` · 2 pts

Description:

```
Summarize the variable 'What is your (primary) major?'. Build the figure in your notebook first, then answer.
```

### Question 5.1 — title: `This variable has many more categories. Which visualization handles that best?` · 1 pt

```
(x) A bar chart drawn horizontally, so the major labels stay readable
( ) A vertical bar chart with the major labels overlapping
( ) A pie chart with one slice per major
( ) A histogram of majors
```

### Question 5.2 — title: `How many students in the dataset are not economics majors?` · 1 pt

```
( ) 13
( ) 23
(x) 27
( ) 37
```
