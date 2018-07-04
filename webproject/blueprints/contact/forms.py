from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms_components import EmailField
from wtforms.validators import InputRequired, Length


class ContactForm(FlaskForm):
    email = EmailField("What's your e-mail address?",
                       [InputRequired(), Length(3, 150)])
    message = TextAreaField("What's your question or issue?",
                            [InputRequired(), Length(1, 2048)])
