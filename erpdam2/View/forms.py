from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField,EmailField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo,NumberRange


class LoginForm(FlaskForm):
    """
    Hacer login
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegisterContact(FlaskForm):
    """
    Dar de alta contacto
    """
    email = EmailField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired(), NumberRange(min=111111111,max=999999999)])
    picture = StringField("Email", validators=[DataRequired(), Email()])


"""
 self,
        email,
        phone,
        picture,
        address,
        company_name=None,
        first_name=None,
        last_name=None,
"""