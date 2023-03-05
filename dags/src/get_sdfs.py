import glob
import os
from datetime import datetime


BASE_DIR = '/opt/airflow/dags'


def get_sdfs():
    out_filename = f'{BASE_DIR}/data/sdf/output/{datetime.utcnow().isoformat(timespec="seconds")}-ligands.sdf'
    filenames = glob.glob(f'{BASE_DIR}/data/sdf/input/**/*.sdf', recursive=True)

    with open('filenames.txt', 'w') as f:
        f.write(' '.join(filenames))
    os.system(f"cat $(grep -v '^#' filenames.txt) > {out_filename}")
    os.remove('filenames.txt')
    return out_filename
