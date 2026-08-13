student = {
"name": "Rahul",
"age": 22,
"course": "BDA"
}

# Q1 Print the student's name.

print(student["name"])

# Q2 Print the age.

print(student["age"])

# Q3 Change age to 23.

student["age"]=23
print(student)

# Q4 Add:

# city → Mumbai

student["city"]='Mumbai'
print(student)

# Q5 Check whether "course" exists.

print("course" in student)

# Q6 Check whether "salary" exists.

print("salary" in student)

# Q7 Remove "age" using pop() and store the removed value.

student.pop("age")
print(student)

# Q8 Print all keys.

for i in student:
print(i)

# Q9 Print all values.

for i in student.values():
print(i)

# Q10 Print every key and value using .items()

for key,value in student.items():
print(key,value)

# Do all 10 together.