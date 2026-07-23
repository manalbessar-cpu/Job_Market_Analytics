import os
import pandas as pd
from sqlalchemy import create_engine
from minio import Minio

# ==========================
# PostgreSQL Configuration
# ==========================

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "job_market_db"
DB_USER = "postgres"
DB_PASSWORD = "2004"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================
# MinIO Configuration
# ==========================

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="admin12345",
    secure=False
)

bucket_name = "job-market"

tables = [
    "dim_company",
    "dim_date",
    "dim_job",
    "dim_location",
    "fact_jobs"
]

for table in tables:

    print(f"Exporting {table}...")

    df = pd.read_sql(f"SELECT * FROM {table}", engine)

    file_name = f"{table}.parquet"

    df.to_parquet(file_name, index=False)

    client.fput_object(
        bucket_name,
        f"gold/{file_name}",
        file_name
    )

    os.remove(file_name)

    print(f"{table} uploaded successfully.")

print("Gold Layer exported to MinIO successfully!")