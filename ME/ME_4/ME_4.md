**Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Student ID:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_&#x20;

# ECON 0150 | MiniExam 4 | Spring 2026

This MiniExam will take 20 minutes with a quick break to follow. MiniExams are designed to both test your knowledge and challenge you to apply familiar concepts in new environments. Treat it as if you're trying to show me that you understand the material. Answer clearly, completely, and concisely.

#### Academic Conduct Code

The following academic conduct code is designed to protect the integrity of your work. Print your name/initials beside the three academic honesty agreements. I pledge to my fellow students, the university, and the instructor, that:

\_\_\_\_ I will complete this MiniExam solely using my own work.

\_\_\_\_ I will not use any digital resources unless explicitly allowed by the instructor.

\_\_\_\_ I will not communicate directly or indirectly with others during the MiniExam.

##### Q1. A researcher wants to understand whether mental heath outcomes are related to wealth inequality. Using data from 60 US cities, they measure each city’s Gini coefficient (`gini`, normalized to a between 0-100 where higher = more inequality) and average depression rate (`depression_rate`, cases per 1,000 residents).

<br />

\_\_\_\_\_\_\_\_\_\_\_ = \_\_\_\_\_\_\_\_\_\_\_ + \_\_\_\_\_\_\_\_\_\_\_ $\times$ \_\_\_\_\_\_\_\_\_\_\_ + \_\_\_\_

a) Write down (*above*) a statistical model to test this question.

<br />

b) Sketch (*to the right ->*) a visualization of this model.

<br />

c) Interpret an estimated coefficient of $\beta_1$ = 0.48 in words:

<br />

d) What is the default null hypothesis for $\beta_1$?     \_\_\_\_\_\_\_\_\_\_\_

##### Q2. A school district tests whether a free tutoring program affects math scores recorded as `scores`. We code `tutoring` as 1 for students in the program and 0 for students not in the program. In a sample of 90 students, those in the tutoring program scored an average of 78 and those not in the program scored an average of 72.

<br />

\_\_\_\_\_\_\_\_\_\_\_ = \_\_\_\_\_\_\_\_\_\_\_ + \_\_\_\_\_\_\_\_\_\_\_ $\times$ \_\_\_\_\_\_\_\_\_\_\_ + \_\_\_\_

a) Write down (*above*) a statistical model to test this question.

<br />

b) Based on the information given, what would $\beta_0$ equal? \_\_\_\_

<br />

c) Based on the information given, what would $\beta_1$ equal? \_\_\_\_

<br />

d) If we instead coded **`no_tutoring`** as 1 for students NOT in the program and 0 for students in the program, what would $\beta_0$ equal? \_\_\_\_

<br />

##### Q3. A public health researcher studies whether air quality (PM2.5 concentration) predicts hospital admission rates per 100,000 people using data from $n = 120$ counties with the following output:

```text exec
                            coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept                 35.200      4.800      7.333      0.000      25.700      44.700
pm25                       2.150      0.620      3.468      0.001       0.923       3.377
------------------------------------------------------------------------------
```

a) Sketch (*to the right ->*) how you would visualize the fitted model. Label the intercept and slope using the fitted values.

<br />

<br />

b) Interpret the Intercept coefficient (35.20) in context:

<br />

<br />

c) Interpret the **`pm25`** coefficient(2.15) in context:

<br />

<br />

d) What does the p-value of 0.001 for the pm25 coefficient mean? *(select one)*

> $\square$ If air quality has no effect on admissions, 0.1% of samples would have a coefficient this far from zero
>
> $\square$ Out of 1000 samples where air quality truly matters, only 1 would show a coefficient this large
>
> $\square$ Only 0.1% of the hospital admissions difference is due to random chance
>
> $\square$ There's a 99.9% probability that the true coefficient is at least 2.15
>
> $\square$ The coefficient of 2.15 has a 0.1% margin of error

##### Q4. Draw the sampling distribution under the null hypothesis ($\beta_1 = 0$) for the `pm25` coefficient from Q3. The observed coefficient is 2.15 with a standard error of 0.620 and a p-value of 0.001. Mark our observed coefficient and shade the region(s) that represent the p-value.

<br />

<br />

<br />

<br />

<br />

##### Q5. A researcher fits a regression model and examines the residual plot (predicted values on x-axis, residuals on y-axis). The plot shows residuals tightly clustered near zero for small predicted values but spreading out widely for large predicted values (a fan shape).

a) Which model assumption does this pattern suggest is violated?

<br />

b) Name one approach the researcher could use to address this issue
