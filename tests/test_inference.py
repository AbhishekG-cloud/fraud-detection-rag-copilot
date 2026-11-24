
from demo_transactions import LEGIT, FRAUD

from src.pipeline.predict_pipeline import (
    CustomData,
    PredPipeline
)


def run_prediction(transaction, label):

    # Remove the target column.
    transaction = transaction.copy()
    transaction.pop("Class", None)

    # Convert transaction into the expected DataFrame.
    data = CustomData(**transaction)
    features = data.get_data_as_dataframe()

    # Run the saved model pipeline.
    pipeline = PredPipeline()
    prediction, probability = pipeline.predict(features)

    fraud_probability = float(probability[0][1])

    print(f"\n{'=' * 45}")
    print(f"TRANSACTION: {label}")
    print(f"{'=' * 45}")

    print("Prediction:", int(prediction[0]))
    print(f"Fraud Probability: {fraud_probability:.6f}")
    print(f"Fraud Probability: {fraud_probability * 100:.2f}%")

    return int(prediction[0]), fraud_probability


if __name__ == "__main__":

    run_prediction(LEGIT, "LEGITIMATE EXAMPLE")
    run_prediction(FRAUD, "FRAUD EXAMPLE")
