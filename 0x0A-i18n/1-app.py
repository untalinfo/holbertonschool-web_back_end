#!/usr/bin/env python3
"""
app module
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configuration of available languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """
    Home page
    """

    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
