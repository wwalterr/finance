from cryptocompare import get_coin_list


__all__ = ['cryptocompare_cryptos']


def cryptocompare_cryptos(symbol=None):
    cryptos_list = get_coin_list(format=False)

    return cryptos_list.get(symbol) if symbol else cryptos_list
