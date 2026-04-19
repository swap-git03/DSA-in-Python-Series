# for i in range(start, stop, step):
    # code

# Q10: Take a number N and print numbers from 1 to N using a for loop.

n = int(input('enter your number : '))

for i in range (1, n+1):
    print(i);



# Q11: Take a number from the user and print the multiplication table of that number from 1 to 10.
number = int(input("NEter your number"))
for i in range(1,11):
   print(number*i)

# Q12: Take a number from the user and print the factorial of that number using a loop.
n = int(input("Enter your number"))
fact = 1
for i in range(1, n+1):
  fact *= i
  print(fact)

# Q13: Take a number from the user and print the sum of its digits using a loop.
n = int(input("Enter your number"))
sum = 0
for i in range(1, n+1):
  sum += i
  print(sum)
  
# Q14: Take a number from the user and print the reverse of that number using a loop.
n = int(input("Enter your number"))
for i in range(1, n+1):
  rev = n-i
  print(rev)

# Q15: Take a number and count how many digits it has using a loop.
n = input("Enter number: ")
count = 0

for i in n:
    count += 1

print(count)

# Q16: Take a number and print the square of numbers from 1 to that number.
n = int(input("Enter number: "))
for i in range(n, n+1):
  square = n**2
  print(square)


# while num > 0:
#     num = num // 10
# Q17: Take a number and check if it is a palindrome number using loops.
n = int(input("Enter number: "))
temp = number
rev = 0
while n > 0:
  digit = n%10
  rev = rev * 10 + digit
  n = n//10
if temp == rev:
  print('Number is palindrome')
else:
  print('Number is not a palindrome')

# Q6: Take a number N and print the sum of numbers from 1 to N using a for loop.

n = int(input("Enter a number : "))
sum = 0;
for i in range(1, n+1):
    sum = sum + i
print(sum);