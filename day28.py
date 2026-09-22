##2 Day 28: Employee Management System Project Using OOP and File Handling in Python

## Features of Employee Management System  in Health and Family Welfare Department:

#1 Add Employee
# Add a new employee and save details in a CSV file.
#2 View All Employees
# Display all employee records.
#3 Search Employee
# Find an employee using Employee ID.
#4 Update Employee
# Change name, designation, salary, or phone number.
#5 Delete Employee
# Remove an employee record.
#6 Promotion
# Change an employee’s designation after promotion.
#7 Salary Increment
# Increase salary by percentage or fixed amount.
#8 Transfer Employee
# Move an employee to a different department.
#9 View Activity History
# Show promotion, increment, and transfer history of an employee.
#10 Exit
#Close the program..

import csv
import os
import tempfile
from datetime import datetime


DEPARTMENT_NAME = "Health and Family Welfare Department"


class Employee:
    """Formats one employee record read from the CSV file."""

    def __init__(
        self, employee_id, name, designation, salary, phone, department=DEPARTMENT_NAME
    ):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = float(salary)
        self.phone = phone

    @classmethod
    def from_row(cls, row):
        return cls(
            row["employee_id"],
            row["name"],
            row["designation"],
            row["salary"],
            row["phone"],
            row.get("department", DEPARTMENT_NAME),
        )

    def to_row(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "salary": self.salary,
            "phone": self.phone,
        }

    def display_details(self):
        print("\n----------------------------------------")
        print("Employee ID  :", self.employee_id)
        print("Name         :", self.name)
        print("Department   :", self.department)
        print("Designation  :", self.designation)
        print("Salary       : ₹", self.salary)
        print("Phone Number :", self.phone)
        print("----------------------------------------")


