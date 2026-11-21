# SHAP Explanation Output Schema

## Purpose

The SHAP explanation function provides a structured, JSON-compatible explanation of an individual transaction's prediction from the locked XGBoost V1 fraud detection model.

The output is designed to be consumed by downstream applications, including the Layer 2 RAG Investigator Copilot.

## Output Structure

```json
{
  "transaction_id": 276864,
  "prediction": 1,
  "fraud_probability": 0.999998,
  "top_features": [
    {
      "feature": "V14",
      "shap_value": 6.341073,
      "direction": "toward_fraud"
    }
  ]
}
```

## Fields

### `transaction_id`

The stable identifier used to locate the transaction in the evaluation dataset.

For the current implementation, this corresponds to the transaction's DataFrame index.

### `prediction`

The binary prediction produced by the locked V1 model.

```text
0 → predicted legitimate
1 → predicted fraud
```

The prediction is determined using the configured V1 classification threshold.

### `fraud_probability`

The model's predicted probability for the fraud class.

This represents the model's prediction score/probability and is distinct from the SHAP value.

### `top_features`

A list containing the most influential features for the individual transaction.

Features are ranked by:

```text
absolute SHAP value
```

rather than by signed SHAP value.

### `feature`

The name of the model input feature.

Examples:

```text
V14
V10
Amount
Time
```

### `shap_value`

The SHAP contribution of the feature to the model output being explained.

* Positive value → contribution toward fraud.
* Negative value → contribution away from fraud.
* Larger absolute value → stronger contribution.

A SHAP value is **not a probability** and should not be interpreted as a percentage change in fraud probability.

### `direction`

Human-readable interpretation of the SHAP sign.

Allowed values:

```text
toward_fraud
away_from_fraud
neutral
```

`neutral` is used when the SHAP contribution is exactly zero.

## Example Interpretation

For:

```json
{
  "feature": "V14",
  "shap_value": 6.341073,
  "direction": "toward_fraud"
}
```

the correct interpretation is:

> V14 made a strong contribution toward the model's fraud prediction for this transaction.

It does **not** mean:

> V14 caused the transaction to be fraudulent.

## PCA Feature Limitation

Features `V1` through `V28` are anonymized PCA components.

The explanation may identify these components as influential, but their underlying business meaning cannot be inferred from the SHAP output alone.

Therefore, downstream applications must not invent semantic descriptions for these features.

## Intended Downstream Use

The structured output can later be incorporated into the Layer 2 retrieval corpus:

```text
Transaction
    ↓
V1 prediction
    ↓
SHAP explanation
    ↓
Structured JSON
    ↓
RAG retrieval context
    ↓
Investigator Copilot
```

The structured representation is preferred over storing only SHAP plots because applications can directly retrieve and process individual feature contributions.

## Design Requirements

The function output must remain:

* JSON serializable
* Consistent across transactions
* Explicit about prediction and probability
* Explicit about SHAP contribution and direction
* Ranked by absolute SHAP magnitude
* Independent of model retraining
* Compatible with downstream RAG processing
