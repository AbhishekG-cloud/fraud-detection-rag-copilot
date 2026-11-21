# Credit Card Fraud Dataset Summary

## Source
ULB Machine Learning Group (Kaggle Credit Card Fraud Detection Dataset)

## Dataset Shape
- Rows: 284,807
- Columns: 31

## Features
- PCA Features: V1–V28
- Additional Features: Time, Amount

## Target
- Class

## Class Distribution
- Legitimate (0): 284,315
- Fraud (1): 492

## Percentages
- Legitimate: 99.8273%
- Fraud: 0.1727%

## Class Imbalance Ratio
Approximately 578:1

## Observation
The dataset is extremely imbalanced, with fraudulent transactions representing less than 0.2% of all observations. This makes accuracy an unreliable evaluation metric and motivates the use of imbalance-aware techniques and metrics in later stages of the project.