from flask import Flask


app = Flask(__name__)

from controller import note_controller, notebook_controller

if (__name__ == "__main__"):
    app.run()
