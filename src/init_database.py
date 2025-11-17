from dotenv import load_dotenv
import os
import pandas as pd
import psycopg2
import glob

def init_database(overwrite=False, verbose=False):
    # --- Load .env variables ---
    load_dotenv()

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")

    # --- Create/Overwrite database ---
    conn = psycopg2.connect(
        dbname="postgres",
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

    conn.autocommit = True
    with conn.cursor() as cursor:
        if (overwrite):
            cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
            if verbose:
                print(f"Database {db_name} dropped.")
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(f"CREATE DATABASE {db_name};")
            if verbose:
                print(f"Database {db_name} created.")

    conn.close()

    # --- Connect to db_name ---
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    if verbose:
        print(f'Connected to database {db_name} at {db_host}:{db_port} as user {db_user}')

    # IMPORTANT: this code will probably need to be changed
    # depending on the specifics of the imported csv files
    # specifically the clean data section
    with conn.cursor() as cursor:
        csv_files = glob.glob("data/*.csv")
        for file in csv_files:
            filename = os.path.splitext(os.path.basename(file))[0]

            # --- Read CSV file ---
            df = pd.read_csv(file)

            # --- Clean Data ---
            df.rename({df.columns[0]: 'Department'}, inplace=True)
            df.fillna(0, inplace=True)
            for i in range(2006, 2024):
                df[str(i)] = df[str(i)].map(lambda x: str(x).replace('$', '').replace(',', '')).map(lambda x: int(x) if x.replace('-', '').isdigit() else 0)

            # --- Convert from wide -> long format
            df_long = pd.melt(df, id_vars=['Department'], var_name='year', value_name='value')

            # --- skip if table already exists ---
            cursor.execute(f"""
                SELECT to_regclass('{filename}');
            """)
            table_exists = cursor.fetchone()[0]
            if table_exists:
                if verbose:
                    print(f"Table {filename} already exists. Skipping data insertion.")
                continue

            # --- Create table ---
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {filename} (
                    id SERIAL PRIMARY KEY,
                    department TEXT,
                    year INT,
                    value INT
                );
            """)

            # --- Insert data into table ---
            for _, row in df_long.iterrows():
                cursor.execute(f"""
                    INSERT INTO {filename} (department, year, value)
                    VALUES (%s, %s, %s);
                """, (row['Department'], row['year'], row['value']))
            if verbose:
                print(f"Data from {file} inserted into table {filename}.")

    print("Database initialization complete.")
    conn.commit()