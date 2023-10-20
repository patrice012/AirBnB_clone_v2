"""
Script that starts a Flask web application

Listening on 0.0.0.0, port 5000
Use the option strict_slashes=False in route definition
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""

from flask import Flask, render_template
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
def c(text):
    """
    Print argument value
    """
    new_text = re.sub("_", " ", text)
    return f"C {new_text}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """display Python"""
    new_text = re.sub("_", " ", text)
    return f"Python {new_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Print n only if it's a number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """render  to template"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """render values  to template"""
    parity = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
