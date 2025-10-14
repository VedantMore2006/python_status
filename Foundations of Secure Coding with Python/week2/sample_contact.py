# lis = [1,2,3,4]
# lis.pop(0)
# print(lis) for the deleting the contact with the help of the pop method

print("Welcome to the Sample contact mini project")
contact = []
while True:
    cmd = input("Please enter the below commands for the contact operations.\n'add'\n'remove'\n'show'\n'exit'\n >> ")
    if cmd == "add":
        contact_add = int(input("Enter the number that you want to save : "))
        contact.append(contact_add)
        print("Contact Added")
    elif cmd == 'remove':
        contact_remove = int(input("Enter the contact that tou wnat to remove : "))
        contact.remove(contact_remove)
        print("Contact removed")
    elif cmd == 'show':
        print("The below are your contact")
        for i in contact:
            print("-->", i)
    elif cmd == 'exit':
        print("Exit from the program!!")
        break
    else:
        print("Unknown command, Try again")