from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Manal",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="job_market_pipeline",
    default_args=default_args,
    description="Job Market Analytics ETL Pipeline",
    start_date=datetime(2026, 7, 24),
    schedule=None,
    catchup=False,
    tags=["ETL", "MinIO", "PostgreSQL"],
) as dag:

    etl_pipeline = BashOperator(
        task_id="etl_pipeline",
        bash_command="cd /opt/airflow/project && python -m ETL.main",
    )

    export_gold = BashOperator(
        task_id="export_gold",
        bash_command="cd /opt/airflow/project && python export_gold_to_minio.py",
    )

    etl_pipeline >> export_gold