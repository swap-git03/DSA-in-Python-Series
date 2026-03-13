# Q10: Take a number N from the user and print numbers from 1 to N using a loop.
n = int(input("Enter a number"))
for i in range(1,n):
  print(i)


# Q11: Take a number from the user and print the multiplication table of that number from 1 to 10.
number = int(input("NEter your nukmber"))
for i in range(1,11):
   print(number*i)

# Q12: Take a number from the user and print the factorial of that number using a loop.
n = int(input("Enter your number"))
fact = 1
for i in range(1, n+1):
  fact *= i
  print(fact)
  
  