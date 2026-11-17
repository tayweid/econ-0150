# %% [markdown]
# # Exercise 5.1 | Gender Wage Gap
#
# Is there a wage gap between male and female? We'll use the general linear model with a **categorical control** (a "fixed effect") to test for a difference in income by gender, then add education as a control.
#
# The data is a sample of 1,000 people from the 2019 American Community Survey. `INCLOG10` is the log (base 10) of total income, `EDU` is years of education, and `MALE` is 1 for male and 0 for female.
#
# Complete the notebook, then enter your answers in Gradescope.

# %%
# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

# File Path
file_path = 'https://econ-0150.tayweid.io/data/'

# %%
# Load Data
data = pd.read_csv(file_path + 'usa_00041_sample.csv')
# Create a variable: MALE
data['MALE'] = 1 - data['SEX']
# Display header
data.head()

# %% [markdown]
# ## Model 1 | Basic Gender Wage Gap

# %% [markdown]
# **Question 1.** Fit the model with just the male indicator and print the coefficient table. What is the estimated gender wage gap, $\beta_1$?
#
# $$INCLOG10_i = \beta_0 + \beta_1 \cdot MALE_i + \epsilon_i$$
#
# *Hint: save `smf.ols('INCLOG10 ~ MALE', data=data).fit()` as `model1`, then use `print(model1.summary().tables[1])`.*

# %%
# ...

# %% [markdown]
# ## Model 2 | Education + Gender Wage Gap

# %% [markdown]
# **Question 2.** Add education as a control and print the coefficient table. What is the estimated gender wage gap, $\beta_2$, now?
#
# $$INCLOG10_i = \beta_0 + \beta_1 \cdot EDU_i + \beta_2 \cdot MALE_i + \epsilon_i$$
#
# *Hint: save `smf.ols('INCLOG10 ~ EDU + MALE', data=data).fit()` as `model2`, then use `print(model2.summary().tables[1])`.*

# %%
# ...
