import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import folium
import io
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium
from sklearn import preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor



st.set_page_config(page_title="House Price Prediction",
                   page_icon=":house:",
                   layout="wide")

def Load_data():
   st.subheader("Upload csv file")
   file = st.file_uploader("upload file",type="csv")

   if file is not None:
      data = pd.read_csv(file)
      st.dataframe(data)
      return data

def Analyse_data(data):
    
    st.subheader("First five rows of the dataset")
    st.write(data.head())

    st.subheader("Columns in dataset:")
    st.write(data.columns.tolist())

    st.subheader("Numerical columns in dataset:")
    st.write([col for col in data.columns if data[col].dtypes != "object"])

    st.subheader("Categorical columns in dataset:")
    st.write([col for col in data.columns if data[col].dtypes == "object"])

    st.subheader("Information of the CSV file:")
    buffer = io.StringIO()
    data.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.subheader("Statistical data of the dataset:")
    st.write(data.describe())

    st.subheader("Check for duplicates in the dataset:")
    st.write(data.duplicated().sum())

    st.subheader("Unique values in the dataset:")
    st.write(data.nunique())

    st.subheader("Check for null values in the dataset:")
    st.write(data.isnull().sum())

def preprocess_data(data):
   st.subheader("droping the unnecessary columns such as id, date")
   drop_column = st.multiselect("Select column that you drop",options=data.columns.tolist())
     
   data.drop(columns=drop_column, axis=1,inplace=True)
   st.write(f"### DataFrame after dropping columns: {drop_column}")
   st.write(data)
         
    
   st.subheader("Checking types of columns")
   st.write(data.dtypes)

   st.subheader("Coverting data type float to int")
   float_columns = data.select_dtypes(include=['float']).columns
   
   Float_col = st.multiselect("Select columns",float_columns)

   data[Float_col] = data[Float_col].astype(int)
   st.subheader(f"Dataset after converting column float to integer {Float_col}")
   st.write(data)

   st.write("Renaming the column yr_built to age and changing the values to age")
   data.rename(columns={'yr_built':'age'},inplace = True)

   st.subheader("Calculating current Age of house")
   today = datetime.now()
   data["age"] = today.year - data["age"]
   st.write(data["age"])

   st.subheader("Chenging the column yr_renovated to renovated and changing the values to 0 and 1")
   data.rename(columns={'yr_renovated':'renovated'},inplace=True)
   data['renovated'] = data['renovated'].apply(lambda x: 0 if x == 0 else 1)
   
   st.write(data["renovated"])
    
   st.subheader("Using Feature scaling of some column")
   columns_to_scale = ['sqft_living', 'sqft_living15', 'sqft_lot', 'sqft_above', 'sqft_basement', 'sqft_lot15']
   data[columns_to_scale] = data[columns_to_scale].apply(lambda x: x / x.max())
   st.write(f"Data after feature scaling of column {columns_to_scale}",data)


   return data

