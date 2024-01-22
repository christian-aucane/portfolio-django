#!/bin/bash

# TODO : Add MODE option (DEV or PROD), actually only DEV

python -m venv venv
if [ -d "venv/bin" ]; then
    VENV_PATH="venv/bin/activate"
# If not, check that the Scripts directory exists (for Windows)
elif [ -d "venv/Scripts" ]; then
    VENV_PATH="venv/Scripts/activate"
else
    echo "Erreur : Répertoire d'environnement virtuel introuvable."
    exit 1
fi

source $VENV_PATH
pip install -r requirements.txt


python scripts/write_env_file.py DEV

python src/manage.py migrate