
import streamlit as st
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredPipeline
from demo_transactions import LEGIT, FRAUD


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 2. CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* Main application */

.stApp {
    background-color: #0B1120;
    color: #E5E7EB;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}

/* Typography */

h1, h2, h3 {
    color: #F8FAFC !important;
    font-weight: 650 !important;
}

p, li {
    color: #CBD5E1;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #263449;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #F8FAFC !important;
}

/* Metrics */

[data-testid="stMetric"] {
    background-color: #151F32;
    border: 1px solid #263449;
    padding: 18px;
    border-radius: 12px;
}

[data-testid="stMetricLabel"] {
    color: #94A3B8 !important;
}

[data-testid="stMetricValue"] {
    color: #38BDF8 !important;
}

/* Buttons */

.stButton > button {
    background-color: #17243A;
    color: #E2E8F0;
    border: 1px solid #334155;
    border-radius: 9px;
    padding: 0.65rem 1rem;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #164E63;
    border-color: #22D3EE;
    color: white;
}

.stButton > button[kind="primary"] {
    background-color: #0891B2;
    border: 1px solid #06B6D4;
    color: white;
}

.stButton > button[kind="primary"]:hover {
    background-color: #0E7490;
}

/* Dataframes */

[data-testid="stDataFrame"] {
    border: 1px solid #263449;
    border-radius: 10px;
    overflow: hidden;
}

/* Dividers */

hr {
    border-color: #263449 !important;
}

/* Alerts */

[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Section labels */

.section-label {
    color: #38BDF8;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

/* Hero header */

.hero-container {
    background: linear-gradient(110deg, #14243B, #102D42);
    border: 1px solid #164E63;
    border-radius: 16px;
    padding: 32px;
    margin-bottom: 30px;
}

.hero-title {
    color: #F8FAFC;
    font-size: 35px;
    font-weight: 750;
    margin-top: 14px;
    margin-bottom: 5px;
}

.hero-subtitle {
    color: #94A3B8;
    font-size: 14px;
    margin-top: 10px;
    line-height: 1.8;
}

.status-indicator {
    color: #34D399;
    font-size: 13px;
    font-weight: 600;
    margin-top: 22px;
}

/* KPI cards */

.dashboard-card {
    background-color: #151F32;
    border: 1px solid #263449;
    border-radius: 12px;
    padding: 20px;
    min-height: 125px;
    box-sizing: border-box;
}

.dashboard-card-title {
    color: #94A3B8;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

.dashboard-card-value {
    color: #38BDF8;
    font-size: 25px;
    font-weight: 700;
    margin-top: 10px;
}

.dashboard-card-description {
    color: #94A3B8;
    font-size: 12px;
    margin-top: 5px;
}

/* Footer */

.footer {
    text-align: center;
    color: #64748B;
    font-size: 12px;
    padding: 25px 0 10px 0;
    line-height: 2;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 💳 FraudGuard")

    st.caption("Intelligent Transaction Monitoring")

    st.divider()

    st.markdown("### System Overview")

    st.markdown("""
    An ML-powered credit card fraud
    detection application designed to
    identify suspicious transactions
    using an XGBoost classifier.
    """)

    st.divider()

    st.markdown("### Model Information")

    st.markdown("""
    **Algorithm:** XGBoost

    **Explainability:** SHAP

    **Problem:** Binary Classification

    **Dataset:** Kaggle ULB

    **Fraud Rate:** 0.17%
    """)

    st.divider()

    st.markdown("### Technology Stack")

    st.markdown("""
    - Python
    - Pandas
    - Scikit-learn
    - XGBoost
    - SHAP
    - Streamlit
    """)

    st.divider()

    st.caption("Credit Card Fraud Detection System")
    st.caption("Machine Learning Project | 2026")


# ============================================================
# 4. MAIN DASHBOARD HEADER
# IMPORTANT: Use st.html(), NOT st.markdown()
# ============================================================

st.html("""
<div class="hero-container">

    <div class="section-label">
        MACHINE LEARNING • FINANCIAL SECURITY
    </div>

    <div class="hero-title">
        Credit Card Fraud Detection
    </div>

    <div class="hero-subtitle">
        Intelligent transaction classification and
        explainable fraud analysis powered by XGBoost and SHAP.
    </div>

    <div class="status-indicator">
        ● MODEL INTERFACE READY
    </div>

</div>
""")


# ============================================================
# 5. ABOUT THE PROJECT
# ============================================================

st.markdown(
    '<div class="section-label">PROJECT OVERVIEW</div>',
    unsafe_allow_html=True
)

st.subheader("About This Project")

st.markdown("""
This application predicts whether a credit card transaction is fraudulent
using an XGBoost classifier trained on the Kaggle Credit Card Fraud Detection Dataset.

- **Dataset:** 284,807 transactions
- **Fraud rate:** 0.17%
- **Model:** XGBoost Classifier
- **Explainability:** SHAP
""")

st.divider()


# ============================================================
# 6. DATASET OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-label">DATASET OVERVIEW</div>',
    unsafe_allow_html=True
)

st.subheader("Model and Dataset Snapshot")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.html("""
    <div class="dashboard-card">
        <div class="dashboard-card-title">
            Total Transactions
        </div>
        <div class="dashboard-card-value">
            284,807
        </div>
        <div class="dashboard-card-description">
            Dataset observations
        </div>
    </div>
    """)

with kpi2:
    st.html("""
    <div class="dashboard-card">
        <div class="dashboard-card-title">
            Fraud Rate
        </div>
        <div class="dashboard-card-value">
            0.17%
        </div>
        <div class="dashboard-card-description">
            Highly imbalanced dataset
        </div>
    </div>
    """)

with kpi3:
    st.html("""
    <div class="dashboard-card">
        <div class="dashboard-card-title">
            ML Algorithm
        </div>
        <div class="dashboard-card-value">
            XGBoost
        </div>
        <div class="dashboard-card-description">
            Gradient boosting classifier
        </div>
    </div>
    """)

with kpi4:
    st.html("""
    <div class="dashboard-card">
        <div class="dashboard-card-title">
            Explainability
        </div>
        <div class="dashboard-card-value">
            SHAP
        </div>
        <div class="dashboard-card-description">
            Feature-level interpretation
        </div>
    </div>
    """)

st.divider()


# ============================================================
# 7. TRANSACTION SELECTION
# ============================================================

st.markdown(
    '<div class="section-label">TRANSACTION ANALYSIS</div>',
    unsafe_allow_html=True
)

st.subheader("Select a Transaction")

st.caption(
    "Choose a sample transaction to evaluate its fraud probability "
    "and inspect the model's explanation."
)

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🟢 Load Legitimate Example",
        use_container_width=True
    ):

        st.session_state.transaction = LEGIT

with col2:

    if st.button(
        "🔴 Load Fraud Example",
        use_container_width=True
    ):

        st.session_state.transaction = FRAUD


# ============================================================
# 8. SELECTED TRANSACTION
# ============================================================

if "transaction" in st.session_state:

    txn = st.session_state.transaction.copy()

    st.subheader("Selected Transaction")

    display_data = txn.copy()
    display_data.pop("Class", None)

    st.dataframe(
        pd.DataFrame([display_data]),
        use_container_width=True
    )

    st.caption(
        "Review the selected transaction features before running the analysis."
    )


    # ========================================================
    # 9. PREDICTION ENGINE
    # ORIGINAL LOGIC PRESERVED
    # ========================================================

    if st.button(
        "🔍 Predict and Explain",
        type="primary"
    ):

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


            # ====================================================
            # 10. PREDICTION RESULTS
            # ====================================================

            st.divider()

            st.markdown(
                '<div class="section-label">MODEL OUTPUT</div>',
                unsafe_allow_html=True
            )

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

                st.error("🚨 Fraudulent Transaction Detected")

            else:

                st.success("✓ Legitimate Transaction")


            # ====================================================
            # 11. FRAUD PROBABILITY INDICATOR
            # ====================================================

            st.markdown("### Fraud Probability Indicator")

            st.progress(
                max(
                    0.0,
                    min(
                        1.0,
                        float(fraud_probability / 100)
                    )
                )
            )

            st.caption(
                f"Model-estimated fraud probability: "
                f"{fraud_probability:.2f}%"
            )

            st.divider()


            # ====================================================
            # 12. SHAP EXPLANATION
            # ORIGINAL LOGIC PRESERVED
            # ====================================================

            st.markdown(
                '<div class="section-label">MODEL INTERPRETABILITY</div>',
                unsafe_allow_html=True
            )

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


            # ====================================================
            # 13. SHAP FEATURE TABLE
            # ====================================================

            st.markdown("### Top Contributing Features")

            st.dataframe(
                explanation_df,
                use_container_width=True,
                hide_index=True
            )


            # ====================================================
            # 14. SHAP CONTRIBUTION CHART
            # ====================================================

            st.subheader("Feature Contribution Chart")

            chart_df = explanation_df[
                ["Feature", "SHAP Value"]
            ].set_index("Feature")

            st.bar_chart(chart_df)


            # ====================================================
            # 15. SHAP INTERPRETATION NOTE
            # ====================================================

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


# ============================================================
# 16. FOOTER
# IMPORTANT: Use st.html()
# ============================================================

st.divider()

st.html("""
<div class="footer">

    <b>FraudGuard | Credit Card Fraud Detection System</b>

    <br><br>

    Powered by XGBoost • Explained using SHAP • Built with Streamlit

    <br>

    Machine Learning Project | 2026

</div>
""")
