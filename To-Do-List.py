todo_list = []
def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['task']} [{status}]")
def add_task():
    task = input("Enter your new task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added!")
def mark_complete():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as completed: "))
        if 0 < task_no <= len(todo_list):
            todo_list[task_no - 1]["done"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")