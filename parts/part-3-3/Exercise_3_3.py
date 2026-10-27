# /// script
# requires-python = ">=3.13"
# dependencies = []
#
# [tool.uv]
# exclude-newer = "2026-10-27T00:00:00Z"
# ///

# %% [markdown]
# # Exercise 3.3 | Confidence Intervals
#
# Suppose we know that the true effect of the NJ minimum wage on employment is $\mu = 0$ FTE and the population standard deviation is $\sigma = 9.8$ FTE. Card and Krueger surveyed $n = 331$ restaurants.

# %%
# Imports
import numpy as np
from scipy import stats

# %% [markdown]
# ## Confidence Intervals with Known $\mu$ and $\sigma$
#
# Set up the population parameters and calculate the standard error.

# %%
mu = 0
sigma = 9.8
n = 331

# %% [markdown]
# **Question 1.** What is the standard error of the sample mean?

# %%
# ...

# %% [markdown]
# **Question 2.** What is the probability that $\bar{x}$ falls within $1 \times SE$ of $\mu$?

# %%
# ...

# %% [markdown]
# **Question 3.** What is the probability that $\bar{x}$ falls within $2 \times SE$ of $\mu$?

# %%
# ...

# %% [markdown]
# ## Simulating Confidence Intervals
#
# Now let's simulate. Draw a sample of 331 restaurants from the population.

# %%
sample = np.random.normal(mu, sigma, n)

# %% [markdown]
# **Question 4.** Calculate the sample mean $\bar{x}$. Does it fall within $\pm 1 \times SE$ of $\mu$?

# %%
# ...

# %% [markdown]
# **Question 5.** Does it fall within $\pm 2 \times SE$ of $\mu$?

# %%
# ...

# %% [markdown]
# ## Class Data
#
# Enter 1 if your $\bar{x}$ was within $\pm 2 \times SE$ of $\mu$, and 0 if it wasn't.

# %%
class_results = [

]

# %% [markdown]
# **Question 6.** What fraction of the class had $\bar{x}$ inside the interval?

# %%
# ...
