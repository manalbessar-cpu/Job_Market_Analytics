-- ==========================
-- Clean Dimensions
-- ==========================

TRUNCATE TABLE fact_jobs RESTART IDENTITY CASCADE;

TRUNCATE TABLE dim_company RESTART IDENTITY CASCADE;
TRUNCATE TABLE dim_location RESTART IDENTITY CASCADE;
TRUNCATE TABLE dim_job RESTART IDENTITY CASCADE;
TRUNCATE TABLE dim_date RESTART IDENTITY CASCADE;


-- ==========================
-- Load dim_company
-- ==========================

INSERT INTO dim_company (
    company_name,
    industry,
    company_size
)
SELECT DISTINCT
    company_name,
    industry,
    company_size
FROM jobs
WHERE company_name IS NOT NULL;


-- ==========================
-- Load dim_location
-- ==========================

INSERT INTO dim_location (
    city,
    country,
    region
)
SELECT DISTINCT
    city,
    country,
    region
FROM jobs;


-- ==========================
-- Load dim_job
-- ==========================

INSERT INTO dim_job (
    job_title,
    experience_level,
    employment_type,
    remote_type,
    education,
    skills
)
SELECT DISTINCT
    job_title,
    experience_level,
    employment_type,
    remote_type,
    education,
    skills
FROM jobs;


-- ==========================
-- Load dim_date
-- ==========================

INSERT INTO dim_date (
    posted_date,
    posted_year,
    posted_month
)
SELECT DISTINCT
    posted_date,
    EXTRACT(YEAR FROM posted_date),
    EXTRACT(MONTH FROM posted_date)
FROM jobs;