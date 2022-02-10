from wsgiref import validate
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField, DecimalField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange
from erpdam2.models.user import User


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
    
    def validate_email(self, field):
        if(User.email_exists(field.data)):
            return ValidationError("Email already exists")
    
    def validate_username(self, field):
        if(User.username_exists(field.data)):
            return ValidationError("Username alredy exists")

class LoginForm(FlaskForm):
    """
    Hacer login
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegisterSale(FlaskForm):

    """Register Sales"""
    id_product = StringField("Id_Product", validators=[DataRequired()])
    id_provider = IntegerField("Id_Provider", validators=[DataRequired()])
    price = DecimalField("Price", validators=[DataRequired(), Length(max=8)])
    quantity = IntegerField("Quantity", validators=[DataRequired(), Length(10)])
    transaction_type = StringField("Transaction_Type", validators=[DataRequired()])
    
class RegisterProduct(FlaskForm):
    """
    Registro de producto
    """     
    id_product = IntegerField('ID', validators=[DataRequired(),NumberRange(min=1)])
    name_product = StringField('Nombre', validators=[DataRequired(), Length(max=60)])
    description = StringField('Descripción', validators=[DataRequired(), Length(max=200)])
    quantity = IntegerField('Cantidad', validators=[DataRequired(),NumberRange(min=1)])
    price = DecimalField('Precio', validators=[DataRequired(),NumberRange(min=0.1)])
    picture = StringField('Descripción', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Insertar')

class RegisterContact(FlaskForm):
    """
    Dar de alta contacto 2 
    """
    email = EmailField("Email", validators=[DataRequired(), Email()])
    phone = IntegerField("Phone", validators=[DataRequired(), NumberRange(min=111111111,max=999999999)])
    picture = StringField("Picture", validators=[Length(max=255)])
    address=StringField("Adress", validators=[Length(max=250)])
    company_name=StringField("Company_Name",validators=[DataRequired(),Length(max=50)])
    first_name=StringField("First_Name",validators=[DataRequired(),Length(max=50)])
    last_name=StringField("Last_Name",validators=[DataRequired(),Length(max=50)])
    
class RegisterRole(FlaskForm):
    """
    Registro de rol
    """     
    id_role = IntegerField('ID', validators=[DataRequired(),NumberRange(min=1)])
    name_role = StringField('Nombre', validators=[DataRequired(), Length(max=60)])
    description = StringField('Descripción', validators=[DataRequired(), Length(max=200)])
    is_admin = SelectField(u'Administrador',choices=[('1', 'Sí'), ('2', 'No')],validators=DataRequired())
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(max=60)])
    submit = SubmitField('Insertar')    
