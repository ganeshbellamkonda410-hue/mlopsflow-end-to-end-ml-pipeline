# MLOpsFlow — End-to-End Machine Learning Pipeline

MLOpsFlow is a production-grade machine learning project that automates the complete ML lifecycle: data ingestion, validation, preprocessing, feature engineering, model training, experiment tracking, evaluation, and deployment.

This project predicts student dropout risk using an XGBoost classifier and exposes the trained model through a FastAPI prediction API.

---

## Features

- End-to-end ML pipeline
- Data validation and preprocessing
- Feature engineering
- XGBoost model training
- MLflow experiment tracking
- Model metrics report
- FastAPI prediction endpoint
- Dockerized deployment
- PostgreSQL service included for production-style architecture
- Airflow DAG for orchestration

---

## Tech Stack

**Machine Learning:** Python, scikit-learn, XGBoost  
**MLOps:** MLflow, Apache Airflow  
**API:** FastAPI  
**Database:** PostgreSQL  
**Deployment:** Docker, Docker Compose  

---

## Architecture

```text
CSV Dataset
    ↓
Data Ingestion
    ↓
Data Validation
    ↓
Preprocessing
    ↓
Feature Engineering
    ↓
Model Training
    ↓
MLflow Tracking
    ↓
Evaluation Report
    ↓
FastAPI Model Serving
    ↓
Prediction API
```

---

## Project Structure

```text
mlopsflow-end-to-end-ml-pipeline/
├── airflow/
│   └── dags/
│       └── ml_pipeline_dag.py
├── app/
│   ├── main.py
│   ├── predict.py
│   └── schema.py
├── data/
│   ├── raw/
│   │   └── students.csv
│   └── processed/
├── models/
├── pipelines/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── evaluation.py
│   └── run_pipeline.py
├── reports/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/mlopsflow-end-to-end-ml-pipeline.git
cd mlopsflow-end-to-end-ml-pipeline
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the ML pipeline

```bash
python -m pipelines.run_pipeline
```

This command will:
- Load dataset
- Validate data
- Create features
- Train XGBoost model
- Save trained model
- Generate metrics report

### 5. Start FastAPI

```bash
uvicorn app.main:app --reload
```

Open API docs:

```text
http://localhost:8000/docs
```

---

## Docker Setup

```bash
docker-compose up --build
```

FastAPI:

```text
http://localhost:8000/docs
```

MLflow:

```text
http://localhost:5000
```

PostgreSQL:

```text
localhost:5432
```

---

## API Example

### POST `/predict`

Request:

```json
{
  "attendance": 82,
  "assignments_completed": 7,
  "exam_score": 74,
  "engagement_score": 65
}
```

Response:

```json
{
  "dropout_risk": "Low",
  "confidence": 0.91,
  "risk_probability": 0.09
}
```

---

## MLflow Tracking

To start MLflow manually:

```bash
mlflow ui
```

Open:

```text
http://localhost:5000
```

Tracked items:
- Model parameters
- Accuracy
- Precision
- Recall
- F1-score
- Trained model artifact

---

## Airflow DAG

The project includes an Airflow DAG:

```text
airflow/dags/ml_pipeline_dag.py
```

DAG task:

```text
run_training_pipeline
```

This can be used to orchestrate the full ML pipeline in a production-like environment.

---

## Portfolio Description

Built a production-grade MLOps pipeline that automates data ingestion, validation, preprocessing, feature engineering, model training, evaluation, experiment tracking, and deployment. Integrated MLflow for experiment tracking, FastAPI for real-time inference, Docker for containerized deployment, and Airflow DAG for pipeline orchestration.

---

## Resume Bullets

- Built an end-to-end MLOps pipeline using Python, XGBoost, MLflow, FastAPI, Docker, and Airflow to automate model training, evaluation, and deployment workflows.
- Implemented data validation, preprocessing, and feature engineering modules to improve model readiness and ensure clean training data.
- Integrated MLflow experiment tracking to log parameters, metrics, and model artifacts for reproducible model lifecycle management.
- Developed a FastAPI prediction service for real-time student dropout risk inference and containerized the application using Docker Compose.

---

## Future Improvements

- Add AWS S3 model storage
- Add CI/CD with GitHub Actions
- Add model monitoring and drift detection
- Add frontend dashboard
- Deploy to AWS ECS or Kubernetes

---

## Author

Nivas Ramagiri
