#!/usr/bin/env python3
"""
app module
"""

from flask import Flask, render_template, request, flash, g
from flask_babel import Babel, _
from typing import Optional, Union
import gettext
import os

app = Flask(__name__)
babel = Babel(app)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "CASA123")


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration of Bavel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user(login_as: int) -> Union[dict, None]:
    """
    get name based on user_id
    """
    try:
        name = users[int(login_as)]["name"]
        return name
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """
    Set user before other functions run
    """
    g.user = get_user(request.args.get("login_as"))


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
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
