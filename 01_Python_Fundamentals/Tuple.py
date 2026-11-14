# Q1 Create: (10, 20, 30, 40, 50)
num = (10,20,30,40)

# Print the first and last element.
print(num[0], num[-1])
# Q2 Print: 30 using indexing.
print(num[2])

num2 = (10, 20, 30, 40, 50,20)
# Q3 Print the last three elements using slicing.
print(num2[-3:])
# Q4 Count how many times 20 occurs:
count = 0
for i in num2:
    if i == 20:
        count +=1
print(count)


# t = (10, 20, 30, 20, 40, 20)
t = (10, 20, 30, 20, 40, 20)
# Q5 Find the first index of 30.
print(t.index(30))

# Q7 Create a single-element tuple containing 50.
single= (50,)
print(single)

# Q8 Convert:
# [10, 20, 30] into a tuple.
mylist=[10,20,30]
mytuple = tuple(mylist)
print(mytuple)


# Q9Convert:(10, 20, 30)
# into a list.
mytuple=(10,20,30)
mylist=list(mytuple)
print(mylist)


# Q10 point = (10, 20)
# Unpack it into x and y, then print both.
point = (10,20)
x, y = point
print(x, y)


# Q12 student = ("Rahul", 22, "BDA")
# Unpack into name, age, course.
student = ("swap", 22, "BDA")
name, age, course = student
print(student)