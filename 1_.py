# Functions are way to wrap your code
# into reuseable units

#how you define a function
#I only define tyhe functrion ONCE!!!!!!
#Whatever i pass inside of the perentese
#is called a parameter
#A parameter is a placeholder for future information
# def sayHello():
#     print("say Hello")
#     print("Hello Governor")
#     print("Welcome back")

# #Once you define a function
# #You must call or invoke the function
# #When i pass in information into
# #the called function, its called an argument
# sayHello()
# sayHello()
#-----------------------------------------------------------------------
# def sayHello(name,age,color):
#     print(f"say Hello {name}")
#     print("Hello Governor")
#     print(f"Welcome back {name}")
#     print(f"Your age is {age}")
#     print(f"Your favortie color {color}")

# sayHello("cristal",15, "blue")
# sayHello("bob", 49, "green")
# sayHello("Flor", 18, "blue")
#---------------------------------------------------------------------------------------------------------------

# def determinEligibility(age):
#     #if your age is over 18, you can vote
#     #otherwise you can't
#     if age >= 18:
#         print("you can vote")
#     else:
#         print("you have to wait")

# determinEligibility(12)
# determinEligibility(15)
# determinEligibility(19)
#--------------------------------------------------------------------------------------------------------------------
# def willYouGraduate(gpa,credits,SAT):
#     #gpa :number float variable
#     #credits: a number variable
#     #passed SAT : BOOLEAN
#     if (gpa >= 3.0) and (credits >= 28) and (SAT == True):
#         print("you passed, Good Luck in College ")
#     elif (gpa < 3.0) and (credits < 28) or (SAT != True):
#         print(" back to the drawing board ")
#     else:
#         print(" talk to your counselor")
    
# willYouGraduate(2.8, 15, True)
# willYouGraduate(3.5, 28, False)
# willYouGraduate( 4.0, 28, True)
#--------------------------------------------------------------------------------------------------------
# Short Video:
# return = statment used ti end a function and send a result back to the caller

# z = 3 #add(1,2)
# def add(x,y):
#     z = x + y
#     return z

# def subtract(x,y):
#     z = x - y 
#     return z

# def multiply(x,y):
#     z = x * y 
#     return z

# def divide(x,y):
#     z = x / y
#     return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(irst, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + "" + last

full_name = create_name ("spongebob", "squarepants")

print(full_name)