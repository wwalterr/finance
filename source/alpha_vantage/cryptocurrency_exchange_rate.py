from ..settings import SETTINGS

from alpha_vantage.cryptocurrencies import CryptoCurrencies

import sys

sys.path.insert(0, '../')


__all__ = ['alpha_vantage_cryptocurrency_exchange_rate']


SETTINGS_ALPHA_VANTAGE = SETTINGS.get('alpha_vantage')


cryptocurrencies = CryptoCurrencies(
    key=SETTINGS_ALPHA_VANTAGE.get('key'),
    output_format=SETTINGS_ALPHA_VANTAGE.get('output_format'),
)


def alpha_vantage_cryptocurrency_exchange_rate(
    from_currency=SETTINGS_ALPHA_VANTAGE.get('cryptocurrencies_from_currency'),
    to_currency=SETTINGS_ALPHA_VANTAGE.get('cryptocurrencies_to_currency')
):
    data, meta_data = cryptocurrencies.get_digital_currency_exchange_rate(
        from_currency=from_currency,
        to_currency=to_currency
    )

    return {'data': data, 'meta_data': meta_data}
