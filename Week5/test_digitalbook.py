from digitalbook import DigitalBook

ebook = DigitalBook("Python Programming", "John Doe", 2023, 5, "PDF")

print(ebook.get_details())
print(ebook.download())
print(ebook.stream())