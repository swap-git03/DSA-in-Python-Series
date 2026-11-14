# ◆ Beginner
# 11. Check if a number is even or odd.
num = int(input('Enter a number: '))
if num % 2 ==0:
    print("even")
else:
    print("odd")
    

# 12. Input three numbers and print the largest without using max().
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
if num1>=num2 and num1>=num3:
    print(f"num {num1} is greated")
elif num2>=num1 and num2>=num3:
    print(f"num {num2} is greated")
else:
    print(f"num {num3} is greated")

# 13. Check if a year is a leap year.
year = int(input("Enter your year : "))
if (year % 4== 0) and (year % 100 != 0) or (year % 400 ==0):
    print("Year is a leap year")
else:
    print("Not a leap year")

# 14. Input marks and print grade: A (90+), B (75+), C (60+), D (45+), F (below 45).
marks = int(input("Enter marks"))
if marks >= 90:
    print("Grade is A")
elif marks >= 75:
    print("Grade is B")
elif marks >= 60:
    print("Grade is C")
elif marks >= 45:
    print("Grade is D")
else:
    print("F")

# 15. Check if a number is divisible by both 3 and 5.
num = int(input('Enter a number: '))
if (num % 3 == 0) and (num % 5 == 0):
    print(f"{num}Divisible by 3 and 5")
else:
    print(f"{num}NOT Divisible by 3 and 5")


# 16. Input three sides of a triangle; check if it's valid, then classify it (equilateral / isosceles /
# scalene).
a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))
if (a+b>c) and (b+c>a) and (a+c>b):
    if a==b==c:
        print('Equilateral Triangle')
    elif (a==b) or (b==c) or (a==c):
        print('Isosceles Triangle')
    else:
        print('Scalene Triangle')
else:
    print("Not a triangle")

# 17. Build a simple calculator: input two numbers and operator (+, -, *, /), print result.
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(num1+num2)
if operator == "-":
    print(num1-num2)
if operator == "*":
    print(num1*num2)
if operator == "/":
    print(num1/num2)

# 18. Input a character; check if it's a vowel, consonant, digit, or special character.
char = input("Enter a character : ")
if char in "aeiouAEIOU": 
    print("Character is vowel")
elif char.isalpha():
    print("Character is consonent")
elif char.isdigit():
    print("Character is digit")
else:
    print("Character is special")