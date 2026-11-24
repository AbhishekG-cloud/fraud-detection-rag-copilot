
import pandas as pd

from demo_transactions import LEGIT, FRAUD
from src.utils import load_object
from src.pipeline.predict_pipeline import CustomData
from layer1_fraud.explainability.shap_explaner import SHAPExplainer


# Load saved artifacts
model = load_object("artifacts/model.pkl")
preprocessor = load_object("artifacts/preprocessor.pkl")


def explain_transaction(transaction, transaction_id):

    transaction = transaction.copy()
    transaction.pop("Class", None)

    # Convert into DataFrame
    data = CustomData(**transaction)
    raw_features = data.get_data_as_dataframe()

    # Apply the same preprocessing used during inference
    transformed = preprocessor.transform(raw_features)

    # Preserve feature names if the transformer exposes them
    if hasattr(preprocessor, "get_feature_names_out"):
        columns = preprocessor.get_feature_names_out()
    else:
        columns = raw_features.columns

    X = pd.DataFrame(
        transformed,
        columns=columns,
        index=[transaction_id]
    )

    # Generate SHAP explanation
    explainer = SHAPExplainer(
        model=model,
        X_test=X
    )

    result = explainer.get_shap_explanation(
        transaction_id=transaction_id,
        top_k=5
    )

    print(f"\n{'=' * 45}")
    print("SHAP EXPLANATION:", transaction_id)
    print(f"{'=' * 45}")

    print(result)


if __name__ == "__main__":

    explain_transaction(LEGIT, 0)
    explain_transaction(FRAUD, 1)
