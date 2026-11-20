# ECON 0150 | Homework 4.1 {++Solutions++}

*Due: Friday, Nov. 13 at 5PM*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Submit your figures and answers to Gradescope.

### Q1. Unemployment and BMI

The article *[Zhang, Q., Lamichhane, R., & Wang, Y. (2014)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4449673/)* in the Journal of Clinical Medicine studies the associations between US adult obesity and mental health and state/county economic conditions in recessions. The Homework 4.1 Notebook loads a sample of individual-level data from the 2011 Behavioral Risk Factor Surveillance System (BRFSS), which includes the following variables:

- `BMI5` – individual Body Mass Index (kg/m²)
- `MENTHLTH` – days of poor mental health in the past 30 days
- `unemployment_rate` – county-level unemployment rate (in percentage points)

Using this data, estimate the following linear model:

$$
\texttt{BMI5}_i = \beta_0 + \beta_1 \cdot \texttt{unemployment\_rate}_i + \varepsilon_i
$$

a\) Report the estimated coefficients $\hat\beta_0$ and $\hat\beta_1$, and the p-value on $\hat\beta_1$.

$\hat\beta_0 = 26.647$ and $\hat\beta_1 = 0.090$. The p-value on $\hat\beta_1$ prints as 0.000 in the coefficient table; it is about $4 \times 10^{-57}$. `statsmodels` drops the respondents with a missing BMI automatically.

b\) State the null hypothesis for $\beta_1$.

$H_0: \beta_1 = 0$. There is no linear relationship between the county unemployment rate and individual BMI.

c\) Interpret your estimated coefficient $\hat\beta_1$ in words. What does the estimate suggest about the relationship between county unemployment and individual BMI?

A one percentage point higher county unemployment rate is associated with a BMI that is about 0.09 kg/m² higher, on average. The slope is about 16 standard errors from zero, so the relationship is statistically significant, but it is small: a 10 percentage point gap in unemployment corresponds to less than one BMI point. People in counties with higher unemployment tend to have slightly higher BMI. This is an association, not evidence that unemployment causes weight gain.

\newpage

### Q2. Unemployment and Mental Health

The 2011 BRFSS also includes information on mental health. The variable `MENTHLTH` records the number of days in the past 30 days when the respondent’s mental health was “not good.” Estimate the following linear model:

$$
\texttt{MENTHLTH}_i = \beta_0 + \beta_1 \cdot \texttt{unemployment\_rate}_i + \varepsilon_i
$$

a\) Report and interpret the estimated coefficient $\hat\beta_1$.

$\hat\beta_1 = 0.138$. A one percentage point higher county unemployment rate is associated with about 0.14 more days of poor mental health in the past 30 days, on average.

b\) Write a complete interpretation of the p-value for $\hat\beta_1$ from your model in part (a). What exactly does it tell us in words?

The p-value is the probability of estimating a slope at least as far from zero as 0.138, in either direction, if county unemployment and poor mental health days were truly unrelated ($\beta_1 = 0$). Here it prints as 0.000 (about $8 \times 10^{-83}$): a slope this large would essentially never arise from sampling noise alone, so we reject the null hypothesis. The p-value says nothing about how large or important the relationship is, and it is not the probability that the null hypothesis is true.

### Q3. Reading a Regression Output

A researcher wants to test whether temperature (in °F) predicts daily ice cream sales (in dollars) using data from 60 days at a local shop. Their regression output shows:

```
                  coef  std err        t    P>|t|   [0.025   0.975]
-------------------------------------------------------------------
Intercept      -159.47   42.300   -3.771    0.000  -244.17   -74.77
temperature       4.78    0.540    8.852    0.000     3.70     5.86
-------------------------------------------------------------------
```

a\) Write the regression model being estimated.

$$\texttt{sales}_i = \beta_0 + \beta_1 \cdot \texttt{temperature}_i + \varepsilon_i$$

b\) Interpret the intercept coefficient (-159.47) in context. Does it have a meaningful interpretation here?

The intercept is the predicted daily sales when the temperature is 0°F: −\$159.47. It has no meaningful interpretation here. Sales cannot be negative, and 0°F is far outside the temperatures in the data. The intercept only positions the line.

c\) Interpret the slope coefficient (4.78) in context.

Each additional degree Fahrenheit is associated with \$4.78 more in daily ice cream sales, on average.

d\) What is the null hypothesis being tested for the `temperature` coefficient?

$H_0: \beta_1 = 0$. There is no linear relationship between temperature and daily ice cream sales.

e\) Interpret the p-value for the `temperature` coefficient in words.

The p-value prints as 0.000. If temperature and sales were truly unrelated ($\beta_1 = 0$), a sample of 60 days would almost never produce a slope at least as far from zero as 4.78, which is nearly nine standard errors away. We reject the null hypothesis.

f\) If the temperature on a given day is 80°F, what does the model predict for ice cream sales?


$\hat{y} = -159.47 + 4.78 \times 80 = 222.93$

The model predicts \$222.93 in ice cream sales on an 80°F day.
