# 🚗 Driver-Side Alpha (DSA)

**Driver-Side Alpha (DSA)** is a predictive analytics project designed to identify high-demand windows for rideshare drivers by clustering **event** and **flight data**. The goal is to surface the most lucrative times and locations to drive, based on real-world signals.

---

## 📡 Data Sources

DSA pulls from two primary APIs:

- **SeatGeek API** – Weekly event data for a given city  
- **Flight Schedule API** – Weekly flight arrival/departure data

These datasets are clustered to identify **temporal and geographic hotspots** for rideshare demand.

---

## 🧱 Architecture Overview

### 1. Data Ingestion
- API calls are made to SeatGeek and the flight schedule provider
- Raw data is stored locally as `.csv` files (to be migrated to AWS S3 + Athena)

### 2. Modeling & Clustering
- A separate Python module ingests the `.csv` files
- Machine learning processes cluster the data by time and location
- Not every city will yield clustered event data—this is handled gracefully

### 3. Output Storage
- Clustered and summarized data is saved to the `modeled/` folder as `.csv`

### 4. Visualization
- Each city has its own dashboard file
- Dashboards are built using **Plotly**, allowing interactive exploration of demand windows

---

## 🧠 Design Intent

DSA is modular by design.  
Each city functions as its own node, with localized data pipelines and dashboards.  
The system is built to scale across multiple cities, with future integration into cloud-native infrastructure.

---
