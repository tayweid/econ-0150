# Gradescope build sheet — HW 1.2

Instructor-facing. The homework file is free response worked in the notebook; this sheet is the selection form students submit. It mirrors the Online Assignment editor's structure: each `## Question N` is a parent question — put its title in the title field and paste its **Description** block into the Description box. Each `### Question N.M` under it is a sub-question — put its title in the sub-question's title field and paste its block into the **Problem** box. Parent points are the sum of their sub-questions. Gradescope parses the typed syntax directly: consecutive `( )` lines become a multiple-choice field and consecutive `[ ]` lines a select-all field, with `(x)`/`[x]` marked correct.

**Assignment settings:** Online Assignment · name: `HW 1.2` · due Friday, Sept. 4, 5:00 PM. 4 parent questions, 16 sub-questions at 1 pt each. Select-all fields keep default (strict) scoring — completion-graded anyway. Question 4's Description needs the Better Life Index histogram (`parts/part-1-2/i/hw_01.png`) inserted with **Insert Image**; all four sub-questions read from it.

Answer check, from `Survey_26F.csv` (distance in miles): mean 924.66, standard deviation 2326.71, median 250, quartiles 21.25 and 350; 5 students are more than 2000 miles out and one is 12000. With 100-mile bins the 0-100 bar holds 17 students; with 500-mile bins the 0-500 bar holds 41. Birthyear runs 2002-2007 for 48 students, with 2 typo responses of 2026; 2005 is the most common. Q4 reads off the Better Life Index histogram (`data/HW_01_Q1_Leisure_Time_OECD.csv`, hours converted to minutes, 38 countries): 750-800 has 2, 800-850 has 3, 850-900 has 18, 900-950 has 11, 950-1000 has 4. So the most common range is 850-900, 3 countries are in 800-850, 15 are above 900, and the top two bars differ by 7.

---

## Question 1 — title: `Histograms, Means, and Standard Deviations` · 6 pts

Description:

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

Lets continue using the class survey dataset to understand who is in our class! Use it to create a histogram of "Approximately how many miles away from Pittsburgh is your hometown?"
```

### Question 1.1 — title: `Create a histogram with bins of width 100 miles. Which bin holds the most students?` · 1 pt

```
(x) 0 - 100 miles
( ) 100 - 200 miles
( ) 200 - 300 miles
( ) 850 - 950 miles
```

### Question 1.2 — title: `Create a histogram with bins of width 500 miles. How many students fall in the first bar, 0 - 500 miles?` · 1 pt

```
( ) 17
( ) 30
(x) 41
( ) 50
```

### Question 1.3 — title: `Which bin width better shows the distribution?` · 1 pt

```
There is no single right answer here — select the statements that correctly describe what your two figures show.
[x] The 100-mile bins reveal how tightly the class clusters near Pittsburgh.
[x] The 500-mile bins put most of the class in a single bar, hiding that detail.
[x] Both figures show a long right tail of students far from Pittsburgh.
[ ] The 500-mile bins reveal a second cluster the 100-mile bins hide.
[ ] The two bin widths give the same shape.
```

### Question 1.4 — title: `Calculate the mean distance from Pittsburgh.` · 1 pt

```
( ) 250 miles
( ) 660 miles
(x) 925 miles
( ) 2327 miles
```

### Question 1.5 — title: `Calculate the standard deviation of distance from Pittsburgh.` · 1 pt

```
( ) 250 miles
( ) 925 miles
( ) 1664 miles
(x) 2327 miles
```

### Question 1.6 — title: `Which interpretation uses both values correctly?` · 1 pt

```
(x) The average student is about 925 miles from Pittsburgh; distances typically vary by about 2327 miles from that average.
( ) The average student is about 2327 miles from Pittsburgh; distances typically vary by about 925 miles from that average.
( ) Half of students live within 925 miles of Pittsburgh, and half live farther than 2327 miles.
( ) Every student lives between 925 and 2327 miles from Pittsburgh.
```

---

## Question 2 — title: `Boxplots and Quartiles` · 3 pts

Description:

```
Use the class survey dataset to create a boxplot with a stripplot of "Approximately how many miles away from Pittsburgh is your hometown?"
```

### Question 2.1 — title: `Create a boxplot with stripplot. Where does the box itself sit?` · 1 pt

```
(x) Between about 21 and 350 miles, well to the left of the far points
( ) Centered on the mean, at about 925 miles
( ) Spanning the full range from 0 to 12000 miles
( ) Between about 900 and 1000 miles
```

### Question 2.2 — title: `What is the median distance from Pittsburgh?` · 1 pt

```
( ) 21 miles
(x) 250 miles
( ) 350 miles
( ) 925 miles
```

### Question 2.3 — title: `Explain why the mean and the median differ.` · 1 pt

```
Select all that apply.
[x] The distribution is right-skewed.
[x] A handful of students live very far away — five are more than 2000 miles out, one is 12000.
[x] Those few large values pull the mean up, while the median only depends on the middle position.
[ ] The mean was computed on a different set of students than the median.
[ ] The median is always smaller than the mean for any dataset.
```

---

## Question 3 — title: `Choosing the Right Tool` · 3 pts

Description:

```
Use the class survey dataset to visualize "When is your birthyear?"
```

### Question 3.1 — title: `Create a histogram of birthyear. Which birthyear is most common?` · 1 pt

```
Set aside any implausible responses.
( ) 2004
(x) 2005
( ) 2006
( ) 2007
```

### Question 3.2 — title: `Create a boxplot with stripplot of birthyear. What does it show is wrong with the data?` · 1 pt

```
(x) Two responses give a birthyear of 2026, which is a typo rather than a real value
( ) Every birthyear is missing for students who live outside Pennsylvania
( ) Birthyear was recorded as text rather than as a number
( ) Two students share the same birthday
```

### Question 3.3 — title: `Given the number of students in our class, which visualization better shows the distribution?` · 1 pt

```
Select the statements about your two figures that are true.
[x] Birthyear takes only a handful of distinct values, so the stripplot piles points on top of each other.
[x] The histogram shows the shape more clearly — most of the class was born in 2005 or 2006.
[x] The boxplot is what makes the two bad values obvious.
[ ] The boxplot shows the shape of the distribution better than the histogram does.
[ ] Neither figure can show the two bad values.
```

---

## Question 4 — title: `Interpreting Histograms` · 4 pts

Description:

```
The following data from the Better Life Index was collected from OECD countries using time-use surveys. This question is aimed at practicing the skill of analyzing continuous variables displayed visually.
```

*(Insert `parts/part-1-2/i/hw_01.png` into this Description with **Insert Image**.)*

### Question 4.1 — title: `What is the most common 50 minute range of time spent on leisure?` · 1 pt

```
( ) 750 - 800
( ) 800 - 850
(x) 850 - 900
( ) 900 - 950
( ) 950 - 1000
```

### Question 4.2 — title: `In how many countries do people spend between 800 and 850 minutes on leisure and personal care?` · 1 pt

```
( ) 2
(x) 3
( ) 5
( ) 18
```

### Question 4.3 — title: `How many countries spend more than 900 minutes on leisure and personal care?` · 1 pt

```
( ) 4
( ) 11
(x) 15
( ) 18
```

### Question 4.4 — title: `What is the approximate difference in counts between the two most common ranges?` · 1 pt

```
( ) 0 - 2 countries
( ) 3 - 5 countries
(x) 6 - 8 countries
( ) 9 - 11 countries
```
