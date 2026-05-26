# Section 1 Basic


# # 1. Take your name as input and print: Hello, [name]! Welcome to coding.
name = input("Enter your name : ")
print(f"Hello, {name}! Welcome to coding")


# 2. Take two numbers as input and print their sum, difference, product, and quotient.
num1 = int(input('Enter number 1'))
num2 = int(input('Enter number 2'))
addition = num1 + num2
print(f"sum is {addition}")
difference = num1 - num2
print(f"difference is {difference}")
prod = num1 * num2
print(f"product is {prod}")
quotient = num1 / num2
print(f"quotient is {quotient}")

# 3. Input your birth year and print your current age.
b_year = int(input('Enter your birth year: '))
c_year = 2026
age = c_year - b_year
print(f"Your current age is: {age}")


# 4. Take radius as input and print area and circumference of a circle (use math.pi).
import math
radii = int(input('Enter radius : '))
area = math.pi * (radii ** 2)
circumference = 2 * math.pi * radii
print(f"area is {area}, Circumference is {circumference}")

# 5. Input three subject marks and print the total and average.
mark1 = int(input('Enter mark1 '))
mark2= int(input('Enter mark2'))
mark3 = int(input('Enter mark3'))
total_marks = mark1+ mark2+ mark3
avg_marks = (mark1+ mark2+ mark3)/3
print(f"Total marks are {total_marks}, Average marks are {avg_marks}")
