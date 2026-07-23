CREATE TABLE fact_jobs (
    fact_id SERIAL PRIMARY KEY,

    job_id INT,

    company_id INT,
    location_id INT,
    job_dim_id INT,
    date_id INT,

    salary_min DECIMAL(10,2),
    salary_max DECIMAL(10,2),
    salary_avg DECIMAL(10,2),

    applicants INT,
    views INT,
    status VARCHAR(100),

    CONSTRAINT fk_company
        FOREIGN KEY (company_id)
        REFERENCES dim_company(company_id),

    CONSTRAINT fk_location
        FOREIGN KEY (location_id)
        REFERENCES dim_location(location_id),

    CONSTRAINT fk_job
        FOREIGN KEY (job_dim_id)
        REFERENCES dim_job(job_dim_id),

    CONSTRAINT fk_date
        FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);