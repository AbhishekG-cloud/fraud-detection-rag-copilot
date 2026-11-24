
from demo_transactions import LEGIT, FRAUD
from src.pipeline.predict_pipeline import CustomData, PredPipeline


def test_transaction(transaction, transaction_id):
    input_data = {
        key: value
        for key, value in transaction.items()
        if key != "Class"
    }

    custom_data = CustomData(**input_data)
    features = custom_data.get_data_as_dataframe()

    pipeline = PredPipeline()

    result = pipeline.predict_with_explanation(
        features=features,
        top_k=5
    )

    print(f"\nTRANSACTION {transaction_id}")
    print("=" * 50)
    print(result)


if __name__ == "__main__":
    test_transaction(LEGIT, 0)
    test_transaction(FRAUD, 1)
