# %% [markdown]
# # Exercise 4.3 | Model Assumptions
#
# Every model gives us coefficients, standard errors, and p-values. Those numbers are only trustworthy when the model's assumptions hold:
#
# 1. **Linearity**: the relationship between $x$ and $y$ is linear
# 2. **Homoskedasticity**: equal error variance across all values of $x$
# 3. **Independence**: observations are independent from each other
# 4. **Normality**: errors are normally distributed
#
# We check them with two quantities every model produces: the **residuals** ($\hat{\varepsilon}_i = y_i - \hat{y}_i$) and the **predictions** ($\hat{y}_i$). We'll diagnose the happiness and GDP model from Exercise 4.1, then return to the income and mental health model from Exercise 4.2. Complete the notebook, then enter your answers in Gradescope.

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
# As in Exercise 4.1, we use the 2024 observations of `Life_Evaluation_GDP_PerCap.csv`, one row per country. We drop the one country that is missing GDP per capita so that every row has a residual.

# %%
# Load Data
data = pd.read_csv(file_path + 'Life_Evaluation_GDP_PerCap.csv')
# Log10 of GDP per capita
data['log_GDP_PerCap'] = np.log10(data['GDP_Per_Cap'])
# Keep 2024 and drop the country missing GDP per capita
data = data[data['Year'] == 2024].dropna().reset_index(drop=True)
# Display header
data.head()

# %% [markdown]
# ## Assumption 1: Linearity
#
# In Exercise 4.1 we took the log of GDP per capita before fitting. Was that necessary? Start with the model in dollars:
#
# $$LifeEvaluation_i = \beta_0 + \beta_1 \cdot GDP_i + \epsilon_i$$

# %% [markdown]
# **Question 1.** Fit the model in dollars, then make a residual plot: predictions on the x-axis and residuals on the y-axis, with a horizontal line at zero. Do the residuals look like random scatter around zero, or is there a pattern?
#
# *Hint: save `smf.ols('Life_Evaluation ~ GDP_Per_Cap', data=data).fit()` as `model_dollars`. The residuals are `model_dollars.resid` and the predictions are `model_dollars.predict()`. Then use `plt.scatter(predictions, residuals)` and `plt.axhline(0, color='black', linestyle='--')`.*

# %%
# ...

# %% [markdown]
# **Question 2.** Now fit the log model from Exercise 4.1 and make the same residual plot. Did the log transformation fix the pattern from Question 1?
#
# $$LifeEvaluation_i = \beta_0 + \beta_1 \cdot logGDP_i + \epsilon_i$$
#
# *Hint: save `smf.ols('Life_Evaluation ~ log_GDP_PerCap', data=data).fit()` as `model`, then save `model.resid` as `residuals` and `model.predict()` as `predictions`. We use `model`, `residuals`, and `predictions` for the rest of this section.*

# %%
# ...

# %% [markdown]
# **Question 3.** What is the mean of the residuals from the log model? Which country has the most negative residual, and what does a negative residual mean for that country?
#
# *Hint: `residuals.mean()` and `data.loc[residuals.idxmin()]`.*

# %%
# ...

# %% [markdown]
# ## Assumption 2: Homoskedasticity
#
# The spread of the residuals should be about the same across the whole range of predictions. A fan shape in the residual plot means the spread is changing.

# %% [markdown]
# **Question 4.** Look again at your residual plot from Question 2. Is the spread of the residuals the same on the left and the right? Check by calculating the standard deviation of the residuals for the countries with below-median predictions and for the countries with above-median predictions.
#
# *Hint: `low = predictions < np.median(predictions)`, then `residuals[low].std()` and `residuals[~low].std()`.*

# %%
# ...

# %% [markdown]
# **Question 5.** Robust standard errors adjust for a changing spread. Refit the log model with robust standard errors and print the coefficient table. How much does the standard error on the slope change? Does the conclusion about the slope change?
#
# *Hint: `smf.ols('Life_Evaluation ~ log_GDP_PerCap', data=data).fit(cov_type='HC3')`. The coefficients are identical; only the standard errors, test statistics, and p-values change.*

# %%
# ...

# %% [markdown]
# ## Assumption 3: Independence
#
# A lagged residual plot puts each residual against the residual of the row before it. If neighboring rows have similar residuals, the points line up along a diagonal and the observations are not independent.

# %% [markdown]
# **Question 6.** Make a lagged residual plot for the log model. The rows are countries in alphabetical order. Do you see a pattern? Why would we expect a pattern if the rows were the same country in consecutive years instead?
#
# *Hint: `lagged_residuals = residuals[:-1].values` and `current_residuals = residuals[1:].values`, then `plt.scatter(lagged_residuals, current_residuals)`.*

# %%
# ...

# %% [markdown]
# ## Assumption 4: Normality

# %% [markdown]
# **Question 7.** Make a histogram of the residuals from the log model. Is it roughly bell-shaped? With 146 countries, how much should a modest departure from normality worry us?
#
# *Hint: `sns.histplot(residuals, kde=True)`.*

# %%
# ...

# %% [markdown]
# ## A Binary Predictor
#
# At the end of Exercise 4.2 we plotted the residuals from the income and mental health model and saw only two predictions, one per income group. The cell below refits that model.

# %%
# Load BRFSS data and keep complete responses
brfss = pd.read_csv(file_path + 'BRFSS_cleaned.csv')
brfss = brfss[['INCOME2', 'MENTHLTH']].dropna().copy()

# Binary indicator: household income below $35,000
brfss['low_income'] = (brfss['INCOME2'] <= 5).astype(int)

# The model from Exercise 4.2
model_brfss = smf.ols('MENTHLTH ~ low_income', data=brfss).fit()
print(model_brfss.summary().tables[1])

# %% [markdown]
# **Question 8.** Calculate the standard deviation of the residuals in each income group. Which assumption does this model violate? Refit it with robust standard errors and compare the standard error on `low_income`. Does the conclusion change?
#
# *Hint: `model_brfss.resid.groupby(brfss['low_income']).std()`, then refit with `.fit(cov_type='HC3')`.*

# %%
# ...
