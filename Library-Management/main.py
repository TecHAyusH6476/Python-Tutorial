from book import Book
from library import Library


def main():
    # creating an instance
    lib = Library()

    while True:
        print("\nLibrary Managment : \n")
        print("\n1. Add Book \n")
        print("\n2. Display Book \n")
        print("\n3. Borrow Book \n")
        print("\n4. Return Book \n")
        print("\n5. End the code!!! \n")

        choice = int(input("Enter your choice!!"))

        if choice == 1:
            title = input("Enter the title= ")
            author = input("Enter the author= ")
            isbn = input("Enter the isbn= ")

            new_book = Book(title=title, author=author, isbn=isbn)
            lib.add_book(new_book)
            print("\n Added the book !!!!")

        elif choice == 2:
            print("\n All Books in library !!")
            lib.display_books()

        elif choice == 3:
            isbn = input("enter the isbn of book to be issued !! = ")
            lib.borrow_book(isbn=isbn)

        elif choice == 4:
            isbn = input("enter the isbn of book to be returned !! = ")
            lib.return_book(isbn=isbn)

        elif choice == 5:
            break

        else:
            print("Invalid choice !!! = ")


if __name__ == "__main__":
    main()
