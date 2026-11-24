
import numpy as np
import pytest

from demo_transactions import LEGIT, FRAUD
from src.pipeline.predict_pipeline import CustomData, PredPipeline


@pytest.fixture(scope="module")
def pipeline():
    return PredPipeline()


def run_prediction(pipeline, transaction):
    transaction = transaction.copy()
    transaction.pop("Class", None)

    data = CustomData(**transaction)
    features = data.get_data_as_dataframe()

    prediction, probability = pipeline.predict(features)

    return int(prediction[0]), float(probability[0][1])


def test_legitimate_transaction(pipeline):
    prediction, probability = run_prediction(pipeline, LEGIT)

    assert prediction == 0
    assert 0 <= probability <= 1
    assert np.isfinite(probability)


def test_fraud_transaction(pipeline):
    prediction, probability = run_prediction(pipeline, FRAUD)

    assert prediction == 1
    assert 0 <= probability <= 1
    assert np.isfinite(probability)


def test_prediction_with_shap_explanation(pipeline):
    transaction = LEGIT.copy()
    transaction.pop("Class", None)

    data = CustomData(**transaction)
    features = data.get_data_as_dataframe()

    result = pipeline.predict_with_explanation(
        features=features,
        top_k=5
    )

    assert result is not None
