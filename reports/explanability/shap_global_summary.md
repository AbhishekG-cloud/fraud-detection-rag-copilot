# Global SHAP Analysis — XGBoost V1

## Objective

Explain the global prediction behavior of the locked XGBoost V1
fraud detection model.

## Model

- Model: XGBoost
- Version: V1
- max_depth: 3
- learning_rate: 0.2
- n_estimators: 300
- scale_pos_weight: 545.3908872901678

## Dataset Used

Describe the held-out test dataset used for explanation.

State whether the complete test set or a representative sample
was used.

## SHAP Method

TreeExplainer was used because the model is an XGBoost tree-based
model.

## Global Feature Importance

List the top features based on mean absolute SHAP value.

## Interpretation

Discuss:

- Most influential features
- Direction of contributions
- Magnitude/distribution
- Any notable patterns

## PCA Feature Caveat

V1-V28 are anonymized PCA-derived features. Their predictive
importance can be discussed, but their underlying business meaning
cannot be inferred from the dataset alone.

## Limitations

- SHAP explains model behavior rather than causality.
- Global explanations do not explain individual transactions.
- Feature importance does not establish that a feature is a causal
  driver of fraud.