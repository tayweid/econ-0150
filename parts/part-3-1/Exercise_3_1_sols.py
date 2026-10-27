# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib==3.11.2",
#     "numpy==2.5.3",
#     "scipy==1.18.1",
#     "seaborn==0.13.2",
# ]
#
# [tool.uv]
# exclude-newer = "2026-10-26T13:43:32Z"
# ///

# %% [markdown]
# # Exercise 3.1 | County A Sleep Times: Known Distribution

# %%
# Imports
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# %% [markdown]
# ## County A Sleep Time Parameters

# %%
mu = 7.2
sigma = 1.5

# %% [markdown]
# ## Q1. What proportion of the population sleeps less than 5 hours?

# %%
stats.norm.cdf(5,mu, sigma)
#-> np.float64(0.0712333774139861)

# %% [markdown]
# ## Q2. What proportion of the population sleeps more than 9 hours?

# %%
1 - stats.norm.cdf(9,mu,sigma)
#-> np.float64(0.11506967022170822)

# %% [markdown]
# ## Q3. How much sleep does the middle 92% of the population get?

# %%
stats.norm.ppf(0.04,mu,sigma)
#-> np.float64(4.5739708931217455)

# %%
stats.norm.ppf(0.96,mu,sigma)
#-> np.float64(9.826029106878254)

