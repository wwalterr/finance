from json import dumps


__all__ = ['print_formated']


DEFAULT_OPTIONS_JSON_DUMPS = {'indent': 4, 'sort_keys': False, 'default': str}


def print_formated(text, data, options=DEFAULT_OPTIONS_JSON_DUMPS):
    print(f'{text}: {dumps(data, **options)}')
