def display_emp():
    employees = []

    while True:
        print("=" * 30)
        print("Employee Management System")
        print("=" * 30)
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Add Employee selected.")

            emp_id = int(input("Enter employee ID: "))

            found = False

            for emp in employees:
                if emp['id'] == emp_id:
                    found = True
                    break

            if found:
                print("Employee ID already exists.")

            else:
                name = input("Enter employee name: ")
                salary = int(input("Enter employee salary: "))

                emp_dict = {
                    'name': name,
                    'id': emp_id,
                    'salary': salary
                }

                employees.append(emp_dict)
                print(f"Success! {name} has been added as an employee.")

        elif choice == '2':
            print("View Employees selected.")

            if len(employees) == 0:
                print("No employees found.")
            else:
                for emp in employees:
                    print(
                        f"Employee name: {emp['name']} | "
                        f"Employee ID: {emp['id']} | "
                        f"Employee Salary: {emp['salary']}"
                    )

        elif choice == '3':
            print("Search Employee selected.")

            search_id = int(input("Enter employee ID: "))

            for emp in employees:
                if emp['id'] == search_id:
                    print("\nEmployee Found:")
                    print(
                        f"ID: {emp['id']} | "
                        f"Name: {emp['name']} | "
                        f"Salary: {emp['salary']}"
                    )
                    break
            else:
                print("No employee found for this ID.")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


display_emp()
