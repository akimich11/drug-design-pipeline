import glob
import logging
import os
from datetime import datetime
from src.settings import BASE_DIR


def get_smiles():
    logger = logging.getLogger('airflow.task')
    out_filename = f'{BASE_DIR}/data/csv/output/{datetime.utcnow().isoformat(timespec="hours")}-ligands.csv'
    filenames = glob.glob(f'{BASE_DIR}/data/csv/input/**/*.csv', recursive=True)

    logger.info(f'FOUND CSV FILES: {filenames}')
    tmp_filename = f'{BASE_DIR}/csv_filenames.txt'

    with open(tmp_filename, 'w') as f:
        f.write(' '.join(filenames))
    os.system(f"cat $(grep -v '^#' {tmp_filename}) > {out_filename}")
    logger.info(f'MERGED ALL CSV FILES AS {out_filename}')
    os.remove(tmp_filename)
    return out_filename
