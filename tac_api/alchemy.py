from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:men1zeero00@localhost:3306/tac'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    email = db.Column('email', db.Unicode, unique=True)
    password = db.Column('password', db.Unicode)
    role = db.Column('role', db.Unicode)

    def __repr__(self):
        return " email: {email}\t Role: {role} ".format(email=self.email, role=self.role)

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

class Pages(db.Model):
    __tablename__ = 'role'
    role_id = db.Column('role_id', db.Integer, primary_key=True)
    pages = db.Column('pages', db.Unicode, primary_key=True)
    role = db.Column('role', db.Unicode)
    rights = db.Column('rights', db.Unicode)

    def __repr__(self):
        return " Role: {role}\tPages: {pages}".format(pages=self.pages.split(", \n"), role=self.role)

    def __init__(self, pages, role, rights):
        self.pages = pages
        self.role = role
        self.righs = rights

