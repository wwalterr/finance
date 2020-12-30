from ..settings import SETTINGS

from alpha_vantage.techindicators import TechIndicators

import sys

sys.path.insert(0, '../')


__all__ = ['alpha_vantage_tech_indicators']


SETTINGS_ALPHA_VANTAGE = SETTINGS.get('alpha_vantage')


tech_indicators = TechIndicators(
    key=SETTINGS_ALPHA_VANTAGE.get('key'),
    output_format=SETTINGS_ALPHA_VANTAGE.get('output_format'),
)


def alpha_vantage_tech_indicators(
    symbol,
    time_period=SETTINGS_ALPHA_VANTAGE.get('time_period'),
):
    data, meta_data = tech_indicators.get_bbands(
        symbol=symbol,
        time_period=time_period
    )

    return {'data': data, 'meta_data': meta_data}
