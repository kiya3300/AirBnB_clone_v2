#!/usr/bin/python3
"""the `5-number_template` module
starts a flask web application listening on `0.0.0.0:5000`
"""
from flask import Flask, escape, render_template

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


@app.route("/number/<int:n>")
def number(n):
    """returns `n` + `is a number` only if `n` is an integer"""
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    """returns `n` + `is a number` only if `n` is an integer"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """returns `n` + `is even` if `n` is even
    else returns `n` + `is odd`
    """
    parity = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html",
                           number=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
