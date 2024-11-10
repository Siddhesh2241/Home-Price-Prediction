from CONFIG.Database_conn import Create_connection

def insert_data(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition,
                grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, 
                sqft_living15, sqft_lot15, prediction):


    """Inserts input data and the prediction into the MySQL database."""
    conn = Create_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO house_data (bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, `condition`, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, `long`, sqft_living15, sqft_lot15, prediction)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);

    """
    values = (bedrooms,
         bathrooms,
         sqft_living,
         sqft_lot,
         floors,
         waterfront,
         view,
         condition,
         grade,
         sqft_above,
         sqft_basement,
         yr_built,
         yr_renovated,
         zipcode,
         lat,
         long,
         sqft_living15,
         sqft_lot15,
         prediction)

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
