import mysql.connector

def create_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password="your_password_here"
            database='secure_access_control'
        )
        print('Connection to the database was successful.')
        return conn

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
# This function creates a connection to the MySQL database.
# It uses the mysql.connector library to connect to the database with specified credentials.
# If the connection is successful, it returns the connection object; otherwise, it prints an error message and returns None.    
