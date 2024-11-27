from colorama import Fore
import datetime
import os
import json

FILE_NAME = "todo_list"
tasks = []


def add(tasks):
    task = input(Fore.YELLOW + "Enter a new task: ").strip()
    if task:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append((f"Task: {task} | Timestamp: {timestamp}"))
        print(Fore.GREEN + f"Task '{task}' added!")
    else:
        print(Fore.RED + "Task cannot be empty!")


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
            new_task = input(f"Edit '{current_task}': ").strip()
            if new_task:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tasks[task_number - 1] = f"Task: {new_task} | Timestamp: {timestamp}"
                print(Fore.GREEN + f"Task updated to '{new_task}' on: {timestamp}.")
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


def menu():
    print(Fore.WHITE + "\nTo-Do List Menu\n--------------------")
    print(Fore.BLUE + "1. Add Task")
    print(Fore.BLUE + "2. Remove Task")
    print(Fore.BLUE + "3. View Task")
    print(Fore.BLUE + "4. Edit Task")
    print(Fore.BLUE + "5. Search Task")
    print(Fore.BLUE + "6. Save Tasks")
    print(Fore.BLUE + "7. Exit")


while True:
    menu()
    choice = input("\nChoose an option (1-7): ")
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
        print(Fore.GREEN + "Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
