import streamlit as st
import pandas as pd
import os
import joblib


# Load Model & Columns


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "..",
    "src",
    "model1.pkl"
)

columns_path = os.path.join(
    BASE_DIR,
    "..",
    "src",
    "columns.pkl"
)

model = joblib.load(model_path)
columns = joblib.load(columns_path)


# Streamlit Page Config


st.set_page_config(
    page_title="Nepal House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title


st.title("🏠 Nepal House Price Prediction")

st.markdown(
    "Predict house prices using Machine Learning"
)

st.divider()


# User Inputs


area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=10000,
    value=1200,
    step=100
)

bedrooms = st.slider(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.slider(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

parking = st.slider(
    "Parking Spaces",
    min_value=0,
    max_value=5,
    value=1
)

locations = [
    "Kathmandu",
    "Pokhara",
    "Lalitpur",
    "Bhaktapur",
    "Biratnagar",
    "Birgunj",
    "Butwal",
    "Chitwan",
    "Damak",
    "Dhangadhi",
    "Dharan",
    "Ghorahi",
    "Hetauda",
    "Ilam",
    "Itahari",
    "Janakpur",
    "Kalaiya",
    "Kirtipur",
    "Lahan",
    "Nepalgunj",
    "Tikapur",
    "Tulsipur",
    "Bhairahawa",
    "Birtamod",
    "Banepa"
]

location = st.selectbox(
    "Select Location",
    sorted(locations)
)

st.divider()


# Prediction Button


if st.button("Predict Price"):

    # Create empty dataframe
    input_df = pd.DataFrame(
        columns=columns
    )

    # Fill all values with 0
    input_df.loc[0] = 0

    # Add numerical values
    input_df["area"] = area
    input_df["bedrooms"] = bedrooms
    input_df["bathrooms"] = bathrooms
    input_df["parking"] = parking

    # Encode selected location
    location_column = f"location_{location}"

    if location_column in input_df.columns:
        input_df[location_column] = 1

    # Prediction
    prediction = model.predict(input_df)[0]

    # Display Result
    st.success(
        f"Estimated House Price: NPR {prediction:,.0f}"
    )

    st.balloons()