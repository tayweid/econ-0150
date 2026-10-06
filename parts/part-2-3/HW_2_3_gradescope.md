# Homework 2.3 | Gradescope

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

## Q1: `Explore the Data`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The dataset amazon_book_sales.csv lists Amazon's 50 bestselling books each year from 2009 to 2022 (700 rows). Prices are in US dollars, rounded to the nearest dollar. The column Genre marks each book as Fiction or Non Fiction.
```

### Q1.1: `How many unique books are in the dataset?`

```
[____](=441+-0)
```

### Q1.2: `How many books made the bestseller list in more than one year?`

```
[____](=122+-0)
```

## Q2: `Price and Ratings by Genre`

```
Use the same amazon_book_sales.csv dataset.
```

### Q2.1: `Create a scatterplot of Price (x-axis) vs User Rating (y-axis), colored by Genre. Upload your figure.`

```
|files|
```

### Q2.2: `Is the relationship between price and rating positive, negative, or unclear?`

```
( ) Strongly positive
( ) Weakly positive
(x) Weakly negative
( ) Strongly negative
```

### Q2.3: `Does the relationship look different for Fiction and Non Fiction?`

```
(x) No: both genres show a similar weak negative relationship
( ) Yes: the relationship is positive for Fiction and negative for Non Fiction
( ) Yes: the relationship is negative for Fiction and positive for Non Fiction
```

## Q3: `Reviews and Ratings`

```
Use the same amazon_book_sales.csv dataset.
```

### Q3.1: `Create a scatterplot of Reviews (x-axis) vs User Rating (y-axis) for all books. Upload your figure.`

```
|files|
```

### Q3.2: `Is there a relationship between reviews and ratings? If so, is it positive, negative, or unclear?`

```
(x) Weakly positive or unclear: most books are squeezed against the left side of the plot
( ) Strongly positive
( ) Strongly negative
```

### Q3.3: `How might you use a transformation to improve this figure?`

```
(x) Take the log of Reviews to spread out the many books with few reviews
( ) Take the log of User Rating to spread out the high ratings
( ) Square Reviews to emphasize the books with the most reviews
```

## Q4: `Does the Relationship Differ by Genre?`

```
Use the same amazon_book_sales.csv dataset.
```

### Q4.1: `Create a scatterplot of Reviews vs User Rating, colored by Genre, using the transformation you suggested in Q3.3. Upload your figure.`

```
|files|
```

### Q4.2: `Does the relationship between reviews and ratings differ between Fiction and Non Fiction?`

```
(x) Yes: Non Fiction shows a positive relationship, while Fiction shows almost no relationship
( ) Yes: Fiction shows a positive relationship, while Non Fiction shows almost no relationship
( ) No: both genres show the same positive relationship
( ) No: neither genre shows any relationship
```

### Q4.3: `In one sentence, what hypothesis might explain the difference you observe?`

```
|____|
```

## Answer check

Computed from `data/amazon_book_sales.csv` (700 rows, 50 per year for 2009 to 2022, 312 Fiction and 388 Non Fiction, no missing values, minimum of 37 reviews so the log is defined). `Name` has 441 unique values, and 122 of them appear in more than one year (the APA *Publication Manual* and *The Very Hungry Caterpillar* appear 10 times each). Price vs User Rating: correlation −0.146 for Fiction and −0.152 for Non Fiction, so Q2.3 keys "no difference." Reviews vs User Rating: correlation 0.080 raw and 0.182 with log Reviews across all books, so Q3.2 keys weak/unclear. With log Reviews by genre: Non Fiction r = 0.375 (slope 0.057 rating points per log unit), Fiction r = −0.056 (slope −0.014), so Q4.2 keys the Non Fiction positive / Fiction flat choice. Fiction books also have more reviews (median 14,439 vs 7,911). The earlier Spring key said both genres were weakly positive; that was wrong.
