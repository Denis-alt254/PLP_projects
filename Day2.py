print('Hello World')

age = 25;
name = "Denis";
is_student = True;

print("Name: ", name)
print("Age: ", age)
print("Is student: ", is_student)

#int (integers)
num = 23;

#str (string)
name = "Derick"

#float
gpa = 4.0

#boolean
student = True

#check data type
print(("num"),type(num))
print(("name"),type(name))
print(("gpa"),type(gpa))
print(("student"),type(student))

if age>=20:{
    print("Above 18: True")
}
else:{
    print("Below 18")
}
if is_student:{
    print(("Is student: "), is_student)
}
else:{
    print("Is not a student")
}
if gpa>3.5:{
    print(gpa, ("Is a serious student. Distinction 🏆"))
}
else:{
    print(gpa, ("Is a reluctant student. Fail ❌"))
}
    
for i in range(5):
    print(i)

countdown = 5;

while countdown>0:
    print("Count down", countdown)

    countdown -=1;

print("Blast off 🎇")

def greet(name):
    print("Hello "+name)

greet("Denis")

import random
roll_down = random.randint(1,10)
print("You rolled a", roll_down)