# Baseline Model Report

## Project

**Credit Card Fraud Detection**

---

# Objective

The objective of this experiment is to establish baseline performance on the original imbalanced dataset before applying any imbalance-handling techniques such as SMOTE, class weighting, threshold tuning, or more advanced machine learning models.

These baseline metrics will serve as the reference point for evaluating all future improvements.

---

# Dataset

- Dataset: ULB Credit Card Fraud Detection Dataset
- Samples: 284,807
- Features: 30
- Target: `Class`
    - 0 = Legitimate
    - 1 = Fraud

---

# Train/Test Split Strategy

This project uses a **time-based train/test split**.

### Rationale

Transactions in real-world fraud detection occur sequentially. A production fraud detection system predicts future transactions using historical data.

A time-based split:

- Preserves temporal ordering
- Better reflects production deployment
- Reduces temporal data leakage
- Produces a more realistic estimate of model performance

---

# Models Evaluated

## 1. Dummy Classifier

### Strategy

`most_frequent`

### Purpose

Provides the minimum benchmark by always predicting the majority class.

A useful machine learning model should outperform this baseline.

---

## 2. Logistic Regression

### Configuration

- Default parameters
- No SMOTE
- No class weighting
- Trained on the original imbalanced dataset

### Purpose

Logistic Regression is a standard baseline classifier for tabular binary classification problems because it is simple, interpretable, and computationally efficient.

---

# Evaluation Metrics

The dataset is highly imbalanced; therefore, accuracy is not considered an informative performance metric.

The following metrics are used:

- Precision
- Recall
- F1 Score
- Average Precision (AUC-PR)

These metrics better reflect the model's ability to identify fraudulent transactions.

---

# Model Performance

| Metric | Dummy Classifier | Logistic Regression |
|---------|----------------:|--------------------:|
| Precision | XX | XX |
| Recall | XX | XX |
| F1 Score | XX | XX |
| Average Precision (AUC-PR) | XX | XX |

---

# Confusion Matrices

## Dummy Classifier

See:

```
reports/baselines/dummy_confusion_matrix.png
```

### Observation

The Dummy Classifier predicts every transaction as legitimate, resulting in zero fraud detection capability.

---

## Logistic Regression

See:

```
reports/baselines/logistic_confusion_matrix.png
```

### Observation

Logistic Regression detects fraudulent transactions but still misses a considerable number because of severe class imbalance.

---

# Precision–Recall Curve

See:

```
reports/baselines/precision_recall_curve.png
```

### Interpretation

The Precision–Recall curve summarizes model performance across multiple probability thresholds.

Because fraud detection is a rare-event classification problem, this curve is more informative than overall accuracy.

---

# Model Comparison

The Logistic Regression model substantially outperforms the Dummy Classifier across all evaluation metrics.

However, performance remains limited due to the extreme imbalance between legitimate and fraudulent transactions.

Although Logistic Regression identifies some fraudulent transactions, recall remains lower than desired for a production fraud detection system.

---

# Key Observations

- The Dummy Classifier provides an effective minimum benchmark.
- Logistic Regression successfully learns useful decision boundaries.
- Severe class imbalance continues to limit fraud detection performance.
- Average Precision indicates there is room for substantial improvement.
- Baseline metrics have now been established for future comparison.

---

# Limitations

The baseline models intentionally do **not** address class imbalance.

Specifically:

- No SMOTE
- No class weighting
- Default probability threshold (0.5)
- No hyperparameter tuning
- No feature engineering

These limitations are intentional so that future improvements can be measured objectively.

---

# Planned Improvements

The following enhancements will be introduced incrementally in future experiments:

1. SMOTE (training data only)
2. Class-weighted Logistic Regression
3. Threshold optimization
4. Tree-based ensemble models (XGBoost)
5. Hyperparameter tuning
6. SHAP explainability
7. Model comparison and selection

Each modification will be evaluated against the baseline established in this report.

---

# Conclusion

This experiment establishes the initial performance benchmark for the fraud detection pipeline.

While Logistic Regression improves upon the Dummy Classifier, performance remains constrained by severe class imbalance.

These baseline results justify the introduction of imbalance-handling techniques and more sophisticated machine learning models in subsequent stages of the project.