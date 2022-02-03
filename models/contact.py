from ..app import db

class Contacto(db.Model):
    __tablename__ = "contacts"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), index=True, unique=True)
    #phone_number = db.Column(db.)