# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib==3.11.2",
#     "numpy==2.5.3",
#     "pandas==3.1.0",
#     "scipy==1.18.1",
#     "seaborn==0.13.2",
#     "statsmodels==0.15.0",
# ]
#
# [tool.uv]
# exclude-newer = "2026-10-27T16:34:19Z"
# ///

# %% [markdown]
# # Exercise 3.4 | The Simplest GLM
#
# You have 30 paired observations of wait times at a coffee shop. Each value is the afternoon wait minus the morning wait, measured in minutes. A positive difference means the afternoon wait was longer. Is there a systematic difference, or is it just noise?
#
# For this exercise, treat the pairs as independent observations from a population of comparable visits. Complete the notebook, then enter your answers in Gradescope.

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as smf

# %%
wait_difference = [1.3, 2.4, 2.2, 1.3, 3.0, 2.3, 0.8, 2.7, 2.0, 2.9, 1.7, 1.9, 2.2,
                   2.1, 2.4, 1.7, 1.7, 1.9, 1.7, 2.5, 2.4, 2.2, 1.9, 1.9, 2.7, 1.8,
                   1.8, 2.0, 1.9, 2.1]
data = pd.DataFrame({'wait_difference': wait_difference})

# %% [markdown]
# ## Explore the Data

# %% [markdown]
# **Question 1.** Compute the sample mean and sample standard deviation of the wait time differences, in minutes. Use the sample standard deviation (`ddof=1`).

# %%


# %% [markdown]
# **Question 2.** Make a histogram of the wait time differences. Are the values centered near zero, or somewhere else?

# %%


# %% [markdown]
# ## Choosing the Best Prediction
#
# The simplest model predicts every observation with a single number $b$:
#
# $$\hat{y}_i = b$$
#
# The residual for each observation is $e_i = y_i - b$. We measure the model's total "wrongness" with **Mean Squared Error**:
#
# $$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - b)^2$$
#
# Because the differences are measured in minutes, MSE is measured in squared minutes.

# %% [markdown]
# **Question 3.** Compute the MSE when $b = 2.5$.
#
# *Hint: `np.mean((data['wait_difference'] - b)**2)`*

# %%


# %% [markdown]
# **Question 4.** Compute the MSE when $b = 1.5$.

# %%


# %% [markdown]
# **Question 5.** Compute the MSE when $b = \bar{y}$ (the sample mean). Which of the three values of $b$ gives the smallest MSE?

# %%


# %% [markdown]
# ## Fitting the Model
#
# The intercept-only model is written $y \sim 1$. It finds the value of $b$ that minimizes MSE. We can fit it in Python with `statsmodels`.

# %% [markdown]
# **Question 6.** Fit the intercept-only model and print the coefficient table.
#
# *Hint: save `smf.ols('wait_difference ~ 1', data=data).fit()` as `model`, then use `print(model.summary().tables[1])`.*

# %%


# %% [markdown]
# **Question 7.** Compare the intercept coefficient (`coef`) to the sample mean you calculated in Question 1. What do you notice?
#
# What null hypothesis does the p-value on the intercept test?

# %% [markdown]
#
