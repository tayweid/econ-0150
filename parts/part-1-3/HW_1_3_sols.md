# ECON 0150 | Homework 1.3 {++Solutions++}

*Due: Sunday, Sept. 20*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely. You are welcomed and encouraged to work in groups so long as your work is your own. Submit your figures and answers to Gradescope.

### Q1. US Economic Growth

The dataset `us_real_gdp.csv` contains annual US Real GDP (in trillions of dollars) from 1970 to 2024.

a) What is the data structure of this dataset?

**Time series data.** We observe a single entity (the US) across multiple time periods (years). The index variable is Year.

b) Create a line graph of US Real GDP over time.

![](i/hw_1_3_sols_01.png)

c) Describe the overall trend. Are there any periods where the trend changes noticeably?

The overall trend is upward — US Real GDP has grown substantially from about 5 trillion in 1970 to over 20 trillion by 2023. There are noticeable dips during recessions (early 1980s, 2008-2009 financial crisis, and 2020 COVID pandemic), but the economy recovers each time and continues growing.

### Q2. US Economic Growth Rates

Use the same `us_real_gdp.csv` dataset to create a new column that calculates the **annual growth rate** of Real GDP. The growth rate formula is:

$$
g_t = \frac{GDP_t - GDP_{t-1}}{GDP_{t-1}}
$$

a) Create a line graph of the growth rate over time. (*Hint: use `gdp['Real_GDP'].pct_change()` to calculate the percent change.*)

![](i/hw_1_3_sols_02.png)

b) In which years did the US economy shrink (negative growth)? What might explain these periods?

The US economy shrank in years including 1974-75 (oil crisis), 1980 and 1982 (stagflation/Volcker recession), 1991 (early 90s recession), {++2009++} (financial crisis), and 2020 (COVID-19 pandemic). These correspond to major economic shocks — oil price spikes, monetary policy tightening to fight inflation, financial market collapses, and the pandemic shutdown.

c) What is the average growth rate over this period?

The average annual growth rate is approximately 2.8%.

### Q3. Seasonal Patterns in Coffee Prices

The dataset `Monthly_Coffee_Prices_dated.csv` contains monthly coffee prices from 1973 to 2024.

a) Create a multi-boxplot of coffee prices grouped by month.

![](i/hw_1_3_sols_03.png)

b) Which month has the highest median price?

The highest median price is in May.

c) Which months show the most price variability (largest range)?

The highest variability in price happens in April.

d) Based on your multi-boxplot, is there a clear seasonal pattern in coffee prices? Explain in one sentence.

There is no strong seasonal pattern in coffee prices. The medians and distributions across months are fairly similar, suggesting that month-to-month variation is less important than year-to-year variation driven by supply shocks, weather events, and global market conditions.

### Q4. Choosing the Right Visualization

You’ve now created line graphs (Q1-Q2) and a multi-boxplot (Q3).

a) If you wanted to know whether coffee prices are higher today than in 2000, which visualization would you use?

**A line graph.** A line graph shows prices over time, so you can directly compare the price level at different points in time (2000 vs today).

b) If you wanted to know whether coffee prices tend to be higher in certain months, which visualization would you use?

**A multi-boxplot grouped by month.** This shows the distribution of prices for each month across all years, making it easy to compare whether certain months consistently have higher or lower prices.
