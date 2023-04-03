# Importing Miscellaneous operating system interfaces
import os

# Import flask. Add the Flask.flash, Flask.request,  Flask.redirect, Flask.url_for objects. Add the Flask.json object.
from flask import Flask, flash, request, redirect, url_for, jsonify

# Import secure_filename method from werkzeug to secure the audio file name before storing it in our filesystem. 
from werkzeug.utils import secure_filename

# Importing find_tempo method from tempo_detector
from tempo_detector import find_tempo

# Importing find_length method from length_detector
from length_detector import find_length

# Defining path where to upload audio files in UPLOAD_FOLDER
UPLOAD_FOLDER = "/Users/gabrielparizet/Desktop/Sound_Data/api/audio_files/"

# Defininf allowed audio files extension for the upload
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'aiff', 'flac', 'ogg'}

# Instantiate flask app and assign it to app variable.
app = Flask(__name__)

# Configure Upload_folder as the path where we will store our audio_files in our filesystem.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# allowed_file function checks if an extension is valid
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
   if request.method == "POST":
      # check if the post request has the file part
         if 'audioFile' not in request.files:
            flash('No file part')
            return redirect(request.url)
         file = request.files['audioFile']
         # If the user does not select a file, the browser submits an
         # empty file without a filename.
         if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
         if file and allowed_file(file.filename):
            audio_file = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], audio_file))
            new_path = "/Users/gabrielparizet/Desktop/Sound_Data/api/audio_files/" + audio_file
            audio_file_data = {
               "tempo": find_tempo(new_path),
               "duration": find_length(new_path)
            }
            return jsonify(audio_file_data)



