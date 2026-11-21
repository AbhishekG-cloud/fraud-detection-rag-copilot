# Layer 1 Error Analysis v1

## Objective

The objective of this analysis is to identify recurring false-positive (FP) and false-negative (FN) behaviors in the locked XGBoost V1 fraud detection model.

The analysis uses the untouched held-out test set and SHAP values to investigate whether particular features repeatedly contribute to incorrect predictions.

No model retraining, tuning, or modification was performed during this analysis.

---

## Error Population

The V1 model was evaluated on the held-out test set.

The error analysis identified:

* **False positives:** 12
* **False negatives:** 19

A false positive is a legitimate transaction predicted as fraud.

A false negative is a fraudulent transaction predicted as legitimate.

Because the number of errors is relatively small, the identified patterns should be treated as observed behaviors in this evaluation sample rather than universal characteristics of the model.

---

# False Positive Patterns

## FP Pattern 1 — Strong V14-driven fraud signal

### Description

V14 was the strongest contributor among the observed false positives.

### SHAP evidence

Across the FP population:

* Mean SHAP: **+3.892**
* Mean absolute SHAP: **4.178**
* Toward-fraud contribution rate: **83.3%**

Therefore, V14 generally contributed strongly toward the fraud prediction for legitimate transactions that were incorrectly flagged.

This is also consistent with the previously analyzed false-positive transaction 274467, where V14 had a SHAP contribution of **+6.189**.

### Interpretation

The observed false positives frequently contain a V14-related model signal that strongly pushes the prediction toward fraud.

This suggests that some legitimate transactions have feature patterns that V1 associates strongly with fraudulent transactions.

### Hypothesis

One possible explanation is that some legitimate transactions occupy regions of feature space that resemble patterns learned from fraudulent observations.

This is a hypothesis and would require further investigation to establish.

---

## FP Pattern 2 — Additional positive contributions from V10 and V4

### Description

In addition to V14, V10 and V4 frequently contributed toward fraud among the observed false positives.

### SHAP evidence

**V10:**

* Mean SHAP: **+0.911**
* Mean absolute SHAP: **1.416**
* Toward-fraud rate: **66.7%**

**V4:**

* Mean SHAP: **+0.860**
* Mean absolute SHAP: **1.220**
* Toward-fraud rate: **75.0%**

### Interpretation

The false-positive errors are not explained solely by V14. V10 and V4 also frequently provide positive contributions toward fraud.

This indicates that some legitimate transactions receive a combination of fraud-oriented evidence across multiple features.

Because XGBoost learns nonlinear feature relationships, these contributions should not be interpreted as independent causal effects.

---

# False Negative Patterns

## FN Pattern 1 — Consistent negative contribution from Time

### Description

Time showed a particularly consistent contribution among the observed false negatives.

### SHAP evidence

* Mean SHAP: **−1.074**
* Mean absolute SHAP: **1.074**
* Toward-fraud rate: **0%**

Therefore, Time contributed away from fraud for **all 19 observed false negatives**.

### Interpretation

Among the observed fraudulent transactions that V1 failed to detect, the Time feature consistently contributed in the non-fraud direction.

This indicates that temporal information was systematically associated with lower model fraud output within this FN sample.

### Hypothesis

A possible explanation is that some fraudulent transactions occur in temporal regions where the learned model provides weaker fraud evidence.

This hypothesis should not be treated as proof that particular times cause missed fraud.

---

## FN Pattern 2 — Repeated non-fraud contributions from V1, V10 and V12

### Description

Several features repeatedly contributed away from fraud among the false negatives.

### SHAP evidence

**V1:**

* Mean SHAP: **−0.913**
* Mean absolute SHAP: **0.972**
* Toward-fraud rate: **15.8%**

**V12:**

* Mean SHAP: **−0.864**
* Mean absolute SHAP: **1.141**
* Toward-fraud rate: **21.1%**

**V10:**

* Mean SHAP: **−0.545**
* Mean absolute SHAP: **0.999**
* Toward-fraud rate: **15.8%**

These features therefore provided negative contributions in most of the observed false negatives.

### Interpretation

A recurring characteristic of the FN population is the presence of feature contributions that push the model toward the legitimate class.

This can create a situation where the transaction contains some fraud-oriented evidence but the combined model evidence is insufficient to cross the classification threshold.

This interpretation is consistent with the previously examined FN transaction 274475, where V14 and V10 provided positive contributions while V2, V28, V8, Time, Amount, and V9 provided negative contributions.

---

# Key Findings

1. **V14 was highly influential among false positives.** It had the highest mean absolute SHAP value among the FP errors and pushed toward fraud in 83.3% of observed cases.

2. **False positives can result from multiple simultaneous fraud-oriented signals.** V10 and V4 also frequently contributed toward fraud, suggesting that some legitimate transactions contain combinations of features that the model considers suspicious.

3. **Time showed a consistent negative contribution among false negatives.** All 19 observed FNs had a negative SHAP contribution from Time, making it a notable candidate for further investigation.

4. **False negatives often contained conflicting evidence.** Features such as V14 could push toward fraud while V1, V10, V12, and Time frequently pushed away from fraud. This demonstrates that a fraud transaction can contain meaningful fraud signals while still receiving an overall legitimate prediction.

5. **The same feature can behave differently across error types.** For example, V10 had a positive mean SHAP contribution among FPs but a negative mean SHAP contribution among FNs. Therefore, feature influence is transaction- and error-context-dependent.

---

# Limitations

* The analysis contains only **12 false positives and 19 false negatives**, so the identified patterns should not be treated as universal model behavior.
* SHAP describes how features contribute to the model's prediction; it does not establish causal relationships.
* The identified patterns are based on the held-out evaluation sample and may not generalize to future transaction populations.
* The PCA-derived features V1–V28 are anonymized, so their real-world business meanings cannot be inferred from the analysis.
* SHAP patterns alone cannot establish data leakage, data-quality problems, or overfitting.
* The analysis does not modify or tune V1. Any model changes motivated by these findings should be treated as new V2 experiments and evaluated using an appropriate validation and evaluation process.
* Further investigation with larger samples and additional transaction-level analysis would be required before taking operational or modeling actions based on these observations.
