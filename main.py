from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Abhay786@localhost:3306/dbbooks"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_SILENCE_UBER_WARNING'] = True

db = SQLAlchemy(app)

from modal import Book

@app.route('/')
def home():
    ##READ ALL RECORDS
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("add.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)