# ECON 0150 | Homework 4.2 {++Solutions++}

*Due: Friday, Nov. 13 at 5PM*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Submit your figures and answers to Gradescope.

### Q1. Mental Health and Income Group

The 2011 Behavioral Risk Factor Surveillance System (BRFSS) contains individual-level data with the following variables:

- `MENTHLTH` – days of poor mental health in the past 30 days
- `INCOME2` – income category (1 = less than \$10,000, …, 8 = \$75,000 or more)

The Homework 4.2 Notebook loads the data and, as in Exercise 4.2, drops respondents with a missing income or mental health response. Create a binary variable `under_10k` equal to 1 if `INCOME2 == 1` and 0 otherwise. Then estimate the following linear model:

$$
\texttt{MENTHLTH}_i = \beta_0 + \beta_1 \cdot \texttt{under\_10k}_i + \varepsilon_i
$$

a\) Report $\hat\beta_0$. What does it represent in context?

$\hat\beta_0 = 3.195$. It is the average number of poor mental health days in the past 30 days for the reference group (`under_10k = 0`): respondents with household income of \$10,000 or more. It equals that group's sample mean.

b\) Report $\hat\beta_1$. What does it represent in context?

$\hat\beta_1 = 4.834$. It is the difference in group means: respondents with household income under \$10,000 report about 4.8 more poor mental health days on average than everyone else, for a group mean of $3.195 + 4.834 = 8.029$ days.

\newpage

### Q2. Reading Regression Output

A researcher wants to test whether having a college degree is associated with higher hourly wages. They code a binary variable `college` equal to 1 if the worker has a college degree and 0 otherwise, then estimate the following model:

$$
\texttt{wage}_i = \beta_0 + \beta_1 \cdot \texttt{college}_i + \varepsilon_i
$$

Their regression output shows:

```
                coef  std err        t    P>|t|   [0.025   0.975]
-----------------------------------------------------------------
Intercept      18.42    0.310   59.419    0.000    17.81    19.03
college         9.65    0.440   21.932    0.000     8.79    10.51
-----------------------------------------------------------------
```

a\) Interpret the intercept coefficient (18.42) in context.

The intercept is the average hourly wage of workers without a college degree (`college = 0`): \$18.42 per hour.

b\) Interpret the slope coefficient (9.65) in context.

Workers with a college degree earn \$9.65 more per hour on average than workers without one. Their average wage is $18.42 + 9.65 = 28.07$ dollars per hour.

c\) What is the null hypothesis being tested for the `college` coefficient?

$H_0: \beta_1 = 0$. Workers with and without a college degree have the same average hourly wage.

d\) Interpret the p-value in words.

The p-value prints as 0.000. If the two groups truly had the same average wage ($\beta_1 = 0$), a sample would almost never show a gap at least as large as \$9.65, which is about 22 standard errors from zero. We reject the null hypothesis: the wage gap is statistically significant. This is an association; it does not by itself show that the degree causes the higher wage.
