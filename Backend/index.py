# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import json
import os
from time import sleep
from flask import Flask, request
from visions import Object
from nn import getPrediction
from threading import Thread

# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

status = None


def task():
    global status


@app.route("/")
def index():
    t1 = Thread(target=task)
    t1.start()
    return "Hello"


@app.route("/status", methods=["GET"])
def getStatus():
    statusList = {"status": status * 10}
    return json.dumps(statusList)


@app.route("/data", methods=["POST"])
def get_data():
    data = request.get_json()
    flips = data["flips"]
    seconds = data["seconds"]
    data = json.loads(getPrediction(flips, seconds).data)
    return str(round(data["prediction"], 2))


@app.route("/predict", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Get the file from post request
        f = request.files["file"]

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, "uploads", secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)

        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        pred_class = decode_predictions(preds, top=1)  # ImageNet Decode
        result = str(pred_class[0][0][1])  # Convert to string
        return result
    return None


# main driver function
if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
