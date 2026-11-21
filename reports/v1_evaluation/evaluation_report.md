# V1 Final Evaluation Report

## 1. Model

**Model:** XGBoost V1

**Imbalance strategy:** `scale_pos_weight`

**Model configuration:**

```text
max_depth = 3
learning_rate = 0.20
n_estimators = 300
scale_pos_weight = 545.3908872901678
```

The configuration was selected during the first hyperparameter-tuning pass and subsequently locked as the project's V1 candidate. The planned second tuning pass was deferred to a future V2 iteration.

---

## 2. Evaluation Strategy

The model was evaluated using the project's previously established time-based train/test split.

The held-out test set was not used for hyperparameter selection.

The test set was evaluated only after the V1 configuration had been locked.

The training data remained imbalanced and `scale_pos_weight` was used during XGBoost training.

The test data was not resampled or otherwise modified.

---

## 3. Final Test Results

| Metric            |         V1 |
| ----------------- | ---------: |
| Precision         | **0.8235** |
| Recall            | **0.7467** |
| F1                | **0.7832** |
| Average Precision | **0.7968** |

Average Precision is the primary metric for this project because fraud represents a very small minority class.

---

## 4. Historical Comparison

| Model               |  Precision |     Recall |         F1 | Average Precision |
| ------------------- | ---------: | ---------: | ---------: | ----------------: |
| Logistic Regression |     0.9032 |     0.3733 |     0.5283 |            0.6726 |
| XGBoost + SMOTE     |     0.7532 |     0.7733 |     0.7632 |            0.7999 |
| **XGBoost V1**      | **0.8235** | **0.7467** | **0.7832** |        **0.7968** |

V1 provides a substantially stronger F1-score than the Logistic Regression baseline and a much higher recall.

Compared with XGBoost + SMOTE, V1 has higher precision and F1 but slightly lower recall and Average Precision.

Therefore, V1 should not be described as universally superior to every previous model.

---

## 5. Confusion Matrix

The confusion matrix shows four categories:

* True Positive — fraud correctly detected.
* False Positive — legitimate transaction incorrectly flagged as fraud.
* True Negative — legitimate transaction correctly classified.
* False Negative — fraud incorrectly classified as legitimate.

For fraud detection, false negatives are particularly important because they represent fraudulent transactions that escaped detection.

False positives also have operational costs because they may require investigation or create customer friction.

The saved confusion matrix is:

```text
reports/v1_evaluation/confusion_matrix.png
```

---

## 6. Precision-Recall Curve

The Precision-Recall curve was generated using the predicted fraud probabilities from V1.

The curve demonstrates how precision and recall change as the classification threshold changes.

Average Precision for the held-out test set is:

**0.7968**

The model therefore has meaningful fraud-ranking capability, but the default classification threshold represents only one possible operating point.

Threshold optimization is intentionally left for a later stage rather than being incorporated into this final V1 evaluation.

---

## 7. Business Interpretation

At the current classification threshold, V1 achieves a precision of 0.8235 and recall of 0.7467.

This means the model detects a substantial proportion of fraudulent transactions while maintaining relatively high precision among transactions flagged as fraud.

However, approximately one quarter of actual fraud cases are still missed at this operating point.

The system therefore represents a useful fraud-detection candidate but should not be considered a complete production fraud decision system.

The appropriate operating threshold should ultimately depend on the relative business cost of missed fraud, false-positive investigations, customer friction, and available investigation capacity.

---

## 8. Model Artifact

The locked V1 model was serialized using XGBoost's JSON model format:

```text
models/xgboost_v1/model.json
```

The saved model was reloaded and its predictions were checked to verify that the serialized artifact produces the expected Average Precision.

---

## 9. Limitations

Several limitations remain:

1. V1 has not undergone threshold optimization.
2. The second hyperparameter-tuning pass was deferred to a future V2 iteration.
3. The evaluation dataset represents a historical period and may not perfectly represent future fraud patterns.
4. Fraud prevalence and behavior can change over time.
5. A model score alone does not determine the financial cost of fraud detection errors.
6. Further error analysis is required before deployment.
7. Model explainability is still required to understand the drivers of individual predictions.

---

## 10. Conclusion

The locked XGBoost V1 model provides a strong initial fraud-detection candidate.

It achieves:

* Precision: **0.8235**
* Recall: **0.7467**
* F1: **0.7832**
* Average Precision: **0.7968**

The model provides a substantial improvement over the Logistic Regression baseline in recall, F1, and Average Precision while maintaining strong precision.

Compared with the XGBoost + SMOTE baseline, V1 shifts the operating point toward higher precision and F1 with a small reduction in recall and Average Precision.

V1 is therefore locked as the reference model for subsequent explainability, error-analysis, packaging, and deployment work.

Future improvements should be treated as new model versions rather than modifications to the locked V1 artifact.
