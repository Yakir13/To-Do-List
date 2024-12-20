from colorama import Fore
import datetime
import os
import json

FILE_NAME = "todo_list"
tasks = []


def load():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save(tasks):
    save_data = {
        "tasks": tasks,
        "last_saved": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    with open(FILE_NAME, "w") as file:
        json.dump(save_data, file, indent=4)
        if save_data:
            print(Fore.GREEN + "Saved successfuly!")


def menu():
    print(Fore.BLUE + "\nTo-Do List Menu\n" + "-" * 20)
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Edit Task")
    print("5. Search Task")
    print("6. Save Tasks")
    print("7. Clear Tasks")
    print("8. Exit")


def add(tasks):
    task = input(Fore.YELLOW + "Enter a new task: ").strip()
    deadline = input("Enter the deadline: ")
    if task and deadline:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append((f"Task: {task} | Timestamp: {timestamp} | Deadline: {deadline}"))
        print(
            Fore.GREEN
            + f"Task added: '{task}'\nDeadline added: '{deadline}'\nAdded on: '{timestamp}'"
        )
    else:
        print(Fore.RED + "Task or deadline cannot be empty!")


def remove(tasks):
    try:
        task_num = int(input(Fore.YELLOW + "\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(Fore.GREEN + f"Task '{removed}' removed!")
        else:
            print(Fore.RED + "Invalid task number!")
    except ValueError:
        print(Fore.RED + "Please enter a valid number!")


def view(tasks):
    if tasks:
        print(Fore.YELLOW + "\nYour Tasks: ")
        for i, (task) in enumerate(tasks, start=1):
            print(Fore.GREEN + f"{i}. {task}")
    else:
        print(Fore.RED + "\nNo tasks yet! Add a task to get started.")


def edit(tasks):
    view(tasks)
    try:
        task_number = int(
            input(Fore.YELLOW + "\nEnter the number of the task you want to edit: ")
        )
        if 1 <= task_number <= len(tasks):
            current_task = tasks[task_number - 1]
            new_task = input(f"Edit task: ").strip()
            if new_task:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                deadline = input("Enter the deadline: ")
                tasks[task_number - 1] = (
                    f"Task: {new_task} | Timestamp: {timestamp} | Deadline: {deadline}"
                )
                print(
                    Fore.GREEN
                    + f"Task updated to '{new_task}' and deadline updated to '{deadline}' on '{timestamp}'."
                )
            else:
                print(Fore.RED + "Task cannot be empty.")
        else:
            print(Fore.RED + "Invalid task number.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")


def search(tasks):
    type = input(Fore.YELLOW + "Enter task to search: ")
    if type:
        matching_tasks = [task for task in tasks if type in task]
        if matching_tasks:
            print(Fore.GREEN + f"Tasks matching: {type} ")
            for i, task in enumerate(matching_tasks, start=1):
                print(Fore.GREEN + f"{i}. {task}")
        else:
            print(Fore.RED + f"No tasks found matching: {type}.")
    else:
        print(Fore.RED + "You have to search task!")


def clear(tasks):
    confirm = input(
        Fore.YELLOW + "Are you sure you want to clear all tasks? (yes/no): "
    ).lower()
    if confirm == "yes":
        tasks.clear()
        save(tasks)
        print(Fore.GREEN + "All tasks cleared")
    else:
        print(Fore.RED + "Action cancelled")


while True:
    menu()
    choice = input(Fore.BLUE + "\nChoose an option (1-8): ")
    if choice == "1":
        add(tasks)
    elif choice == "2":
        remove(tasks)
    elif choice == "3":
        view(tasks)
    elif choice == "4":
        edit(tasks)
    elif choice == "5":
        search(tasks)
    elif choice == "6":
        save(tasks)
    elif choice == "7":
        clear(tasks)
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
