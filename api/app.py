# Import flask. Add the Flask.request object.
from flask import Flask, request
# Instantiate flask app and assign it to app variable.
app = Flask(__name__)

from sound_detector import find_tempo

@app.route("/upload", methods=["POST"])
def upload_file():
    audio_file = request.files["audioFile"]
    audio_file.save("/Users/gabrielparizet/Desktop/Sound_Data/api/audio_files/" + audio_file.filename)
    new_path = "/Users/gabrielparizet/Desktop/Sound_Data/api/audio_files/" + audio_file.filename
    find_tempo(new_path)
    return find_tempo(new_path)

