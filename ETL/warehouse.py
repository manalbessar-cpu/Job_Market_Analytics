import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)


def run_sql_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        sql = file.read()

    with engine.begin() as conn:
        # كنقسم الملف على ; باش يقدر يشغل أكثر من Query
        statements = sql.split(";")

        for statement in statements:
            statement = statement.strip()

            if statement:
                conn.execute(text(statement))

    print(f"✅ Executed: {file_path}")