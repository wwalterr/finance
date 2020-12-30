from yfinance import Ticker


__all__ = ['yahoo_stock']


def yahoo_stock(symbol):
    return Ticker(symbol)
