
import sys
import pandas as pd
import os
from dataclasses import dataclass

from src.exception import CustomException
from src.utils import load_object
from layer1_fraud.explainability.shap_explaner import SHAPExplainer


@dataclass
class CustomData:
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

    def get_data_as_dataframe(self):
        return pd.DataFrame([self.__dict__])


class PredPipeline:
    def __init__(self):
        pass

    def _load_artifacts(self):
        model_path = os.path.join("artifacts", "model.pkl")
        preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

        model = load_object(file_path=model_path)
        preprocessor = load_object(file_path=preprocessor_path)

        return model, preprocessor

    def predict(self, features):
        try:
            model, preprocessor = self._load_artifacts()

            transformed_data = preprocessor.transform(features)

            preds = model.predict(transformed_data)
            proba = model.predict_proba(transformed_data)

            return preds, proba

        except Exception as e:
            raise CustomException(e, sys)

    def predict_with_explanation(self, features, top_k=5):
        try:
            model, preprocessor = self._load_artifacts()

            transformed_data = preprocessor.transform(features)

            feature_names = preprocessor.get_feature_names_out()

            transformed_df = pd.DataFrame(
                transformed_data,
                columns=feature_names,
                index=[0]
            )

            explainer = SHAPExplainer(
                model=model,
                X_test=transformed_df
            )

            explanation = explainer.get_shap_explanation(
                transaction_id=0,
                top_k=top_k
            )

            return explanation

        except Exception as e:
            raise CustomException(e, sys)
