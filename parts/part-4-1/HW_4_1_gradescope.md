# Homework 4.1 | Gradescope

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

## Q1: `Unemployment and BMI`

```
Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Work through the questions in your notebook first, computing each number, then enter your answers here as selections. You are welcomed and encouraged to work in groups so long as your work is your own.

The article Zhang, Lamichhane, & Wang (2014) in the Journal of Clinical Medicine studies the associations between US adult obesity and mental health and state/county economic conditions in recessions. The Homework 4.1 Notebook loads a sample of individual-level data from the 2011 Behavioral Risk Factor Surveillance System (BRFSS) with BMI5 (Body Mass Index), MENTHLTH (days of poor mental health in the past 30 days), and unemployment_rate (county-level unemployment rate, in percentage points). Estimate the linear model

$$BMI5_i = \beta_0 + \beta_1 \cdot unemployment\_rate_i + \varepsilon_i$$
```

### Q1.1: `Report the estimated coefficients and the p-value on the slope.`

```
Intercept $$\hat\beta_0$$ (three decimal places)
[____](=26.647+-0.005)

Slope $$\hat\beta_1$$ (three decimal places)
[____](=0.0898+-0.001)

What does the coefficient table show for the p-value on the slope?
(x) 0.000, meaning the p-value is smaller than 0.0005
( ) 0.006
( ) 0.047
( ) 15.940
```

### Q1.2: `State the null hypothesis for the slope.`

```
(x) $$\beta_1 = 0$$: there is no linear relationship between county unemployment and individual BMI
( ) $$\beta_1 > 0$$: BMI rises with county unemployment
( ) $$\hat\beta_1 = 0.09$$: the estimated slope equals the true slope
( ) $$\beta_0 = 0$$: average BMI is zero when unemployment is zero
```

### Q1.3: `Interpret your estimated slope in words.`

```
Which statement matches the estimate?
(x) A one percentage point higher county unemployment rate is associated with about 0.09 higher BMI, on average
( ) A one percent increase in BMI is associated with a 0.09 point higher unemployment rate
( ) Becoming unemployed raises a person's BMI by 0.09
( ) People in counties with zero unemployment have an average BMI of 0.09

What does the estimate suggest about the relationship between county unemployment and individual BMI?
|____|
```

## Q2: `Unemployment and Mental Health`

```
The 2011 BRFSS also includes information on mental health. The variable MENTHLTH records the number of days in the past 30 days when the respondent's mental health was "not good." Estimate the linear model

$$MENTHLTH_i = \beta_0 + \beta_1 \cdot unemployment\_rate_i + \varepsilon_i$$
```

### Q2.1: `Report and interpret the estimated slope.`

```
Slope $$\hat\beta_1$$ (three decimal places)
[____](=0.1375+-0.001)

Which statement matches the estimate?
(x) A one percentage point higher county unemployment rate is associated with about 0.14 more poor mental health days in the past 30, on average
( ) A one percentage point higher county unemployment rate is associated with about 14 more poor mental health days
( ) Each additional poor mental health day raises county unemployment by 0.14 percentage points
( ) About 14% of respondents in high-unemployment counties report poor mental health
```

### Q2.2: `Write a complete interpretation of the p-value for the slope. What exactly does it tell us in words?`

```
|____|
```

## Q3: `Reading a Regression Output`

```
A researcher wants to test whether temperature (in °F) predicts daily ice cream sales (in dollars) using data from 60 days at a local shop. Their regression output is in the handout and the notebook: the Intercept row shows coef -159.47, std err 42.300, t -3.771, p 0.000; the temperature row shows coef 4.78, std err 0.540, t 8.852, p 0.000.
```

### Q3.1: `Write the regression model being estimated.`

```
(x) $$sales_i = \beta_0 + \beta_1 \cdot temperature_i + \varepsilon_i$$
( ) $$temperature_i = \beta_0 + \beta_1 \cdot sales_i + \varepsilon_i$$
( ) $$sales_i = \beta_0 + \varepsilon_i$$
( ) $$sales_i = \beta_1 \cdot temperature_i$$
```

### Q3.2: `Interpret the intercept coefficient (-159.47) in context. Does it have a meaningful interpretation here?`

```
(x) It is the predicted sales at 0°F; it is not meaningful here because sales cannot be negative and 0°F is far outside the data
( ) It is the average daily sales across the 60 days
( ) It is the change in sales for each additional degree
( ) It is the predicted sales at the average temperature, so the shop loses money on a typical day

Explain briefly.
|____|
```

### Q3.3: `Interpret the slope coefficient (4.78) in context.`

```
(x) Each additional degree Fahrenheit is associated with $4.78 more in daily sales, on average
( ) Each additional dollar of sales is associated with a 4.78 degree higher temperature
( ) Sales rise by 4.78% for each additional degree
( ) The shop sells $4.78 of ice cream on a 1°F day
```

### Q3.4: `What is the null hypothesis being tested for the temperature coefficient?`

```
(x) $$\beta_1 = 0$$: temperature has no linear relationship with daily sales
( ) $$\beta_1 = 4.78$$
( ) $$\beta_0 = 0$$: sales are zero at 0°F
( ) $$\beta_1 \neq 0$$: temperature is related to daily sales
```

### Q3.5: `Interpret the p-value for the temperature coefficient in words.`

```
|____|
```

### Q3.6: `If the temperature on a given day is 80°F, what does the model predict for ice cream sales?`

```
Predicted sales, in dollars (two decimal places)
[____](=222.93+-0.01)
```

## Answer check

Verified with statsmodels OLS fits on data/BRFSS_cleaned.csv (243,402 rows; statsmodels drops rows with a missing outcome):

- Q1: 229,655 observations. Intercept 26.6469 (standard error 0.047); slope 0.0898 (standard error 0.006, t = 15.940); the slope's p-value is 3.6 × 10⁻⁵⁷ and prints as 0.000. The slope tolerance accepts 0.09 and 0.090.
- Q2: 238,881 observations. Intercept 2.3047; slope 0.1375 (standard error 0.007, t = 19.286); p = 8.2 × 10⁻⁸³. The tolerance accepts both 0.137 and 0.138.
- Q3: −159.47 + 4.78 × 80 = 222.93.
