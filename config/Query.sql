create database if not exists House_Price;

use House_price;

DROP TABLE IF EXISTS house_data;

CREATE TABLE house_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bedrooms INT,
    bathrooms FLOAT,
    sqft_living INT,
    sqft_lot INT,
    floors FLOAT,
    waterfront TINYINT,  -- 0 or 1 for binary values
    view TINYINT,
    `condition` TINYINT,  -- Enclose in backticks to avoid syntax issues
    grade TINYINT,
    sqft_above INT,
    sqft_basement INT,
    yr_built INT,
    yr_renovated INT,
    zipcode INT,
    lat FLOAT,  -- Remove precision to avoid deprecation warnings
    `long` FLOAT,  -- Remove precision to avoid deprecation warnings
    sqft_living15 INT,
    sqft_lot15 INT,
    prediction FLOAT
);

select * from house_data;

drop table if exists house_data;

-- Drop the table if it already exists
DROP TABLE IF EXISTS house_data;

-- Create a new table with the specified structure
CREATE TABLE house_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bedrooms INT,
    bathrooms FLOAT,
    sqft_living INT,
    sqft_lot INT,
    floors FLOAT,
    waterfront TINYINT,  -- 0 or 1 for binary values
    view TINYINT,
    `condition` TINYINT,  -- Enclose in backticks to avoid syntax issues
    grade TINYINT,
    sqft_above INT,
    sqft_basement INT,
    yr_built INT,
    yr_renovated INT,
    zipcode INT,
    lat FLOAT,  -- Remove precision to avoid deprecation warnings
    `long` FLOAT,  -- Enclose in backticks to avoid syntax issues
    sqft_living15 INT,
    sqft_lot15 INT,
    prediction FLOAT
);

