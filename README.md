# 🏠 Real Estate Buyer Segmentation & Investment Intelligence

An AI-powered data science project that segments real estate buyers using machine learning and generates actionable investment insights through an interactive Streamlit dashboard.

---

## 🚀 Project Overview

Real estate companies often treat all buyers the same, leading to inefficient marketing and missed investment opportunities.

This project solves that problem using **unsupervised machine learning (K-Means clustering)** to identify hidden buyer segments and generate data-driven business insights.

---

## 🎯 Objectives

- Segment buyers based on behavior and investment patterns
- Understand geographic and demographic differences
- Identify high-value investors
- Provide actionable business recommendations
- Build an interactive analytics dashboard

---

## 📊 Dataset Features

### Clients Data:
- client_id
- client_type
- gender
- country, region
- date_of_birth
- acquisition_purpose
- satisfaction_score
- loan_applied
- referral_channel

### Properties Data:
- listing_id
- transaction_date
- unit_category
- floor_area_sqft
- sale_price
- listing_status
- client_ref

---

## 🧠 Machine Learning Approach

### 1. Data Preprocessing
- Handled missing values
- Merged datasets (clients + properties)
- Converted categorical variables

### 2. Feature Engineering
- Age calculation from date_of_birth
- Total investment per client
- Property count per client

### 3. Clustering Model
- K-Means Clustering
- Optimal clusters selected using Elbow Method & Silhouette Score

### 4. Segments Identified
- High-Value Investors
- First-Time Buyers
- Corporate Buyers
- Luxury Investors

---

## 📈 Key Insights

- Identified distinct buyer behavior patterns
- High-value investors contribute disproportionately to revenue
- First-time buyers rely heavily on loans
- Geographic differences strongly influence investment behavior

---

## 🧠 AI Decision Engine

The dashboard automatically generates:

- Best performing customer segment
- Low satisfaction segments needing attention
- High-value customer count
- Marketing strategy recommendations

---

## 📊 Streamlit Dashboard Features

- Interactive filters (country, segment, client type)
- KPI metrics (investment, customers, satisfaction)
- Segment distribution charts
- Investment behavior analysis
- Customer age vs investment analysis
- AI-generated business insights

---

## 🛠 Tech Stack

- Python 🐍
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/real-estate-segmentation.git
cd real-estate-segmentation
pip install -r requirements.txt
streamlit run app.py
