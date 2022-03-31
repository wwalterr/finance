# Finance

Stock data from Speech Synthesis and Named-entity Recognition

## Setup

1. Create and virtual environment

```sh
python3 -m venv venv
```

2. Activate the virtual environment

```sh
source venv/bin/activate
```

> All the steps below can be done by running the installation script `./install.sh`

3. Install dependencies

```sh
sudo apt install libncurses5 # Spacy
```

```sh
apt install portaudio19-dev python-all-dev python3-all-dev # Speech recognition
```

```sh
pip install -r requirements.txt
```

```sh
pip install spacy-transformers --pre -f https://download.pytorch.org/whl/torch_stable.html
```

1. Download a language model

```sh
python -m spacy download en_core_web_trf
```

Check available language model [releases](https://github.com/explosion/spacy-models/releases).

## Execute

1. Run the entry point

```sh
python main.py
```