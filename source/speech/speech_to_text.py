from ..settings import SETTINGS

from io import BytesIO

import speech_recognition

import sys

sys.path.insert(0, '../')


__all__ = ['speech_to_text']


SETTINGS_GCP = SETTINGS.get('gcp')


recognizer = speech_recognition.Recognizer()


def speech_to_text(audio_buffer):
    source_buffer_memory = BytesIO(audio_buffer[0].read())

    with speech_recognition.AudioFile(source_buffer_memory) as source:
        audio = recognizer.record(source)

        text = recognizer.recognize_google_cloud(
            audio,
            credentials_json=SETTINGS_GCP.get('credentials'),
            language=SETTINGS_GCP.get('speech_language'),
            # preferred_phrases=SETTINGS_GCP.get('preferred_phrases'),
            show_all=SETTINGS_GCP.get('show_all'),
        )

        return text
