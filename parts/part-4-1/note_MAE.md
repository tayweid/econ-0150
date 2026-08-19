## Future addition: Mean Absolute Error (MAE) as intuition builder

Consider adding a slide in concept_4_1 when first fitting a regression line that introduces MAE before SSE/R²:

- MAE = average of |actual - predicted| across all observations
- Interpretable in the units of the outcome: "on average, our prediction is off by X BMI points"
- Students can compute it by hand for a few points
- Provides intuition for what an error metric *is* before squaring makes things abstract

Then transition: "In practice, we minimize squared errors (SSE) because they have nicer mathematical properties for estimation..."

Inspired by Brilliant's regression course, which uses MAE as the first model comparison tool (comparing which predictor of Happiness has the lowest MAE: Freedom vs Life Expectancy vs Corruption).
