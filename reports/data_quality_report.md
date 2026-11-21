# Data Quality Report

## Missing Values
- Total missing values: 0


## Duplicate Rows
- Duplicate rows detected: 1081


## Outliers
### Amount
- Right-skewed with many high-value observations.
- Outliers appear to be genuine financial transactions.

### Time
- Sequential transaction index.
- No obvious quality issues.

## Train/Test Split Strategy

Recommended: Time-based split

### Justification
- Preserves transaction chronology.
- Better represents real-world fraud detection.
- Reduces temporal data leakage.
- More realistic evaluation than a random split.

