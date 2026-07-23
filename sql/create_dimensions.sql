DROP TABLE IF EXISTS dim_company CASCADE;
DROP TABLE IF EXISTS dim_location CASCADE;
DROP TABLE IF EXISTS dim_job CASCADE;
DROP TABLE IF EXISTS dim_date CASCADE;

CREATE TABLE dim_company (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    industry VARCHAR(100),
    company_size VARCHAR(50)
);

CREATE TABLE dim_location (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100)
);

CREATE TABLE dim_job (
    job_dim_id SERIAL PRIMARY KEY,
    job_title VARCHAR(255),
    experience_level VARCHAR(100),
    employment_type VARCHAR(100),
    remote_type VARCHAR(100),
    education VARCHAR(100),
    skills TEXT
);

CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    posted_date DATE,
    posted_year INT,
    posted_month INT
);