# Beginner Python Practice
#Author: Kadija Conteh
# Description: This file contains basic Python practice questions
#Covering input, condition, loops, functions, and lists.

#---------------------------------------------------
# Excercise 1 - Write a program that:
# Asks the user for their name
# Prints: "Hello, <name>!"  

name = input("Enter you name: ")   
print(f"Hello, {name}")     


#------------------------------------
#Exercise 2 - Write a program:
#Asks the user for a number
#Prints whether the number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#----------------------------------
#Exercise 3 - Write a program that:
# Prints their: sum, difference, product.

operator = input("Enter an operator(+, /, *): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
else:
    print("Invalid Operator")
