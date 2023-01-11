from flaskr import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    phone = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))