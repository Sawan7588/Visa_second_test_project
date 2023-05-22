import os
import sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter your project name : ")
    if project_name !='':
        break

logging.basicConfig(
    level= logging.INFO,
    format="[%(asctime)s: %(levelname)s] %(message)s"
)
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "setup.py",
    "main.py",
    "requirements.txt",
    "demo.py"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating new directory at : {filedir} for file:{filename}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating new file at :{filedir} for file: {filename}")
    else:
        logging.info(f"file is already present at: {filename}")
