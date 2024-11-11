# House Price Prediction App

This repository contains a Streamlit web application for predicting house prices based on various features such as square footage, location, number of bedrooms, and more. The app leverages a pre-trained machine learning model to make predictions and stores data in a MySQL database.

## Table of Contents

*  Overview
*  Project Structure
*  Installation
*  Usage
*  Data Description
*  Model Training
*  MySQL Database Integration
*  Configuration
*  Acknowledgements

## Project Structure

* app.py: Main application file that runs the Streamlit web app.
* CONFIG/Database_conn.py: Contains the function Create_connection to connect to the MySQL database.
* CONFIG/insert_data.py: Defines the insert_data function that inserts user input data and prediction results into the MySQL table.
* notebook/Model/RandomRegressor_model.pkl: Pre-trained model file.
* requirements.txt: List of dependencies required for the project.