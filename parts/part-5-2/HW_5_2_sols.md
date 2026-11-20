## ECON 0150 | Spring 2026 | Homework 5.2 {++Solutions++}

### Due: Sunday April 12, at 11:59PM

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Use the provided datasets to answer the following questions. Then submit your figures and answers to Gradescope.

#### Q1. Reading Regression Output with Interactions

A researcher studies whether the effect of class size on standardized test scores differs between public and private schools. Using data from $n = 300$ schools, they estimate:

$$
\texttt{score}_i = \beta_0 + \beta_1 \times \texttt{class\_size}_i + \beta_2 \times \texttt{private}_i + \beta_3 \times \texttt{class\_size}_i \times \texttt{private}_i + \varepsilon_i
$$
where `private` = 1 for private schools and 0 for public schools.

```
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
Intercept             88.50      3.200     27.656      0.000      82.20      94.80
class_size            -0.95      0.140     -6.786      0.000      -1.22      -0.68
private                5.40      5.100      1.059      0.290      -4.63      15.43
class_size:private     0.60      0.280      2.143      0.033       0.05       1.15
------------------------------------------------------------------------------------
```

a) What is the predicted test score for a public school with a class size of 0? What coefficient tells you this?

The predicted test score for a public school with class size 0 is 88.50. This is the intercept ($\hat\beta_0$).



b) What is the effect of one additional student in class size for a public school? What coefficient tells you this?

For public schools, one additional student is associated with a 0.95-point decrease in test scores. This is $\hat\beta_1 = -0.95$.



c) What is the effect of one additional student in class size for a private school? Show how you calculate this.

For private schools, the effect is $\hat\beta_1 + \hat\beta_3 = -0.95 + 0.60 = -0.35$. One additional student is associated with a 0.35-point decrease in test scores for private schools.



d) Interpret the coefficient and p-value on `private` in context.

The coefficient on `private` (5.40) represents the predicted difference in test scores between private and public schools when class size is 0. It is not statistically significant (p = 0.290), so we cannot conclude that private schools score differently from public schools at a class size of zero.



e) Interpret the interaction coefficient on `class_size:private` (0.60) in context. What does it tell us about how class size affects scores differently in public versus private schools?

The interaction coefficient (0.60) tells us that the negative effect of class size is 0.60 points smaller for private schools than for public schools. Private schools are less harmed by larger class sizes. This is statistically significant (p = 0.033), so there is evidence that the class size effect differs by school type.



#### Q2. Do Recessions Affect Men and Women Differently? (*optional*)

In Homework 5.1, you estimated `BMI5 ~ unemployment_rate + Female`, which assumes that unemployment affects BMI equally for men and women (parallel lines with the same slope). But what if the effect is different? [Zhang et al. (2014)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4449673/) find that the relationship between economic conditions and health outcomes varies across subgroups. Let's test for this using interaction terms.

a) A researcher suspects that the effect of county unemployment on BMI may differ for men and women. Write a regression model that allows the effect of unemployment on BMI to differ by gender. Include both a fixed effect and an interaction term.

$$\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{unemployment\_rate}_i + \beta_2 \times \texttt{Female}_i + \beta_3 \times \texttt{unemployment\_rate}_i \times \texttt{Female}_i + \varepsilon_i$$



b) Fit an interaction model (without the fixed effect):

$$
\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{unemployment\_rate}_i + \beta_2 \times \texttt{unemployment\_rate}_i \times \texttt{Female}_i + \varepsilon_i
$$
Report the estimated coefficients. What is the effect of a 1 percentage point increase in county unemployment on BMI for Female?

{++Intercept: 26.620. unemployment_rate: 0.137. unemployment_rate:Female: -0.074.++}

- For males: the effect of a 1 pp increase in unemployment on BMI is $\hat\beta_1$
- For females: the effect is $\hat\beta_1 + \hat\beta_2$

{++For Female, a 1 percentage point increase in county unemployment is associated with a 0.063 increase in BMI.++}



c) Now fit the full model you wrote in part (a). Report all four estimated coefficients. Interpret each one in context.

{++Intercept: 27.837. unemployment_rate: -0.006. Female: -2.056. unemployment_rate:Female: 0.165.++}

- $\hat\beta_0$: predicted BMI for a male in a county with 0% unemployment
- $\hat\beta_1$: for males, a 1 pp increase in unemployment is associated with a $\hat\beta_1$ change in BMI
- $\hat\beta_2$: at 0% unemployment, females have $\hat\beta_2$ units different BMI than males
- $\hat\beta_3$: the difference in the unemployment effect between females and males — for females, the effect of a 1 pp increase in unemployment is $\hat\beta_1 + \hat\beta_3$



d) Based on the full model in (c), calculate the predicted BMI for each of the following:

- A male in a county with 5% unemployment
- A female in the same county
- A male in a county with 10% unemployment
- A female in the same county

{++Male, 5% unemployment: 27.81. Female, 5% unemployment: 26.58. Male, 10% unemployment: 27.78. Female, 10% unemployment: 27.38.++}



e) What does the interaction term ($\hat\beta_3$) tell us about whether the effect of unemployment on BMI differs by gender?

If $\hat\beta_3$ is large and statistically significant, the effect of unemployment on BMI differs by gender — the parallel lines assumption from HW 5.1 doesn't hold. If $\hat\beta_3$ is small or insignificant, the simpler model with parallel lines may be sufficient.

