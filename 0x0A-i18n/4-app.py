#!/usr/bin/env python3
"""
app module
"""

from flask import Flask, render_template, request, flash
from flask_babel import Babel, _
from typing import Optional
import gettext
import os

app = Flask(__name__)
babel = Babel(app)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "CASA123")


class Config:
    """
    Configuration of Bavel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Return best match from accepted languages
    """
    if request.args.get("locale") in app.config['LANGUAGES']:
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """
    Home page
    """
    flash(_('home_title'))
    flash(_('home_header'))
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
