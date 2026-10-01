# Homework 2.2 | Gradescope

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

## Q1: `Amazon Book Sales by Genre`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The dataset amazon_book_sales.csv lists Amazon's 50 bestselling books each year from 2009 to 2021 (700 books). The column Genre marks each as Fiction or Non Fiction.
```

### Q1.1: `Create a boxplot showing the distribution of User Rating by Genre. Upload your figure.`

```
|files|
```

### Q1.2: `Add a stripplot on top of your boxplot to see individual books. Upload your figure.`

```
|files|
```

### Q1.3: `Calculate the mean, standard deviation, and count of User Rating by Genre. Round to two decimals.`

```
Mean User Rating for Fiction:
[____](=4.66+-0.01)

Standard deviation of User Rating for Fiction:
[____](=0.25+-0.01)

Number of Fiction books:
[____](=312+-0)

Mean User Rating for Non Fiction:
[____](=4.62+-0.01)

Standard deviation of User Rating for Non Fiction:
[____](=0.19+-0.01)

Number of Non Fiction books:
[____](=388+-0)
```

### Q1.4: `Which genre has the higher average rating?`

```
(x) Fiction
( ) Non Fiction
( ) The two means are identical
```

### Q1.5: `Do the two distributions overlap much?`

```
(x) Yes: the boxes overlap heavily and the stripplot shows books from both genres at nearly every rating level
( ) No: most Fiction books are rated above every Non Fiction book
( ) No: most Non Fiction books are rated above every Fiction book
```

## Q2: `Marriage Rates by Continent`

```
The dataset marriage_rates_by_continent.csv reports the crude marriage rate, marriages per one thousand inhabitants, for 100 countries, one per row.
```

### Q2.1: `Create a boxplot of Marriage_Rate_per_1000 by Continent. Upload your figure.`

```
|files|
```

### Q2.2: `Add a stripplot to see individual countries within each continent. Upload your figure.`

```
|files|
```

### Q2.3: `Calculate the mean, standard deviation, and count by continent. Round to two decimals.`

```
Mean marriage rate in Europe:
[____](=4.67+-0.01)

Standard deviation of marriage rates in Europe:
[____](=1.47+-0.01)

Number of European countries:
[____](=42+-0)

Mean marriage rate in Asia:
[____](=6.06+-0.01)

Standard deviation of marriage rates in Asia:
[____](=2.07+-0.01)

Number of Asian countries:
[____](=23+-0)
```

### Q2.4: `Which continent has the lowest mean marriage rate?`

```
( ) Africa
( ) Asia
( ) Europe
( ) North America
( ) Oceania
(x) South America
```

### Q2.5: `Which continent has the highest standard deviation?`

```
( ) Africa
( ) Asia
( ) Europe
( ) North America
(x) Oceania
( ) South America
```

## Answer check

Computed from `data/amazon_book_sales.csv` (700 books, 312 Fiction and 388 Non Fiction, no missing ratings) and `data/marriage_rates_by_continent.csv` (100 countries, no missing values). Grouped `User Rating`: Fiction mean 4.664, sd 0.252; Non Fiction mean 4.620, sd 0.185. Fiction is higher by about 0.04 and the distributions overlap almost completely, so Q1.5 keys the overlap choice. Grouped `Marriage_Rate_per_1000`: South America 3.88 (sd 1.91, n 10), North America 4.47 (1.86, 13), Europe 4.67 (1.47, 42), Oceania 5.05 (3.17, 4), Asia 6.06 (2.07, 23), Africa 6.31 (2.04, 8). South America has the lowest mean and Oceania the highest standard deviation, though Oceania has only four countries; a student who flags Asia as the most variable among well-sampled continents has a defensible notebook answer, but Q2.5 keys Oceania as the question asks for the highest standard deviation.
