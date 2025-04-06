try:
    with open("sample.txt", "r") as file:
        data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
    # file.close()