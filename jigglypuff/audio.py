from pathlib import Path
from pydub import AudioSegment


def load_audio(path: Path) -> AudioSegment:
    audio_file = AudioSegment.from_file(str(path.resolve()))

    return audio_file

def export_audio(audio: AudioSegment, path: Path, format, parameters=[]):
    audio.export(str(path.resolve()), format=format, parameters=parameters)