class EmployeeManagementSystem:
    FILE_NAME = "health_department_employees.csv"
    HISTORY_FILE_NAME = "employee_activity_history.csv"
    FIELD_NAMES = [
        "employee_id",
        "name",
        "department",
        "designation",
        "salary",
        "phone",
    ]
    HISTORY_FIELD_NAMES = [
        "timestamp",
        "employee_id",
        "employee_name",
        "action",
        "old_value",
        "new_value",
        "details",
    ]

    def log_activity(self, employee, action, old_value, new_value, details=""):
        """Append an auditable promotion, increment, or transfer record."""
        is_new_file = (
            not os.path.exists(self.HISTORY_FILE_NAME)
            or os.path.getsize(self.HISTORY_FILE_NAME) == 0
        )
        with open(
            self.HISTORY_FILE_NAME, "a", newline="", encoding="utf-8"
        ) as history_file:
            writer = csv.DictWriter(
                history_file, fieldnames=self.HISTORY_FIELD_NAMES
            )
            if is_new_file:
                writer.writeheader()
            writer.writerow(
                {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "employee_id": employee.employee_id,
                    "employee_name": employee.name,
                    "action": action,
                    "old_value": old_value,
                    "new_value": new_value,
                    "details": details,
                }
            )

    def find_employee(self, employee_id):
        """Find an employee by searching the CSV, without a memory cache."""
        if not os.path.exists(self.FILE_NAME):
            return None

        with open(self.FILE_NAME, "r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                if row["employee_id"] == employee_id:
                    return Employee.from_row(row)
        return None

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        if self.find_employee(employee_id):
            print("Employee ID already exists.")
            return

        name = input("Enter Employee Name: ")
        designation = input("Enter Designation: ")
        try:
            salary = float(input("Enter Monthly Salary: "))
        except ValueError:
            print("Invalid salary. Please enter a number.")
            return
        phone = input("Enter Phone Number: ")

        employee = Employee(employee_id, name, designation, salary, phone)
        is_new_file = not os.path.exists(self.FILE_NAME) or os.path.getsize(self.FILE_NAME) == 0
        with open(self.FILE_NAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.FIELD_NAMES)
            if is_new_file:
                writer.writeheader()
            writer.writerow(employee.to_row())
        print("Employee added successfully.")

    def view_all_employees(self):
        if not os.path.exists(self.FILE_NAME) or os.path.getsize(self.FILE_NAME) == 0:
            print("No employee records available.")
            return

        found_employee = False
        print("\nHEALTH AND FAMILY WELFARE DEPARTMENT")
        print("EMPLOYEE MANAGEMENT SYSTEM")
        with open(self.FILE_NAME, "r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                Employee.from_row(row).display_details()
                found_employee = True
        if not found_employee:
            print("No employee records available.")

    def _replace_employee_rows(self, employee_id, replacement=None):
        """Rewrite the CSV one row at a time and return whether an ID was found."""
        found_employee = False
        directory = os.path.dirname(os.path.abspath(self.FILE_NAME))
        with tempfile.NamedTemporaryFile(
            "w", newline="", encoding="utf-8", delete=False, dir=directory
        ) as temporary_file:
            temporary_name = temporary_file.name
            writer = csv.DictWriter(temporary_file, fieldnames=self.FIELD_NAMES)
            writer.writeheader()

            if os.path.exists(self.FILE_NAME):
                with open(self.FILE_NAME, "r", newline="", encoding="utf-8") as file:
                    for row in csv.DictReader(file):
                        if row["employee_id"] == employee_id:
                            found_employee = True
                            if replacement is not None:
                                writer.writerow(replacement.to_row())
                        else:
                            writer.writerow(row)

        if found_employee:
            os.replace(temporary_name, self.FILE_NAME)
        else:
            os.remove(temporary_name)
        return found_employee

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        employee = self.find_employee(employee_id)
        if not employee:
            print("Employee not found.")
            return

        print("Press Enter without typing anything to keep old data.")
        name = input(f"Name ({employee.name}): ")
        designation = input(f"Designation ({employee.designation}): ")
        salary = input(f"Salary ({employee.salary}): ")
        phone = input(f"Phone ({employee.phone}): ")

        if name:
            employee.name = name
        if designation:
            employee.designation = designation
        if salary:
            try:
                employee.salary = float(salary)
            except ValueError:
                print("Invalid salary. Old salary retained.")
        if phone:
            employee.phone = phone

        self._replace_employee_rows(employee_id, employee)
        print("Employee details updated successfully.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        if self._replace_employee_rows(employee_id):
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    def promote_employee(self):
        employee_id = input("Enter Employee ID to promote: ")
        employee = self.find_employee(employee_id)
        if not employee:
            print("Employee not found.")
            return

        new_designation = input(
            f"New designation for {employee.name} ({employee.designation}): "
        ).strip()
        if not new_designation:
            print("Promotion cancelled. A new designation is required.")
            return

        previous_designation = employee.designation
        employee.designation = new_designation
        self._replace_employee_rows(employee_id, employee)
        self.log_activity(
            employee,
            "Promotion",
            previous_designation,
            new_designation,
            "Designation changed after promotion.",
        )
        print(
            f"{employee.name} promoted from {previous_designation} to {new_designation}."
        )

    def give_increment(self):
        employee_id = input("Enter Employee ID for salary increment: ")
        employee = self.find_employee(employee_id)
        if not employee:
            print("Employee not found.")
            return

        print("1. Percentage increment")
        print("2. Fixed-amount increment")
        increment_type = input("Choose increment type: ")
        try:
            value = float(input("Enter increment value: "))
            if value <= 0:
                raise ValueError
        except ValueError:
            print("Invalid increment. Enter a positive number.")
            return

        old_salary = employee.salary
        if increment_type == "1":
            employee.salary += employee.salary * value / 100
        elif increment_type == "2":
            employee.salary += value
        else:
            print("Invalid increment type.")
            return

        self._replace_employee_rows(employee_id, employee)
        increment_description = (
            f"{value:.2f}% increment"
            if increment_type == "1"
            else f"₹ {value:.2f} fixed increment"
        )
        self.log_activity(
            employee,
            "Salary Increment",
            f"₹ {old_salary:.2f}",
            f"₹ {employee.salary:.2f}",
            increment_description,
        )
        print(
            f"Salary updated from ₹ {old_salary:.2f} to ₹ {employee.salary:.2f}."
        )

    def transfer_employee(self):
        employee_id = input("Enter Employee ID to transfer: ")
        employee = self.find_employee(employee_id)
        if not employee:
            print("Employee not found.")
            return

        new_department = input(
            f"New department for {employee.name} ({employee.department}): "
        ).strip()
        if not new_department:
            print("Transfer cancelled. A new department is required.")
            return

        old_department = employee.department
        employee.department = new_department
        self._replace_employee_rows(employee_id, employee)
        self.log_activity(
            employee,
            "Transfer",
            old_department,
            new_department,
            "Department transfer completed.",
        )
        print(
            f"{employee.name} transferred from {old_department} to {new_department}."
        )

    def view_employee_history(self):
        employee_id = input("Enter Employee ID to view activity history: ")
        if not os.path.exists(self.HISTORY_FILE_NAME):
            print("No promotion, increment, or transfer history is available.")
            return

        records_found = False
        print("\nEMPLOYEE ACTIVITY HISTORY")
        print("----------------------------------------")
        with open(
            self.HISTORY_FILE_NAME, "r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                if row["employee_id"] == employee_id:
                    records_found = True
                    print("Date       :", row["timestamp"])
                    print("Employee   :", row["employee_name"])
                    print("Action     :", row["action"])
                    print("Changed    :", f"{row['old_value']} -> {row['new_value']}")
                    print("Details    :", row["details"])
                    print("----------------------------------------")
        if not records_found:
            print("No activity history found for this employee.")


def main():
    system = EmployeeManagementSystem()
    while True:
        print("\n==============================================")
        print("HEALTH AND FAMILY WELFARE DEPARTMENT")
        print("EMPLOYEE MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Promote Employee")
        print("7. Give Salary Increment")
        print("8. Transfer Employee")
        print("9. View Employee Activity History")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_employee()
        elif choice == "2":
            system.view_all_employees()
        elif choice == "3":
            employee = system.find_employee(input("Enter Employee ID to search: "))
            if employee:
                employee.display_details()
            else:
                print("Employee not found.")
        elif choice == "4":
            system.update_employee()
        elif choice == "5":
            system.delete_employee()
        elif choice == "6":
            system.promote_employee()
        elif choice == "7":
            system.give_increment()
        elif choice == "8":
            system.transfer_employee()
        elif choice == "9":
            system.view_employee_history()
        elif choice == "10":
            print("Thank you. Program closed.")
            break
        else:
            print("Invalid choice. Please select between 1 and 10.")


if __name__ == "__main__":
    main()
