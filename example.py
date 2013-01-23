"""
Flask-Jsonpify example
===================
This is a tiny Flask Application demonstrating Flask-Jsonpify, an extension to
Flask's jsonify function, returning JSON-Padded responses when a callback is
specified as request's arguments.

:copyright: (C) 2013 by Cory Dolphin.
:license:   MIT/X11, see LICENSE for more details.
"""
from flask import Flask
from flask.ext.jsonpify import jsonify 

app = Flask(__name__)
SECRET_KEY = "yeah, not actually a secret"
app.config.from_object(__name__)


@app.route("/")
def index():
    return jsonify(user="lala")


if __name__ == "__main__":
    app.run(debug=True)
