# Problem Statement
# Create a Python program that accepts a student's name and marks out of 100.

# Calculate and display the student's grade according to these conditions:
# - 90–100: Grade A
# - 75–89: Grade B
# - 60–74: Grade C
# - 40–59: Grade D
# - Below 40: Fail
# Reject marks below 0 or above 100.

# Display the student's name, marks and grade.
def calculate_grade(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    elif marks >= 40:
        return "Grade D"
    else:
        return "Fail"

  
def main():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        return

    grade = calculate_grade(marks)

    print("\n----- Student Result -----")
    print(f"Student Name : {name}")
    print(f"Marks        : {marks}")
    print(f"Grade        : {grade}")


main()