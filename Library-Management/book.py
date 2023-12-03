class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_details(self):
        print("Title of book = ", self.title, "\n")
        print("Author of book = ", self.author, "\n")
        print("ISBN of book = ", self.isbn, "\n")
