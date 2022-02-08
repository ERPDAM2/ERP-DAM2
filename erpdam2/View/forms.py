from wsgiref import validate
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField, DecimalField,EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange,length

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


class RegisterSale(FlaskForm):

    id_product = StringField("Id_Product", validators=[DataRequired()])
    id_provider = IntegerField("Id_Provider", validators=[DataRequired()])
    price = DecimalField("Price", validators=[DataRequired(), Length(max=8)])
    quantity = IntegerField("Quantity", validators=[DataRequired(), Length(10)])
    transaction_type = StringField("Transaction_Type", validators=[DataRequired()])

class RegisterContact(FlaskForm):
    """
    Dar de alta contacto 2 
    """
    email = EmailField("Email", validators=[DataRequired(), Email(max=100)])
    phone = IntegerField("Phone", validators=[DataRequired(), NumberRange(min=111111111,max=999999999)])
    picture = StringField("Picture", validators=[length(max=255)])
    address=StringField("Adress", validators=[length(max=250)])
    company_name=StringField("Company_Name",validators=[DataRequired(),length(max=50)])
    first_name=StringField("First_Name",validators=[DataRequired(),length(max=50)])
    last_name=StringField("Last_Name",validators=[DataRequired(),length(max=50)])
