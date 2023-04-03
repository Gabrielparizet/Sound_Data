# Import flask. Add the Flask.request object.
from flask import Flask, request
# Instantiate flask app and assign it to app variable.
app = Flask(__name__)

# @app.get("/")
# def test_route():
#    return "Your connected to your flask server"

@app.route("/upload", methods=["POST"])
def upload_file():
    audio_file = request.files["audioFile"]
    audio_file.save("/Users/gabrielparizet/Desktop/Sound_Data/api/audio_files/" + audio_file.filename)
    return "File uploaded successfully"