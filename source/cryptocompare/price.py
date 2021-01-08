from cryptocompare import get_price


__all__ = ['cryptocompare_price']


def cryptocompare_price(symbol_from, symbool_to=None):
    if not symbool_to:
        return get_price(symbol_from)
    else:
        return get_price(symbol_from, curr=symbool_to)
