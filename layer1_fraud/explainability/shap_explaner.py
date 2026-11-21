import numpy as np
import pandas as pd
import shap


class SHAPExplainer:

    def __init__(self, model, X_test):
        self.model = model
        self.X_test = X_test
        self.explainer = shap.TreeExplainer(model)

    def get_shap_explanation(self, transaction_id, top_k=5):
        if transaction_id not in self.X_test.index:
            raise ValueError(
                f"Transaction ID {transaction_id} not found in test data."
            )

        if top_k <= 0:
            raise ValueError("top_k must be greater than 0.")

        transaction = self.X_test.loc[[transaction_id]]

        shap_explanation = self.explainer(transaction)
        shap_values = shap_explanation.values[0]

        probabilities = self.model.predict_proba(transaction)[0]
        fraud_probability = float(probabilities[1])

        prediction = int(fraud_probability >= 0.5)

        explanation = pd.DataFrame({
            "feature": self.X_test.columns,
            "shap_value": shap_values
        })

        explanation["abs_shap"] = explanation["shap_value"].abs()

        explanation = (
            explanation
            .sort_values("abs_shap", ascending=False)
            .head(top_k)
        )

        top_features = []

        for _, row in explanation.iterrows():

            shap_value = float(row["shap_value"])

            if shap_value > 0:
                direction = "toward_fraud"
            elif shap_value < 0:
                direction = "away_from_fraud"
            else:
                direction = "neutral"

            top_features.append({
                "feature": row["feature"],
                "shap_value": shap_value,
                "direction": direction
            })

        return {
            "transaction_id": int(transaction_id),
            "prediction": prediction,
            "fraud_probability": fraud_probability,
            "top_features": top_features
        }