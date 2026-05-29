# ---------------------------------
# FOR LOOP BASICS
# ---------------------------------

# Q1: Print 1 to N
n = int(input("Enter number: "))
for i in range(1, n+1):
    print(i)


# Q2: Multiplication table (1–10)
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i)


# Q3: Factorial using for loop
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)


# Q4: Sum from 1 to N
n = int(input("Enter number: "))
total = 0
for i in range(1, n+1):
    total += i
print(total)


# Q5: Squares from 1 to N  ❌ (your logic was wrong)
n = int(input("Enter number: "))
for i in range(1, n+1):
    print(i**2)


# ---------------------------------
# WHILE LOOP (DIGITS BASED)
# ---------------------------------

# Q6: Sum of digits
n = int(input("Enter number: "))
total = 0
while n > 0:
    digit = n % 10
    total += digit
    n //= 10
print(total)


# Q7: Reverse number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print(rev)


# Q8: Palindrome number ❌ (your version had wrong variables + indentation)
n = int(input("Enter number: "))
rev = 0
temp = n
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if temp == rev:
    print('IS Palindrom')
else:
    print('Not a palindrome')


# Q9: Count digits
n = input("Enter number: ")
count = 0
for i in n:
    count += 1
print(count)


# Q10: Product of digits
n = int(input("Enter number: "))
prod = 1

while n > 0:
    digit = n % 10
    prod *= digit
    n //= 10

print(prod)


# ---------------------------------
# STRING BASED
# ---------------------------------

# Q11: Count vowels
s = input("Enter string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)


# Q12: Reverse string
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)


# Q13: String palindrome
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Print numbers from 1 to N
# - skip numbers divisible by 3
# - print "Five" for multiples of 5
# - stop if divisible by 7

n = int(input("Enter number: "))

for i in range(1, n+1):
    if i % 7 == 0:
        break;
    elif i % 3 == 0:
        continue
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)


# for loop is used when you know number of iterations are known before you start the loop
# while loop is used when you know end condition


# ◆ Beginner
#conditionalls from placement prep series
# 21. Print numbers 1 to 100 using a loop.
for i in range(1, 101):
    print(i)


# 22. Print all even numbers between 1 and 50.
for i in range(2, 51, 2):
    print(i)

# 23. Print the multiplication table of any user-inputted number.
n = int(input("Enter number: "))
for i in range(1, 11):
    print(i*n)

# 24. Find the sum of all digits in a number (e.g., 1234 → 10).
n = int(input("Enter number: "))
sum = 0
while n>0:
    digit = n % 10
    sum += digit
    n = n//10
print(sum)

# 25. Count how many times digit 7 appears in a given number
n = int(input("Enter number: "))
seven = 0;
while n>0:
    digit = n % 10
    if digit ==7:
        seven += 1
    n = n//10
print(seven)


#  Intermediate

# 27. Reverse a number without converting it to a string (e.g., 1234 → 4321).
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n  = n //10
print(rev)

# 28. Check if a number is a palindrome using a loop.
n = int(input("Enter number: "))
rev = 0
temp = n
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if temp == rev:
    print('IS Palindrom')
else:
    print('Not a palindrome')