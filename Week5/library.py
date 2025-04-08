from book import Book

class Library:
    def __init__(self, name):
        # Initialize the library with a name and an empty collection of books
        self.name = name
        self.books = []
        
    def add_book(self, book):
        # Add a book to the library's collection
        self.books.append(book)
        return f"'{book.title}' has been added to the library."
    
    def list_books(self):
        # List all books in the library
        return [book.get_details() for book in self.books]
    
    def find_book(self, title):
        # Find a book by its title
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None