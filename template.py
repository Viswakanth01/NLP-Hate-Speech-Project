import os
from pathlib import Path
import logging

logging.basicConfig(format='[%(asctime)s] : %(levelname)s : %(message)s', level=logging.INFO)


project_name = 'hate_speech'

list_of_files = [
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestion.py',
    f'{project_name}/components/data_transformation.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/components/model_evaluator.py',
    f'{project_name}/components/model_pusher.py',
    f'{project_name}/configuration/__init__.py',
    f'{project_name}/configuration/gcloud_syncer.py',
    f'{project_name}/constants/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/entity/config_entity.py',
    f'{project_name}/entity/artifact_entity.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/constants/train_pipeline.py',
    f'{project_name}/constants/prediction_pipeline.py',
    f'{project_name}/ml/__init__.py',
    f'{project_name}/ml/model.py',
    'main.py',
    'demo.py',
    'requirements.txt',
    'Dockerfile',
    'setup.py'
    ".dockerignore"
]

for file_path in list_of_files:
    file = Path(file_path)

    filedir, filename = os.path.split(file_path)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f'Creating empty file {file_path}')

    else:
        logging.info(f"File {filename} already exists")
