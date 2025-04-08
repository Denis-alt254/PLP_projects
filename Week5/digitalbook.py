from book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year, file_size, format_type):
        # Initialize the digital book with title, author, year, file size, and format type
        super().__init__(title, author, year)
        self.file_size = file_size  # in MB
        self.format_type = format_type  # e.g., PDF, EPUB

    def download(self):
        # Simulate downloading the digital book
        return f"Downloading '{self.title}' in {self.format_type} format ({self.file_size} MB)..."

    def get_details(self):
        # Return the details of the digital book
        return f"'{self.title}' by {self.author}, published in {self.year}, Size: {self.file_size} MB, Format: {self.format_type}"
    
    def stream(self):
        # Simulate streaming the digital book
        return f"Streaming '{self.title}'..."
    
    def borrow(self):
        # Digital books can't be borrowed, but you can stream them online
        return f"You can't borrow a digital book '{self.title}' but you can stream it online."