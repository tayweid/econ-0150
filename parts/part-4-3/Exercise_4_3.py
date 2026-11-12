# %% [markdown]
# # Exercise 4.3 | Model Assumptions
#
# Our test results are only valid when the model assumptions are valid. We'll diagnose the happiness and GDP model from Exercise 4.1 by checking each assumption with the model's **residuals** and **predictions**:
#
# 1. **Linearity**: the relationship between $x$ and $y$ is linear
# 2. **Homoskedasticity**: equal error variance across all values of $x$
# 3. **Independence**: observations are independent from each other
# 4. **Normality**: errors are normally distributed
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
data = pd.read_csv(file_path + 'Life_Evaluation_GDP_PerCap.csv')
# Log10 of GDP per capita
data['log_GDP_PerCap'] = np.log10(data['GDP_Per_Cap'])
# Keep 2024
data = data[data['Year'] == 2024]
# Display header
data.head()

# %% [markdown]
# ## General Linear Model

# %% [markdown]
# **Question 1.** Fit the model from Exercise 4.1 and print the coefficient table.
#
# $$LifeEvaluation_i = \beta_0 + \beta_1 \cdot logGDP_i + \epsilon_i$$
#
# *Hint: save `smf.ols('Life_Evaluation ~ log_GDP_PerCap', data=data).fit()` as `model`, then use `print(model.summary().tables[1])`.*

# %%
# ...

# %% [markdown]
# ## Residuals

# %% [markdown]
# **Question 2.** Calculate the model's residuals and predictions.
#
# *Hint: save `model.resid` as `residuals` and `model.predict()` as `predictions`.*

# %%
# ...

# %% [markdown]
# ## Assumptions 1 and 2: Residual Plot

# %% [markdown]
# **Question 3.** Make a residual plot: predictions against residuals. Is there a curve in the residuals (linearity)? Is their spread about the same everywhere (homoskedasticity)?
#
# *Hint: `plt.scatter(predictions, residuals)`.*

# %%
# ...

# %% [markdown]
#

# %% [markdown]
# ## Assumption 3: Lagged Residual Plot

# %% [markdown]
# **Question 4.** Make a lagged residual plot: each residual against the residual of the row before it. Do you see a pattern?
#
# *Hint: save `residuals[:-1]` as `lagged_residuals` and `residuals[1:]` as `current_residuals`, then use `plt.scatter(lagged_residuals, current_residuals)`.*

# %%
# ...

# %% [markdown]
#

# %% [markdown]
# ## Assumption 4: Normality of Residuals

# %% [markdown]
# **Question 5.** Make a histogram of the residuals. Are they roughly normally distributed?
#
# *Hint: `sns.histplot(residuals, kde=True)`.*

# %%
# ...

# %% [markdown]
#
