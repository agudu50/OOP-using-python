class Book:
    def __init__(self, book_id: str, title: str, author: str, available_copies: int):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.available_copies = available_copies

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def available_copies(self):
        return self.__available_copies

    @available_copies.setter
    def available_copies(self, value: int):
        if value < 0:
            raise ValueError("Available copies cannot be negative")
        self.__available_copies = value

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
        else:
            raise ValueError("No copies available to borrow")

    def return_book(self):
        self.available_copies += 1

    def __str__(self):
        return f"Book [ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available Copies: {self.available_copies}]"