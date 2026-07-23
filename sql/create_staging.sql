DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
    job_id INT PRIMARY KEY,
    job_title VARCHAR(255),
    company_name VARCHAR(255),
    industry VARCHAR(100),
    company_size VARCHAR(50),
    city VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    experience_level VARCHAR(100),
    employment_type VARCHAR(100),
    remote_type VARCHAR(100),
    salary_min NUMERIC(10,2),
    salary_max NUMERIC(10,2),
    education VARCHAR(100),
    applicants INT,
    views INT,
    posted_date DATE,
    skills TEXT,
    salary_avg NUMERIC(10,2)
);