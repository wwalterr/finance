import spacy


__all__ = ['spacy_ner']


nlp = spacy.load('en_core_web_trf')


def spacy_ner(text):
    document = nlp(text)

    return [{'label': entity.label_, 'text': entity.text} for entity in document.ents]
