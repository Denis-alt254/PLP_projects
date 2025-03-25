# Guest = print(input("Enter your name: "))

def greet_guest(Guest = input("Enter your name: ")):
    return(f"Hello, {Guest}!")

print(greet_guest())