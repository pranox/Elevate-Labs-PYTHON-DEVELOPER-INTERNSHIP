import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.\n")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully.")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()

