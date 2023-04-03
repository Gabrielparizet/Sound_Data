# Importing librosa.
import librosa

def find_tempo(filename):
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    file_tempo = format_tempo(tempo)
    return f'Your audio file tempo is of {file_tempo} bpm.'


def format_tempo(float):
    float = "{:.2f}".format(float)
    return float