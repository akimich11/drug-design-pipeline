import logging
from datetime import datetime
import pandas as pd
from src.settings import BASE_DIR


def drop_duplicates(ti):
    logger = logging.getLogger("airflow.task")
    sdf_filename, smiles_filename = ti.xcom_pull(task_ids=[
        'sdf_to_smiles',
        'get_smiles'
    ])

    df_from_sdf = pd.read_csv(sdf_filename)
    df_from_smiles = pd.read_csv(smiles_filename)
    del df_from_smiles['babel_smiles'], df_from_smiles['filepath_smi']

    df = pd.concat([df_from_sdf, df_from_smiles])

    full_size = df['smiles'].shape[0]
    unique_size = df['smiles'].unique().shape[0]
    logger.info(f"TOTAL COMPOUNDS: {full_size}, UNIQUE COMPOUNDS: {unique_size}")

    filename = f'{BASE_DIR}/data/csv/{datetime.utcnow().isoformat(timespec="hours")}-unique-smiles.csv'
    df = df.drop_duplicates(subset=['smiles'])
    df = df.reset_index(drop=True)
    df.to_csv(filename)

    return filename
