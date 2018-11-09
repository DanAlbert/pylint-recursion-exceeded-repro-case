#!/bin/bash
virtualenv -p python3.6 env
source env/bin/activate
pip install --pre -U pylint
pylint foo
