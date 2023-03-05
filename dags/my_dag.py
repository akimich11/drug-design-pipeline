from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.get_sdfs import get_sdfs
from src.sdf_parse_energies import parse_energies
from src.sdf_to_smiles import sdf_to_smiles

with DAG("my_dag", start_date=datetime(2021, 1, 1), catchup=False) as dag:
    get_sdfs_task = PythonOperator(
        task_id="get_sdfs",
        python_callable=get_sdfs
    )
    parse_energies_task = PythonOperator(
        task_id="sdf_parse_energies",
        python_callable=parse_energies
    )

    sdf_to_smiles_task = PythonOperator(
        task_id="sdf_to_smiles",
        python_callable=sdf_to_smiles
    )

    get_sdfs_task >> parse_energies_task >> sdf_to_smiles_task
