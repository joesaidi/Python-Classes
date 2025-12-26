class Library:
    def __init__(self, name):
        self.name = name
        self.books = []   # collection of Book objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.info())

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"{self.title} by {self.author}"

# Books exist independently
book1 = Book("Clean Code", "Robert C. Martin")
book2 = Book("Python Crash Course", "Eric Matthes")

# Library aggregates books
library = Library("City Library")

library.add_book(book1)
library.add_book(book2)

library.list_books()
