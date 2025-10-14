tasks = []

while True:
    command = input("Enter a command (add/show/remove/exit)")

    if command == 'add':
        task = input("Enter a new task :")
        tasks.append(task)
        print("Task Added.")
    elif command == "show":
        print("Your Tasks.")
        for t in tasks:
            print("-", t)
    elif command == "remove":
        task = input("Enter the task to remove : ")
        if task in tasks:
            task.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
    elif command == "exit":
        print("Exit Program!!")
        break
    else:
        print("Unknown Command, Try again")
    
