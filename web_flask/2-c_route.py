"""
Script that starts a Flask web application

Listening on 0.0.0.0, port 5000
Use the option strict_slashes=False in route definition
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""

from flask import Flask
import re

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Print hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """
    Print argument value
    """
    new_text = re.sub("_", " ", text)

    return f"C {new_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
