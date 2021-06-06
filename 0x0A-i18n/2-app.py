#!/usr/bin/env python3
"""
app module
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Optional
import os

app = Flask(__name__)


class Config:
    """
    Configuration of Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Return best match from accepted languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """
    Home page
    """

    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
