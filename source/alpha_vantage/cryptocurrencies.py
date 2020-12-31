from ..settings import SETTINGS

from alpha_vantage.cryptocurrencies import CryptoCurrencies

import sys

sys.path.insert(0, '../')


__all__ = ['alpha_vantage_cryptocurrencies']


SETTINGS_ALPHA_VANTAGE = SETTINGS.get('alpha_vantage')

cryptocurrencies = CryptoCurrencies(
    key=SETTINGS_ALPHA_VANTAGE.get('key'),
    output_format=SETTINGS_ALPHA_VANTAGE.get('output_format'),
)

PERIODS = {
    'daily': cryptocurrencies.get_digital_currency_daily,
    'weekly': cryptocurrencies.get_digital_currency_weekly,
    'monthly': cryptocurrencies.get_digital_currency_monthly,
}


def alpha_vantage_cryptocurrencies(
    symbol,
    market=SETTINGS_ALPHA_VANTAGE.get('cryptocurrencies_market'),
    period=SETTINGS_ALPHA_VANTAGE.get('cryptocurrencies_period')
):
    data, meta_data = PERIODS.get(period)(symbol=symbol, market=market)

    return {'data': data, 'meta_data': meta_data}
