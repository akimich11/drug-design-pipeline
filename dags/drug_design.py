from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.tasks.drop_duplicates import drop_duplicates
from src.tasks.filter_compounds import filter_compounds
from src.tasks.get_smiles import get_smiles
from src.tasks.get_sdfs import get_sdfs
from src.tasks.sdf_parse_energies import parse_energies
from src.tasks.sdf_to_smiles import sdf_to_smiles


with DAG("drug_design", start_date=datetime(2021, 1, 1), catchup=False) as dag:
    get_smiles_task = PythonOperator(
        task_id="get_smiles",
        python_callable=get_smiles
    )
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
    drop_duplicates_task = PythonOperator(
        task_id="drop_duplicates",
        python_callable=drop_duplicates
    )
    filter_compounds_task = PythonOperator(
        task_id="filter_compounds",
        python_callable=filter_compounds
    )

    get_sdfs_task >> parse_energies_task >> sdf_to_smiles_task >> drop_duplicates_task >> filter_compounds_task
    get_smiles_task >> drop_duplicates_task
