#!/usr/bin/python3
"""the `3-python_route` module
starts a flask web application listening on `0.0.0.0:5000`
"""
from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """returns `Hello HBNB!` message"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """returns `HBNB` message"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """returns `c` + `text`"""
    text = text.replace("_", " ")
    return "C %s" % escape(text)


@app.route("/python")
def python():
    "returns `Python is cool`"
    text = "is cool"
    return "Python %s" % escape(text)


@app.route("/python/<text>")
def python_text(text):
    """returns `Python ` + `text`"""
    text = text.replace("_", " ")
    return "Python %s" % escape(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
