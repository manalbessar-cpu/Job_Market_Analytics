import os
from io import BytesIO

import pandas as pd
from dotenv import load_dotenv
from minio import Minio

load_dotenv()


def extract_data():

    client = Minio(
        os.getenv("MINIO_HOST"),
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False,
    )

    obj = client.get_object(
        os.getenv("MINIO_BUCKET"),
        "silver/job_market_cleaned.csv",
    )

    df = pd.read_csv(BytesIO(obj.read()))

    return df