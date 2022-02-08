from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField,EmailField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo,NumberRange

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')
    

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