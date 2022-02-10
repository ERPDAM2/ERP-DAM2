from erpdam2 import db
from erpdam2 import models

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    db.session.add(models.Role("Standard", "Standard role"))
    db.session.commit()
