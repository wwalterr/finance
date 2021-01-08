import spacy


__all__ = ['spacy_ner']


LANGUAGES = {
    'en-US': 'en_core_web_trf'
}


def spacy_ner(text, language=''):
    nlp = spacy.load(LANGUAGES.get(language, 'en_core_web_trf'))

    document = nlp(text)

    return [{'label': entity.label_, 'content': entity.text} for entity in document.ents]
