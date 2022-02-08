from wsgiref import validate
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange

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
    
class RegisterProduct(FlaskForm):
    id_product = IntegerField('ID', validators=[DataRequired(),NumberRange(min=1)])
    name_product = StringField('Nombre', validators=[DataRequired(), Length(max=60)])
    description = StringField('Descripción', validators=[DataRequired(), Length(max=200)])
    quantity = IntegerField('Cantidad', validators=[DataRequired(),NumberRange(min=1)])
    price = DecimalField('Precio', validators=[DataRequired(),NumberRange(min=0.1)])
    picture = StringField('Descripción', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Insertar')
