from book import Book

class Magazine(Book):
    def __init__(self, title, editor, issue_number, year):
        # Initialize the magazine with title, editor, issue number, and year
        super().__init__(title, editor, year)
        self.issue_number = issue_number
        
    def get_details(self):
        # Return the details of the magazine
        return f"'{self.title}' edited by {self.author}, Issue: {self.issue_number}, Year: {self.year}"
    
    def borrow(self):
        # Magazines can't be borrowed, but we can add a message
        return f"You can not borrow '{self.title}'. It's a magazine."