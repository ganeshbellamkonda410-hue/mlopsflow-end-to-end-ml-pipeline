from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "nivas",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="mlopsflow_student_dropout_pipeline",
    default_args=default_args,
    description="End-to-end ML pipeline DAG for student dropout prediction",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["mlops", "mlflow", "xgboost"],
) as dag:

    run_pipeline = BashOperator(
        task_id="run_training_pipeline",
        bash_command="cd /opt/airflow/project && python -m pipelines.run_pipeline",
    )

    run_pipeline
