from ..settings import SETTINGS

from alpha_vantage.timeseries import TimeSeries

import sys

sys.path.insert(0, '../')


__all__ = ['alpha_vantage_symbol_search']


SETTINGS_ALPHA_VANTAGE = SETTINGS.get('alpha_vantage')


time_series = TimeSeries(
    key=SETTINGS_ALPHA_VANTAGE.get('key'),
    output_format=SETTINGS_ALPHA_VANTAGE.get('output_format'),
)


def alpha_vantage_symbol_search(keywords):
    data, meta_data = time_series.get_symbol_search(
        keywords=keywords,
    )

    return {'data': dict(zip(data.columns, next(iter(data.values.tolist())))), 'meta_data': meta_data}
