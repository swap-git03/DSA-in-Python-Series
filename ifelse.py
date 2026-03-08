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
  