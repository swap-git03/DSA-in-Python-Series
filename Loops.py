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


# 26. Print all prime numbers between 1 and 100.
for num in range(2, 100):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num)



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

# 29. Print the Fibonacci sequence up to N terms.
n = int(input("Enter number: "))
a = 0
b = 1
for i in range(n):
    print(a)
    next = a+b
    a = b
    b = next


# 30. Find the factorial of a number using a loop.
n = int(input("Enter number: "))
facto = 1
for i in range(1, n+1):
    facto = facto * i
print(facto)

# 31. Print a right-angled star pattern of N rows.
n = int(input("Enter number: "))
for i in range(1, n+1):
    print("X" * i)

# 32. Print a number pyramid (1 / 1 2 / 1 2 3 …).
n = 3
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


# 32. Print a number pyramid (1 / 1 2 / 1 2 3 …).
n = 3
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


    
# 33. Find the GCD of two numbers using a loop.
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
gcd = 1
for i in range(1, min(n1, n2)+1):
    if (n1 % i ==0) and (n2 % i ==0):
        gcd = i
print(gcd)

# 34. Find all Armstrong numbers up to 1000 (sum of cubes of digits equals the number).
for num in range(1,1000):
    total_sum = 0
    temp = num
    
    while temp > 0:
        digits = temp%10
        total_sum += digits ** 3
        temp = temp//10
        
    if total_sum == num:
        print(num)


# 35. FizzBuzz: print 1–100, replace multiples of 3 with Fizz, 5 with Buzz, both with FizzBuzz
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print(f'{n} is FizzBuzz')
    elif n % 3 == 0:
        print(f'{n} is Fizz')
    elif n % 5 == 0:
        print(f'{n} is Buzz')
    else:
        print(n)


# 36. Print a diamond star pattern of N rows.
# n = 5 
for i in range(1, 6):
    print(" " * (5-i),end='')
    print("*"*(2*i-1))
for j in range(4, 0, -1):
    print(" " * (5-j), end='')
    print("*"*(2*j-1))

# 37. Find all perfect numbers between 1 and 10000.

for i in range(1, 10001,1):
    perfect = 0
    for j in range(1, i//2 + 1):
        if i%j==0:
            perfect += j   
    if perfect == i:
        print(i)
        

# 40. Generate all prime factors of a given number.
n = int(input())
i = 2

while n > 1:
    if n % i ==0:
        print(i)
        n = n // i
    else:
        i = i+1