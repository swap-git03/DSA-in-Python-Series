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