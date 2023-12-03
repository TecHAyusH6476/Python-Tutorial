class Library:
    # we are passing a books list (empty)
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display_details()

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                print("Book ", book.title, " has been issued !!")
                return

        print("Book not found with isbn = ", isbn)

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                print("Book ", book.title, " is available for issue !!")
                return

        print("Book not found with isbn = ", isbn)
