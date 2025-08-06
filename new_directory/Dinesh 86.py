# to_do_manager.py

def display_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{index + 1}. [{status}] {task['task']}")

def add_task(tasks):
    task_text = input("Enter new task: ")
    tasks.append({"task": task_text, "done": False})
    print("Task added!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to remove: ")) - 1
        removed = tasks.pop(choice)
        print(f"Removed task: {removed['task']}")
    except (IndexError, ValueError):
        print("Invalid choice.")

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: ")) - 1
        tasks[choice]["done"] = True
        print(f"Marked '{tasks[choice]['task']}' as done.")
    except (IndexError, ValueError):
        print("Invalid choice.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
