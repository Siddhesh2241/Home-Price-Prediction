import sys
import mysql.connector
from mysql.connector import Error




def Create_connection():
    """Creates and returns a connection to the MySQL database."""

    try:
        connection = mysql.connector.connect(
            host = "127.0.0.1",
            port = "3306",
            username = "root",
            password = "siddhesh2241",
            database = "new_titanic"
        )

        return connection
    
    except Exception as e:
        print("Unable to connect database",e)
        