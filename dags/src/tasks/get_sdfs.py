import glob
import logging
import os
from datetime import datetime
from src.settings import BASE_DIR


def get_sdfs():
    logger = logging.getLogger('airflow.task')
    out_filename = f'{BASE_DIR}/data/sdf/output/{datetime.utcnow().isoformat(timespec="hours")}-ligands.sdf'
    filenames = glob.glob(f'{BASE_DIR}/data/sdf/input/**/*.sdf', recursive=True)

    logger.info(f'FOUND SDF FILES: {filenames}')
    tmp_filename = f'{BASE_DIR}/sdf_filenames.txt'

    with open(tmp_filename, 'w') as f:
        f.write(' '.join(filenames))
    os.system(f"cat $(grep -v '^#' {tmp_filename}) > {out_filename}")
    os.remove(tmp_filename)
    return out_filename
