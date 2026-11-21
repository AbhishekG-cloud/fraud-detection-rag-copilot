# XGBoost Baseline — SMOTE-Resampled Training Data

## 1. Objective

Evaluate whether a default XGBoost classifier trained on SMOTE-resampled training data improves fraud-detection performance compared with the existing Dummy Classifier and Logistic Regression baselines.

The experiment uses the same time-based train/test split established previously. SMOTE is applied only to the training data, while the test set remains completely untouched.

---

## 2. Experimental Setup

### Data Split

A time-based train/test split was used so that the model is trained on earlier transactions and evaluated on later transactions.

This preserves the intended temporal direction of the fraud-detection problem and provides a more realistic estimate of performance on future transactions.

### Class Imbalance Handling

SMOTE was applied exclusively to the training data.

```text
Raw data
    ↓
Time-based train/test split
    ↓
Training data → SMOTE
Test data     → untouched
    ↓
Resampled training data
    ↓
XGBoost
    ↓
Untouched test set
```

The test-set class distribution was not modified.

### XGBoost Configuration

A baseline `XGBClassifier` was used without hyperparameter tuning.

The purpose of this experiment was to establish a clean reference point before performing model optimization.

Random state:

```text
42
```

### Evaluation Metrics

The following metrics were used:

* Precision
* Recall
* F1-score
* Average Precision (AUC-PR)

Average Precision was treated as the primary metric because the fraud-detection dataset is highly imbalanced.

Accuracy was not used as a primary evaluation metric.

---

## 3. Results

| Model               |  Precision |     Recall |         F1 | Average Precision |
| ------------------- | ---------: | ---------: | ---------: | ----------------: |
| Dummy Classifier    |     0.0000 |     0.0000 |     0.0000 |            0.0013 |
| Logistic Regression |     0.9032 |     0.3733 |     0.5283 |            0.6726 |
| **XGBoost + SMOTE** | **0.7532** | **0.7733** | **0.7632** |        **0.7999** |

---

## 4. Analysis

### Average Precision

XGBoost achieved an Average Precision of **0.7999**, compared with **0.6726** for Logistic Regression.

This represents an absolute improvement of approximately **0.1273**.

Therefore, under the current experimental setup, XGBoost provides substantially better precision-recall ranking performance than the Logistic Regression baseline.

### Precision

XGBoost achieved a precision of **0.7532**, compared with **0.9032** for Logistic Regression.

Therefore, XGBoost produces more false-positive fraud alerts at the current classification threshold.

The lower precision is the main trade-off associated with its substantially higher recall.

### Recall

XGBoost achieved a recall of **0.7733**, compared with **0.3733** for Logistic Regression.

Therefore, XGBoost identifies substantially more of the actual fraud transactions.

The recall is more than twice that of the Logistic Regression baseline.

### F1

XGBoost achieved an F1-score of **0.7632**, compared with **0.5283** for Logistic Regression.

This indicates a substantially better balance between precision and recall at the current classification threshold.

---

## 5. Business Interpretation

The results show an important precision-recall trade-off.

Logistic Regression is more conservative:

* High precision
* Lower recall
* Fewer false-positive alerts
* More missed fraud

XGBoost is more aggressive:

* Lower precision
* Much higher recall
* More fraud detected
* More legitimate transactions potentially flagged

The appropriate model therefore depends on the relative business cost of:

1. Missing a fraudulent transaction.
2. Sending a legitimate transaction for investigation.

For a fraud-investigation system, missing fraud can be expensive, so the higher recall achieved by XGBoost is potentially valuable. However, the additional false positives create investigation and operational costs.

Therefore, the model should not be considered production-ready solely because it has a higher Average Precision. Threshold selection and business-cost analysis are still required.

---

## 6. Key Findings

1. XGBoost + SMOTE substantially outperformed Logistic Regression in Average Precision.
2. XGBoost increased recall from **0.3733 to 0.7733**.
3. XGBoost increased F1 from **0.5283 to 0.7632**.
4. The improvement in recall came with a reduction in precision from **0.9032 to 0.7532**.
5. The test set remained untouched and retained its original class distribution.
6. No hyperparameter tuning was performed because this experiment establishes a baseline.
7. Average Precision remains the primary metric for comparing models.
8. Threshold tuning is required before making a final decision about the operating point.

---

## 7. Conclusion

The default XGBoost model trained on SMOTE-resampled training data provides a stronger baseline than Logistic Regression for this fraud-detection task under the current evaluation framework.

Its **0.7999 Average Precision** and **0.7733 recall** indicate substantially stronger minority-class detection and ranking performance.

However, its lower precision demonstrates that improved fraud detection comes with a higher false-positive cost.

The next stages should therefore investigate whether model performance can be improved through controlled experimentation and whether an appropriate probability threshold can achieve a better business trade-off.

MLflow experiment logging was intentionally deferred and will be introduced later when multiple experiments make systematic experiment tracking more valuable.
