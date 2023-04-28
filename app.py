"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db

from forms import AddPetForm, EditPetForm

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

    pets = Pet.query.order_by("id").all()

    return render_template("home.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """validate form and redirect to homepage or re-render form"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,
                  species=species,
                  photo_url=photo_url,
                  age=age,
                  notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"{name} added!")
        return redirect("/")

    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """view pet info and display form to edit info"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet) #pre-fill edit form with stored values

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()

        flash(f"{pet.name} info updated!")
        return redirect('/')

    else:
        return render_template("about_pet.html", pet=pet, form=form)




