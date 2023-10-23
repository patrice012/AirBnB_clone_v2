#!/usr/bin/python3
"""
Script that starts a Flask web application

Listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value of
    the text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
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
