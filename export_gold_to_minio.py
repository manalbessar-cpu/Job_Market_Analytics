import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from minio import Minio

# ==========================
# Load Environment Variables
# ==========================

load_dotenv()

# ==========================
# PostgreSQL Configuration
# ==========================

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

# ==========================
# MinIO Configuration
# ==========================

client = Minio(
    os.getenv("MINIO_HOST"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False,
)

bucket_name = os.getenv("MINIO_BUCKET")

# ==========================
# Tables to Export
# ==========================

tables = [
    "dim_company",
    "dim_date",
    "dim_job",
    "dim_location",
    "fact_jobs",
]

# ==========================
# Export Gold Layer
# ==========================

for table in tables:

    print(f"Exporting {table}...")

    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)

    file_name = f"{table}.parquet"

    df.to_parquet(file_name, index=False)

    client.fput_object(
        bucket_name,
        f"gold/{file_name}",
        file_name,
    )

    os.remove(file_name)

    print(f"✅ {table} uploaded successfully.")

conn.close()

print("✅ Gold Layer exported successfully.")