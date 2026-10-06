# Exercise 2.3 | Gradescope

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

## Q1: `Has county-level voting changed?`

```
Work through the questions in the Exercise 2.3 notebook first, building each figure, then enter your answers here. The notebook merges Elections_By_County.csv (Democratic share of the two-party vote and total votes for each county) with Income_By_County.csv (median household income), then reshapes the 2000 and 2024 vote shares into one dem_share column with a Year column.
```

### Q1.1: `Create a boxplot comparing Democratic vote share in 2000 vs 2024. Upload your figure.`

```
|files|
```

### Q1.2: `How did the typical county's Democratic vote share change from 2000 to 2024?`

```
( ) It rose
(x) It fell
( ) It stayed about the same
```

## Q2: `Do large counties vote differently?`

```
Use the merged data from the notebook.
```

### Q2.1: `Create a scatter plot of county size (total_votes_2024) vs Democratic share (dem_share_2024). Upload your figure.`

```
|files|
```

### Q2.2: `How does county size relate to Democratic share in 2024?`

```
(x) Larger counties tend to vote more Democratic
( ) Larger counties tend to vote less Democratic
( ) There is no relationship
```

### Q2.3: `What would make this figure easier to read?`

```
(x) Put total_votes_2024 on a log scale, since a few very large counties squeeze the rest against the left edge
( ) Put dem_share_2024 on a log scale
( ) Drop the counties with fewer than 10,000 votes
```

## Q3: `Is this related to income?`

```
Use the merged data from the notebook.
```

### Q3.1: `Create a scatter plot of income vs Democratic share (dem_share_2024). Upload your figure.`

```
|files|
```

### Q3.2: `How does county income relate to Democratic share in 2024?`

```
(x) Weakly positive: higher-income counties tend to vote somewhat more Democratic
( ) Strongly positive: nearly every high-income county votes Democratic
( ) Negative: higher-income counties tend to vote less Democratic
( ) No relationship
```

## Q4: `Has the relationship changed?`

```
Use data_long with hue='Year' in sns.lmplot().
```

### Q4.1: `Create a scatter plot of income vs Democratic share, colored by year (2000 vs 2024). Upload your figure.`

```
|files|
```

### Q4.2: `How has the relationship between income and Democratic share changed from 2000 to 2024?`

```
(x) In 2000 the line was nearly flat; by 2024 it slopes upward, so richer counties became relatively more Democratic
( ) In 2000 the line sloped upward; by 2024 it is nearly flat
( ) Both years show the same upward slope
( ) Both years show the same downward slope
```

## Answer check

Computed from the notebook's merge of `data/Elections_By_County.csv` and `data/Income_By_County.csv` (3,108 counties; 3 missing 2000 shares and 10 missing 2024 shares, which seaborn drops). Median Democratic two-party share: 0.41 in 2000 and 0.30 in 2024, and the 2024 interquartile range is wider (0.20 to 0.43 vs 0.33 to 0.49). County size vs 2024 share: r = 0.28 raw and 0.47 with log total votes. Income vs share: r = −0.06 in 2000 (slope −0.004 per $10k) and r = 0.24 in 2024 (slope +0.025 per $10k).

Data caveat: `Elections_By_County.csv` was built from the MIT returns without summing across vote modes, so the 2020 and 2024 columns are wrong for about 620 to 750 counties in states that report by mode (IA, TX, NC, OK, AR, PA, LA, SC, NM, AZ), and `total_votes_2024` is wrong for about 800. 2000 to 2016 are correct. With corrected data, every keyed answer above is unchanged and the relationships get stronger: median 2024 share 0.29, log size r = 0.55, 2024 income r = 0.30.
