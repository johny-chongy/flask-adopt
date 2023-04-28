"""Flask app for adopt app."""

import os

from flask import Flask,render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = "secret"
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.get('/')
def get_home():
    """show home page"""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)