todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Create Task")
    print("2. Update Task")
    print("3. Review Tasks")
    print("4. Exit")

def create_task():
    task = input("Enter the new task: ")
    todo_list.append(task)
    print(" Task created successfully!")

def update_task():
    if not todo_list:
        print("No tasks to update.")
        return
    review_tasks()
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def review_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        create_task()
    elif choice == '2':
        update_task()
    elif choice == '3':
        review_tasks()
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print( "Invalid choice. Please select between 1 and 4.")
