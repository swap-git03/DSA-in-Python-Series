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