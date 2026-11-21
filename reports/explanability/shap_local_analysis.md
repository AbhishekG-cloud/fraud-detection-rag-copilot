# Local SHAP Analysis

## Objective

Analyze three held-out test transactions representing:
- True Positive
- False Positive
- False Negative

using local SHAP explanations from the locked XGBoost V1 model.

## Transaction 1 — True Positive

- Index: 276864
- Actual: 1
- Predicted: 1
- Fraud probability: 0.999998

### Main positive contributors

- V14: +6.341073
- V10: +2.545474
- V12: +2.346457
- V21: +1.050674
- Amount: +0.865655

### Main negative contributors

- V2: -1.174053

### Interpretation

[Your interpretation based on the actual SHAP values.]

---

## Transaction 2 — False Positive

- Index: 274467
- Actual: 0
- Predicted: 1
- Fraud probability: 0.999507

### Main positive contributors

- V14: +6.188727
- V10: +1.791351
- V12: +0.818303
- V4: +0.591288
- V3: +0.551695

### Main negative contributors

- V28: -0.979347
- Time: -0.748909
- V2: -0.696630
- V5: -0.651438

### Interpretation

[Your interpretation based on the actual SHAP values.]

---

## Transaction 3 — False Negative

- Index: 274475
- Actual: 1
- Predicted: 0
- Fraud probability: 0.360186

### Main positive contributors

- V14: +2.157101
- V10: +1.891955
- V3: +0.569120
- V16: +0.504067

### Main negative contributors

- V2: -1.859705
- V28: -1.397488
- V8: -1.061127
- Time: -0.949759
- Amount: -0.567232
- V9: -0.442244

### Interpretation

[Your interpretation based on the actual SHAP values.]

---

## Overall Observations

1. V14 was a dominant contributor in all three transactions.
2. The TP and FP received very strong positive contributions from V14.
3. The FP demonstrates that strong model confidence does not guarantee correctness.
4. The FN contained meaningful fraud-oriented evidence, but several strong negative SHAP contributions pushed the prediction toward legitimate.
5. Local explanations reveal transaction-specific behavior that cannot be obtained from a global feature ranking alone.

## Limitations

- SHAP explains model behavior, not causality.
- V1-V28 are anonymized PCA components, so their business meaning cannot be inferred.
- Three transactions are illustrative and cannot characterize all model errors.
- Local explanations should be interpreted alongside model performance and broader error analysis.