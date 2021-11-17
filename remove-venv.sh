#!/bin/bash

NAME=horses-venv
TOTAL_VENVS=$(pyenv virtualenvs | grep $NAME | wc -l | bc)
if [[ $TOTAL_VENVS == 0 ]]; then
  pyenv uninstall $NAME
fi
