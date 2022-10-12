from flask import Flask
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)


logger = logging.getLogger(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello world! </p>"
