students = ("John", "Alvin", "Amos", "Kelvin")

print(students)
print(students[0])
print(students[1])  #Indexing
print(students[2])
print(students[3])
print(students[-1])  #Negative Indexing 
print(students[-2]) 
print(students[-3]) 
print(students[-4]) 
print(students[1:3])  #Slicing  #Alvin, Amos
print(students[1:4])  #Alvin, Amos, Kelvin  
print(students[:3])  #John, Alvin, Amos 
print(students[1:])  #Alvin, Amos, Kelvin   
print(students[:])  #John, Alvin, Amos, Kelvin  
print(students[::2])  #John, Amos   
print(students[::-1])  #Kelvin, Amos, Alvin, John   
print(students[::-2])  #Kelvin, Alvin
print(len(students))  #4
print("John" in students)  #True
print("Jane" in students)  #False
print("Jane" not in students)  #True
print(students.count("John"))  #1
print(students.index("John"))  #0
print(students.index("Kelvin"))  #3
students = ("John", "Alvin", "Amos", "Kelvin", "John")
print(students.count("John"))  #2
print(students.index("John"))  #0
print(students.index("Kelvin"))  #3
print(students.index("John", 1))  #4
print(students.index("John", 2))  #4
print(students.index("John", 3))  #4
print(students.index("John", 4))  #4
print(students.index("John", 5))  #5
print(students.index("John", 6))  #5
print(students.index("John", 7))  #5
print(students.index("John", 8))  #5
print(students.index("John", 9))  #5
print(students.index("John", 10))  #5
print(students.index("John", 11))  #5
print(students.index("John", 12))  #5
print(students.index("John", 13))  #5
print(students.index("John", 14))  #5
print(students.index("John", 15))  #5
print(students.index("John", 16))  #5
print(students.index("John", 17))  #5
print(students.index("John", 18))  #5
print(students.index("John", 19))  #5
print(students.index("John", 20))  #5
print(students.index("John", 21))  #5