# ECON 0150 | Homework 3.4 {++Solutions++}

*Due: Friday, Oct. 30 at 5PM*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Submit your figures and answers to Gradescope.

### Q1. Study Hours

An economics professor claims that students spend 6 hours per week on average studying for their economics class. You survey 20 students and record the following number of hours they reported studying per week:

```python
study_hours = [5.2, 7.1, 4.8, 6.5, 8.0, 5.5, 7.3, 4.2, 6.7, 5.8,
               7.5, 6.2, 5.0, 7.8, 6.3, 4.5, 6.9, 5.7, 7.2, 6.0]
```

Use an intercept-only regression (GLM) model to test the professor's claim. The p-value on the intercept tests whether the population mean is *zero*, so first subtract 6 from each student's hours. Then the intercept is the average difference from 6 hours, and its p-value tests the null hypothesis that this difference is zero. The Homework 3.4 Notebook includes this step:

```python
study_hours_df['difference'] = study_hours_df['study_hours'] - 6
model = smf.ols('difference ~ 1', data=study_hours_df).fit()
```

a) What is the estimated difference in study hours from 6 hours?

The intercept is 0.21 hours. Students in the sample studied 6.21 hours per week on average, 0.21 hours more than the professor's claim. The intercept-only model's coefficient is exactly the sample mean of the differences.

b) What is the intercept's p-value?

The p-value is about 0.41. The intercept is less than one standard error (0.249 hours) from zero, so a difference this large is unremarkable under the null. We fail to reject $H_0$: the data are consistent with the professor's claim of 6 hours per week.

c) In your own words, what does the p-value in this model represent?

The p-value is the probability of observing a sample mean at least 0.21 hours away from 6 (in either direction) if students really do study 6 hours per week on average. Here about 41% of samples of 20 students would show a gap at least this large by chance alone, so the sample gives no real evidence against the claim. The p-value does not tell us the probability that the claim is true, and it does not say the claim is correct, only that we cannot distinguish the sample from it.

### Q2. Pennsylvania Household Income

According to USAFacts, the median household income in Pennsylvania was reported to be \$73,824 in 2023. The Homework 3.4 Notebook loads a sample of median household incomes for 30 Pennsylvania counties. Use this sample to test whether the average median household income in these counties differs from the statewide figure.

a) Use an intercept-only model to test whether the average median household income in the sample differs from \$73,824. As in Q1, subtract 73,824 from each county's median income before fitting the model. Report:

- Sample mean
- Standard error
- The p-value

<!-- -->

- Sample mean: \$65,699.87, which is \$8,124.13 below the statewide figure (the intercept).
- Standard error: \$1,905.33.
- p-value: about 0.0002 (the coefficient table rounds it to 0.000).

The intercept is more than four standard errors below zero.

b) Based on your results, does the sample provide evidence that the average county median income is different from the statewide figure? Briefly interpret your results in words.

Yes. If the average county median income equaled \$73,824, a sample of 30 counties would land \$8,124 or more away from it in only about 0.02% of samples. We reject $H_0$ at any conventional level: the average county median income in this sample is lower than the statewide figure.

This is not a contradiction. The statewide median counts every household, and populous, higher-income counties around Philadelphia and Pittsburgh carry more weight there. Averaging across counties treats each county equally, so the many small, lower-income rural counties pull the county average down.
