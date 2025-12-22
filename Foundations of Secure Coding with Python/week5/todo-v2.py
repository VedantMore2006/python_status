from pathlib import Path

#--file-path-for-storing-tasks
file_path = Path.home() / "python_status/Foundations of Secure Coding with Python/week5/tasks.txt"

#--Function-to-load-tasks-from-the-file
def load_tasks():
    tasks = []
    if file_path.exists():
        try:
            with file_path.open('r') as f:
                tasks = f.read().splitlines()
        except PermissionError:
            print("Cannot read tasks: Permission denied.")
        except Exception as e:
            print(f"An error occurred while reading tasks: {e}")
    return tasks

#--Function-to-save-tasks-to-the-file
def save_tasks(tasks):
    try:
        with file_path.open('w') as f:
            for task in tasks:
                f.write(task + "\n")
    except PermissionError:
        print("Cannot save tasks: Permission denied.")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")

#--Load-tasks-when-the-program-starts
tasks = load_tasks()

#--Main-program-loop
while True:
    try:

        command = input("Enter a command (add/show/remove/exit): ").lower()

        if not command.strip():
            print("Empty input is not allowed.")
            continue

        if command == "add":
            task = input("Enter a new task: ").strip()

            if not task:
                print("Empty Task Cannot be added")
                continue

            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")

        elif command == "show":
            if tasks:
                print("Your Tasks:")
                for t in tasks:
                    print(">>>", t)
            else:
                print("No tasks found.")

        elif command == "remove":
            task = input("Task to remove: ")
            if task in tasks:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task removed.")
            else:
                print("Task not found.")

        elif command == "exit":
            print("Exit Program.")
            break
        else:
            print("Unknown command, try again.")

    except KeyboardInterrupt:
        print("\n ^C Interrupted and Exiting")
        break
