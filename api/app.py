# Import flask. Add the Flask.request object.
from flask import Flask, request
# Instantiate flask app and assign it to app variable.
app = Flask(__name__)

@app.get("/")
def test_route():
   return "Your connected to your flask server"

