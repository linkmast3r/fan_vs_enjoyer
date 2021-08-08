#!/bin/bash
source env/bin/activate
sudo apt update
sudo apt install ffmpeg imagemagick
pip install -r requirements.txt
