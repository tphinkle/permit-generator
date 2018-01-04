#!/bin/bash
export FLASK_APP=permit_generator.py
pip install --editable .

cd permit_generator
flask run
