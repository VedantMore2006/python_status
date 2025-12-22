import json

data = {
    "username": "Javed",
    "password": "1waare{}rer343./",
    "role": "Help Desk Intern",
    "is_employee": True
}

with open('employees.json', 'w') as f:
    json.dump(data, f, indent=2)