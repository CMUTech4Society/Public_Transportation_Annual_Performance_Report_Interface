from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd

class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        print(f'Connecting to database {db_name} at {db_host}:{db_port} as user {db_user}')
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )

    def get_table_names(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """)
            tables = cursor.fetchall()
            return [table[0] for table in tables]

    def fetch_data(self, table_name):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(f'SELECT * FROM {table_name};')
            except Exception as e:
                print(f"Error fetching data from table {table_name}: {e}")
                return []
            return pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    @property
    def conn(self):
        return self.connection

    @conn.deleter
    def conn(self):
        self.connection.close()
        print("Database connection closed.")
        del self.connection