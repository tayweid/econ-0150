# ECON 0150 | Homework 3.3 {++Solutions++}

*Due: Friday, Oct. 30 at 5PM*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Submit your figures and answers to Gradescope.

### Study Setup

A university runs a campus wellness program designed to reduce student anxiety. Anxiety is measured on a 0–21 scale for the same students before and after the program. For each student, we compute the paired difference:

$$
x_i = \text{after}_i - \text{before}_i
$$

A negative $x_i$ means the student's anxiety decreased. Our aim is to study whether the program worked to reduce student anxiety.

### Q1. Known $\mu$ and $\sigma$

Suppose we know the population of paired differences has mean $\mu = -3$ and standard deviation $\sigma = 5$ and we have a sample of $n = 25$ students.

a) Compute the standard error ($SE$) of $\bar{x}$. Then compute the probability that $\bar{x}$ falls within 1 SE of $\mu$. *(Hint: use `stats.norm.cdf()`)*.

The standard error is $SE = \sigma / \sqrt{n} = 5 / \sqrt{25} = 1$. The probability that $\bar{x}$ lands within one standard error of $\mu$ is about 0.683, the familiar 68% of a normal distribution within one standard deviation of its center.

```typst
#pagebreak()
```

b) Construct a 1 $SE$ confidence interval centered on $\mu$. Then simulate 1,000 samples of size $n = 25$ from this population. What fraction of the 1,000 sample means fall inside the confidence interval?

```python
ci_lower = mu - SE
ci_upper = mu + SE

samples = np.random.normal(loc=mu, scale=sigma, size=(1000, n)) # Samples
sample_means = samples.mean(axis=1) # Sample Mean

inside = (sample_means >= ci_lower) & (sample_means <= ci_upper) # In CI?
mean_inside = np.mean(inside) # Proportion inside
```

The interval is $[-4, -2]$. Here 66.1% of the simulated sample means fall inside it, close to the 68.3% probability from part a). The exact fraction varies from run to run (roughly 0.64 to 0.73 across simulations), since each simulation draws different samples.

### Q2. Testing a Model

In practice we don't know $\sigma$ or $\mu$. Instead of constructing confidence intervals centered on $\mu$ using $\sigma$, we center them on $\bar{x}$ and swap in the sample standard deviation $S$ for $\sigma$. This swap introduces extra uncertainty which we account for using the t-distribution. Let's use this information to test whether the wellness program actually works.

a) A university runs the program on $n = 25$ students and finds $\bar{x} = -2.8$ and $S = 4.6$. State the null hypothesis for testing whether the program has any effect on anxiety.

$H_0: \mu = 0$. The program has no effect on anxiety, so the population mean of the paired differences is zero. The two-sided alternative is $H_A: \mu \neq 0$.

b) Compute the probability of seeing a sample as extreme as $\bar{x}$ given the null hypothesis (*two-sided*).

```python
p_value = 2 * stats.t.cdf(-abs(x_bar), df=n-1, loc=0, scale=S/np.sqrt(n))
```

The p-value is approximately 0.006. Under the null hypothesis, a sample mean at least 2.8 points away from zero would occur in fewer than 1% of samples of 25 students, so the data are hard to square with "no effect." At $\alpha = 0.05$ we reject $H_0$.

c) A large national study of a similar program surveys $n = 2,000$ students and finds $\bar{x} = -0.3$ and $S = 5$. Compute the p-value.

The p-value is approximately 0.007. With $n = 2{,}000$ the standard error shrinks to about 0.11, so even a 0.3-point drop is nearly three standard errors from zero. This result is also statistically significant at $\alpha = 0.05$.

```typst
#pagebreak()
```

d) A clinician considers a drop of at least 2 points on the anxiety scale to be meaningful. The first study found a 2.8-point drop. The second found a 0.3-point drop. Which result is *practically* significant? What does this tell you about the difference between statistical significance and practical significance?

Only the first study is practically significant. Its 2.8-point drop exceeds the clinician's 2-point threshold. The second study's 0.3-point drop is statistically significant but far below the threshold: a change that small on a 21-point scale does not matter clinically.

The two studies have almost the same p-value but very different effect sizes. Statistical significance says the effect is probably not exactly zero. With a large enough sample, even a tiny effect clears that bar because the standard error shrinks. Practical significance asks whether the effect is big enough to matter, which the p-value cannot tell us. Always look at the size of the estimate, not just the p-value.

### Q3. Interpreting p-Values

A researcher studying the effect of a new teaching method on exam scores conducts a hypothesis test and reports a p-value of 0.032.

a) In your own words, what does this p-value tell us?

If the new teaching method had no effect, we would see a difference in exam scores at least as large as the one observed in about 3.2% of studies like this one. The data would be fairly surprising under the null hypothesis. It does *not* say there is a 3.2% chance the method does nothing, and it does not measure how large the effect is.

b) If the researcher used a significance level of $\alpha = 0.05$, would they reject the null hypothesis? What if they used $\alpha = 0.01$?

At $\alpha = 0.05$: yes, reject $H_0$. The p-value (0.032) is less than 0.05, so the result is statistically significant at the 5% level.

At $\alpha = 0.01$: no, do not reject $H_0$. The p-value (0.032) is greater than 0.01, so the result is not significant at the 1% level. The same data can lead to different conclusions depending on how strict the threshold is.

c) For each of the following statements, say whether it is **true or false** and explain your reasoning.

1. A p-value of 0.10 means there is a 10% chance that the null hypothesis is true.
2. If we fail to reject the null hypothesis, we have proven that it is true.
3. A small p-value indicates that our observed result would be unlikely if the null hypothesis were true.

<!-- -->

1. **False.** The p-value is not the probability that $H_0$ is true. The truth is fixed: $\mu$ either equals the null value or it doesn't. The p-value is the probability of seeing data this extreme *assuming* $H_0$ is true. It measures how surprising the data are under the null, not how likely the null is.

2. **False.** Failing to reject $H_0$ means the data are consistent with the null; it does not prove the null is true. There may simply not be enough data to detect a real effect. Absence of evidence is not evidence of absence.

3. **True.** This is the correct interpretation. A small p-value means that, if the null hypothesis were true, data as extreme as what we observed would rarely occur.
