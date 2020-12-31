from ..settings import SETTINGS

from alpha_vantage.cryptocurrencies import CryptoCurrencies

import sys

sys.path.insert(0, '../')


__all__ = ['alpha_vantage_cryptocurrency_rating']


SETTINGS_ALPHA_VANTAGE = SETTINGS.get('alpha_vantage')


cryptocurrencies = CryptoCurrencies(
    key=SETTINGS_ALPHA_VANTAGE.get('key'),
    output_format=SETTINGS_ALPHA_VANTAGE.get('output_format'),
)


def alpha_vantage_cryptocurrency_rating(symbol):
    data, meta_data = cryptocurrencies.get_digital_crypto_rating(symbol=symbol)

    return {'data': data, 'meta_data': meta_data}
