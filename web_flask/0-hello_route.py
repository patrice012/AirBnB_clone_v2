#!/usr/bin/python3
"""
Script that starts a Flask web application

Listening on 0.0.0.0, port 5000
Use the option strict_slashes=False in route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
