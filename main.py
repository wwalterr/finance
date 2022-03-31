from source.utils import print_formated

from source.speech import convert_audio, speech_to_text

from source.spacy_ner import spacy_ner, ner_validation

from source.alpha_vantage import (
    alpha_vantage_time_series,
    alpha_vantage_symbol_search,
    alpha_vantage_tech_indicators,
    alpha_vantage_cryptocurrencies,
    alpha_vantage_cryptocurrency_rating,
    alpha_vantage_cryptocurrency_exchange_rate
)

from source.yahoo import yahoo_stock

from source.cryptocompare import cryptocompare_price, cryptocompare_cryptos


audio_converted = convert_audio(
    open('./source/speech/samples/sample_1_stock.wav', 'rb')
)

speech_text = speech_to_text(audio_converted)

print('Speech to text:', speech_text)


speech_entities = spacy_ner(speech_text)

print('Speech entities: ', speech_entities)


(
    speech_entities_error,
    speech_entities_message,
    speech_entities_validated
) = ner_validation(speech_entities)

print('Speech entities validated:', speech_entities_validated)


STOCK = {
    'name': 'Nvidia',
    'symbol': 'NVDA'
}

CRYPTOCURRENCY = {
    'name': 'Bitcoin',
    'symbol': 'BTC',
    'market': 'CNY',
    'from_currency': 'BTC',
    'to_currency': 'USD'
}


print_formated(
    text=f'Alpha Vantage symbol search, {STOCK.get("name")} stock',
    data=alpha_vantage_symbol_search(STOCK.get('name'))
)

print_formated(
    text=f'Alpha Vantage time series, {STOCK.get("name")} stock',
    data=alpha_vantage_time_series(STOCK.get('symbol'), period='daily')
)

print_formated(
    text=f'Alpha Vantage tech indicators, {STOCK.get("name")} stock',
    data=alpha_vantage_tech_indicators(STOCK.get('symbol'))
)

print_formated(
    text=f'Alpha Vantage cryptocurrency, {CRYPTOCURRENCY.get("name")}',
    data=alpha_vantage_cryptocurrencies(
        CRYPTOCURRENCY.get('symbol'),
        CRYPTOCURRENCY.get('market')
    )
)

print_formated(
    text=f'Alpha Vantage cryptocurrency rating, {CRYPTOCURRENCY.get("name")}',
    data=alpha_vantage_cryptocurrency_rating(CRYPTOCURRENCY.get('symbol'))
)

print_formated(
    text=f'Alpha Vantage cryptocurrency exchange rate, from {CRYPTOCURRENCY.get("from_currency")} to {CRYPTOCURRENCY.get("to_currency")}',
    data=alpha_vantage_cryptocurrency_exchange_rate(
        CRYPTOCURRENCY.get("from_currency"),
        CRYPTOCURRENCY.get("to_currency")
    )
)


yahoo_data = yahoo_stock(STOCK.get('symbol'))

print_formated(
    text=f'Yahoo, {STOCK.get("name")} stock',
    data={
        'info': yahoo_data.info,  # Dict
        # Data Frame
        'history': yahoo_data.history('1d').reset_index(drop=True).to_dict(),
        # Series
        'dividends': yahoo_data.dividends.reset_index(drop=True).to_dict(),
        'splits': yahoo_data.splits.reset_index(drop=True).to_dict(),  # Series
        # Data Frame
        'financials': yahoo_data.financials.reset_index(drop=True).to_dict(),
        # Data Frame
        'major_holders': yahoo_data.major_holders.reset_index(drop=True).to_dict(),
        # Data Frame
        'institutional_holders': yahoo_data.institutional_holders.reset_index(drop=True).to_dict(),
        # 'balance_sheet': yahoo_data.balance_sheet.reset_index(drop=True).to_dict(),  # Data Frame
        # 'cashflow': yahoo_data.cashflow.reset_index(drop=True).to_dict(),  # Data Frame
        # 'earnings': yahoo_data.earnings.reset_index(drop=True).to_dict(),  # Data Frame
        # 'ysustainability': yahoo_data.sustainability.reset_index(drop=True).to_dict(),  # Data Frame
        # 'recommendations': yahoo_data.recommendations.reset_index(drop=True).to_dict(),  # Data Frame
        # Data Frame
        'calendar': yahoo_data.calendar.reset_index(drop=True).to_dict(),
    }
)


print('Crypto compare list', cryptocompare_cryptos(CRYPTOCURRENCY.get('symbol')))

print('Crypto compare price', cryptocompare_price(
    CRYPTOCURRENCY.get('from_currency'), CRYPTOCURRENCY.get('to_currency')))
