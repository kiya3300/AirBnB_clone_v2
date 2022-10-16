#!/usr/bin/python3
"""the `7-states_list` module
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """fetchs the list of states from the database and displays it"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
