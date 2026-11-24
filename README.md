# Credit Card Fraud Detection System
[![CI](https://github.com/AbhishekG-cloud/fraud-detection-xgboost-mlops/actions/workflows/main.yaml/badge.svg)](https://github.com/AbhishekG-cloud/fraud-detection-xgboost-mlops/actions/workflows/main.yaml)

An end-to-end machine learning application for detecting fraudulent credit card transactions using XGBoost, with SHAP-based explainability and an interactive Streamlit interface.

**Live Demo:** https://fraud-detection-rag-copilot-mcc4pvckeztjpn8tov62dx.streamlit.app/

**GitHub:** https://github.com/AbhishekG-cloud/fraud-detection-xgboost-mlops

## 1. Project Overview

Credit card fraud detection is a highly imbalanced binary classification problem. Fraudulent transactions account for only a tiny fraction of all transactions, making conventional accuracy-based evaluation unreliable.

This project implements an end-to-end fraud detection pipeline that combines:

- XGBoost for fraud classification.
- Class-weight adjustment for handling class imbalance.
- Time-based validation to respect transaction chronology.
- SHAP (SHapley Additive exPlanations) for model interpretability.
- Streamlit for interactive predictions and explanations.
- Docker for application containerization.

The application allows users to explore sample transactions, obtain fraud predictions, and understand which features contributed to the model's output.
## 2 Application Preview


### Application Interface

![Application Landing Page](screenshots/Landing%20page.png)

### Legitimate Transaction Prediction

![Legitimate Transaction](screenshots/Legitimate%20trans.png)

### Fraudulent Transaction Prediction

![Fraudulent Transaction](screenshots/Fraud%20trans.png)

## 3. Problem Statement

The objective is to identify fraudulent credit card transactions while balancing two competing requirements:

- Detect as many fraudulent transactions as possible.
- Minimize false positive predictions on legitimate transactions.

With an extremely low fraud prevalence, the model must learn meaningful patterns rather than simply favoring the majority class.

## 4. Dataset

**Source:** [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

| Attribute | Description |
|---|---|
| Total transactions | 284,807 |
| Fraudulent transactions | 492 |
| Legitimate transactions | 284,315 |
| Fraud prevalence | Approximately 0.172% |
| Features | 30 |
| Target | Class |

### Feature Description

- `V1–V28`: Anonymized features obtained through PCA transformation.
- `Time`: Seconds elapsed between each transaction and the first transaction in the dataset.
- `Amount`: Transaction amount.
- `Class`: Target variable (0 = Legitimate, 1 = Fraudulent).

## 5. Machine Learning Pipeline

The project follows a modular machine learning pipeline:

1. Data ingestion and exploration.
2. Data quality assessment.
3. Feature preprocessing.
4. Baseline model development.
5. Imbalance-aware model training.
6. Hyperparameter optimization.
7. Time-based model evaluation.
8. Model serialization and inference.
9. SHAP-based explainability.

### Models Evaluated

The experimentation included baseline classification approaches such as:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

**Final selected model:** XGBoost Classifier.

## 6. Handling Class Imbalance

Fraudulent transactions represent approximately 0.17% of the dataset.

The project uses:

- Class-weight adjustment through `scale_pos_weight`.
- XGBoost-based classification.
- Hyperparameter tuning.
- Precision-Recall evaluation.
- Time-based validation using chronological transaction ordering.

The final model uses class weighting rather than relying on synthetic oversampling in the selected configuration.

### Why Average Precision?

Accuracy can be misleading in highly imbalanced classification.

Average Precision (AP), which summarizes the precision-recall curve, provides a more informative evaluation of how well the model identifies the minority fraud class.

## 7. Model Performance

The following are previously recorded evaluation results for the selected XGBoost model.

| Metric | Score |
|---|---:|
| Precision | 0.8235 |
| Recall | 0.7467 |
| F1 Score | 0.7832 |
| Average Precision | 0.7968 |

These are historical recorded results and have not been independently reproduced as part of this deployment.

## 8. Model Explainability with SHAP

A fraud prediction alone does not explain why a transaction was classified as fraudulent.

To address this, the project integrates SHAP using `TreeExplainer`.

For each prediction, the application provides:

- Predicted fraud probability.
- Predicted transaction classification.
- Top five contributing features.
- Direction of each feature's contribution.
- SHAP contribution visualization.

Feature contributions are categorized as:

- `toward_fraud`
- `away_from_fraud`
- `neutral`

**Important:** SHAP values represent contributions to the model's raw output, not direct percentage-point changes in predicted fraud probability.

The original V1–V28 features are anonymized PCA components, so their individual real-world financial meanings are not directly interpretable.

## 9. Application Architecture

```text
                Transaction Input
                       |
                       v
               Streamlit Frontend
                       |
                       v
                Prediction Pipeline
                       |
                +------+------+
                |             |
                v             v
           Preprocessor    XGBoost Model
                |             |
                +------+------+
                       |
                       v
                 Prediction
                       |
                       v
                 SHAP Explainer
                       |
                       v
              Structured Explanation
                       |
                       v
               Streamlit Results
```

### Main Project Structure

```text
fraud-detection-xgboost-mlops/
│├── .github/
│   └── workflows/
│       └── main.yaml
├── artifacts/
├── screenshots/
├── tests/
│   ├── test_inference.py
│   ├── test_pipeline_explanation.py
│   └── test_shap.py
├── app_streamlit.py
├── app.py
├── demo_transactions.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── configs/
│   └── xgboost_v1.yaml
│
├── docs/
│   └── shap_explanation_schema.md
│
├── layer1_fraud/
│   └── explainability/
│       └── shap_explaner.py
│
├── notebooks/
│   ├── 01_dataset_overview.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_data_quality.ipynb
│   ├── 04_baseline_models.ipynb
│   ├── 05_smote_training.ipynb
│   ├── 06_xgboost_baseline.ipynb
│   ├── 07_xgboost_tuning_pass1.ipynb
│   ├── 08_v1_final_evaluation.ipynb
│   ├── 09_v1_shap_global.ipynb
│   ├── 10_shap_explanation_function.ipynb
│   └── 11_v1_error_analysis.ipynb
│
├── src/
│   ├── components/
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── reports/
│

```

## 10. Deployment

### Streamlit Community Cloud

The application is publicly deployed using Streamlit Community Cloud.

**Live Application:** [Launch Fraud Detection System](https://fraud-detection-rag-copilot-mcc4pvckeztjpn8tov62dx.streamlit.app/)

### Docker Containerization

The application is configured to run inside a Docker container.

Build the image:

```bash
docker build -t credit-card-fraud:v1 .
```

Run the container:

```bash
docker run -d \
  --name fraud_test \
  -p 8501:8501 \
  credit-card-fraud:v1
```

Check application health:

```bash
curl http://localhost:8501/_stcore/health
```

The application runs on port `8501`.

### CI/CD

GitHub Actions is configured to automate the continuous integration workflow.

The workflow performs:

- Python environment setup.
- Dependency installation.
- Automated pytest execution.
- Docker image build verification.

The workflow runs on pushes and pull requests targeting the `main` branch.

The application is deployed separately through Streamlit Community Cloud. AWS-based deployment is currently inactive.

## 11. Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | NumPy, Pandas |
| Machine Learning | Scikit-learn, XGBoost |
| Explainability | SHAP |
| Frontend | Streamlit |
| Model Serialization | Dill, Pickle |
| Containerization | Docker |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |
| CI/CD | GitHub Actions (Automated Testing & Docker Build) |

## 12. Limitations

- The dataset contains anonymized PCA-transformed features.
- The model is trained on a historical dataset and may not generalize to current fraud patterns.
- The application uses sample transactions rather than a live banking transaction feed.
- No real-time model monitoring or automated retraining system is implemented.
- SHAP explanations indicate model behavior, not causal relationships.
- This application is a portfolio demonstration, not a production banking fraud prevention system.

## 13. Future Work

### Fraud Investigator Copilot — Planned Extension

The next planned development is a RAG-based Fraud Investigator Copilot.

The intended architecture will use structured SHAP explanation outputs as input to a retrieval-augmented generation system.

Potential capabilities:

- Generate natural-language transaction investigation reports.
- Summarize important fraud indicators.
- Retrieve relevant fraud investigation documentation.
- Assist analysts in interpreting model predictions.
- Produce structured investigation summaries.

This extension is planned and is not part of the current deployed application.

## 14. Author

**Abhishek Goswami**

M.Sc. Mathematics | NIT Kurukshetra

Interested in Machine Learning, Applied Mathematics, and Data Science.

- GitHub: [AbhishekG-cloud](https://github.com/AbhishekG-cloud)
- Project: [Credit Card Fraud Detection](https://github.com/AbhishekG-cloud/fraud-detection-xgboost-mlops)

---

*Built as an end-to-end machine learning portfolio project, with an emphasis on imbalanced classification, model interpretability, and deployment.*