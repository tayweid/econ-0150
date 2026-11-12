# /// script
# requires-python = ">=3.13"
# dependencies = []
#
# [tool.uv]
# exclude-newer = "2026-11-03T00:00:00Z"
# ///

# %% [markdown]
# # Project Template and Guidance
#
# This Notebook is intended to provide some guidance for getting started with creating your first complete project workflow.

# %% [markdown]
# ## Using Google Drive
#
# Start by saving this Notebook to your Google Drive account. Then go to your Google Drive, click on the Colab Notebooks folder to find
# You'll have to log into Google Drive this way if you want to load your dataset or save save your work as a new dataset.

# %%
# Mount your Google Drive. It will prompt you to log into your Google account.
from google.colab import drive
drive.mount('/content/drive')

# %%
# Change the working directory to your project folder.
import os
drive_path = '/content/drive/MyDrive/Colab Notebooks/'
project_folder = 'Zillow/'
os.chdir(drive_path + project_folder)

# %% [markdown]
# ## Step 0 | Imports and Setup

# %%
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

# %%
# Open a dataset from your project folder in Google Drive
data = pd.read_csv('zillow_data.csv')

# %% [markdown]
# ## Step 1 | Data Preparation
#
# Turn your data into something you can explore through data operations.

# %%
# Data operations here

# %%
# Save your dataset after you've worked on it
data.to_csv('cleaned_data.csv')

# %% [markdown]
# ## Step 2 | Exploratory Data Analysis
#
# Summarize the main variables and relationships of interest.

# %%
# Exploratory Data Analysis here

# %% [markdown]
# ## Step 3 (Part 3 - 5)
#
# Develop your statistical model.
#
# 1. Write down you null hypothesis
# 2. Write down your statistical model
# 3. Run your statistical model
# 4. Visualize your statistical model (if appropriate)

# %%
# Build and run your model here
