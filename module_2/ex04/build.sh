#!/bin/bash

pip install --upgrade pip
pip install wheel
python3 setup.py sdist bdist_wheel
pip install .
