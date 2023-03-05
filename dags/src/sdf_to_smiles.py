from datetime import datetime

from rdkit import Chem
from tqdm import tqdm

BASE_DIR = '/opt/airflow/dags'


def sdf_to_smiles(ti):
    sdf_filename, energies = ti.xcom_pull(task_ids=[
        'get_sdfs',
        'sdf_parse_energies'
    ])
    sdf_file = Chem.SDMolSupplier(sdf_filename)
    out_filename = f'{BASE_DIR}/data/csv/{datetime.utcnow().isoformat(timespec="seconds")}-smiles-from-sdf.csv'

    my_enumerate = enumerate(sdf_file)

    with open(out_filename, "w") as f:
        f.write('energy,smiles\n')
        with tqdm(my_enumerate,
                  bar_format="{postfix[0]:.2f}% | elapsed: {elapsed}", postfix=[0]) as t:
            for i, mol in my_enumerate:
                if mol is not None:  # avoiding compounds that cannot be loaded.
                    smi = Chem.MolToSmiles(mol)
                    f.write(f"{energies[i]},{smi}\n")
                t.postfix[0] = (i + 1) / len(sdf_file) * 100
                t.update()
