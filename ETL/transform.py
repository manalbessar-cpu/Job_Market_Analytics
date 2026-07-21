import pandas as pd

def transform_data(df):

    # Create a copy of the DataFrame
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values in salary_min with the median
    df.loc[:, "salary_min"] = df["salary_min"].fillna(df["salary_min"].median())

    # Convert posted_date to datetime
    df.loc[:, "posted_date"] = pd.to_datetime(df["posted_date"])

    # Standardize employment_type values
    df.loc[:, "employment_type"] = df["employment_type"].replace({
        "Full time": "Full-time"
    })

    # Create average salary column
    df.loc[:, "salary_avg"] = (
        df["salary_min"] + df["salary_max"]
    ) / 2

    return df