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

student = {
    "name": "Rahul",
    "age": 22,
    "course": "BDA"
}


# Q1 Use get() to retrieve "name".
print(student.get("name"))

# Q2 Use get() to retrieve "salary".
print(student.get("salary"))

# Q3 Use get() to retrieve "salary" but return 0 if it doesn't exist.
print(student.get("salary",0))

# Q4 Use update() to add:
student.update({"city":"Mumbai", "phone":9999999999})
print(student)


# Q5 Use update() to change:
# age → 23
student.update({"age":23})
print(student)

# Q6 — Nested Dictionary
student = {
    "name": "Rahul",
    "details": {
        "age": 22,
        "course": "BDA"
    }
}
# Print the course.
print(student["details"]["course"])

# Q7 Change the nested age from 22 to 23.
student["details"]["age"]=23
print(student)

# Q8 Create this:
students = {
    "student1": {
        "name": "Rahul",
        "age": 22
    },
    "student2": {
        "name": "Amit",
        "age": 24
    }
}
# Print "Amit".
print(students["student2"]["name"])
# Q9 Print Rahul's age.
print(students["student1"]["age"])

# Q10 — Using a loop, print:
# student1 Rahul
# student2 Amit
for key, value in students.items():
    print(key, value["name"])


employees = [
    {"name": "Raj", "salary": 50000},
    {"name": "Priya", "salary": 65000},
    {"name": "Amit", "salary": 45000}
]

# Q1. Print Priya's salary using indexing + dictionary key.
print(employees[1]["name"])
# Q2. Using a loop, print only the employee names.
for i in employees:
    print(i["name"])
# Q3. Using a loop, print names of employees whose salary is greater than 50000.
for i in employees:
    if (i["salary"]>50000):
        print(i["name"])
# Q4. Calculate the total salary of all employees using a loop.
total = 0
for i in employees:
    total +=i["salary"]
print(total)
# Q5. Find the employee with the highest salary without using max().
highest_salary = 0
highest_paid_emp = None

for i in employees:
    if i["salary"] > highest_salary:
        highest_salary = i["salary"]  # Keep it an integer!
        highest_paid_emp = i

print(highest_paid_emp)