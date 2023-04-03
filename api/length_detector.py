import librosa

# find_length takes an audio file as argument and returns a formatted string that indicates the length of that audio file.
def find_length(filename):
    # librosa.load is used to load the audio file into memory as a waveform "y" and a sample rate "sr".
    y, sr = librosa.load(filename)
    # Get the duration of our audiofile in seconds with librosa get_duration method.
    duration = librosa.get_duration(y=y, sr=sr)
    file_duration = seconds_to_minutes(duration)
    return file_duration


# The seconds_to_minutes function takes time in float as an argument and converts it to string giving its time in minutes and seconds. 
def seconds_to_minutes(time):
    formated = "{:.2f}".format(time/60)
    formated = str(formated)
    x = formated.split('.')
    minutes = x[0]
    seconds = x[1]
    return f'{minutes} minutes and {seconds} seconds'