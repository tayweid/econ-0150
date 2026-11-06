# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib==3.11.2",
#     "numpy==2.5.3",
#     "pandas==3.1.0",
#     "seaborn==0.13.2",
#     "statsmodels==0.15.0",
# ]
#
# [tool.uv]
# exclude-newer = "2026-11-05T00:00:00Z"
# ///

# %% [markdown]
# # Exercise 4.1 | Numerical Predictors
#
# Are wealthier countries happier? The World Happiness Report asks people in each country to rate their lives on a 0–10 scale. We'll pair those ratings with GDP per capita from the World Bank and fit a bivariate GLM with a numerical predictor:
#
# $$y_i = \beta_0 + \beta_1 x_i + \epsilon_i$$
#
# The outcome ($y$) is **Life Evaluation** (0–10 scale) and the predictor ($x$) is **log10 GDP per capita**. We use the 2024 observations, one per country. Complete the notebook, then enter your answers in Gradescope.

# %%
# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

# File Path
file_path = 'https://econ-0150.tayweid.io/data/'

# %% [markdown]
# The dataset `Life_Evaluation_GDP_PerCap.csv` has one row per country and year, with life evaluation from the Gallup World Poll and GDP per capita from the World Bank. We take the log10 of GDP per capita and keep only 2024. One country is missing GDP per capita in 2024; `statsmodels` drops it automatically when fitting.

# %%
# Load Data
data = pd.read_csv(file_path + 'Life_Evaluation_GDP_PerCap.csv')
# Log10 of GDP per capita
data['log_GDP_PerCap'] = np.log10(data['GDP_Per_Cap'])
# Keep 2024
data = data[data['Year'] == 2024]
# Display header
data.head()

# %% [markdown]
# ## Explore the Data

# %% [markdown]
# **Question 1.** Make a scatter plot with `log_GDP_PerCap` on the x-axis and `Life_Evaluation` on the y-axis. Is there a visible relationship? Which direction does it go?
#
# *Hint: `sns.scatterplot(data=data, x='log_GDP_PerCap', y='Life_Evaluation')`*

# %%
# ...

# %% [markdown]
# ## Fitting the Model
#
# We fit the bivariate GLM:
#
# $$LifeEvaluation_i = \beta_0 + \beta_1 \cdot logGDP_i + \epsilon_i$$
#
# Just like the intercept-only model, the GLM chooses the $\beta_0$ and $\beta_1$ that minimize MSE: the line that is least wrong. In `statsmodels` the model is written `Life_Evaluation ~ log_GDP_PerCap`.

# %% [markdown]
# **Question 2.** Fit the model and print the coefficient table.
#
# *Hint: save `smf.ols('Life_Evaluation ~ log_GDP_PerCap', data=data).fit()` as `model`, then use `print(model.summary().tables[1])`.*

# %%
# ...

# %% [markdown]
# **Question 3.** Visualize the fitted model by making a scatter plot with the regression line overlaid.
#
# *Hint: `sns.regplot(data=data, x='log_GDP_PerCap', y='Life_Evaluation', ci=None)`*

# %%
# ...

# %% [markdown]
# **Question 4.** What is the estimated slope ($\hat{\beta}_1$)? Is it positive or negative?
#
# What is the p-value on the slope, and what null hypothesis does it test?

# %% [markdown]
#

# %% [markdown]
# ## Predictions
#
# Once we have the estimates $\hat{\beta}_0$ and $\hat{\beta}_1$, we can predict life evaluation for any value of log GDP per capita:
#
# $$\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 \cdot x$$

# %% [markdown]
# **Question 5.** Extract the estimated parameters from your model, then predict life evaluation for a country with log10 GDP per capita of 3 (GDP per capita of \$1,000).
#
# *Hint: the estimates are `model.params['Intercept']` and `model.params['log_GDP_PerCap']`.*

# %%
# ...

# %% [markdown]
# **Question 6.** Predict life evaluation for a country with log10 GDP per capita of 4 (GDP per capita of \$10,000). How much higher is this prediction than the one in Question 5? Does the difference make sense given the slope?

# %%
# ...

# %% [markdown]
# ## Interpretation

# %% [markdown]
# **Question 7.** Write a one-sentence interpretation of the slope $\hat{\beta}_1$ in context. Use the format: "For every one-unit increase in [x], [y] increases/decreases by [amount].\"

# %% [markdown]
#

# %% [markdown]
# **Question 8.** What does a one-unit increase in *log10* GDP per capita mean in terms of *actual* GDP per capita?

# %% [markdown]
#
