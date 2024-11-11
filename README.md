# 🏠 House Price Prediction App

This repository contains a 🌐 Streamlit web application for predicting house prices based on various features like square footage, location, number of bedrooms, and more! 
The app uses a pre-trained machine learning model and stores data in a MySQL database for efficient record-keeping.

## 📑Table of Contents

*  Overview
*  Project Structure
*  Installation
*  Usage
*  Data Description
*  Model Training
*  MySQL Database Integration
*  Configuration
*  Acknowledgements

## 🛠 Project Structure

* **app.py** : Main application file that runs the Streamlit web app.
* **CONFIG/Database_conn.py** : Contains the function Create_connection to connect to the MySQL database.
* **CONFIG/insert_data.py** : Defines the insert_data function that inserts user input data and prediction results into the MySQL table.
* **notebook/Model/RandomRegressor_model.pkl** : Pre-trained model file.
* **requirements.txt** : List of dependencies required for the project.

## ⚙️ Installation

* Clone the repository:
  ```bash
  git clone https://github.com/Siddhesh2241/house-price-prediction.git
  cd house-price-prediction
  ```
* Install required libraries:
  ```bash
  pip install -r requirements.txt
  ```
* Set up the MySQL database with the appropriate schema 

* Place the pre-trained model file RandomRegressor_model.pkl in the notebook/Model directory.

## 🚀 Usage

* Run the app locally
 ```bash
 streamlit run app.py
 ```
This will open a local server where you can interact with the app by inputting house details and receiving a price prediction.

## 📊 Data Description

**The app uses the following input features for prediction**

* 🛏bedrooms: Number of bedrooms
* 🚽bathrooms: Number of bathrooms
* 📐sqft_living: Living area in square feet
* 🏞sqft_lot: Lot area in square feet
* 🏢floors: Number of floors
* 🌊waterfront: Indicator if the house is on the waterfront (0 = No, 1 = Yes)
* 👀view: View score (0–4)
* 🔧condition: Condition score (1–5)
* 📈grade: Grade (1–13)
* 📏sqft_above: Above-ground living area in square feet
* 🛠sqft_basement: Basement area in square feet
* 🏗yr_built: Year built
* 🛠yr_renovated: Year renovated (0 if never renovated)
* 📍zipcode: Zip code
* 🌎lat: Latitude
* 🌐long: Longitude
* 🏠sqft_living15: Average living area of nearby homes
* 🌳sqft_lot15: Average lot area of nearby homes

## 🧠 Model Training

The model used in this application is a Random Forest Regressor 🌳🌲, 
trained on housing data similar to the King County housing dataset. 
The model file RandomRegressor_model.pkl is pre-trained and included in this repository.

If you’d like to retrain or update the model, refer to additional notebooks in the notebook/ directory.

## 🗄️ MySQL Database Integration
The app includes an integration with MySQL to store input data along with the predicted house prices.
The table schema used for storing data is

```bash
CREATE TABLE house_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bedrooms INT,
    bathrooms FLOAT,
    sqft_living INT,
    sqft_lot INT,
    floors INT,
    waterfront INT,
    view INT,
    condition INT,
    grade INT,
    sqft_above INT,
    sqft_basement INT,
    yr_built INT,
    yr_renovated INT,
    zipcode INT,
    lat FLOAT,
    long FLOAT,
    sqft_living15 INT,
    sqft_lot15 INT,
    prediction FLOAT
);
```
## 🛠 Configuring the Database
Update your database connection details in CONFIG/Database_conn.py

```bash
def Create_connection():
    conn = mysql.connector.connect(
        host="your-host",
        user="your-username",
        password="your-password",
        database="your-database"
    )
    return conn
```
Ensure the MySQL server is running and create the database if it doesn’t already exist.

## 🌟Acknowledgements
Special thanks to the open-source community for providing tools like Streamlit and MySQL integration with Python!
This project is inspired by the housing price prediction tasks, 
leveraging datasets like the King County Housing dataset. 😊💻
