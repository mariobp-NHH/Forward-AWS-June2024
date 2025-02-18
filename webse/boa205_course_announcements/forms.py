from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AnnouncementForm(FlaskForm):
    title = StringField('Tittel', validators=[DataRequired()])
    content = TextAreaField('Innhold', validators=[DataRequired()])
    submit = SubmitField('Kunngjøring')
