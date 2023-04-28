"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, AnyOf

class AddPetForm(FlaskForm):
    """form for adding pets"""

    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = StringField("Species",
                        validators=[InputRequired(),
                                    #could use selectfield as well
                                    AnyOf(["cat", "dog", "porcupine"])])
    photo_url = URLField("Photo URL")
    age = SelectField("Age",
                      #could declare as global variable
                      choices=[('baby', 'BABY'),
                               ('young', 'YOUNG'),
                               ('adult', 'ADULT'),
                               ('senior', 'SENIOR')])
    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """form for editing pet info"""

    photo_url = URLField("Photo URL")
    notes = StringField("Notes")
    available = BooleanField("Availability")