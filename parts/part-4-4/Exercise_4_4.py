# %% [markdown]
# # Exercise 4.4 | The Problem of Timeseries
#
# **Okun's Law**: when unemployment rises, GDP tends to fall. We'll estimate this relationship with four different models, checking each one for autocorrelation: residuals that are related to the residual of the period before.
#
# The data are quarterly observations for the United States from 1948 through 2019. The outcome is **gdp**, real GDP in billions of dollars, and the predictor is **unemployment**, the unemployment rate in percentage points. Complete the notebook, then enter your answers in Gradescope.

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
# The rows are in time order, one per quarter. We keep the date, GDP, and the unemployment rate, and build every other variable ourselves.

# %%
# Load Data
data = pd.read_csv(file_path + 'okun.csv', index_col=0)
# Keep the date and the two series
data = data[['observation_date', 'gdp', 'unemployment']]
# Display header
data.head()

# %% [markdown]
# ## Explore the Data

# %% [markdown]
# **Question 1.** Plot `gdp` over time and `unemployment` over time. How does each series move over these seven decades?
#
# *Hint: `data['gdp'].plot()` in one cell and `data['unemployment'].plot()` in another. The x-axis is the row number, which counts quarters.*

# %%
# ...

# %%
# ...

# %% [markdown]
# ## Model 1 | Levels
#
# The standard approach puts the two series straight into the model:
#
# $$GDP_t = \beta_0 + \beta_1 \cdot Unemployment_t + \epsilon_t$$

# %% [markdown]
# **Question 2.** Fit the levels model and print the coefficient table. What is the estimated slope? Does its sign agree with Okun's Law?
#
# *Hint: save `smf.ols('gdp ~ unemployment', data=data).fit()` as `model1`, then use `print(model1.summary().tables[1])`.*

# %%
# ...

# %% [markdown]
# **Question 3.** Make a residual plot and a lagged residual plot for `model1`. Then calculate the correlation between each residual and the residual of the quarter before. What do the plots and the correlation tell you about this model?
#
# *Hint: the residual plot is `plt.scatter(model1.predict(), model1.resid)`. For the lag plot, save `model1.resid.values[:-1]` as `lagged_residuals` and `model1.resid.values[1:]` as `current_residuals`, then use `plt.scatter(lagged_residuals, current_residuals)`. The correlation is `np.corrcoef(lagged_residuals, current_residuals)[0, 1]`.*

# %%
# ...

# %%
# ...

# %% [markdown]
# ## Model 2 | First Differences (Y)
#
# We can reduce autocorrelation by modeling the *change* in GDP from one quarter to the next instead of its level:
#
# $$\Delta GDP_t = GDP_t - GDP_{t-1}$$

# %%
# Create first differences of Y
data['gdp_diff'] = data['gdp'].diff()
data = data.dropna()

# %% [markdown]
# **Question 4.** Fit the model `gdp_diff ~ unemployment` and save it as `model2`. Make the lagged residual plot and calculate the lagged residual correlation as in Question 3. How does the correlation compare with Model 1?

# %%
# ...

# %%
# ...

# %% [markdown]
# ## Model 3 | First Differences (X, Y)
#
# Model 2 compares the *change* in GDP with the *level* of unemployment. Okun's Law is about changes in both:
#
# $$\Delta GDP_t = \beta_0 + \beta_1 \cdot \Delta Unemployment_t + \epsilon_t$$

# %%
# Create first differences of X
data['unemployment_diff'] = data['unemployment'].diff()
data = data.dropna()

# %% [markdown]
# **Question 5.** Fit the model `gdp_diff ~ unemployment_diff` and save it as `model3`. Calculate the lagged residual correlation. What are the estimated intercept and slope? Interpret each one in context. Does the sign of the slope agree with Okun's Law now?

# %%
# ...

# %%
# ...

# %% [markdown]
# ## Model 4 | Growth Rates
#
# GDP grows exponentially, so a \$65 billion change means something very different in 1950 than in 2019. Growth rates put every quarter on the same scale:
#
# $$g_{GDP,t} = \beta_0 + \beta_1 \cdot g_{Unemployment,t} + \epsilon_t$$

# %%
# Calculate growth rates (0.01 is growth of 1 percent)
data['gdp_growth'] = data['gdp'].pct_change()
data['unemployment_growth'] = data['unemployment'].pct_change()
data = data.dropna()

# %% [markdown]
# **Question 6.** Fit the model `gdp_growth ~ unemployment_growth` and save it as `model4`. Calculate the lagged residual correlation. What does the intercept say about GDP growth in a quarter when the unemployment rate does not change?

# %%
# ...

# %%
# ...

# %% [markdown]
# ## Comparing the Models

# %% [markdown]
# **Question 7.** Compare the lagged residual correlations from the four models. Which model has the least autocorrelation? Did differencing or growth rates eliminate it?

# %% [markdown]
#

# %% [markdown]
# **Question 8.** Plot Okun's Law: make a scatter plot with `unemployment_diff` on the x-axis and `gdp_growth` on the y-axis, with the regression line overlaid. Describe the relationship in one sentence.
#
# *Hint: `sns.regplot(data=data, x='unemployment_diff', y='gdp_growth', ci=None)`.*

# %%
# ...
