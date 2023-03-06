
def filter_compounds(ti):
    unique_smiles_filename = ti.xcom_pull(task_ids=[
        'drop_duplicates'
    ])
