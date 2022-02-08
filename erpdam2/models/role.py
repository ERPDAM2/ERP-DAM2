from erpdam2 import db


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean(), default=False)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return "<Role: {}>".format(self.name)

    def __init__(
        self,
        name,
        description,
        is_admin,
    ):
        self.name = name
        self.description = description
        self.is_admin = is_admin
