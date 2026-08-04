import os
from io import StringIO

import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, inspect

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)


def load_data(df):

   
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE jobs RESTART IDENTITY;"))

   
    inspector = inspect(engine)
    db_columns = [c["name"] for c in inspector.get_columns("jobs")]

   
    df = df[[c for c in df.columns if c in db_columns]]

   
    df = df.reindex(columns=db_columns)

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME"),
    )

    cursor = conn.cursor()

    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False, na_rep="")
    buffer.seek(0)

    columns = ",".join(db_columns)

    cursor.copy_expert(
        f"COPY jobs ({columns}) FROM STDIN WITH (FORMAT CSV, NULL '')",
        buffer,
    )
    df = df[[c for c in df.columns if c in db_columns]]
    df = df.reindex(columns=db_columns)

    print("=== Final Columns ===")
    print(df.columns.tolist())

    conn.commit()
    cursor.close()
    conn.close()

    db_columns = [c["name"] for c in inspector.get_columns("jobs")]

    
    print(df.columns.tolist())


    
    print(db_columns)
    print(f"✅ {len(df)} rows loaded successfully into jobs.")