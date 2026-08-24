# Simple To-Do List Application

todo_list = []

while True:
    print("\n----- TO-DO LIST MENU -----")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark task as done")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # View all tasks
        if len(todo_list) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")

    elif choice == '2':
        # Add a new task
        task = input("Enter the new task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == '3':
        # Update an existing task
        if len(todo_list) == 0:
            print("Your to-do list is empty.")
        else:
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")
            task_num = int(input("Enter the task number to update: "))

            if 1 <= task_num <= len(todo_list):
                new_task = input("Enter the updated task: ")
                todo_list[task_num - 1] = new_task
                print("Task updated!")
            else:
                print("Invalid task number.")

    elif choice == '4':
        # Delete a task
        if len(todo_list) == 0:
            print("Your to-do list is empty.")
        else:
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")
            task_num = int(input("Enter the task number to delete: "))

            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"Deleted task: {removed}")
            else:
                print("Invalid task number.")

    elif choice == '5':
        # Mark a task as done
        if len(todo_list) == 0:
            print("Your to-do list is empty.")
        else:
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")
            task_num = int(input("Enter the task number to mark as done: "))

            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1] = todo_list[task_num - 1] + " (Done)"
                print("Task marked as done!")
            else:
                print("Invalid task number.")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select a number between 1 and 6.")