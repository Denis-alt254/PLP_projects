class Book:
    def __init__(self, title, author, year):
        # Initialize the book with title, author, and year
        self.title = title
        self.author = author
        self.year = year
        self.available = True # Book is available by default
        self.__rating = 0 # Default rating is 0
        
    def borrow(self):
        # Check if the book is available before borrowing
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        return f"'{self.title}' is currently unavailable."
    
    def return_book(self):
        # Assuming the book was borrowed, we set it back to available
        self.available = True
        return f"You have returned '{self.title}'."
    
    def get_details(self):
        # Return the details of the book
        return f"'{self.title}' by {self.author}, published in {self.year}."
    
    def set_rating(self, rating):
        """
        Set a rating from 0 to 5 for the book.
        This is an example of encapsulation: rating is private
        """
        if 0 <= rating <= 5:
            self.__rating = rating
        else:
            print("Rating must be between 0 and 5")

    def get_rating(self):
        """
        Get the current ratings of the book
        """
        return self.__rating