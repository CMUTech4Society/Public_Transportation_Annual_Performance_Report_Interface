from dotenv import load_dotenv
import os
import psycopg2

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

    def fetch_data(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    @property
    def conn(self):
        return self.connection

    @conn.deleter
    def conn(self):
        self.connection.close()
        print("Database connection closed.")
        del self.connection