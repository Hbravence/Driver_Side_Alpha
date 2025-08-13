# 🚗 Driver-Side Alpha (DSA)

**Driver-Side Alpha (DSA)** is a predictive analytics platform designed to identify high-demand windows for rideshare drivers by clustering **event** and **flight data**. The goal is to surface the most lucrative times and locations to drive, based on real-world signals.

---

## 📡 Data Sources

DSA pulls from two primary APIs:

- **SeatGeek API** – Weekly event data for a given city  
- **Flight Schedule API** – Weekly flight arrival and departure data

These datasets are clustered to identify **temporal and geographic hotspots** for rideshare demand.

---

## 🧱 Architecture Overview

### 1. Data Ingestion
- API calls to SeatGeek and flight schedule providers
- Raw data flattened and stored locally as `.csv` files  
  *(Cloud migration planned: AWS S3 + Athena)*

### 2. Modeling & Clustering
- Python module ingests `.csv` files
- **Flight data**: clustered using **Mean-Shift** to identify time-density clusters  
- **Event data**: clustered using **DBSCAN** with **Haversine logic** to group nearby events  
  *(DBSCAN chosen for its performance on sparse datasets)*

### 3. Output Storage
- Clustered and summarized data saved as `.parquet` files in the `modeled/` folder  
  *(Preserves data types from modeling phase)*

### 4. Visualization
- Each city has its own dashboard built with **Dash** and **Plotly**
- **Event data**: geospatial maps showing clustered events by day of week  
- **Flight data**: timeline graphs showing high-density arrival windows  
- Graphs, filters, data extraction, and style components modularized into reusable Python functions

---

## 🧠 Design Intent

DSA is modular by design:  
- Each city functions as an independent node with localized data pipelines and dashboards  
- Architecture is built to scale across multiple cities  
- Future roadmap includes cloud-native integration and investor-ready deployment

---
