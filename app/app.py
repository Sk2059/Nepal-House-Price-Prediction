import streamlit as st
import pickle
import pandas as pd 

st.set_page_config(
    page_title="Nepal House Price Predictor",
    page_icon="🏠",
    layout="centered"
)
model = pickle.load(open("C:\\Users\\sk\\Documents\\backend\\machineai\\Projects\\house_price_Nepal\\src\\model.pkl", "rb"))

st.title("Nepali House prediction system")
st.write("enter house details below:")


area = st.number_input("Area (sq ft)", min_value=500)

bedrooms = st.number_input("Bedrooms", min_value=1)

bathrooms = st.number_input("Bathrooms", min_value=1)

parking = st.number_input("Parking Spaces", min_value=0)

location = st.selectbox(
    "Location",
    ["Kathmandu", "Pokhara", "Lalitpur", "Bhaktapur"]
)

location_data = {
    "location_Bhaktapur": 0,
    "location_Kathmandu": 0,
    "location_Lalitpur": 0,
    "location_Pokhara": 0
}

location_data[f"location_{location}"] = 1

input_data = pd.DataFrame([{
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "parking": parking,
    **location_data
}])

if st.button("Predict Price"):
    
    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: NPR {int(prediction[0]):,}")