def EDA(data):
   st.subheader("Corfelation matrix find the relatiosheep between the variables")

   correlation_with_price = data.corr()["price"].sort_values(ascending = False)
   st.write("Correlation of features with 'price':")
   st.write(correlation_with_price)


   plt.figure(figsize = (15,12))
   sns.heatmap(data.corr(),annot=True)
   plt.title("Corelation of matrix")
   st.pyplot(plt)

   st.subheader("Visulising the Corelation with price")
   price_plot = data.corr()["price"][:].sort_values()

   plt.figure(figsize=(10, 3))
   price_plot.plot(kind="bar", color="skyblue")
   plt.title("Correlation of Features with Price")
   plt.ylabel("Correlation coefficient")
   plt.xticks(rotation=45)

   st.pyplot(plt)

   st.subheader("Visualizing the relationship between Price and Features")

   fig, ax = plt.subplots(4, 4, figsize=(20, 20))

   sns.scatterplot(x=data['sqft_living'], y=data['price'], ax=ax[0, 0])
   ax[0, 0].set_title("Price vs Sqft Living")

   sns.scatterplot(x=data['sqft_lot'], y=data['price'], ax=ax[0, 1])
   ax[0, 1].set_title("Price vs Sqft Lot")

   sns.scatterplot(x=data['sqft_above'], y=data['price'], ax=ax[0, 2])
   ax[0, 2].set_title("Price vs Sqft Above")

   sns.scatterplot(x=data['sqft_basement'], y=data['price'], ax=ax[0, 3])
   ax[0, 3].set_title("Price vs Sqft Basement")

   sns.scatterplot(x=data['sqft_living15'], y=data['price'], ax=ax[1, 0])
   ax[1, 0].set_title("Price vs Sqft Living15")

   sns.scatterplot(x=data['sqft_lot15'], y=data['price'], ax=ax[1, 1])
   ax[1, 1].set_title("Price vs Sqft Lot15")

   sns.lineplot(x=data['age'], y=data['price'], ax=ax[1, 2])
   ax[1, 2].set_title("Price vs Age")

   sns.boxplot(x=data['renovated'], y=data['price'], ax=ax[1, 3])
   ax[1, 3].set_title("Price vs Renovated")

   sns.scatterplot(x=data['bedrooms'], y=data['price'], ax=ax[2, 0])
   ax[2, 0].set_title("Price vs Bedrooms")

   sns.lineplot(x=data['bathrooms'], y=data['price'], ax=ax[2, 1])
   ax[2, 1].set_title("Price vs Bathrooms")

   sns.barplot(x=data['floors'], y=data['price'], ax=ax[2, 2])
   ax[2, 2].set_title("Price vs Floors")

   sns.boxplot(x=data['waterfront'], y=data['price'], ax=ax[2, 3])
   ax[2, 3].set_title("Price vs Waterfront")

   sns.barplot(x=data['view'], y=data['price'], ax=ax[3, 0])
   ax[3, 0].set_title("Price vs View")

   sns.barplot(x=data['condition'], y=data['price'], ax=ax[3, 1])
   ax[3, 1].set_title("Price vs Condition")

   sns.lineplot(x=data['grade'], y=data['price'], ax=ax[3, 2])
   ax[3, 2].set_title("Price vs Grade")

   sns.lineplot(x=data['age'], y=data['renovated'], ax=ax[3, 3])
   ax[3, 3].set_title("Age vs Renovated")
   
   st.pyplot(fig)
   
   st.subheader("Ploting the location of houses based on the lognitude and latitude of the map")
   # adding a new column price_range and categorizing the price into 4 categories
   data["price_range"] = pd.cut(data["price"],bins = [0,321950,450000,645000,1295648],labels=['Low','Medium','High','Very High'])
   map = folium.Map(location=[47.5480, -121.9836],zoom_start=8)
   marker_cluster = FastMarkerCluster(data[['lat', 'long']].values.tolist()).add_to(map)
   st_folium(map, width=700, height=500)
   

def MlAlgo(data):
   data = data.drop("price_range",axis=1)

   x = data.drop("price",axis=1)
   y = data["price"]

   x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state=10)
   
   st.subheader("1) Linear Regression")
   input = [('scale',StandardScaler()),('polynomial', PolynomialFeatures(degree=2)),('model',LinearRegression())]
   pipe = Pipeline(input)
   
   pipe.fit(x_train,y_train)

   pipe.score(x_test,y_test)

   pipe_pred = pipe.predict(x_test)

   st.write("r2 score of Linear regression algorithm is",r2_score(pipe_pred,y_test))

   st.subheader("2) Ridge Regression")

   Ridgemodel = Ridge(alpha = 0.001)
   
   # training the model
   Ridgemodel.fit(x_train,y_train)
   Ridgemodel.score(x_test,y_test)
   
   #testing the model
   r_pred = Ridgemodel.predict(x_test)
   st.write("r2 score of Ridge regression algorithm is", r2_score(y_test,r_pred))

   st.subheader("3) Random Forest Regressor")
   regressor = RandomForestRegressor(n_estimators=100, random_state=0)

   # training the model
   regressor.fit(x_train,y_train)
   regressor.score(x_test,y_test)
   
   #testing the model
   yhat = regressor.predict(x_test)
   st.write("r2 score of Random Foreset regression algorithm is",r2_score(y_test,yhat))
   
   st.subheader("Updated plot with filled KDE plots for actual and predicted prices")
   fig, ax = plt.subplots(1, 3, figsize=(20, 5))

   # Plotting KDE plots with fill
   sns.kdeplot(y_test, ax=ax[0], color="blue",  label='Actual Price')
   sns.kdeplot(pipe_pred, ax=ax[0], color="red",  label='Predicted Price')

   sns.kdeplot(y_test, ax=ax[1], color="blue", label='Actual Price')
   sns.kdeplot(r_pred, ax=ax[1], color="red",  label='Predicted Price')

   sns.kdeplot(y_test, ax=ax[2], color="blue", label='Actual Price')
   sns.kdeplot(yhat, ax=ax[2], color="red",  label='Predicted Price')

   # Adding legends
   ax[0].legend(['Actual Price', 'Predicted Price'])
   ax[1].legend(['Actual Price', 'Predicted Price'])
   ax[2].legend(['Actual Price', 'Predicted Price'])

   # Model names as titles
   ax[0].set_title('Linear Regression')
   ax[1].set_title('Ridge Regression')
   ax[2].set_title('Random Forest Regression')

   st.pyplot(fig)

def main():
  
  st.title("House Price Prediction :house:")
  st.markdown("Prediction house Price using Regression Algorithm")
  
  data  = Load_data()

  if data is not None:
     Analyse_data(data)
     
     preprocess_data(data)

     EDA(data)

     MlAlgo(data)

if __name__ == "__main__":
    main()