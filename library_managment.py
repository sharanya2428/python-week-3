class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "removed")
        else:
            print("Book not found")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned")

    def display_books(self):
        print("Available books:", self.books)


library = Library()
library.add_book("Python")
library.add_book("Java")
library.display_books()
library.issue_book("Python")
library.return_book("Python")
library.display_books()
