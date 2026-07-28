from extract import extract_data
from transform import transform_data
from load import load_data
from warehouse import run_sql_file


def main():

    print("Extracting data...")
    df = extract_data()

    print("Transforming data...")
    df = transform_data(df)

    print("Loading data into PostgreSQL...")
    load_data(df)

    print("Loading dimensions...")
    run_sql_file("sql/load_dimensions.sql")

    print("Loading fact table...")
    run_sql_file("sql/load_fact.sql")

    print("✅ Data Warehouse updated successfully!")


if __name__ == "__main__":
    main()