# 🏠 Apartment Rent Predictor

A **machine learning web application** that predicts apartment rent prices based on property details, built with **Python, scikit-learn, and Gradio**.  
The app also displays **model performance metrics** in real-time.

---

## 📌 Features
- ✅ Predict rent based on:
  - Bedrooms
  - Bathrooms
  - Size (sqft)
  - Floor number
  - Building age (years)
  - Roofdeck availability
  - Elevator availability
  - Gym availability
- 📊 Displays evaluation metrics:
  - **Predicted Rent (USD)**
  - **Root Mean Square Error (RMSE)**
  - **Mean Rent** from test set
  - **% Error** relative to mean rent
  - **R² Score** (model fit quality)
- 🖥 Interactive **Gradio UI**

---

## ⚙️ How It Works
1. 📂 Loads apartment dataset from Google Drive.
2. 🤖 Trains a **Linear Regression** model using `scikit-learn`.
3. 📝 Accepts apartment details via a web form.
4. 📈 Predicts rent and shows model evaluation metrics.

---

## 📊 Dataset
The dataset contains the following columns:
- `bedrooms`
- `bathrooms`
- `size_sqft`
- `floor`
- `building_age_yrs`
- `has_roofdeck`
- `has_elevator`
- `has_gym`
- `rent` (target variable)

---

## 🛠 Installation

### Requirements
Install dependencies:
```bash
pip install numpy pandas scikit-learn gradio
