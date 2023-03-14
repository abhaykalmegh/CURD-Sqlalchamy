from __main__ import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Book('{self.title}','{self.author}','{self.rating}')"

# Create A New Record
#     new_book = Book(id=8, title="R Kalmegh", author="Python Kids", rating=9.5)
#     db.session.add(new_book)
#     db.session.commit()
# ------------------------
# Read All Records
# all_books = db.session.query(Book).all()
# ------------------------
# Read A Particular Record By Query
# book = Book.query.filter_by(title="Abhay R Kalmegh").first()
# print(book)
# -------------------------
# Update A Particular Record By Query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# Update A Record By PRIMARY KEY
# book_id = 1
# book_to_update = db.session.query(Customers).get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()
# ---------------------------------------

# Delete A Particular Record By PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
