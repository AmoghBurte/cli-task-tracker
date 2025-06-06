tasks = []

def add_task(task):
    tasks.append(task)
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print(f"Task '{task}' not found.")
def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")
def clear_tasks():
    tasks.clear()
    print("All tasks cleared.")
def main():

    while True:
        print("\nTask Tracker")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Clear Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter task to add: ")
            add_task(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            clear_tasks()
        elif choice == '5':
            print("Exiting Task Tracker.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()






