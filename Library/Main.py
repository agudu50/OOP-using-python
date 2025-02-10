from Book import Book
from Member import Member
from Library import Library

if __name__ == "__main__":
    library = Library()

    book1 = Book("B001", "Animal Farm", "George Orwell", 3)
    book2 = Book("B002", "1984", "George Orwell", 2)
    book3 = Book("B003", "Harry Potter", "J.K Rowling", 1)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    member1 = Member("M001", "Anthony Gudu")
    library.register_member(member1)

    print("Available Books:")
    library.display_books()

    try:
        member1.borrow_book(book1)
        print("\nAfter borrowing 'Animal Farm':")
        library.display_books()

        member1.return_book(book1)
        print("\nAfter returning 'Animal Farm':")
        library.display_books()

    except ValueError as e:
        print(f"Error: {e}")
