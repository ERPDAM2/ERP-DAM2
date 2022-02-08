from erpdam2 import db
import erpdam2.models  # required to create tables

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
