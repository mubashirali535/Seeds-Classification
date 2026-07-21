# 🌾 Seeds Classification using Machine Learning

## 🚀 Live Demo

🔗 **https://seeds-classification-zon7zztjbfgslucripjxza.streamlit.app/**

---

## 📖 Project Overview

This project uses Machine Learning to classify wheat seeds into one of three seed varieties based on their physical characteristics.

A trained **K-Nearest Neighbors (KNN)** model predicts the seed variety from seven numerical features. The model is deployed using **Streamlit**, allowing users to interact with it through a simple web interface.

---

## 🎯 Problem Statement

The objective of this project is to classify wheat seeds into one of the following varieties:

- 🌾 Kama
- 🌾 Rosa
- 🌾 Canadian

using their physical measurements.

---

## 📊 Dataset

**Dataset:** UCI Seeds Dataset

**Source:** https://www.kaggle.com/datasets/dongeorge/seed-from-uci

### Features

- Area (A)
- Perimeter (P)
- Compactness (C)
- Kernel Length (LK)
- Kernel Width (WK)
- Asymmetry Coefficient (A_Coef)
- Kernel Groove Length (LKG)

### Target

- Seed Variety (3 Classes)

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📈 Machine Learning Workflow

- Data Loading
- Data Exploration
- Missing Value Analysis
- Duplicate Value Check
- Exploratory Data Analysis (EDA)
- Target Distribution Analysis
- Correlation Analysis
- Feature Selection
- Train-Test Split
- Feature Scaling
- Model Training
- Model Evaluation
- Model Comparison
- Model Saving
- Streamlit Deployment

---

## 🤖 Models Compared

| Model | Accuracy |
|--------|---------:|
| K-Nearest Neighbors (KNN) ✅ | **90.48%** |
| Support Vector Machine (SVM) | **90.48%** |
| Decision Tree Classifier | **88.10%** |

---

## 📋 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

---

## 🏆 Best Model

**K-Nearest Neighbors (KNN)** was selected as the final model because it achieved the highest overall performance on the test dataset.

---

## 📁 Project Structure

```text
Seeds-Classification/
│
├── app.py
├── requirements.txt
├── README.md
├── seeds_classification.py
├── Seed_Data.csv
├── seeds_classification_model.pkl
└── standard_scaler.pkl
```

---



## 👨‍💻 Author

**Mubashir Ali**

- Mechanical Engineer
- Machine Learning Enthusiast

---

