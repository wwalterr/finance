from ..settings import SETTINGS

from alpha_vantage.timeseries import TimeSeries

import sys

sys.path.insert(0, '../')


__all__ = ['alpha_vantage_time_series']


SETTINGS_ALPHA_VANTAGE = SETTINGS.get('alpha_vantage')

time_series = TimeSeries(
    key=SETTINGS_ALPHA_VANTAGE.get('key'),
    output_format=SETTINGS_ALPHA_VANTAGE.get('output_format'),
)

PERIODS = {
    'intraday': time_series.get_intraday,
    'daily': time_series.get_daily,
    'weekly': time_series.get_weekly,
    'monthly': time_series.get_monthly,
}


def alpha_vantage_time_series(
    symbol,
    period=SETTINGS_ALPHA_VANTAGE.get('time_series_period'),
):
    data, meta_data = PERIODS.get(period)(
        symbol=symbol,
    )

    return {'data': data, 'meta_data': meta_data}
