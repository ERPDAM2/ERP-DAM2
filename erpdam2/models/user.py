from werkzeug.security import generate_password_hash, check_password_hash

from erpdam2 import db, login_manager
from flask_login import UserMixin
from erpdam2.models import BaseClass


class User(UserMixin, BaseClass):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    @property
    def password(self):
        # Nos aseguramos mediante este método de que la contraseña no sea accesible para cualquier usuario

        raise AttributeError("La contraseña no es un atributo accesible.")

    @password.setter
    def password(self, password_to_hash):
        # Convertimos la contraseña a una clave cifrada
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password):
        # Comprobamos si la clave cifrada coincide con la contraseña actual
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User: {}>".format(self.username)

    @staticmethod
    def username_exists(email) -> bool:
        return User.query.filter_by(email=email).first() is not None

    @staticmethod
    def email_exists(username) -> bool:
        return User.query.filter_by(username=username).first() is not None

    def is_admin(self) -> bool:
        return self.role.is_admin

    def __init__(self, email, username, first_name, last_name, password, role_id=1):
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role_id = role_id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
