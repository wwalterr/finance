# Rynk

Financial data API.

## Setup

1. Create and virtual environment

```sh
python3 -m venv venv
```

2. Activate the virtual environment

```sh
source venv/bin/activate
```

3. Install dependencies

```sh
pip install -r requirements.txt
```

4. Install language model dependencies

```sh
python -m spacy download en_core_web_trf # English Transformer pipeline, Roberta base
```

Check language model [releases](https://github.com/explosion/spacy-models/releases).

## Execute

1. Run the entry point

```sh
python main.py
```

## To do

- Convert any coin function

- Real time stock data (explore both APIs in use)

- Parse and filter NER

- Get stock data using the company name

- Stock dividends calendar (https://financialmodelingprep.com/developer/docs#Dividend-Calendar | https://iexcloud.io/docs/api/#upcoming-events)

- Crypto (https://www.alphavantage.co/documentation/)

- Speech to text (https://realpython.com/python-speech-recognition/)

- Fast API + security / access (https://fastapi.tiangolo.com/tutorial/first-steps/)

- Deploy (https://www.serverless.com/)

- Cat Boost (yfinance.download('SPY AAPL', start='2017-01-01', end='2017-04-30', group_by='ticker'))

- Update documentation