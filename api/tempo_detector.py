# Importing librosa.
import librosa

# find_tempo takes an audio file as argument and returns a formatted string that indicates the tempo of that audio file.
def find_tempo(file_name):
    # librosa.load is used to load the audio file into memory as a waveform "y" and a sample rate "sr".
    y, sr = librosa.load(file_name)
    # librosa.beat.beat_track is used to calculate the tempo of the audio file based on its beat frames, which are stored in beat_frames.
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    file_tempo = format_tempo(tempo)
    return f'Your audio file tempo is of {file_tempo} bpm.'

# format_tempo takes a floating-point number and returns a string representation of that number with two decimal places.
def format_tempo(float):
    float = "{:.2f}".format(float)
    return float


