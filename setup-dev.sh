#!/bin/bash

NAME=horses-venv
TOTAL_VENVS=$(pyenv virtualenvs | grep $NAME | wc -l | bc)
if [[ $TOTAL_VENVS == 0 ]]; then
  pyenv install -s 3.8.1
  pyenv virtualenv 3.8.1 $NAME
  pyenv local $NAME
fi

pip install .
pip install .[dev]