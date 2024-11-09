from config.database_conn import Create_connection

def insert_data(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition,
                grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, 
                sqft_living15, sqft_lot15, prediction):


    """Inserts input data and the prediction into the MySQL database."""
    conn = Create_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO house_data (
            bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, 
            condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, 
            zipcode, lat, long, sqft_living15, sqft_lot15,prediction
        ) VALUES (
            %(bedrooms)s, %(bathrooms)s, %(sqft_living)s, %(sqft_lot)s, %(floors)s, %(waterfront)s, %(view)s,
            %(condition)s, %(grade)s, %(sqft_above)s, %(sqft_basement)s, %(yr_built)s, %(yr_renovated)s,
            %(zipcode)s, %(lat)s, %(long)s, %(sqft_living15)s, %(sqft_lot15)s, %(prediction)s
        );
    """
    values = {"bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft_living": sqft_living,
        "sqft_lot": sqft_lot,
        "floors": floors,
        "waterfront": waterfront,
        "view": view,
        "condition": condition,
        "grade": grade,
        "sqft_above": sqft_above,
        "sqft_basement": sqft_basement,
        "yr_built": yr_built,
        "yr_renovated": yr_renovated,
        "zipcode": zipcode,
        "lat": lat,
        "long": long,
        "sqft_living15": sqft_living15,
        "sqft_lot15": sqft_lot15,
        "prediction": prediction}

    try:
        # Execute the insertion
        cursor.execute(sql, values)
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
