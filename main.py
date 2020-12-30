from source.alpha_vantage import (
    alpha_vantage_time_series,
    alpha_vantage_symbol_search,
    alpha_vantage_tech_indicators
)

from source.yahoo import yahoo_stock

from source.utils import print_formated

from source.spacy_ner import spacy_ner


STOCK = {
    'name': 'Nvidia',
    'code': 'NVDA'
}


# print_formated(
#     text=f'Alpha Vantage symbol search, {STOCK.get("name")} stock',
#     data=alpha_vantage_symbol_search(STOCK.get('name'))
# )

# print_formated(
#     text=f'Alpha Vantage time series, {STOCK.get("name")} stock',
#     data=alpha_vantage_time_series(STOCK.get('code'), period='daily')
# )

# print_formated(
#     text=f'Alpha Vantage tech indicators, {STOCK.get("name")} stock',
#     data=alpha_vantage_tech_indicators(STOCK.get('code'))
# )


# data = yahoo_stock(STOCK.get('code'))

# print_formated(
#     text=f'Yahoo, {STOCK.get("name")} stock',
#     data={
#         'info': data.info,  # Dict
#         'history': data.history('1d').reset_index(drop=True).to_dict(),  # Data Frame
#         'dividends': data.dividends.reset_index(drop=True).to_dict(),  # Series
#         'splits': data.splits.reset_index(drop=True).to_dict(),  # Series
#         'financials': data.financials.reset_index(drop=True).to_dict(),  # Data Frame
#         'major_holders': data.major_holders.reset_index(drop=True).to_dict(),  # Data Frame
#         'institutional_holders': data.institutional_holders.reset_index(drop=True).to_dict(),  # Data Frame
#         # 'balance_sheet': data.balance_sheet.reset_index(drop=True).to_dict(),  # Data Frame
#         # 'cashflow': data.cashflow.reset_index(drop=True).to_dict(),  # Data Frame
#         # 'earnings': data.earnings.reset_index(drop=True).to_dict(),  # Data Frame
#         # 'ysustainability': data.sustainability.reset_index(drop=True).to_dict(),  # Data Frame
#         # 'recommendations': data.recommendations.reset_index(drop=True).to_dict(),  # Data Frame
#         'calendar': data.calendar.reset_index(drop=True).to_dict(),  # Data Frame
#     }
# )


# print(spacy_ner(
#     '20 Stocks from NVIDIA at the price of 58.23 dolars, purchased at 01/01/2020'
# ))
