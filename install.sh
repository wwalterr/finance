#!/usr/bin/env bash

# Spacy
sudo apt install libncurses5

# Speech recognition
apt install portaudio19-dev python-all-dev python3-all-dev

# Python modules
pip install -r requirements.txt

pip install spacy-transformers --pre -f https://download.pytorch.org/whl/torch_stable.html

python -m spacy download en_core_web_trf