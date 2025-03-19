#Prompt the user to enter numbers
# Prompt the user to enter operation

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose an operation(+, -, *, /): ")

# Carry out the calculation
if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "/":
    if num2 != 0:  #Division by zero is not allowed
        result = num1/num2
        print(f"The result is: {result}")
    else:
        print("Division by zero is not allowed!")
else:
    print("Invalid operation. Please choose between(+, -, *, /)")
