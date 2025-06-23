# Terminal Cheat Sheet

## Create a new project
cp -r ~/Templates/quant_project_template ~/Projects/my_new_project
cd ~/Projects/my_new_project

## Start project
poetry install
poetry shell

## Add a dependency
poetry add numpy

## Run script
poetry run python src/your_module/main.py

## Run tests
poetry run pytest
