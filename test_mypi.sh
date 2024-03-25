#!/bin/bash

conda create -n test python=3.10 pip -y
conda activate test
pip install ml-digits-recognition
python -c "from ml_digits_recognition import drawing; drawing.run()"