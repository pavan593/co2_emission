from flask import Flask, request, jsonify
from threading import Thread
import streamlit as st
import requests

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "CO2 Emission API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Dummy response for now (Replace with actual ML model prediction)
    prediction = {"emission": data.get("value", 0) * 2}
    return jsonify(prediction)

# Function to run Flask on a separate thread
def run_flask():
    app.run(host="0.0.0.0", port=5000, debug=False)

# Start Flask in a separate thread
Thread(target=run_flask, daemon=True).start()

# Streamlit UI
st.title("CO2 Emission Predictor")
st.write("Enter a value and get CO2 emission prediction.")

value = st.number_input("Enter a value:", min_value=0.0)

if st.button("Predict"):
    try:
        response = requests.post("http://127.0.0.1:5000/predict", json={"value": value})
        if response.status_code == 200:
            st.success(f"Predicted CO2 Emission: {response.json()['emission']}")
        else:
            st.error("Failed to get prediction.")
    except Exception as e:
        st.error(f"Error: {e}")
