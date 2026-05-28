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