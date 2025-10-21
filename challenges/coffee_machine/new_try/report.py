from resources import resources

# def print_report(rs):
#     """docstring"""
    
# report.py

def print_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

print_report(resources)