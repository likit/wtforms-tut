from app import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False, info={'label': 'Name'})
    email = db.Column(db.Unicode(255), nullable=False, info={'label': 'E-mail'})