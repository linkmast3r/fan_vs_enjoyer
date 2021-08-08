#!/bin/bash
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
sudo apt update
sudo apt install ffmpeg imagemagick
pip install -r requirements.txt
