from Book import Book
from Member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)

    def register_member(self, member: Member):
        self.members.append(member)

    def search_book_by_title(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise ValueError("Book not found")

    def display_books(self):
        for book in self.books:
            print(book)