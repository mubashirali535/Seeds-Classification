import streamlit as st
import joblib
import numpy as np

# ==========================
# Load Saved Model and Scaler
# ==========================

model = joblib.load("seeds_classification_model.pkl")
scaler = joblib.load("standard_scaler.pkl")

# ==========================
# Streamlit Page Configuration
# ==========================

st.set_page_config(
    page_title="Seeds Classification",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Seeds Classification App")
st.write(
    "Predict the wheat seed variety using its physical measurements."
)

st.markdown("---")

# ==========================
# User Input
# ==========================

area = st.number_input("Area (A)", value=15.0)

perimeter = st.number_input("Perimeter (P)", value=14.5)

compactness = st.number_input("Compactness (C)", value=0.87)

kernel_length = st.number_input("Kernel Length (LK)", value=5.5)

kernel_width = st.number_input("Kernel Width (WK)", value=3.2)

asymmetry = st.number_input("Asymmetry Coefficient (A_Coef)", value=3.0)

groove_length = st.number_input("Kernel Groove Length (LKG)", value=5.2)

# ==========================
# Prediction
# ==========================

if st.button("Predict Seed Class"):

    sample = np.array([[
        area,
        perimeter,
        compactness,
        kernel_length,
        kernel_width,
        asymmetry,
        groove_length
    ]])

    sample_scaled = scaler.transform(sample)

    prediction = model.predict(sample_scaled)[0]

    classes = {
        0: "🌾 Kama",
        1: "🌾 Rosa",
        2: "🌾 Canadian"
    }

    st.success(f"Predicted Seed Variety: **{classes[prediction]}**")