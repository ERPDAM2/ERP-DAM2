from ..app import db
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Purchase (db.Model):
    __tablename__ = "purchases"
    
    id = db.Column(db.Integer, primary_key=True)
    id_product = db.relationship('Product', backref='purchases',lazy='dynamic')
    id_provider = db.relationship('Contact', backref='purchases',lazy='dynamic')
    date = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    price = db.Column(db.Float,nullable=False)
    
    def __init__(self, id, id_product, id_provider, date, price):
        self.id = id
        self.id_product = id_product
        self.id_provider = id_provider
        self.date = date
        self.price = price
        
class Sale (db.Model):
    __tablename__ = "sales"
    
    id = db.Column(db.Integer, primary_key=True)
    id_product = db.relationship('Product', backref='purchases',lazy='dynamic')
    id_provider = db.relationship('Contact', backref='purchases',lazy='dynamic')
    date = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    price = db.Column(db.Float,nullable=False)
    
    def __init__(self, id, id_product, id_provider, date, price):
        self.id = id
        self.id_product = id_product
        self.id_provider = id_provider
        self.date = date
        self.price = price