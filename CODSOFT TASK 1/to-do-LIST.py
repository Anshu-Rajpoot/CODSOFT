import os
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks are:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to update a task
def update_task(task_index, new_task):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("You have choosen Invalid task index.")

# Function to save tasks to a file
def save_tasks_to_file(filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    print(f"Tasks Successfully saved to '{filename}'.")

# Function to load tasks from a file
def load_tasks_from_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            loaded_tasks = file.readlines()
            tasks.extend(loaded_tasks)
        print(f"Tasks loaded from '{filename}'.")
    else:
        print(f"'{filename}' does not exist.")

# Load tasks from a file when the application starts
load_tasks_from_file("tasks.txt")

# Main program loop
while True:
    print("\nTo-Do List Application")
    print("1. Add a Task")
    print("2. List all Tasks")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Save Tasks to File")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task index to update: "))
        new_task = input("Enter the new task description: ")
        update_task(task_index, new_task)
    elif choice == '4':
        task_index = int(input("Enter the task index to delete: "))
        delete_task(task_index)
    elif choice == '5':
        filename = input("Enter the filename to save tasks to: ")
        save_tasks_to_file(filename)
    elif choice == '6':
        save_tasks_to_file("tasks.txt")  # Save tasks before quitting
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
