from re import findall

from numbers import Number


__all__ = ['ner_validation']


REQUIRED_LABELS = ['CARDINAL', 'ORG', 'MONEY']


def ner_validation(entities, ignore_unrequired=True):
    entities_labels = sorted([entity.get('label') for entity in entities])

    unrequired_entities_labels = set(entities_labels) - set(REQUIRED_LABELS)

    if unrequired_entities_labels and not ignore_unrequired:
        return True, 'Unrequired entity (s) not found', list(unrequired_entities_labels)

    required_entities_labels = set(REQUIRED_LABELS) - set(entities_labels)

    if required_entities_labels:
        return True, 'Required entity (s) not found', list(required_entities_labels)

    entities_filtered = {
        entity.get('label'): entity.get('content') for entity in entities
    }

    entities_parted = {
        'symbol': {'value': entities_filtered.get('ORG'), 'label': 'ORG'},
        'quantity': {
            'value': int(
                next(
                    iter(findall(r'\d+', entities_filtered.get('CARDINAL'))), 1
                )
            ),
            'label': 'CARDINAL'
        },
        'price': {
            'value': float(
                next(
                    iter(findall(r'\d+\.\d+', entities_filtered.get('MONEY'))), 1
                ),
            ),
            'label': 'MONEY'
        }
    }

    for entity_key, entity_value in entities_parted.items():
        if isinstance(entity_value.get('value'), Number) and entity_value.get('value') == 0:
            return True, 'Invalid value, zero is not a valid', [entity_value.get('label')]

    return False, '', entities_parted
