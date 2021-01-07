from pydub import AudioSegment


__all__ = ['convert_audio']


# Supports MP3, OGG, FLV, WMA, ACC and MP4 audio / video file to WAV

def convert_audio(audio_buffer=None, convert='wav'):
    try:
        audio = AudioSegment.from_file_using_temporary_files(audio_buffer)
    except Exception as error:
        raise error

    audio_converted = audio.export(format=convert)

    audio_converted.seek(0)

    return audio_converted,
