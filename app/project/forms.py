from flask_wtf import FlaskForm as Form
from wtforms import (StringField,DateField, TextAreaField, SelectField, SubmitField, BooleanField)
from wtforms.validators import Length
from ..models import Volunteer, Role


class AssignProjectForm(Form):
    vol = SelectField('Volunteer', coerce=int)
    confirmed = BooleanField('Confirmed')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(AssignProjectForm, self).__init__(*args, **kwargs)
        self.vol.choices = [(vol.id, vol.name) for vol in Volunteer.query.order_by(Volunteer.name).all()]


class CommentForm(Form):
    date_reported = DateField('Date Reported', format="%Y-%m-%d")
    body = TextAreaField('Message')
    submit = SubmitField('Submit Comment')