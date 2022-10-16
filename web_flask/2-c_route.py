#!/usr/bin/python3
"""the `2-c_route` module
starts a flask web application listening on `0.0.0.0:5000`
"""
from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """returns `Hello HBNB!` message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns `HBNB` message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """returns `c` + `text`"""
    text = text.replace("_", " ")
    return "C %s" % escape(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
