# XGBoost Hyperparameter Tuning — Pass 1

## 1. Objective

The objective of this experiment was to perform the first controlled hyperparameter-tuning pass for the fraud-detection XGBoost model.

The search focused on:

* `max_depth`
* `learning_rate`
* `n_estimators`
* `scale_pos_weight`

Average Precision was used as the primary model-selection metric because the fraud class is highly imbalanced.

The test set was kept completely separate from hyperparameter selection and was used only for final evaluation of the selected configuration.

---

## 2. Experimental Setup

### Train/Test Strategy

The project uses a time-based train/test split.

Earlier observations were used for training, while later observations were reserved as the final test set.

The test set was not used during hyperparameter search.

### Imbalance Strategy

This experiment used XGBoost's `scale_pos_weight` rather than SMOTE.

The model was trained on the original imbalanced training data.

The baseline class ratio was:

```text
scale_pos_weight = 545.39
```

This was calculated approximately as:

```text
number of legitimate training transactions
-------------------------------------------
number of fraud training transactions
```

### Cross-Validation

Five-fold `TimeSeriesSplit` was used within the training data.

Validation fraud counts were:

```text
Fold 1 → 81
Fold 2 → 57
Fold 3 → 86
Fold 4 → 43
Fold 5 → 47
```

Every validation fold contained fraud observations, allowing Average Precision to be calculated for each fold.

The temporal structure was preserved so that validation observations represented later observations relative to their corresponding training data.

---

## 3. Hyperparameter Search Space

The first tuning pass used a deliberately small search space:

| Hyperparameter     | Candidate Values                   |
| ------------------ | ---------------------------------- |
| `max_depth`        | 3, 5, 7                            |
| `learning_rate`    | 0.03, 0.10, 0.20                   |
| `n_estimators`     | 100, 200, 300                      |
| `scale_pos_weight` | 0.5×, 1×, 2× empirical class ratio |

There were 81 possible combinations in the complete search space.

`RandomizedSearchCV` evaluated 20 randomly selected configurations using five-fold cross-validation, resulting in 100 model fits.

---

## 4. Model Selection

The best configuration selected using mean cross-validation Average Precision was:

| Hyperparameter     | Selected Value |
| ------------------ | -------------: |
| `max_depth`        |              3 |
| `learning_rate`    |           0.20 |
| `n_estimators`     |            300 |
| `scale_pos_weight` |         545.39 |

Best mean CV Average Precision:

**0.8111**

The selected configuration therefore preferred relatively shallow trees, a relatively high learning rate, 300 boosting rounds, and the empirical negative-to-positive class ratio for `scale_pos_weight`.

---

## 5. Final Test Results

After hyperparameter selection was completed, the selected model was evaluated on the untouched test set.

| Metric            |     Result |
| ----------------- | ---------: |
| Precision         | **0.8235** |
| Recall            | **0.7467** |
| F1                | **0.7832** |
| Average Precision | **0.7968** |

---

## 6. Comparison With Day 8

| Model                              |  Precision | Recall |         F1 | Average Precision |
| ---------------------------------- | ---------: | -----: | ---------: | ----------------: |
| XGBoost + SMOTE                    |     0.7532 | 0.7733 |     0.7632 |        **0.7999** |
| Tuned XGBoost + `scale_pos_weight` | **0.8235** | 0.7467 | **0.7832** |            0.7968 |

Compared with the Day 8 baseline:

* Precision increased by **0.0703**.
* Recall decreased by **0.0266**.
* F1 increased by **0.0200**.
* Average Precision decreased by **0.0031**.

---

## 7. Interpretation

The tuning experiment changed the model's operating characteristics substantially.

Precision increased from 0.7532 to 0.8235, meaning that fewer transactions flagged as fraud were false positives at the current classification threshold.

Recall decreased from 0.7733 to 0.7467, meaning that the tuned model detected slightly fewer of the actual fraud transactions.

F1 increased from 0.7632 to 0.7832, indicating a better precision-recall balance at the current threshold.

However, Average Precision decreased slightly from 0.7999 to 0.7968. Since Average Precision is the project's primary model-selection metric, the tuning pass should not be described as an improvement in overall ranking performance.

The most accurate conclusion is therefore that the tuning pass produced a different and somewhat more precision-oriented operating point, but did not improve the primary Average Precision metric over the Day 8 SMOTE baseline.

---

## 8. Cross-Validation vs Test Performance

The selected configuration achieved a mean CV Average Precision of **0.8111** and a final test Average Precision of **0.7968**.

The difference is approximately **0.0143**.

This represents a modest generalization gap rather than a dramatic collapse in performance.

However, the difference should still be monitored in later experiments, particularly as model complexity and tuning become more extensive.

---

## 9. Key Findings

1. XGBoost hyperparameters were tuned without using the test set for model selection.
2. Temporal cross-validation was performed using training data only.
3. The selected model used `max_depth=3`, `learning_rate=0.2`, `n_estimators=300`, and `scale_pos_weight=545.39`.
4. The selected configuration achieved mean CV Average Precision of 0.8111.
5. Final test Average Precision was 0.7968.
6. Precision and F1 improved relative to the Day 8 baseline.
7. Recall decreased slightly.
8. Average Precision decreased slightly relative to the Day 8 baseline.
9. Therefore, the tuning pass did not improve the project's primary metric.
10. The experiment demonstrates why model selection should be based on the predefined primary metric rather than whichever metric happens to increase.

---

## 10. Limitations

This was intentionally a small first tuning pass.

Only four hyperparameters were explored, with a limited candidate range and 20 randomly sampled configurations.

The experiment also changed the imbalance strategy from Day 8's SMOTE approach to XGBoost's `scale_pos_weight`, so differences from Day 8 cannot be attributed purely to hyperparameter tuning.

Further experimentation should isolate these factors more carefully.

---

## 11. Conclusion

Pass 1 established a strong tuned XGBoost configuration and demonstrated a useful precision-recall trade-off.

However, because Average Precision decreased slightly from 0.7999 to 0.7968, this configuration does not replace the Day 8 model based on the project's primary metric alone.

The next stage should investigate whether the model's decision threshold can be optimized for the project's fraud-detection objective and whether further controlled tuning can improve Average Precision without unnecessarily increasing false-positive alerts.
