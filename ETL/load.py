import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)


def load_data(df):
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE jobs RESTART IDENTITY;"))

    df.to_sql(
        name="jobs",
        con=engine,
        if_exists="append",
        index=False,
        method="multi",
    )

    print("✅ Data loaded successfully into jobs.")