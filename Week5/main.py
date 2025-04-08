from library import Library
from book import Book
from magazine import Magazine
from digitalbook import DigitalBook

def main():
    library = Library("City Library")
    
    # Adding books to the library
    library.add_book(Book("Master Mind", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    library.add_book(Magazine("National Geographic", "John Doe", 123, 2023))
    library.add_book(DigitalBook("Python Programming", "John Doe", 2023, 5, "PDF"))
    
    while True:
        print("\n 📚📔WELCOME TO CITY LIBRARY📖📕")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Rate a book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\nBooks in the library:")
            for book in library.list_books():
                print(book)
        elif choice == '2':
            title = input("Enter the title of the book: ")
            found = library.find_book(title)
            if found:
                print(f"Found: {found.get_details()}")
            else:
                print("Book not found.")
        elif choice == '3':
            title = input("Enter the title of the book to borrow:")
            found = library.find_book(title)
            if found:
                print(found.borrow())
            else:
                print(f"'{title}' not found in the library.")

        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            found = library.find_book(title)
            if found:
                print(f"You have returned '{title}'.")
            else:
                print(f"'{title}' not found in the library.")
            
        elif choice == "5":
            title = input("Enter the title of the book to rate: ")
            book = library.find_book(title)
            if book:
                try:
                    rating = int(input("Enter a rating from 0 to 5: "))
                    book.set_rating(rating)
                    print(f"Thanks! Current rating: {book.get_rating()}/5")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Book not found.")
                
        elif choice == '6':
            print("Thank you for visiting City library!")
            break
        else:
            print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    main()