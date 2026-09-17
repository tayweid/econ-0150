# Homework 1.2 | Gradescope

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

## Q1: `Histograms, Means, and Standard Deviations`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

Lets continue using the class survey dataset to understand who is in our class! Use it to create a histogram of "Approximately how many miles away from Pittsburgh is your hometown?"
```

### Q1.1: `Create a histogram with bins of width 100 miles. Which bin holds the most students?`

```
(x) 0 - 100 miles
( ) 100 - 200 miles
( ) 200 - 300 miles
( ) 850 - 950 miles
```

### Q1.2: `Create a histogram with bins of width 500 miles. How many students fall in the first bar, 0 - 500 miles?`

```
( ) 17
( ) 30
(x) 41
( ) 50
```

### Q1.3: `Which bin width better shows the distribution?`

```
There is no single right answer here — select the statements that correctly describe what your two figures show.
[x] The 100-mile bins reveal how tightly the class clusters near Pittsburgh.
[x] The 500-mile bins put most of the class in a single bar, hiding that detail.
[x] Both figures show a long right tail of students far from Pittsburgh.
[ ] The 500-mile bins reveal a second cluster the 100-mile bins hide.
[ ] The two bin widths give the same shape.
```

### Q1.4: `Calculate the mean distance from Pittsburgh.`

```
( ) 250 miles
( ) 660 miles
(x) 925 miles
( ) 2327 miles
```

### Q1.5: `Calculate the standard deviation of distance from Pittsburgh.`

```
( ) 250 miles
( ) 925 miles
( ) 1664 miles
(x) 2327 miles
```

### Q1.6: `Which interpretation uses both values correctly?`

```
(x) The average student is about 925 miles from Pittsburgh; distances typically vary by about 2327 miles from that average.
( ) The average student is about 2327 miles from Pittsburgh; distances typically vary by about 925 miles from that average.
( ) Half of students live within 925 miles of Pittsburgh, and half live farther than 2327 miles.
( ) Every student lives between 925 and 2327 miles from Pittsburgh.
```

## Q2: `Boxplots and Quartiles`

```
Use the class survey dataset to create a boxplot with a stripplot of "Approximately how many miles away from Pittsburgh is your hometown?"
```

### Q2.1: `Create a boxplot with stripplot. Where does the box itself sit?`

```
(x) Between about 21 and 350 miles, well to the left of the far points
( ) Centered on the mean, at about 925 miles
( ) Spanning the full range from 0 to 12000 miles
( ) Between about 900 and 1000 miles
```

### Q2.2: `What is the median distance from Pittsburgh?`

```
( ) 21 miles
(x) 250 miles
( ) 350 miles
( ) 925 miles
```

### Q2.3: `Explain why the mean and the median differ.`

```
Select all that apply.
[x] The distribution is right-skewed.
[x] A handful of students live very far away — five are more than 2000 miles out, one is 12000.
[x] Those few large values pull the mean up, while the median only depends on the middle position.
[ ] The mean was computed on a different set of students than the median.
[ ] The median is always smaller than the mean for any dataset.
```

## Q3: `Choosing the Right Tool`

```
Use the class survey dataset to visualize "When is your birthyear?"
```

### Q3.1: `Create a histogram of birthyear. Which birthyear is most common?`

```
Set aside any implausible responses.
( ) 2004
(x) 2005
( ) 2006
( ) 2007
```

### Q3.2: `Create a boxplot with stripplot of birthyear. What does it show is wrong with the data?`

```
(x) Two responses give a birthyear of 2026, which is a typo rather than a real value
( ) Every birthyear is missing for students who live outside Pennsylvania
( ) Birthyear was recorded as text rather than as a number
( ) Two students share the same birthday
```

### Q3.3: `Given the number of students in our class, which visualization better shows the distribution?`

```
Select the statements about your two figures that are true.
[x] Birthyear takes only a handful of distinct values, so the stripplot piles points on top of each other.
[x] The histogram shows the shape more clearly — most of the class was born in 2005 or 2006.
[x] The boxplot is what makes the two bad values obvious.
[ ] The boxplot shows the shape of the distribution better than the histogram does.
[ ] Neither figure can show the two bad values.
```

## Q4: `Interpreting Histograms`

```
The following data from the Better Life Index was collected from OECD countries using time-use surveys. This question is aimed at practicing the skill of analyzing continuous variables displayed visually.

![Better Life Index: minutes of leisure and personal care per day, OECD countries](https://econ-0150.tayweid.io/parts/part-1-2/i/hw_01.png)
```

### Q4.1: `What is the most common 50 minute range of time spent on leisure?`

```
( ) 750 - 800
( ) 800 - 850
(x) 850 - 900
( ) 900 - 950
( ) 950 - 1000
```

### Q4.2: `In how many countries do people spend between 800 and 850 minutes on leisure and personal care?`

```
( ) 2
(x) 3
( ) 5
( ) 18
```

### Q4.3: `How many countries spend more than 900 minutes on leisure and personal care?`

```
( ) 4
( ) 11
(x) 15
( ) 18
```

### Q4.4: `What is the approximate difference in counts between the two most common ranges?`

```
( ) 0 - 2 countries
( ) 3 - 5 countries
(x) 6 - 8 countries
( ) 9 - 11 countries
```
