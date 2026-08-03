📊 Job Market Analytics
📖 Overview

Job Market Analytics is an end-to-end Data Engineering and Business Intelligence project designed to analyze job market trends through an automated ETL pipeline and interactive Power BI dashboards.

The project covers the complete data lifecycle, from data extraction and transformation to data warehousing and business visualization.

🎯 Project Objectives
Collect job market data.
Clean and transform data using Python.
Build an automated ETL pipeline.
Store data in a Data Lake (MinIO).
Design a PostgreSQL Data Warehouse.
Implement a Star Schema.
Create interactive Power BI dashboards.
Support business decision-making with data-driven insights.
🏗️ Project Architecture
Source Dataset
      │
      ▼
Python ETL
      │
      ▼
PostgreSQL Staging
      │
      ├────────► MinIO
      │          Bronze
      │          Silver
      │          Gold
      ▼
PostgreSQL Data Warehouse
      │
      ▼
Power BI Dashboard
🗄️ Data Warehouse
Fact Table
fact_jobs
Dimension Tables
dim_company
dim_job
dim_location
dim_date
🛠️ Technologies
Python
Pandas
NumPy
PostgreSQL
SQLAlchemy
SQL
MinIO
Docker
Apache Airflow
Power BI
Git & GitHub
📊 Dashboard

The Power BI dashboard contains three pages.

1️⃣ Executive Dashboard
Global KPIs
Countries
Cities
Hiring Trends
Remote Jobs
2️⃣ Job Market Analysis
Skills
Job Titles
Salary
Experience
Employment Types
3️⃣ Company Analysis
Companies
Industries
Company Size
Hiring Locations
🚀 Features
Automated ETL Pipeline
Medallion Architecture
PostgreSQL Data Warehouse
Star Schema
Interactive Dashboard
Cross-page Filters
Navigation Buttons

👩‍💻 Author

Manal Bessar

Junior Data Analyst