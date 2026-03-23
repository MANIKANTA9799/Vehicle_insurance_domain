# 🚗 Vehicle Insurance MLOps Pipeline

This is my **first industry-grade, end-to-end MLOps project**, where I built a complete machine learning pipeline for vehicle insurance data. The goal of this project was to go beyond basic model building and implement a **production-level system** covering data pipelines, cloud deployment, and CI/CD automation.

---

## 📌 Project Overview

In this project, I designed and implemented a full ML lifecycle pipeline:

Data Ingestion → Data Validation → Data Transformation → Model Training → Model Evaluation → Model Deployment → CI/CD Automation

The system is modular, scalable, and follows industry best practices for real-world machine learning systems.

---

## 📁 Project Setup and Structure

### Step 1: Project Template
I initialized the project using a custom template.py to generate a clean folder structure and reusable components.

### Step 2: Package Management
Configured local package imports using:
- setup.py
- pyproject.toml

### Step 3: Virtual Environment & Dependencies
conda create -n vehicle python=3.10 -y  
conda activate vehicle  
pip install -r requirements.txt  
pip list  

---

## 📊 MongoDB Setup and Data Management

### Step 4: MongoDB Atlas Configuration
- Created a cloud cluster (M0 free tier)
- Configured authentication and IP access
- Stored connection string securely

### Step 5: Data Ingestion to MongoDB
- Used Jupyter notebook (mongoDB_demo.ipynb) to push dataset
- Verified data inside MongoDB Atlas collections

---

## 📝 Logging, Exception Handling, and EDA

### Step 6: Logging & Exception Handling
I implemented custom logging and exception handling modules to ensure robustness and traceability across the pipeline.

### Step 7: Exploratory Data Analysis & Feature Engineering
- Performed EDA in notebooks
- Engineered features for model training
- Converted notebook logic into reusable pipeline components

---

## 📥 Data Ingestion Pipeline

### Step 8: Data Ingestion
- Built MongoDB connection utilities (configuration.mongo_db_connections.py)
- Implemented ingestion logic in data_access and components.data_ingestion.py
- Defined ingestion configs and artifacts

### Environment Variables
# bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."

# powershell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>...."

---

## 🔍 Data Validation, Transformation & Model Training

### Step 9: Data Validation
- Defined schema in config.schema.yaml
- Implemented validation logic

### Step 10: Data Transformation
- Built transformation pipeline
- Created estimator logic for training

### Step 11: Model Training
- Trained ML model using structured pipeline components
- Ensured reproducibility and modular design

---

## 🌐 AWS Setup for Model Evaluation & Deployment

### Step 12: AWS Setup
- Configured IAM user with required permissions
- Set AWS credentials as environment variables

export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"  
export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"  

### Step 13: Model Storage (S3)
- Created S3 bucket for model storage
- Implemented push/pull logic for model versioning

---

## 🚀 Model Evaluation, Deployment & Prediction Pipeline

### Step 14: Model Evaluation & Pusher
- Built evaluation pipeline
- Implemented model deployment logic

### Step 15: Prediction Pipeline & API
- Developed app.py for serving predictions
- Created basic web interface using templates and static files

---

## 🔄 CI/CD Pipeline (Docker + GitHub Actions + AWS)

### Step 16: Docker & GitHub Actions
- Containerized application using Docker
- Automated workflows using GitHub Actions
- Stored secrets securely (AWS keys, region, ECR repo)

### Step 17: AWS EC2 & ECR
- Deployed container using EC2 instance
- Configured EC2 as self-hosted GitHub runner
- Used ECR for container registry

### Step 18: Final Deployment
- Opened port 5080 on EC2
- Accessed deployed app via:
http://<public_ip>:5080

---

## 🛠️ Tech Stack

- Python  
- MongoDB Atlas  
- AWS (S3, EC2, ECR, IAM)  
- Docker  
- GitHub Actions (CI/CD)  
- Scikit-learn / ML pipeline components  

---

## 🎯 Key Highlights

- Built a complete end-to-end ML pipeline  
- Implemented production-level modular architecture  
- Integrated cloud storage and deployment (AWS)  
- Designed CI/CD automation pipeline  
- Developed API + UI for model inference  

---

## 💡 Learnings

This project helped me understand how machine learning systems work in real production environments, including:
- Backend engineering for ML systems  
- Cloud deployment and infrastructure  
- Automation using CI/CD pipelines  
- Designing scalable and maintainable ML workflows  

---

## 🚀 Future Work

This is my first full-scale industry-style project. I plan to:
- Improve scalability and monitoring  
- Add experiment tracking (MLflow)  
- Enhance model performance and versioning  
- Build more advanced MLOps systems  

---

## 📬 Connect

If you found this project interesting or have any suggestions, feel free to connect with me!
