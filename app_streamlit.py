
import streamlit as st
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredPipeline
from demo_transactions import LEGIT, FRAUD


st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.title("Credit Card Fraud Detection System")
st.caption("XGBoost-based fraud detection with SHAP explainability")

st.markdown("""
### About This Project

This application predicts whether a credit card transaction is fraudulent
using an XGBoost classifier trained on the Kaggle Credit Card Fraud Detection Dataset.

- **Dataset:** 284,807 transactions
- **Fraud rate:** 0.17%
- **Model:** XGBoost Classifier
- **Explainability:** SHAP
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("Load Legitimate Example", use_container_width=True):
        st.session_state.transaction = LEGIT

with col2:
    if st.button("Load Fraud Example", use_container_width=True):
        st.session_state.transaction = FRAUD


if "transaction" in st.session_state:

    txn = st.session_state.transaction.copy()

    st.subheader("Selected Transaction")

    display_data = txn.copy()
    display_data.pop("Class", None)

    st.dataframe(
        pd.DataFrame([display_data]),
        use_container_width=True
    )

    if st.button("Predict and Explain", type="primary"):

        try:
            input_data = {
                key: value
                for key, value in txn.items()
                if key != "Class"
            }

            data = CustomData(**input_data)
            pred_df = data.get_data_as_dataframe()

            pipeline = PredPipeline()

            with st.spinner("Analyzing transaction..."):
                result = pipeline.predict_with_explanation(
                    features=pred_df,
                    top_k=5
                )

            prediction = result["prediction"]
            fraud_probability = result["fraud_probability"] * 100

            st.divider()
            st.subheader("Prediction Results")

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric(
                    "Predicted Fraud Probability",
                    f"{fraud_probability:.2f}%"
                )

            with metric2:
                st.metric(
                    "Model Classification",
                    "Fraudulent" if prediction == 1 else "Legitimate"
                )

            if prediction == 1:
                st.error("Fraudulent Transaction Detected")
            else:
                st.success("Legitimate Transaction")

            st.divider()
            st.subheader("SHAP Explanation")

            st.markdown("""
            SHAP identifies how individual features contribute to the
            model's prediction.

            - Positive SHAP value: pushes the prediction toward fraud.
            - Negative SHAP value: pushes the prediction away from fraud.
            """)

            top_features = result["top_features"]

            explanation_df = pd.DataFrame(top_features)

            explanation_df["feature"] = (
                explanation_df["feature"]
                .str.replace("tran_pipeline__", "", regex=False)
            )

            explanation_df = explanation_df.rename(
                columns={
                    "feature": "Feature",
                    "shap_value": "SHAP Value",
                    "direction": "Contribution Direction"
                }
            )

            st.dataframe(
                explanation_df,
                use_container_width=True,
                hide_index=True
            )

            st.subheader("Feature Contribution Chart")

            chart_df = explanation_df[
                ["Feature", "SHAP Value"]
            ].set_index("Feature")

            st.bar_chart(chart_df)

            st.caption(
                "SHAP values represent contributions to the model output "
                "(raw margin), not percentage-point changes in fraud probability. "
                "V1–V28 are anonymized PCA-transformed features."
            )

        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

else:
    st.info(
        "Select a legitimate or fraudulent example to test the model."
    )
