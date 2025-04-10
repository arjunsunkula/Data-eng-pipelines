# 🚀 ELT Pipeline using Airflow, GCP, BigQuery & Looker Studio

This project showcases the development of a fully automated ELT (Extract, Load, Transform) pipeline using **Apache Airflow**, **Google Cloud Platform (GCP)**, **BigQuery**, and **Looker Studio**.

---

## 📁 Overview

- **Source:** `global_health_data.csv` (uploaded to GCS)
- **Destination:** BigQuery table `lateral-rider-456109-s6.initial_dataset.global_data`
- **Tooling:** Apache Airflow for orchestration, BigQuery for storage, Looker Studio for reporting

---

## 🧱 Architecture

```
Google Cloud Storage
        ↓
   Apache Airflow
        ↓
     BigQuery
        ↓
   Looker Studio
```

---

## ⚙️ Setup Steps

### 1. Airflow Environment on GCP

- Created a GCP VM named `airflow1`
- Installed Python, created virtual environment
- Installed Apache Airflow with GCP provider
- Enabled port 8080 and accessed the Airflow UI
- Configured `airflow.cfg` to hide example DAGs

### 2. GCS Bucket & File Upload

- Created bucket: `airflow-bucket01`
- Uploaded file: `global_health_data.csv`

### 3. BigQuery Integration

- Created dataset: `initial_dataset`
- Loaded data to: `global_data` table
- Schema auto-detected during ingestion

### 4. DAGs & File Sensor

- Implemented file sensor to wait for file availability in GCS
- Triggered DAG to load and transform data by country

### 5. Data Transformation

- Country-level tables created using dynamic SQL logic
- Views created for optimized querying and reporting

---

## 📊 Looker Studio Visualization

Connected Looker Studio to BigQuery to build:
- 📈 Disease Distribution by Country
- 📉 Disease Occurrence by Year

Reports are based on the view tables to improve performance and reduce cost.

---

## ✅ Outcome

- Reliable ingestion and transformation of over 1M records
- Dynamic, filterable visual dashboards
- Cost-efficient queries via materialized views

---

## 🧠 Learnings

- Using sensors in Airflow improves reliability
- BigQuery works seamlessly with Looker Studio
- Views help reduce query cost significantly

---

## 📜 License

MIT – Free to use, adapt, and share.
