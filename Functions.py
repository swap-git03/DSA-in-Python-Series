# 🔹 What is a function?

# A function is: a block of code that you can reuse
# def function_name():
#     # code

# def greet(name):
#     print("Hello", name)
# Call:
# greet("Rahul")

# Q1 ] Create a function that takes a number
# and prints its square

def square(a):
    return a * a
user_input = int(input("Enter a num: "))
print(square(user_input))


# Q2 Create a function that takes a number
# and RETURNS:
# "Even" if even
# "Odd" if odd

def evenodd(a):
    if a % 2 == 0:
        return "even"
    else:
        return "Odd"
n = int(input("enter num: "))
print(evenodd(n))

# Q3 Create a function that takes two numbers
# and returns the greater number
def greater(a, b):
    if a > b:
        return a;
    else:
        return b;
        
print(greater(5, 8))

# Q3 Create a function that takes 3 numbers
# and returns the largest among them

def greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(greatest(5, 4, 2))

# Q4 Create a function that takes a number
# and returns the sum of its digits

def sum(a):
    total = 0
    while a > 0:
        digit = a % 10
        total += digit
        a //= 10
    return total
num = int(input("Enter number: "))
print(sum(num))


# Q5 Create a function that takes a number
# and returns True if it is palindrome
# else False

def palindrome(a):
    rev = 0
    temp = a
    while a > 0:
        digit = a % 10
        rev = rev * 10 + digit
        a= a // 10
    if temp == rev:
        return True
    else:
        return False

print(palindrome(451))

# Q6 Create a function that takes a number
# and returns count of digits in that number

def count(a):
    count = 0
    while a > 0:
        digit = a % 10
        a = a // 10
        count +=1
    return count
print(count(451))


# Create a function that takes a number
# and returns the sum of EVEN digits only
def even_digits(a):
    total = 0
    while a > 0:
        digit = a % 10
        if  digit % 2 ==0:
            total += digit
        a = a // 10

    return total
print(even_digits(4584))

# Q1 Create: def show(**kwargs):
# Print the complete kwargs.
# Call it with:
# name="Rahul"
# age=22
# course="BDA"
def show(**kwargs):
    print(kwargs)
show(age=22, course="BDA")


# Q2 Write a function:
# student_info(**kwargs)
# that prints only the student's name.

def student_info(**kwargs):
    print(kwargs.get("name"))

student_info(name="Rahul", age=22,course = "BDA")


# Q3 Write a function that loops through kwargs and prints:
# name → Rahul
# age → 22
# course → BDA
def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
student_info(name="Rahul", age=22,course = "BDA")


# Q4 Write:
# def add(*args): and return the sum of all numbers.
# Test: 10, 20, 30, 40
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(10,20,30,40)

# Q5 — def profile(name, *skills, **details):
# Call it like:

# profile(
#     "Rahul",
#     "Python",
#     "SQL",
#     "Spark",
#     age=22,
#     city="Mumbai"
# )

# Inside the function, print:

# name
# skills
# details

def profile(name, *skills, **details):
    print("Name:")
    print(name)
    
    print("\nSkills:")
    print(skills)
    
    print("\nDetails:")
    print(details)

# Calling the function exactly as requested
profile(
    "Rahul",
    "Python",
    "SQL",
    "Spark",
    age=22,
    city="Mumbai"
)
