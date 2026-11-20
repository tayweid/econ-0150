## ECON 0150 | Spring 2026 | Homework 5.3 {++Solutions++}

### Due: Sunday April 19, at 11:59PM

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Use the provided datasets to answer the following questions. Then submit your figures and answers to Gradescope.


#### Q1. Adding Numerical Controls to the Recession and Health Model

Over the past several assignments, you have progressively built up a model of the relationship between county unemployment and BMI using 2011 BRFSS data. You started with a simple regression in HW 4.1, added a categorical control in HW 5.1, and tested for interaction effects in HW 5.2. [Zhang et al. (2014)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4449673/) also control for numerical variables like age and income. Let's do the same.

a) A researcher wants to estimate the effect of county unemployment on BMI while controlling for age, gender, college education, and marital status. Write the regression model.

$$\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{unemployment\_rate}_i + \beta_2 \times \texttt{Female}_i + \beta_3 \times \texttt{AGE}_i + \beta_4 \times \texttt{College}_i + \beta_5 \times \texttt{Married}_i + \varepsilon_i$$



b) Fit a multiple regression with both unemployment and age:

$$
\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{unemployment\_rate}_i + \beta_2 \times \texttt{AGE}_i + \varepsilon_i
$$
Report the estimated coefficients. Interpret each one using "holding constant" language. How does the coefficient on `unemployment_rate` compare to your simple regression from HW 4.1?

{++Intercept: 26.538. unemployment_rate: 0.090. AGE: 0.002.++}

Holding age constant, a one percentage point increase in county unemployment is associated with a change in BMI of $\hat\beta_1$ units. Holding unemployment constant, a one year increase in age is associated with a change in BMI of $\hat\beta_2$ units. The coefficient on unemployment_rate should be similar to the simple regression from HW 4.1, though it may change somewhat once we account for age differences across counties.



c) Now fit the full model you wrote in part (a):

$$
\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{unemployment\_rate}_i + \beta_2 \times \texttt{Female}_i + \beta_3 \times \texttt{AGE}_i + \beta_4 \times \texttt{College}_i + \beta_5 \times \texttt{Married}_i + \varepsilon_i
$$


Report the estimated coefficients. How does the coefficient on `unemployment_rate` compare to the simple model from HW 4.1? Has the sign, magnitude, or significance changed?

{++Intercept: 27.803. unemployment_rate: 0.081. Female: -0.756. AGE: 0.001. College: -0.992. Married: -0.085.++}

The coefficient on unemployment_rate has changed compared to the simple model from HW 4.1. The sign remains positive but the magnitude has shifted, suggesting that some of the original association was confounded by differences in age, education, gender, and marital status across counties. The relationship remains statistically significant, but the estimated effect of unemployment on BMI is different once we hold these other factors constant.



#### Q2. Reading Regression Output with Multiple Controls

A labor economist studies the determinants of hourly wages using a sample of $n = 500$ full-time workers. They estimate:

$$
\texttt{wage}_i = \beta_0 + \beta_1 \times \texttt{experience}_i + \beta_2 \times \texttt{education}_i + \beta_3 \times \texttt{urban}_i + \varepsilon_i
$$


where `experience` is years of work experience, `education` is years of schooling, and `urban` = 1 if the worker lives in an urban area.

```
                 coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        3.20      1.450      2.207      0.028       0.35       6.05
experience       0.45      0.060      7.500      0.000       0.33       0.57
education        1.85      0.180     10.278      0.000       1.50       2.20
urban            2.90      0.720      4.028      0.000       1.49       4.31
--------------------------------------------------------------------------------
```

a) Interpret the coefficient on `experience` (0.45) in context. What does "holding constant" mean here?

Holding education and urban/rural status constant, each additional year of work experience is associated with $0.45 higher hourly wages. "Holding constant" means we are comparing workers with the same level of education and the same location type, isolating the effect of experience alone.



b) Interpret the coefficient on `education` (1.85) in context.

Holding experience and urban/rural status constant, each additional year of education is associated with $1.85 higher hourly wages.



c) Interpret the coefficient on `urban` (2.90) in context. How is the interpretation of a binary control variable different from a numerical one?

Holding experience and education constant, workers in urban areas earn $2.90 more per hour than workers in rural areas. A binary variable represents a difference between two groups rather than a per-unit change. Instead of "each additional unit," we say "compared to the reference group."



d) What is the predicted hourly wage for a worker with 10 years of experience, 16 years of education, living in an urban area?

$\hat{y} = 3.20 + 0.45(10) + 1.85(16) + 2.90(1) = 3.20 + 4.50 + 29.60 + 2.90 = 40.20$

The predicted hourly wage is $40.20.



e) What is the predicted hourly wage for a worker with the same experience and education, but living in a rural area?

$\hat{y} = 3.20 + 0.45(10) + 1.85(16) + 2.90(0) = 3.20 + 4.50 + 29.60 + 0 = 37.30$

The predicted hourly wage is $37.30. The difference from part (d) is exactly $2.90, the coefficient on `urban`.
