# /// script
# requires-python = ">=3.13"
# dependencies = []
#
# [tool.uv]
# exclude-newer = "2026-10-27T00:00:00Z"
# ///

# %% [markdown]
# # Exercise 3.2 | Sampling and the Central Limit Theorem
#
# In this exercise we simulate sampling distributions to see the central limit theorem in action.

# %%
# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# %% [markdown]
# ## Die Rolls
#
# The dice distribution is uniform. Every face is equally likely.

# %% [markdown]
# ### Sample Size: n=1
#
# Roll a die once. Record your result below.

# %%
# Roll 1 die
n = 1
np.random.randint(1, 7, n)

# %% [markdown]
# ### Sample Size: n=2
#
# Roll a die twice and compute the mean of your two rolls.

# %%
n = 2

# %% [markdown]
# ### Sample Size: n=3
#
# Simulate 1,000 samples of size 3 from a fair die and plot the distribution of sample means.

# %%
n = 3

# %% [markdown]
# ### Sample Size: n=30
#
# Simulate 1,000 samples of size 30 and plot the distribution of sample means.

# %%
n = 30

# %% [markdown]
# ## Skewed Population
#
# Now let's test whether the CLT works for a skewed population: the chi-squared distribution (df=3), where most values are small but a few are very large.
#
# Simulate 1,000 sample means from a chi-squared(df=3) population.

# %% [markdown]
# ### Sample Size: n=1
#
# Start with a sample size n=1. Plot the histogram.

# %%
# Simulate 1000 sample means from a skewed population
samples = stats.chi2.rvs(df=3, size=(1000, 1))
sample_means = samples.mean(axis=1)
sns.histplot(sample_means, bins=30, stat="density")

# %%
# Plot the distribution
x = np.linspace(0, 15, 1000)
y = stats.chi2.pdf(x, df=3)
sns.lineplot(x=x, y=y, color='red', linestyle='--')

# %% [markdown]
# ### Sample Size: n=5
#
# Now increase the sample size to n=5. Plot the histogram.

# %%
# ...

# %% [markdown]
# ### Sample Size: n=30
#
# Increase to n=30.

# %%
# ...

# %% [markdown]
# ### Sample Size: n=1000
#
# Increase to n=1000.

# %%
# ...

# %% [markdown]
# ### Overlay: n=1 vs n=1000
#
# Overlay the n=1 distribution behind the n=1000 distribution to see how the sampling distribution transforms from skewed to normal.

# %%
# ...
