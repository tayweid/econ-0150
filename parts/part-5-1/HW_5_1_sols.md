## ECON 0150 | Spring 2026 | Homework 5.1 {++Solutions++}

### Due: Sunday April 12, at 11:59PM

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Use the provided datasets to answer the following questions. Then submit your figures and answers to Gradescope.


#### Q1. Revisiting the Recession and Health

In Homework 4.1, you estimated a simple relationship between county unemployment and BMI using 2011 BRFSS data, inspired by [Zhang, Lamichhane, & Wang (2014)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4449673/). Your simple model was:

$$
\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{unemployment\_rate}_i + \varepsilon_i
$$
But as Zhang et al. note, individual characteristics like gender and education may confound this relationship. In Part 5.1 we developed models with categorical controls to account for group-level differences. Let's revisit the BRFSS data and add them.

a) A researcher wants to test whether county unemployment affects BMI, while controlling for gender. Write a regression model to test this question.

$$\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{unemployment\_rate}_i + \beta_2 \times \texttt{Female}_i + \varepsilon_i$$



b) Start with a simple fixed-effect model:

$$
\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{Female}_i + \varepsilon_i
$$
Report the estimated coefficients. What does $\hat\beta_0$ represent in context? What does $\hat\beta_1$ tell us about the gender gap in BMI?

{++Intercept: 27.792. Female: -0.724.++}

$\hat\beta_0$ is the average BMI for males (the reference group, when Female = 0). $\hat\beta_1$ is the difference in average BMI between females and males. If negative, females have lower average BMI than males.



c) Now fit the model you wrote in part (a):

$$
\texttt{BMI5}_i = \beta_0 + \beta_1 \times \texttt{unemployment\_rate}_i + \beta_2 \times \texttt{Female}_i + \varepsilon_i
$$
Report the estimated coefficients. Interpret each one in context.

{++Intercept: 27.050. unemployment_rate: 0.093. Female: -0.733.++}

- $\hat\beta_0$: predicted BMI for a male in a county with 0% unemployment
- $\hat\beta_1$: a 1 percentage point increase in county unemployment is associated with a $\hat\beta_1$ unit change in BMI, holding gender constant
- $\hat\beta_2$: females have $\hat\beta_2$ units different BMI than males on average, holding unemployment constant



d) Compare the coefficient on `unemployment_rate` in part (c) to the one you estimated in HW 4.1 (without the gender control). Did it change much? What does this tell you about whether gender is a confounding variable for the unemployment–BMI relationship?

The coefficient on `unemployment_rate` should be very similar to the simple regression in HW 4.1. This tells us that gender is not a major confounding variable — it does not substantially change the estimated relationship between unemployment and BMI.



e) What does this model assume about how unemployment affects BMI for men versus women? *(Hint: think about what "parallel lines" means in this context.)*

The model assumes that the effect of unemployment on BMI is the same for men and women. The two lines (one for males, one for females) are parallel — they have the same slope ($\beta_1$) but different intercepts. This means unemployment shifts BMI by the same amount regardless of gender.



#### Q2. Reading Regression Output

Zhang et al. (2014) progressively add controls to their models. Below is output from a similar analysis: a researcher uses data from $n = 150$ US counties to study whether hospital admission rates (per 100,000 residents) differ between high-poverty and low-poverty counties, controlling for the share of residents without health insurance. They estimate:

$$
\texttt{admission\_rate}_i = \beta_0 + \beta_1 \times \texttt{high\_poverty}_i + \beta_2 \times \texttt{uninsured\_pct}_i + \varepsilon_i
$$
where `high_poverty` = 1 if the county poverty rate exceeds 15%, and 0 otherwise.

```
                 coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      320.50     28.400     11.285      0.000     264.40     376.60
high_poverty   145.30     35.600      4.082      0.000      75.10     215.50
uninsured_pct    8.70      1.850      4.703      0.000       5.04      12.36
--------------------------------------------------------------------------------
```

a) Interpret the intercept (320.50) in context.

The intercept (320.50) is the predicted admission rate for a low-poverty county (high_poverty = 0) with 0% uninsured residents. It represents the baseline admission rate.



b) Interpret the coefficient on `high_poverty` (145.30) in context.

High-poverty counties have 145.30 more admissions per 100,000 residents than low-poverty counties, holding the uninsured rate constant. This is statistically significant (p < 0.001).



c) Interpret the coefficient on `uninsured_pct` (8.70) in context.

Each 1 percentage point increase in the uninsured rate is associated with 8.70 more admissions per 100,000 residents, holding poverty status constant. This is statistically significant (p < 0.001).



d) What is the predicted admission rate for a high-poverty county where 20% of residents are uninsured?

Predicted admission rate for a high-poverty county with 20% uninsured:

$\hat{y} = 320.50 + 145.30(1) + 8.70(20) = 320.50 + 145.30 + 174.00 = 639.80$



e) What is the predicted admission rate for a low-poverty county with the same 20% uninsured rate?

Predicted admission rate for a low-poverty county with 20% uninsured:

$\hat{y} = 320.50 + 145.30(0) + 8.70(20) = 320.50 + 174.00 = 494.50$
