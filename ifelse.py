# Q1: Take a number from user and print "Even" if the number is even otherwise print "Odd".

number = int(input("Enter a number"))
if (number%2==0):
  print(f"The given numbber {number} is even")
else:
    print(f"The given numbber {number} is odd")

# Q2: Take two numbers from the user and print which number is larger.
num1 = (input("Enter 1st number"))
num2 = (input("Enter 2nd number"))
if (num1>num2):
  print(f"{num1}>{num2}")
else:
  print(f"{num2}>{num1}")

  from typing import AsyncGenerator
# Q3: Take age as input and print "Eligible to vote" if age is 18 or more otherwise print "Not eligible".
age = int(input("Enter your age"))
if (age>=18):
  print("You can vote")
else:
  print("You cant vote ")

# Q4: Take a number from user and print "Positive", "Negative", or "Zero".
num1 = int(input("Enter 1st number"))
if (num1>0):
  print(f"{num1}is positive")
elif(num1<0):
  print(f"{num1}is negative")
else:
  print("NUmber is zero")

# Q5: Take three numbers from the user and print the largest number.
num1 = float(input("Enter 1st number"))
num2 = float(input("Enter 2nd number"))
num3 = float(input("Enter 3rd number"))
if (num1>num2 and num1>num3):
  print(f"{num1} is greater")
elif (num2>num1 and num2>num3):
  print(f"{num2} is greater")
elif (num3>num1 and num3>num2):
  print(f"{num3} is greater") 
else:
  print("Neet number tak re")

# Q6: Take marks as input and print grade using rules: >=90 A, >=75 B, >=50 C, else Fail.
marks = int(input("Enter marks"))
if (marks>=90):
  print("you got A")
elif (marks>=75):
  print("you got B")
elif (marks>=50):
  print("you got C")
else:
  print("you got failed😒")

# Q7: Take three numbers from the user and print the second largest number.

num1 = float(input("Enter 1st number"))
num2 = float(input("Enter 2nd number"))
num3 = float(input("Enter 3rd number"))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print(f"{num1} is second largest")

elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print(f"{num2} is second largest")

else:
    print(f"{num3} is second largest")