from minio import Minio
from io import BytesIO
import pandas as pd


def extract_data():

    client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    obj = client.get_object(
        "job-market",
        "silver/job_market_cleaned.csv"
    )

    df = pd.read_csv(BytesIO(obj.read()))

    return df