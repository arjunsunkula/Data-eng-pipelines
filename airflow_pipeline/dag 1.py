from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

# DAG default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# DAG definition
with DAG(
    dag_id='load_gcs_to_bq',
    default_args=default_args,
    description='Load a CSV file from GCS to BigQuery',
    schedule_interval=None,  # You can set to '@daily' or a cron later
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['bigquery', 'gcs', 'csv'],
) as dag:

    # Task to load CSV from GCS to BigQuery
    load_csv_to_bigquery = GCSToBigQueryOperator(
        task_id='load_csv_to_bq',
        bucket='airflow-bucket01',  # ✅ Your GCS bucket name
        source_objects=['global_health_data.csv'],  # ✅ File path in bucket
        destination_project_dataset_table='lateral-rider-456109-s6.initial_dataset.global_data',
        source_format='CSV',
        allow_jagged_rows=True,
        ignore_unknown_values=True,
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows=1,
        field_delimiter=',',
        autodetect=True,
        # google_cloud_storage_conn_id='google_cloud_default',
        # bigquery_conn_id='google_cloud_default',
    )

    load_csv_to_bigquery





