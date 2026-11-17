# Homework 4.3 | Gradescope

This is an instructor-facing document to make it easy to enter questions into Gradescope. This sheet is the selection form students submit on Gradescope after completing their work in a notebook, taken from the Homework file. 

- Each `## QN` is a parent question. Put its title in the title field and paste its block into the Description box. A parent question can only hold description text; students answer the sub-questions.

- Each `### QN.M` under it is a sub-question. Put its title in the sub-question’s title field and paste its block into the **Problem** box.

- Ignore points. Each sub-question is worth 1 point by default on Gradescope.

Gradescope parses the code directly. Every input field must sit on its own line with no text before or after it, and a question can hold several fields:

- Text is Markdown, and LaTeX goes between `$$`. Images can be inserted with **Insert Image** or as a Markdown link `![alt](url)` to a file on the course site.
- Multiple choice: consecutive `( )` lines become a multiple-choice field, with `(x)` marking the correct answer. A blank line between choices starts a new group.
- Select all: consecutive `[ ]` lines become a select-all field, with `[x]` marking each correct answer. Students must mark every correct answer to get the point.
- Short answer: `[____](answer)` gives a one-line text box, autograded against the answer in parentheses. For numbers, `[____](=2+-0)` accepts any equivalent of 2 and `[____](=2+-0.2)` accepts anything from 1.8 to 2.2. Leave the parentheses empty to grade by hand.
- Free response: `|____|` gives a multi-paragraph text box. Any question with one is graded by hand.
- File uploads: `|files|` lets students upload any file type (a PNG of a figure, a notebook, a PDF). Uploads can be viewed and graded but not annotated.

## Q1: `Happiness and GDP`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, building each figure and fitting each model, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

This question is based on our work during Exercise 4.1 and Exercise 4.3 in class. The Homework 4.3 Notebook loads the happiness dataset Life_Evaluation_GDP_PerCap.csv, with Year, Country, Life_Evaluation (a composite measure of happiness based on survey polling), and GDP_Per_Cap (the country's GDP in that year divided by the population).
```

### Q1.1: `Create a scatterplot with GDP Per Capita on the horizontal axis and happiness on the vertical axis for the year 2024.`

```
Upload your figure.
|files|
```

### Q1.2: `Does there appear to be a relationship between the two variables?`

```
(x) Yes, positive: countries with higher GDP per capita tend to report higher happiness
( ) Yes, negative: countries with higher GDP per capita tend to report lower happiness
( ) No visible relationship
```

### Q1.3: `Does the relationship appear to be linear?`

```
(x) No: happiness rises steeply at low GDP per capita and flattens at high GDP per capita
( ) Yes: the points follow a straight line
( ) No: the points form a U shape
```

### Q1.4: `Perform a natural log transformation of GDP Per Capita (np.log) and create a scatterplot with log GDP Per Capita on the horizontal axis and happiness on the vertical axis.`

```
Upload your figure.
|files|
```

### Q1.5: `Fit a linear regression model to predict happiness using log GDP Per Capita. What is the interpretation of the intercept coefficient?`

```
(x) The predicted happiness when log GDP per capita is zero (a GDP per capita of $1), which is far outside the data and not meaningful here
( ) The average happiness across all countries in 2024
( ) The change in happiness for a one-unit increase in log GDP per capita
( ) The predicted happiness for a country with a GDP per capita of zero dollars
```

### Q1.6: `What is the interpretation of the slope coefficient?`

```
(x) A one-unit increase in log GDP per capita is associated with happiness about 0.66 points higher, on average
( ) A $1 increase in GDP per capita is associated with happiness about 0.66 points higher, on average
( ) A one-point increase in happiness is associated with log GDP per capita about 0.66 higher
( ) Countries with higher GDP per capita are about 66% happier
```

### Q1.7: `What is the interpretation of the p-value of the slope coefficient?`

```
|____|
```

## Q2: `Model Diagnostics`

```
Using the model you fit in Q1(e), answer the following questions about model assumptions.
```

### Q2.1: `Extract the residuals and predicted (fitted) values from your model. Create a residual plot with predicted values on the x-axis and residuals on the y-axis. Add a horizontal line at zero.`

```
Upload your figure.
|files|
```

### Q2.2: `Does the residual plot show signs of heteroskedasticity? Explain what you see and which assumption this relates to.`

```
|____|
```

### Q2.3: `Create a histogram of the residuals. Do they appear roughly normal?`

```
Upload your figure.
|files|

(x) Roughly: bell-shaped and centered at zero, with a longer left tail
( ) No: the histogram is flat
( ) No: the histogram has two separate peaks
```

### Q2.4: `Create a lagged residual plot by plotting each residual against the previous residual. Does this model appear to violate the independence assumption?`

```
Upload your figure.
|files|

(x) No: the points show no pattern
( ) Yes: the points follow a clear upward diagonal
( ) Yes: the points follow a clear downward diagonal
```

### Q2.5: `Re-fit the model using robust standard errors by adding cov_type='HC3' to the .fit() call. How do the standard errors and p-values change compared to Q1(e)?`

```
(x) They change only slightly, and the slope is still clearly different from zero
( ) The standard errors double, and the slope is no longer statistically significant
( ) The standard errors fall to zero
( ) The coefficients change, but the standard errors do not
```

## Q3: `Reading a Residual Plot`

```
A researcher fits a linear model predicting test scores from hours of study. Their residual plot (predicted values on the x-axis, residuals on the y-axis) shows a clear fan shape: residuals are tightly clustered near zero for low predicted values but spread out widely for high predicted values.
```

### Q3.1: `Which model assumption does this residual plot suggest is violated?`

```
(x) Homoskedasticity
( ) Linearity
( ) Independence
( ) Normality
```

### Q3.2: `What is the name for this pattern?`

```
(x) Heteroskedasticity
( ) Autocorrelation
( ) Non-linearity
( ) Skewness
```

### Q3.3: `Does this violation affect the estimated coefficients, or does it affect the standard errors and p-values? Explain briefly.`

```
|____|
```

### Q3.4: `What is one approach the researcher could use to address this issue?`

```
(x) Use robust standard errors
( ) Take first differences of the data
( ) Drop the observations with large residuals
( ) Collect a larger sample
```

## Answer check

Verified by running the solutions notebook against `data/Life_Evaluation_GDP_PerCap.csv`, 2024 rows, with the natural log of GDP per capita (146 countries; one is missing GDP per capita):

- Q1: intercept −0.2502 (standard error 0.364, p = 0.493); slope 0.6578 (standard error 0.0405, t = 16.225, p ≈ 2.6 × 10⁻³⁴, prints as 0.000). Log GDP per capita ranges from 6.11 to 11.69. With log10, as in Exercises 4.1 and 4.3, the slope would be 1.515; the intercept, t-statistic, and p-value are the same.
- Q2.2: the residual standard deviation is 0.826 for the 73 countries with below-median predictions and 0.527 for the 73 above, so the spread is somewhat larger at low predictions. This is the homoskedasticity assumption.
- Q2.3: residual skewness −0.656; the most negative residual is Afghanistan at −2.535.
- Q2.4: the correlation between each residual and the previous one is −0.010.
- Q2.5: with HC3 the intercept's standard error is 0.381 (p = 0.511) and the slope's is 0.0397 (z = 16.560, p prints as 0.000).
