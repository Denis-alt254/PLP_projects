from book import Book
from library import Library

lib = Library("City Library")
lib.add_book(Book("Master Mind", "George Orwell", 1949))
lib.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))

print("Books in the library:")
for book in lib.list_books():
    print(book)
    
    
found = lib.find_book("Master Mind")
print(f"\nFound: {found}")

