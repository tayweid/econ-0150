# ECON 0150 | Homework 2.3 {++Solutions++}

*Due: Friday, Oct. 9 at 5PM*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Submit your figures and answers to Gradescope.

### Q1. Explore the Data

The dataset `amazon_book_sales.csv` lists Amazon's 50 bestselling books each year from 2009 to 2022. Prices are in US dollars, rounded to the nearest dollar. The column `Genre` marks each book as Fiction or Non Fiction.

a) How many unique books are in the dataset? *(hint: use `.unique()` to count a book only once even if it shows up in multiple years)*

There are 441 unique books. The dataset has 700 rows because many books appear in more than one year.

b) How many books made the bestseller list in more than one year? *(hint: `.value_counts()` counts how many times each `Name` appears)*

122 books made the list in more than one year. The most frequent repeats (10 years each) are the *Publication Manual of the American Psychological Association* and *The Very Hungry Caterpillar*.

### Q2. Price and Ratings by Genre

a) Create a scatterplot of `Price` (x-axis) vs `User Rating` (y-axis), colored by `Genre`.

![](i/hw_2_3_sols_01.png)

b) Is the relationship between price and rating positive, negative, or unclear?

Weakly negative. Higher-priced books tend to have slightly lower ratings, but the pattern is faint (correlation about −0.15) and most books cluster below $25.

c) Does the relationship look different for Fiction and Non Fiction?

No. The relationship looks about the same in both genres: Fiction and Non Fiction each have a weak negative relationship (correlation about −0.15 in each).

### Q3. Reviews and Ratings

a) Create a scatterplot of `Reviews` (x-axis) vs `User Rating` (y-axis) for all books.

![](i/hw_2_3_sols_02.png)

b) Is there a relationship between reviews and ratings? If so, is it positive, negative, or unclear?

There is at most a weak positive relationship (correlation about 0.08). It is hard to see because `Reviews` is heavily right-skewed, which squeezes most books into the left side of the plot.

c) How might you use a transformation to improve this figure?

Take the log of `Reviews`. A log transformation spreads out the many books with few reviews and pulls in the handful with very many, so the relationship is easier to see.

### Q4. Does the Relationship Differ by Genre?

a) Create a scatterplot of `Reviews` vs `User Rating`, colored by `Genre`. Use any transformation you suggested in Q3.c).

![](i/hw_2_3_sols_03.png)

b) Does the relationship between reviews and ratings differ between Fiction and Non Fiction? Describe the pattern.

Yes. For Non Fiction there is a clear positive relationship: books with more reviews tend to have higher ratings (correlation about 0.38). For Fiction there is essentially no relationship (correlation about −0.06): heavily reviewed novels are rated about the same as lightly reviewed ones. Fiction books also tend to have more reviews (median about 14,400 vs 7,900).

c) In one sentence, what hypothesis might explain the difference you observe?

Non Fiction readers may review a book mainly when it delivers on what it promised, so well-reviewed books are also well-liked, while popular novels draw many casual readers whose ratings vary regardless of how many reviews pile up.
