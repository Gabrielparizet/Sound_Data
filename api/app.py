# Import flask. Add the Flask.request object.
from flask import Flask, request
# Instantiate flask app and assign it to app variable.
app = Flask(__name__)

# Importing find_tempo method from tempo_detector
from tempo_detector import find_tempo

# Importing find_length method from length_detector
from length_detector import find_length


@app.route("/upload", methods=["POST"])
def upload_file():
   audio_file = request.files["audioFile"]
   audio_file.save("/Users/gabrielparizet/Desktop/Sound_Data/api/audio_files/" + audio_file.filename)
   new_path = "/Users/gabrielparizet/Desktop/Sound_Data/api/audio_files/" + audio_file.filename
   result_response = find_tempo(new_path) + " " + find_length(new_path)
   return result_response

