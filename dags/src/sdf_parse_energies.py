BASE_DIR = '/opt/airflow/dags'


def parse_energies(ti):
    sdf_filename = ti.xcom_pull(task_ids='get_sdfs')
    is_next_energy = False

    energies = []

    with open(sdf_filename) as f:
        for line in f:
            if 'minimizedAffinity' in line:
                is_next_energy = True
                continue
            elif is_next_energy:
                energies.append(float(line))
                is_next_energy = False
    return energies
