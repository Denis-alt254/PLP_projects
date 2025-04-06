try:
    with open("Week4/example.txt", "a") as file:
        data = file.append("myname")
    print(data)
except FileNotFoundError:
    print("File not found. Please check the filename.")
finally:
    print("Execution completed.")
    file.close()