from wtforms import SubmitField, TextField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class ReviewForm(FlaskForm):
    movie = TextField('Movie', validators=[Required()])
    message = TextField('Message', validators=[Required()])
    submit = SubmitField('Submit')
