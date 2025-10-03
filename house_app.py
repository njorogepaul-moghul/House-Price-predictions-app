import streamlit as st
import pandas as pd
import joblib

# Load model and features
model = joblib.load("model.pkl")
top_features = joblib.load("train_columns.pkl")

st.title("🏡 House Price Prediction App")

st.write("Adjust the sliders below to predict the house price.")

# Define some reasonable ranges for top features
feature_ranges = {
    "OverallQual": (1, 10, 5),
    "GrLivArea": (400, 4000, 1500),   # sq ft
    "GarageCars": (0, 4, 2),
    "GarageArea": (0, 1200, 500),     # sq ft
    "TotalBsmtSF": (0, 3000, 800),    # sq ft
    "1stFlrSF": (400, 3000, 1000),    # sq ft
    "FullBath": (0, 4, 2),
    "YearBuilt": (1870, 2020, 1975),
    "YearRemodAdd": (1950, 2020, 2005),
    "TotRmsAbvGrd": (2, 14, 6)
}

# Collect inputs
input_data = {}
for feature in top_features:
    if feature in feature_ranges:
        min_val, max_val, default_val = feature_ranges[feature]
        input_data[feature] = st.slider(
            f"{feature}", min_value=min_val, max_value=max_val, value=default_val
        )
    else:
        # Fallback if feature not in predefined ranges
        input_data[feature] = st.number_input(f"{feature}", value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted House Price: ${prediction:,.2f}")
