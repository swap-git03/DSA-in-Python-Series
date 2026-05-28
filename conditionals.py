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
    