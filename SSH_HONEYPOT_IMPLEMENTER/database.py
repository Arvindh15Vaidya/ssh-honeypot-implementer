"""
Handles all interactions with the MySQL database.
"""

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def connect_to_db():
    """Establish a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None

def create_logs_table():
    """Creates a logs table if it doesn't exist."""
    query = """
    CREATE TABLE IF NOT EXISTS logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        ip_address VARCHAR(45),
        username VARCHAR(255),
        password VARCHAR(255),
        message TEXT
    );
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

def insert_log(ip_address, username=None, password=None, message=None):
    """Inserts a log entry into the database."""
    query = """
    INSERT INTO logs (ip_address, username, password, message)
    VALUES (%s, %s, %s, %s);
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query, (ip_address, username, password, message))
        connection.commit()
        cursor.close()
        connection.close()
