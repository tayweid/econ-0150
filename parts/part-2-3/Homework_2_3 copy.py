# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib==3.11.2",
#     "numpy==2.5.3",
#     "pandas==3.0.6",
#     "seaborn==0.13.2",
# ]
#
# [tool.uv]
# exclude-newer = "2026-10-06T16:03:32Z"
# ///

# %% [markdown]
# # Homework 2.3 | Bivariate Relationships by Category
#
# *Homework is designed to both test your knowlege and challenge you to apply familiar concepts to new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Submit your figures and answers to [Gradescope](https://www.gradescope.com).*

# %%
# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# File Path
file_path = 'https://econ-0150.tayweid.io/data/'

# %%
# Load Data
books = pd.read_csv(file_path + 'amazon_book_sales.csv', index_col=0)
books.head()
#->                                                 Name  ... Median_Price
#-> 0  Act Like a Lady, Think Like a Man: What Men Re...  ...         12.0
#-> 1  Arguing with Idiots: How to Stop Small Minds a...  ...         12.0
#-> 2          Breaking Dawn (The Twilight Saga, Book 4)  ...         12.0
#-> 3        Crazy Love: Overwhelmed by a Relentless God  ...         12.0
#-> 4  Dead And Gone: A Sookie Stackhouse Novel (Sook...  ...         12.0
#->
#-> [5 rows x 8 columns]

# %% [markdown]
# ## Q1. Explore the Data
#
# The dataset `amazon_book_sales.csv` contains the 50 bestselling Amazon books each year between 2009 and 2021. Prices are expressed in US dollars and rounded to the nearest dollar.

# %% [markdown]
# a) How many unique books are in the dataset *(hint: use .unique() to count a book only once even if it shows up in multiple years)*?

# %%
len(books)
#-> 700

# %%
len(books.Name.unique())
#-> 441

# %% [markdown]
# b) How many books are Fiction? How many are Non-Fiction? *(hint: use a filter)*

# %%
books[books.

# %% [markdown]
# ## Q2. Ratings by Genre
#
# The column `Genre` describes whether the bestseller is Fiction or Non-Fiction.

# %% [markdown]
# a) Create a boxplot of `User Rating` by `Genre`. Add a stripplot overlay.

# %%
sns.boxplot(books, x='Genre', y='User Rating', whis=(0,100))
sns.stripplot(books, x='Genre', y='User Rating')
#-> <Axes: xlabel='Genre', ylabel='User Rating'>

# %% [markdown]
# b) Calculate the mean and standard deviation of `User Rating` by `Genre`.

# %%
books.groupby('Genre')['User Rating'].mean()
#-> Genre
#-> Fiction        4.664103
#-> Non Fiction    4.620361
#-> Name: User Rating, dtype: float64

# %%
books.groupby('Genre')['User Rating'].std()

# %% [markdown]
# c) Which genre has higher average ratings? Is the difference large or small relative to the variation within each group?

# %% [markdown]

# %% [markdown]
# ## Q3. Reviews and Ratings

# %% [markdown]
# a) Create a scatter plot of `Reviews` (x-axis) vs `User Rating` (y-axis) for all books.

# %%
sns.scatterplot(books, x='Reviews', y='User Rating')

# %% [markdown]
# b) Is there a relationship between reviews and ratings? If so, is it positive, negative, or unclear?

# %% [markdown]

# %% [markdown]
# c) How might you use a transformation to improve this figure?

# %% [markdown]
# Take a log of reviews!

# %% [markdown]
# ## Q4. Does the Relationship Differ by Genre?

# %% [markdown]
# a) Create a scatter plot of `Reviews` vs `User Rating`, colored by `Genre`. Use any transformations you suggested in Q3.c). 

# %%
sns.lmplot(books, x='lnReviews', y='User Rating', hue='Genre')

# %% [markdown]
# b) Does the relationship between reviews and ratings differ between Fiction and Non-Fiction? Describe the pattern you observe.

# %% [markdown]

# %% [markdown]
# c) In one sentence, what might explain any differences you observe?

# %% [markdown]
