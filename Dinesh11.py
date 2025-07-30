# Simple To-Do List Program

todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = todo_list.pop(task_num - 1)
        print(f"Removed task: {removed}")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
