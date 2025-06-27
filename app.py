# -*- coding: utf-8 -*-
!pip install streamlit
import streamlit as st

import numpy as np
import joblib

# Load the model
model = joblib.load("/content/sonar_model.pkl")

st.title("🔍 Rock vs Mine Prediction Project1")

st.markdown("""
This app predicts whether a sonar signal is coming from a rock 🪨 or a mine 💣 based on 60 frequency features.
""")

# Collect 60 features from user
inputs = []
for i in range(60):
    val = st.number_input(f"Feature {i+1}", value=0.0, format="%.6f")
    inputs.append(val)

# Predict button
if st.button("Predict"):
    prediction = model.predict([inputs])[0]
    if prediction == 'R':
        st.success("🪨 This is predicted to be a **Rock** signal!")
    else:
        st.success("💣 This is predicted to be a **Mine** signal!")
