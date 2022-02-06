from ..app import db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contact(db.Model):
    __tablename__ = "contacts"
    
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), index=True, unique=True)
    phone_number = db.Column(db.Integer, nullable=True)
    picture = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(250), nullable=True)

    @staticmethod
    def fromCompany():
        return Contact()

    @staticmethod
    def fromPerson():
        return Contact()
