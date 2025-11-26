import os
from dotenv import load_dotenv
import psycopg2

# Load variables from .env
load_dotenv()

# Read the DB connection info
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_connection():
    """
    Create and return a new database connection.
    Caller should close the connection when done.
    """
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Example usage:
if __name__ == "__main__":
    conn = get_connection()
    print("Successfully connected to the database!")
    conn.close()
