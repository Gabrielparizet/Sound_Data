# Importing librosa.
import librosa


# Importing our audio file as filename.
filename = "/Users/gabrielparizet/Desktop/Sound_Data/api/audio_files/donato_dozzy_your_eyes.mp3"


# Load our audiofile in librosa.
y, sr = librosa.load(filename)


# Find the tempo and the beat_frames from our audiofile with librosa beat_track method.
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)


# The format_temp function takes a float as argument and rounds it to two decimals. 
def format_tempo(float):
    float = "{:.2f}".format(float)
    return float


# Get the duration of our audiofile in seconds with librosa get_duration method.
duration = librosa.get_duration(y=y, sr=sr)


# Get the duration of our audiofile in seconds with librosa get_duration method.
duration = librosa.get_duration(y=y, sr=sr)


# The seconds_to_minutes function takes time in float as an argument and converts it to string giving its time in minutes and seconds. 
def seconds_to_minutes (time):
    formated = "{:.2f}".format(time/60)
    formated = str(formated)
    x = formated.split('.')
    minutes = x[0]
    seconds = x[1]
    return f'{minutes} minutes and {seconds} seconds'


# Function calls:
file_duration = seconds_to_minutes(duration)
file_tempo = format_tempo(tempo)


print(f'Your audio file tempo is of {file_tempo} bpm.')
print(f'Your audio file is {file_duration} long.')