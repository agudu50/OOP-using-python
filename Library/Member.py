class Member:
    def __init__(self, member_id: str, name: str):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_books = []

    def borrow_book(self, book):
        if book in self.__borrowed_books:
            raise ValueError("Book already borrowed by this member")
        book.borrow_book()
        self.__borrowed_books.append(book)

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
        else:
            raise ValueError("This book was not borrowed by the member")

    def __str__(self):
        return f"Member [ID: {self.__member_id}, Name: {self.__name}, Borrowed Books: {len(self.__borrowed_books)}]"

