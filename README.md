# 🏡 DreamHome Price Prediction App  
> Predict house prices instantly using Machine Learning and Streamlit

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📘 Project Overview
The **DreamHome Price Prediction App** is a Machine Learning project that predicts the **estimated price of a house** based on its features such as:
- Lot area
- Number of bedrooms
- Neighborhood
- Street type
- Overall quality and condition

This project demonstrates a complete **end-to-end ML workflow** — from **data preprocessing and model training** to **deployment via a Streamlit web app** with an engaging, user-friendly interface.

---

## 🎯 Objectives
- Understand the relationship between property features and price.
- Build and evaluate a **Linear Regression model** to predict home prices.
- Create a **beautiful Streamlit app** for real-time user predictions.

---

## 🧩 Dataset
**Source:** Housing dataset (Ames Housing-style dataset)

| Column | Description |
|--------|--------------|
| LotArea | Lot size in square feet |
| Neighborhood | Location of the property |
| Street | Road type (Paved/Gravel) |
| OverallQual | Overall material and finish quality |
| OverallCond | Overall condition rating |
| Price | Sale price of the property (target variable) |

---

## ⚙️ Data Preprocessing Steps
1. **Handle Missing Values:**  
   - Filled numeric columns (e.g., LotArea) using median.  
   - Categorical columns (e.g., BsmtCond) filled using mode.  

2. **Encoding Categorical Features:**  
   - Used `OneHotEncoder` from `scikit-learn` inside a `ColumnTransformer`.

3. **Feature Engineering:**  
   - Combined numerical and categorical columns for model input.

4. **Splitting Data:**  
   - Used `train_test_split()` (80–20 split).

---

## 🧠 Model Building
- Algorithm: **Linear Regression**
- Evaluation Metrics:
  - **R² Score:** `0.74`
  - **MAE:** `28,883`
  - **MAPE:** `17.9%`

---

## 💻 Streamlit Web App Features
✅ Clean, modern interface with gradient background  
✅ Animated **Lottie** illustration for a home feel  
✅ Dropdown + manual input for all fields  
✅ Displays estimated price with a green highlight box  
✅ Balloon animation after successful prediction  

---

## 🚀 Run the Project Locally
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Savan3027/<ML Project>.git
cd <ML Project>
