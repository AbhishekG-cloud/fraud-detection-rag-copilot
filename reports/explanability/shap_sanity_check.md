# SHAP Sanity Check — V1

* **Consistent dominant feature:** `V14` is the strongest local contributor in the TP (`+6.341`), FP (`+6.189`), and remains an important contributor in the FN (`+2.157`). This is broadly consistent with the Day 13 global SHAP analysis identifying V14 as an influential feature. However, this reflects predictive influence, not causality.

* **Different transactions produce different explanations:** The FN demonstrates that a feature can support fraud while other features simultaneously push strongly away from fraud. In this case, `V14` and `V10` pushed toward fraud, while `V2`, `V28`, `V8`, and `Time` pushed away from fraud. This is reasonable model behavior because predictions depend on the combined feature evidence rather than one feature alone.

* **False-positive behavior is worth monitoring:** The FP received an extremely high fraud probability (`0.999507`) despite being legitimate. Strong positive contributions from `V14`, `V10`, `V12`, `V4`, and `V3` outweighed several negative contributions. This suggests that some legitimate transactions can contain feature patterns that the model strongly associates with fraud.

* **No direct evidence of leakage or data-quality problems was identified from the SHAP analysis alone:** The observed explanations do not by themselves establish leakage, poor data quality, or overfitting. These issues require separate validation using the data pipeline, evaluation results, and broader error analysis.

* **PCA limitation:** `V1`–`V28` are anonymized PCA components. Their predictive influence can be discussed, but their underlying real-world/business meanings cannot be inferred from the SHAP results. SHAP explains the behavior of the trained model and does not establish causal relationships.
