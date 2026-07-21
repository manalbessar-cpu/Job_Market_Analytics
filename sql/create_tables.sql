-- =====================================================
-- Job Market Analytics Data Warehouse
-- Star Schema
-- =====================================================

-- ===========================
-- Dimension Table: Company
-- ===========================

CREATE TABLE IF NOT EXISTS dim_company (

    company_id SERIAL PRIMARY KEY,

    company_name VARCHAR(255) NOT NULL,

    industry VARCHAR(150),

    company_size VARCHAR(100)

);

-- ===========================
-- Dimension Table: Location
-- ===========================

CREATE TABLE IF NOT EXISTS dim_location (

    location_id SERIAL PRIMARY KEY,

    city VARCHAR(100),

    country VARCHAR(100),

    region VARCHAR(100)

);

-- ===========================
-- Dimension Table: Job
-- ===========================

CREATE TABLE IF NOT EXISTS dim_job (

    job_dim_id SERIAL PRIMARY KEY,

    job_title VARCHAR(255) NOT NULL,

    experience_level VARCHAR(100),

    employment_type VARCHAR(100),

    remote_type VARCHAR(100),

    education VARCHAR(255),

    skills TEXT

);

-- ===========================
-- Dimension Table: Date
-- ===========================

CREATE TABLE IF NOT EXISTS dim_date (

    date_id SERIAL PRIMARY KEY,

    posted_date DATE NOT NULL,

    posted_year INT,

    posted_month INT

);

-- ===========================
-- Fact Table: Jobs
-- ===========================

CREATE TABLE IF NOT EXISTS fact_jobs (

    fact_id SERIAL PRIMARY KEY,

    job_id INT NOT NULL,

    company_id INT NOT NULL,

    location_id INT NOT NULL,

    job_dim_id INT NOT NULL,

    date_id INT NOT NULL,

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