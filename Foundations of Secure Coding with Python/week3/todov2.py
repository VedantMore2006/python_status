#----TO-DO-List-program---

#------functions----------
def show_tasks(tasks):
    print("Your Tasks:")
    for t in tasks:
        print(">>>", t)

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

#------store-data-in-list----------
tasks = []

#-----condition------
while True:
    command = input("Enter a command (add/show/remove/exit): ")

#----calling-above-functions-----
    if command == "add":
        add_task(tasks)
    elif command == "show":
        show_tasks(tasks)
    elif command == "remove":
        remove_task(tasks)
    elif command == "exit":
        print("Exit Program!")
        break
    else:
        print("Unknown command, try again.")
