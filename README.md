# 🏡 House Price Prediction App

## 📌 Overview
This is an interactive web application built with **Streamlit** that predicts house prices based on user-provided features.  
It uses our **tuned LightGBM model**, trained on the Kaggle Ames Housing dataset.  

To improve efficiency and simplify the app, we applied **feature reduction**, selecting only the top **10 most predictive features**. This keeps the app fast and user-friendly while maintaining strong accuracy.

---

## 🚀 Features
- User-friendly interface with **sliders** for the most important house attributes  
- Predicts house prices instantly using the trained model (`model.pkl`)  
- Uses **reduced feature set (top 10 features)** for simplicity & speed  
- Clean, interactive design  

---

## ⚙️ How It Works
1. The app loads a trained **LightGBM model** (`model.pkl`) and the list of reduced features (`train_columns.pkl`).  
2. Users adjust house attributes (e.g., quality, living area, garage, year built) using sliders.  
3. The input is passed to the model, which outputs a predicted **house price in USD**.  

---

## 🖥️ Usage

### Run Locally
Clone the repo and install dependencies:
```bash
git clone https://github.com/njorogepaul-moghul/house-price-app.git
cd house-price-app
pip install -r requirements.txt

streamlit run house_app.py
## project structure
├── house_app.py         # Main Streamlit app
├── model.pkl            # Trained LightGBM model (with reduced features)
├── train_columns.pkl    # Top 10 features used in training
├── requirements.txt     # Project dependencies
└── README.md            # App documentation

