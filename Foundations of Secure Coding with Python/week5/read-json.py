import json

with open('employees.json', 'r') as f:
    employees = json.load(f)
    print(employees)