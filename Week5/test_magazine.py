from magazine import Magazine

mag = Magazine("National Geographic", "John Doe", 2023, 2023)

print(mag.get_details())  # Should print details of the magazine
print(mag.borrow())  # Should print that magazines can't be borrowed