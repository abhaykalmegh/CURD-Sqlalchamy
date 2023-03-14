from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Abhay@786@localhost/books"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

'''


# CREATE RECORD
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

if __name__ == "__main__":
    app.app_context()
    app.run(debug=True)
'''
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)

# create the extension
db = SQLAlchemy()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()
'''