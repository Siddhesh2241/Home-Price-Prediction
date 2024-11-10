import streamlit as st
import pickle
import numpy as np
from CONFIG.insert_data import insert_data
import dill


# Load the trained model
model_path = "notebook\Model\RandomRegressor_model.pkl"  # Adjust the path if necessary
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("House Price Prediction App")

# User inputs
st.header("Enter House Details")

bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
sqft_living = st.number_input("Living Area (in sqft)", min_value=500, max_value=10000, value=2000)
sqft_lot = st.number_input("Lot Area (in sqft)", min_value=500, max_value=100000, value=5000)
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=1)
waterfront = st.selectbox("Waterfront", [0, 1])  # 0 = No, 1 = Yes
view = st.slider("View (0-4)", min_value=0, max_value=4, value=0)
condition = st.slider("Condition (1-5)", min_value=1, max_value=5, value=3)
grade = st.slider("Grade (1-13)", min_value=1, max_value=13, value=7)
sqft_above = st.number_input("Above Ground Living Area (in sqft)", min_value=500, max_value=10000, value=1500)
sqft_basement = st.number_input("Basement Area (in sqft)", min_value=0, max_value=5000, value=0)
yr_built = st.number_input("Year Built", min_value=1800, max_value=2023, value=1990)
yr_renovated = st.number_input("Year Renovated (0 if never)", min_value=0, max_value=2023, value=0)
zipcode = st.number_input("Zip Code", min_value=10000, max_value=99999, value=98001)
lat = st.number_input("Latitude", format="%.6f", value=47.5480)
long = st.number_input("Longitude", format="%.6f", value=-121.9836)
sqft_living15 = st.number_input("Living Area of Nearby Homes (in sqft)", min_value=500, max_value=10000, value=2000)
sqft_lot15 = st.number_input("Lot Area of Nearby Homes (in sqft)", min_value=500, max_value=100000, value=5000)

# Predict button
if st.button("Predict House Price"):
    # Prepare the input data
    input_data = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, 
                            condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, 
                            zipcode, lat, long, sqft_living15, sqft_lot15]])
    
    # Predict the price
    prediction = model.predict(input_data)[0]
    
    # Display the prediction
    st.subheader(f"Predicted House Price: ${prediction:,.2f}")
    
    # Store input and prediction in database
    try:
        insert_data(
             bedrooms=int(bedrooms),
            bathrooms=float(bathrooms),
            sqft_living=int(sqft_living),
            sqft_lot=int(sqft_lot),
            floors=int(floors),
            waterfront=int(waterfront),
            view=int(view),
            condition=int(condition),
            grade=int(grade),
            sqft_above=int(sqft_above),
            sqft_basement=int(sqft_basement),
            yr_built=int(yr_built),
            yr_renovated=int(yr_renovated),
            zipcode=int(zipcode),
            lat=float(lat),
            long=float(long),
            sqft_living15=int(sqft_living15),
            sqft_lot15=int(sqft_lot15),
            prediction=float(prediction)
        )
        st.success("Data successfully inserted into the database!")
    except Exception as e:
        st.error(f"Failed to insert data into the database: {e}")
