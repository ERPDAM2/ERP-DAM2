from erpdam2 import db
from erpdam2.models import BaseClass


class Contact(BaseClass):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    picture = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(250), nullable=True)
    transactions = db.relationship("Transaction", backref="contact", lazy=True)

    @staticmethod
    def from_company(company_name, email, phone, picture, address):
        return Contact(email, phone, picture, address, company_name=company_name)

    @staticmethod
    def from_person(first_name, last_name, email, phone, picture, address):
        return Contact(
            email, phone, picture, address, first_name=first_name, last_name=last_name
        )

    def __init__(
        self,
        email,
        phone,
        picture,
        address,
        company_name=None,
        first_name=None,
        last_name=None,
    ):
        self.company_name = company_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone
        self.picture = picture
        self.address = address
