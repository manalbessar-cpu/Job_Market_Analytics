-- ==========================
-- Clean Fact Table
-- ==========================

TRUNCATE TABLE fact_jobs RESTART IDENTITY;


-- ==========================
-- Load fact_jobs
-- ==========================

INSERT INTO fact_jobs (
    job_id,
    company_id,
    location_id,
    job_dim_id,
    date_id,
    salary_min,
    salary_max,
    salary_avg,
    applicants,
    views,
    status
)

SELECT
    j.job_id,
    dc.company_id,
    dl.location_id,
    dj.job_dim_id,
    dd.date_id,
    j.salary_min,
    j.salary_max,
    (j.salary_min + j.salary_max) / 2 AS salary_avg,
    j.applicants,
    j.views,
    'Active'

FROM jobs j

JOIN dim_company dc
    ON j.company_name = dc.company_name
   AND j.industry = dc.industry
   AND j.company_size = dc.company_size

JOIN dim_location dl
    ON j.city = dl.city
   AND j.country = dl.country
   AND j.region = dl.region

JOIN dim_job dj
    ON j.job_title = dj.job_title
   AND j.experience_level = dj.experience_level
   AND j.employment_type = dj.employment_type
   AND j.remote_type = dj.remote_type
   AND j.education = dj.education
   AND j.skills = dj.skills

JOIN dim_date dd
    ON j.posted_date = dd.posted_date;