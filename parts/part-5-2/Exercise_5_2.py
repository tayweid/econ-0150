# %% [markdown]
# # Exercise 5.2 | Gender Wage Gap
#
# Are the returns to education different between male and female? We'll continue with the data from Exercise 5.1 and use an **interaction** to let the slope on education differ by gender.
#
# The data is a sample of 1,000 people from the 2019 American Community Survey. `LNINC` is the natural log of total income, `EDU` is years of education, and `MALE` is 1 for male and 0 for female. With $\ln(Income)$ as the outcome, we interpret coefficients as percent changes.
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
# Create a variable: LNINC, the natural log of income
data['LNINC'] = np.log(data['INCTOT'])
# Display header
data.head()

# %% [markdown]
# ## Model 3 | Differential Returns to Education

# %% [markdown]
# **Question 1.** Fit the education-gender interaction model and print the coefficient table. What is the additional male return to education, $\beta_2$?
#
# $$LNINC_i = \beta_0 + \beta_1 \cdot EDU_i + \beta_2 \cdot EDU_i \cdot MALE_i + \epsilon_i$$
#
# *Hint: save `smf.ols('LNINC ~ EDU + EDU:MALE', data=data).fit()` as `model3`, then use `print(model3.summary().tables[1])`.*

# %%
# ...

# %% [markdown]
# ## Model 4 | Full Model

# %% [markdown]
# **Question 2.** Fit the full model with both the fixed effect and the interaction, then print the coefficient table. What is the male education return premium, $\beta_3$, now?
#
# $$LNINC_i = \beta_0 + \beta_1 \cdot EDU_i + \beta_2 \cdot MALE_i + \beta_3 \cdot EDU_i \cdot MALE_i + \epsilon_i$$
#
# *Hint: save `smf.ols('LNINC ~ EDU + MALE + EDU:MALE', data=data).fit()` as `model4`, then use `print(model4.summary().tables[1])`.*

# %%
# ...
