
tasks = []
completed_tasks = []
incompleted_tasks = []

def add_tasks():
    print("Add a task")
    add_task = input("What task would you like to add? ")
    tasks.append(add_task)
    incompleted_tasks.append(add_task)
    print("Task added to list!")

def view_tasks():
    print("View tasks")
    print(tasks)

def mark_task_complete():
    print("Mark a task as complete")
    print(incompleted_tasks)
    complete_task = input("Enter the task you wish to mark as complete: ")
    completed_tasks.append(complete_task)
    incompleted_tasks.remove(complete_task)
    print(f"Completed tasks: {completed_tasks}")
    print(f"Incomplete tasks: {incompleted_tasks}")

def delete_task():
    print("Delete a task")
    delete_task = input("What task would you like to remove? ")
    if delete_task in tasks:
        tasks.remove(delete_task)
        print(f"{delete_task} has been removed...")
    else:
        print(f"{delete_task} was not found in your task list...")

def main_menu():
    while True:
            print("Welcome to the To-Do List App!")
            print("\nMenu:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as complete")
            print("4. Delete a task")
            print("5. Quit")
            choice = input("Enter a menu choice: ")
            if choice == "1":
                add_tasks()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                mark_task_complete()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                print("Quitting To-Do List App")
                break
            else:
                print("Invalid entry")
try:
    main_menu()
except Exception as e:
    print("An unexpected error occurred")
finally:
    print("That was so much fun!")



