def km_to_miles(km):
    return km * 0.6

def miles_to_km(miles):
    return miles / 0.6

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    print("\nOur Mini Project unit Converter")
    print("1. Km to Miles")
    print("2. Miles to Km")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        km = float(input("Enter distance in km: "))
        print("In miles:", km_to_miles(km))
    elif choice == "2":
        miles = float(input("Enter distance in miles: "))
        print("In km:", miles_to_km(miles))
    elif choice == "3":
        c = float(input("Enter temperature in °C: "))
        print("In °F:", celsius_to_fahrenheit(c))
    elif choice == "4":
        f = float(input("Enter temperature in °F: "))
        print("In °C:", fahrenheit_to_celsius(f))
    elif choice == "5":
        print("Exit Progrma!")
        break
    else:
        print("Invalid choice, try again.")
