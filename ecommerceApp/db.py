# db.py
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='ecommerce'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None
