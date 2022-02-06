# app/models.py

from werkzeug.security import generate_password_hash, check_password_hash

from models.rol import Role

from ..app import db, login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        # Nos aseguramos mediante este método de que la contraseña no sea accesible para cualquier usuario

        raise AttributeError('La contraseña no es un atributo accesible.')

    @password.setter
    def password(self, password):
        # Convertimos la contraseña a una clave cifrada
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # Comprobamos si la clave cifrada coincide con la contraseña actual
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def username_exists(self) -> bool:
        return db.session.query(User.id).filter_by(email=self.email).first() is not None

    def email_exists(self) -> bool:
        return db.session.query(User.id).filter_by(username=self.username).first() is not None


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
