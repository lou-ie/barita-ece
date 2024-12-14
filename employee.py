class Employee:
    def __init__(self, employee_id, name, organization, attendance=0):
        self.employee_id = employee_id
        self.name = name
        self.organization = organization
        self.attendance = attendance


employees = []


def add_employee():
    employee_id = input("Enter ID: ")
    name = input("Enter Name: ")
    organization = input("Enter affiliated  Organization: ")
    employees.append(Employee(employee_id, name, organization))
    print("Employee Added Successfully!\n")


def mark_attendance():
    emp_id = input("Enter Employee ID: ")
    for emp in employees:
        if emp.employee_id == emp_id:
            emp.attendance += 1
            print(f"Attendance has been recorded for {emp.name}. Total Attendance: {emp.attendance}\n")
            return
    print("Employee not found!\n")


def display_employees():
    if not employees:
        print("No Employees Found.\n")
        return
    for emp in employees:
        print(f"ID: {emp.employee_id}, Name: {emp.name}, Organization: {emp.organization}, Attendance: {emp.attendance}")
    print()


def attendance_percentage():
    total_days = int(input("Enter the total number of working days: "))
    if total_days == 0:
        print("Total days cannot be 0.\n")
        return
    for emp in employees:
        percentage = (emp.attendance / total_days) * 100
        print(f"Employee: {emp.name}, Employee ID: {emp.employee_id} has an attendance percentage of {percentage:.2f}%")
    print()


def main():
    while True:
        print("Employee Attendance Tracker:")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. Display All Employee Records")
        print("4. Percentage of Attendance per Employee")
        print("5. Quit Program")

        choice = input("Enter Choice (1-5): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            display_employees()
        elif choice == "4":
            attendance_percentage()
        elif choice == "5":
            print("Program has been shut down! Thank you!")
            break
        else:
            print("Invalid Choice. Please Try Again!\n")


if __name__ == "__main__":
    main()
