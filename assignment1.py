# Step 1: Initialize sample employee data
employees = {
    101: {'name': 'aryan', 'age': 27, 'department': 'HR', 'salary': 5000},
    102: {'name': 'sunil', 'age': 30, 'department': 'Finance', 'salary': 7000}
}

# Step 2: Main menu loop
def main_menu():
    while True:
        print("\n=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice 1-4: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using Employee Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

# Step 3: Add employee function
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Try again with a new ID.")
            return
        
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        
        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print(f"Employee {name} added successfully.")
    except ValueError:
        print("Invalid input. Please enter correct data types.")

# Step 4: View all employees
def view_employees():
    if not employees:
        print("No employees available.")
    else:
        print("\nID\tName\t\tAge\tDepartment\tSalary")
        print("-" * 50)
        for emp_id, info in employees.items():
            print(f"{emp_id}\t{info['name']}\t\t{info['age']}\t{info['department']}\t\t{info['salary']}")

# Step 5: Search for an employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            info = employees[emp_id]
            print("\nEmployee Found:")
            print(f"Name      : {info['name']}")
            print(f"Age       : {info['age']}")
            print(f"Department: {info['department']}")
            print(f"Salary    : {info['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

# Start the program
main_menu()
