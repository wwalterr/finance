# Finance

Stock data from speech recognition and named-entity recognition

## Setup

Use the package manager APT to install the general dependencies.

```sh
sudo apt install python3 python3-dev python3-pip python3-venv
```

```sh
apt install libncurses5
```

```sh
apt install portaudio19-dev
```

Use the Python 3 to create a virtual environment.

```sh
python3 -m venv venv
```

Activate the virtual environment.

```sh
source ./venv/bin/activate
```

Use the package manager Pip to install the dependencies.

```sh
pip install -r requirements.txt
```

Use the module Spacy to install the PyTorch base and the language model.

```sh
pip install spacy-transformers --pre -f https://download.pytorch.org/whl/torch_stable.html
```

```sh
python -m spacy download en_core_web_trf
```

Add your credentials to _source/settings.py_ by replacing the empty quotes.

## Usage

You can add your speech sample on the base of this repository, change the path on _main.py_ and execute the script.

```sh
python main.py
```

## Documentation

To download more Spacy language models realted to the Transformer architecture check [released](https://github.com/explosion/spacy-models/releases) models.

After the virtual environment is created the dependencies can be easily installed through the script `./install.sh`.

## Contributing

Pull requests are welcome. Please, consider the following.

1. Make sure your code is standardized
2. Make sure your code is secure
3. Make sure your code is fast
4. Make sure your code is documented
5. Describe the changes that were done

> No issue or PR template required, but be informative

## License

[MIT](./LICENSE.md)
