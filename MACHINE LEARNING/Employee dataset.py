# Employee dataset
employees = [
    {"name": "Ali", "salary": 75000},
    {"name": "Suleman", "salary": 50000},
    {"name": "Abdul Basit", "salary": 65000},
    {"name": "Hammad", "salary": 85000},
    {"name": "Sayyam", "salary": 45000},
]
threshold = 60000
above_threshold = [emp for emp in employees if emp["salary"] > threshold]

print("Employees earning above", threshold, "are:")
for emp in above_threshold:
    print(f"- {emp['name']}: {emp['salary']} Rs")

total_salary = sum(emp["salary"] for emp in employees)
average_salary = total_salary / len(employees)

print("\nThe average salary of all employees is:", f"{average_salary:.2f} Rs")
