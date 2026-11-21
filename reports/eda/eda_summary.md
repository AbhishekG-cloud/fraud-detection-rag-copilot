# Exploratory Data Analysis Summary

## Amount
- Strong right-skewed distribution.
- Majority of transactions are low-value.
- Presence of several large-value outliers.

## Time
- Represents elapsed seconds from the first transaction.
- Appears continuous with no obvious gaps.

## PCA Features (V1–V28)
- Most distributions are centered around zero.
- Variance differs across components.
- Some components exhibit long tails and potential outliers.
- Individual PCA components cannot be assigned business meaning.

## Correlation Analysis
- Overall feature correlations are generally weak.
- Some features exhibit moderate correlation with the target (`Class`).
- No causal conclusions can be drawn from correlation alone.

## Data Quality
- No obvious structural issues observed during visual inspection.

## Future Considerations
- Investigate scaling strategies for `Amount`.
- Handle severe class imbalance during model training.
- Explore feature importance and SHAP after model development.