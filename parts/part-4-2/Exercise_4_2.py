# %% [markdown]
# # Exercise 4.2 | Categorical Predictors
#
# Do individuals in households earning under $35,000 report more poor mental health days? We'll use the 2011 Behavioral Risk Factor Surveillance System (BRFSS) data to fit a bivariate GLM with a binary predictor.
#
# The outcome is **MENTHLTH**, the number of days in the past 30 days when mental health was not good. The predictor is **low_income**: 1 for annual household income below $35,000, and 0 for $35,000 or more. Complete the notebook, then enter your answers in Gradescope.

# %%
# Imports
import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt

# File Path
file_path = 'https://econ-0150.tayweid.io/data/' 

# %% [markdown]
# The cleaned dataset uses income categories 1–8. Categories 1–5 represent household income below $35,000; categories 6–8 represent $35,000 or more. Drop missing income and mental-health responses **before** creating the indicator so that missing income is not classified as higher income.
#
# For this exercise, we fit an unweighted model to these observations. We do not use the BRFSS survey weights or survey design to estimate population-wide effects.

# %%
# Load BRFSS data and keep complete responses
data = pd.read_csv(file_path + 'BRFSS_cleaned.csv')
data = data[['INCOME2', 'MENTHLTH']].dropna().copy()

# Create binary indicator: household income below $35,000
data['low_income'] = (data['INCOME2'] <= 5).astype(int)
data.head()

# %% [markdown]
# ## Explore the Data

# %% [markdown]
# **Question 1.** Make a box plot of `MENTHLTH` for each income group. Which group appears to report more poor mental health days? Describe the shape of the distributions.
#
# *Hint: `sns.boxplot(data=data, x='low_income', y='MENTHLTH')`. Remember that 0 is $35,000 or more and 1 is below $35,000.*

# %%
# ...

# %% [markdown]
# **Question 2.** Calculate the number of observations and the mean of `MENTHLTH` in each group. What is the difference in means (below $35,000 minus $35,000 or more)?
#
# *Hint: `data.groupby('low_income')['MENTHLTH'].agg(['count', 'mean'])`.*

# %%
# ...

# %% [markdown]
# ## Fitting the Model
#
# We fit the bivariate GLM:
#
# $$MentalHealthDays_i = \beta_0 + \beta_1 \cdot LowIncome_i + \epsilon_i$$
#
# When the predictor is binary, the fitted values are the two group means. The reference group (`low_income = 0`) is households earning $35,000 or more.

# %% [markdown]
# **Question 3.** Fit the model and print the coefficient table.
#
# *Hint: save `smf.ols('MENTHLTH ~ low_income', data=data).fit()` as `model`, then use `print(model.summary().tables[1])`.*

# %%
# ...

# %% [markdown]
# **Question 4.** Report the estimated intercept ($\hat{\beta}_0$) and slope ($\hat{\beta}_1$). Compare the intercept to the reference-group mean and the slope to the difference in means from Question 2. What do you notice?

# %% [markdown]
#

# %% [markdown]
# ## Predictions

# %% [markdown]
# **Question 5.** Use the estimated coefficients to predict poor mental health days for each income group. How do these predictions compare with the group means?
#
# *Hint: use `model.params['Intercept']` for the reference group and add `model.params['low_income']` for the lower-income group.*

# %%
# ...

# %% [markdown]
# ## Interpretation

# %% [markdown]
# **Question 6.** What is the p-value on `low_income`? State the null hypothesis in terms of the two population means. Would you reject it at the 5% significance level under this model's assumptions?

# %% [markdown]
#

# %% [markdown]
# **Question 7.** Interpret the intercept and slope in context, including the units (days out of the past 30 days). Does this observational comparison establish that lower income causes worse mental health? Explain.

# %% [markdown]
#

# %% [markdown]
# ## Looking Ahead: Residuals
#
# **Question 8.** Plot residuals against fitted values. Why are there only two fitted values? Do the groups appear to have the same residual spread? We'll examine model diagnostics and their implications for inference in Exercise 4.3.
#
# *Hint: `sns.scatterplot(x=model.fittedvalues, y=model.resid, alpha=0.05)` and `plt.axhline(0, color='black', linestyle='--')`.*

# %%
# ...
