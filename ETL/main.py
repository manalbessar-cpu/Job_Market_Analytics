from extract import extract_data
from transform import transform_data
from load import load_data

input_file = "data/job_market_analytics.csv"

df = extract_data(input_file)
df = transform_data(df)

load_data(df)

print("ETL Pipeline completed successfully!")
