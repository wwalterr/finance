__all__ = ['SETTINGS']

SETTINGS = {
    'alpha_vantage': {
        'key': '',
        'output_format': 'json',
        'time_series_period': 'intraday',
        'tech_indicators_time_period': 60,
        'cryptocurrencies_period': 'daily',
        'cryptocurrencies_market': 'CNY',
        'cryptocurrencies_from_currency': 'BTC',
        'cryptocurrencies_to_currency': 'USD',
    },
    'gcp': {
        'credentials': r'''
			{
				"type": "",
				"project_id": "",
				"private_key_id": "",
				"private_key": "",
				"client_email": "",
				"client_id": "",
				"auth_uri": "",
				"token_uri": "",
				"auth_provider_x509_cert_url": "",
				"client_x509_cert_url": ""
			}
    	''',
        'speech_language': 'en-US',
        'preferred_phrases': [
            '$CARDINAL'
            '$ORGANIZATION'
            'MONEY'
            '$DATE'
        ],
        'show_all': False
    }
}
