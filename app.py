import streamlit as st
import pandas as pd
import joblib

# --- Load the Trained Model ---
# This line loads the .pkl file you created earlier.
try:
    pipeline = joblib.load(r"D:\\programing\\intership 2025\\Project 4\\delivery_time_model.pkl")
    print("Model loaded successfully!")
except FileNotFoundError:
    st.error("Error: 'delivery_time_model.pkl' not found. Please run the training script first to create the model file.")
    st.stop()


# --- Streamlit App Interface ---

st.title('Amazon Delivery Time Prediction 🚚')

st.write("Enter the details of the order to get a predicted delivery time.")

# --- Input Fields for User ---
# We create columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Agent Age', min_value=18, max_value=70, value=30, help="Enter the age of the delivery agent.")
    rating = st.slider('Agent Rating', min_value=1.0, max_value=5.0, value=4.5, step=0.1, help="Slide to select the agent's rating.")
    distance = st.number_input('Distance (km)', min_value=0.1, max_value=100.0, value=10.0, help="Total distance from store to drop-off location.")
    hour = st.slider('Order Hour', min_value=0, max_value=23, value=12, help="What hour of the day was the order placed? (24-hour format)")

with col2:
    weather = st.selectbox('Weather Conditions', ['Sunny', 'Stormy', 'Sandstorms', 'Cloudy', 'Fog', 'Windy'])
    traffic = st.selectbox('Traffic Conditions', ['Low', 'High', 'Jam', 'Medium'])
    vehicle = st.selectbox('Vehicle Type', ['motorcycle', 'scooter', 'van', 'bicycle'])
    area = st.selectbox('Area Type', ['Urban', 'Metropolitan', 'Semi-Urban'])
    category = st.selectbox('Product Category', ['Clothing', 'Electronics', 'Sports', 'Skincare'])


# --- Prediction Logic ---
# When the user clicks the button, this block of code runs.
if st.button('Predict Delivery Time'):
    # Create a DataFrame from the user's inputs
    input_data = pd.DataFrame({
        'Agent_Age': [age],
        'Agent_Rating': [rating],
        'Distance_km': [distance],
        'Order_Hour': [hour],
        'Weather': [weather],
        'Traffic': [traffic],
        'Vehicle': [vehicle],
        'Area': [area],
        'Category': [category]
    })

    # Use the loaded model to make a prediction
    prediction = pipeline.predict(input_data)

    # Display the result

    st.success(f"Predicted Delivery Time: {prediction[0]:.0f} minutes")
