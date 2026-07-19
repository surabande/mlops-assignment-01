# MLOps Assignment 01: Heart Disease Prediction 

**Author:** Suraj Suresh Bande / 2024ac05403
**Repository:** https://github.com/surabande/mlops-assignment-01
**Video Walkthrough:** [Link to your hosted video recording][cite: 2]

---

## 1. Project Overview
This project is an end-to-end machine learning pipeline that predicts the risk of heart disease based on patient health data. It demonstrates modern MLOps best practices, including experiment tracking, automated CI/CD pipelines, containerization, and local Kubernetes deployment.

---

## 2. Setup & Installation Instructions
To run this project locally, ensure you have Python 3.12 and Docker installed.

**1. Clone the repository:**
bash
git clone https://github.com/surabande/mlops-assignment-01
cd mlops-assignment-01

**2. Set up the environment and install dependencies:**
bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

**3. Run the API locally:**
bash
uvicorn api.main:app --reload --host 127.0.0.1 --port 8000

## 3. Exploratory Data Analysis (EDA) Findings
The dataset was acquired from the UCI Machine Learning Repository.
Missing Values: Addressed using median imputation to maintain dataset integrity.

## 4. Modeling Choices & Experiment Tracking
Two classification models were evaluated: Logistic Regression and Random Forest.
-Preprocessing: A robust ColumnTransformer pipeline was utilized to scale numerical features and one-hot encode categorical variables.
-Experiment Tracking: MLflow was integrated to log hyperparameters, accuracy metrics, and the serialized model artifacts.

![alt text](<Screenshot 2026-07-19 at 2.10.43 PM.png>) ![alt text](<Screenshot 2026-07-19 at 2.11.39 PM.png>)

## 5. Architecture Diagram

```mermaid
graph TD
    A[Data Ingestion<br/>UCI Dataset] --> B(Data Preprocessing & Training<br/>Scikit-Learn)
    B --> C[(MLflow<br/>Experiment Tracking)]
    B --> D[FastAPI Application<br/>Model Serving]
    
    D --> E{GitHub Actions<br/>CI/CD Pipeline}
    E -- Pytest Passes --> F[Docker<br/>Containerization]
    
    F --> G[Local Kubernetes<br/>Docker Desktop]
    G --> H[Deployment]
    G --> I[Service / LoadBalancer<br/>Port 8080]
    
    I --> J((Swagger UI / Client<br/>Predictions))

    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef highlight fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    class C,E,F,G highlight;```

## 6. CI/CD Pipeline
An automated GitHub Actions workflow was implemented to ensure code quality and build stability. The pipeline triggers on pushes to the main branch and automates:
1. Environment setup and dependency installation.
2. Unit testing using Pytest.
3. Docker build validation.

![alt text](<Screenshot 2026-07-15 at 2.10.15 AM.png>)

## 7. Production Deployment & Monitoring
The FastAPI application was containerized using Docker and deployed to a local Kubernetes cluster (Docker Desktop).
- Deployment: Managed via deployment.yaml defining the pod specifications.
- Networking: Exposed locally via a LoadBalancer defined in service.yaml.
- Monitoring: Basic monitoring was achieved via stdout API request logging.

Kubernetes Pods & Services:
![alt text](<Screenshot 2026-07-15 at 2.37.16 AM.png>) ![alt text](<Screenshot 2026-07-15 at 2.24.43 AM.png>)

Live API Prediction:
![alt text](<Screenshot 2026-07-15 at 1.03.47 AM.png>)

