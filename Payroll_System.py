print("Company Payroll")

employee_num = int(input("\nHow many workers does your company have?: "))
sum_salary = 0
i = 0
y = 1

while employee_num != i:
    employee_name = input(f"\nEnter employee number {y} name: ")
    hourly_rate = float(input(f"Enter {employee_name}'s hourly rate: "))
    hours_worked = float(input(f"Enter {employee_name}'s worked hours: "))
    overtime_hours = float(input("Total hours of overtime: "))
    late_hours = float(input("Total hours of late: "))

    # Formula
    overtime_payment = (hourly_rate / 8) * overtime_hours
    deduction = late_hours * hourly_rate
    total_salary = (hourly_rate * hours_worked) + overtime_payment - deduction

    # Payroll Summary
    print(f"\nPayroll summary of Employee number {y}: {employee_name}")
    print(f"Employee number: {y}")
    print(f"Employee name: {employee_name}")
    print(f"Hourly Rate: {hourly_rate}")
    print(f"Total hours worked: {hours_worked}")
    print(f"Total hours of overtime: {overtime_hours}")
    print(f"Overtime payment of {employee_name} is: {overtime_payment}")
    print(f"Total hours of late: {late_hours}")
    print(f"Total deduction of {employee_name}: {deduction}")
    print(f"Total salary of {employee_name} is: {total_salary}")

    sum_salary += total_salary
    y += 1
    i += 1

print(f"\nTotal Salary Paid to {employee_num} Workers is: {sum_salary}")
