from wsgiref import validate
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange


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
