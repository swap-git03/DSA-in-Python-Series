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
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


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