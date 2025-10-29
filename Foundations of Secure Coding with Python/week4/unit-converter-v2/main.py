import conversions
while True:
    print("\nUnit Convertor")
    print("1. For Km to Miles")
    print("2. Miles to Km")
    print("3. Fahrenhite to Celsius")
    print("4. Clesius to Fahrenite")
    print("5. Exit")

    choose = input("Enter your choise : ")

    if choose == "1":
        km = int(input("Enter the KM to Convert : "))
        print(f"The conversion of Km to Miles is {conversions.km_to_miles(km)}")
    elif choose == "2":
        miles = int(input("Enter the miles to convert : "))
        print(f"The conversion of miles to km is {conversions.miles_to_km(miles)}")
    elif choose == "3":
        fah= int(input("Enter the temp in Fahrenhite : "))
        print(f"The conversion of Fahrenhite to Celsius is {conversions.fah_to_celsius(fah)}")
    elif choose == "4":
        cel = int(input("Enter temp in celsius : "))
        print(f"The conversion of the Clesius to Fahrenite is {conversions.celsius_to_fah(cel)}")
    else:
        break
