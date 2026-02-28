# from colorama import Fore, Style, Back
from rich.prompt import Prompt
from rich import print
import datetime
import time
import sys
import json
import os

todo_list = []


def add():
    while True:
        task = Prompt.ask("[bold yellow]\nEnter a task")
        if task:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            todo_list.append((task, timestamp))
            time.sleep(2)
            print(f"[bold green]\nTask '{task}' added! ({timestamp}).")
            break
        else:
            print("[bold red]Task cannot be empty! Try again.")
            continue


def view():
    if not todo_list:
        print("[bold red]\nYour to-do list is empty.")
    else:
        print("[bold yellow]\nYour Tasks:")
        for i, (task, timestamp) in enumerate(todo_list, start=1):
            print(f"[bold green]{i}. {task} (added on: {timestamp})")


def remove():
    view()
    while True:
        try:
            task_num = int(Prompt.ask("[bold yellow]\nEnter task number to remove"))
            if task_num:
                removed = todo_list.pop(task_num - 1)
                print(f"[bold red]\nTask '{removed[0]}' removed.")
                break
        except (IndexError, ValueError):
            print("[bold red]\nInvalid input!")
            continue


def edit():
    view()
    try:
        task_num = int(Prompt.ask("[bold yellow]\nEnter task number to edit"))
        new_text = Prompt.ask("[bold yellow]\nEnter new task description")
        task, status = todo_list[task_num - 1]
        todo_list[task_num - 1] = (new_text, status)
        print(f"[bold green]\nTask '{task}' updated to '{new_text}'.")
    except:
        print("[bold red]\nInvalid input.")


def search():
    keyword = Prompt.ask("[bold yellow]\nEnter keyword to search").lower()
    found = False
    for idx, (task, timestamp) in enumerate(todo_list, start=1):
        if keyword in task.lower():
            print(f"\n[bold green]{idx}. {task} (added on: {timestamp})")
            found = True
    if not found:
        print("[bold red]\nNo tasks found with that keyword.")


def clear():
    confirm = Prompt.ask(
        "[bold yellow]\nAre you sure you want to delete ALL tasks? (yes/no)"
    ).lower()
    if confirm == "yes":
        todo_list.clear()
        print("[bold green]\nAll tasks deleted.")
    else:
        print("[bold red]\nOperation canceled.")


def exit():
    print("[bold green]\nExiting the program...\n")
    time.sleep(2)
    sys.exit()


def menu():
    print("[bold blue]\nTo-Do List Menu\n" + "-" * 20)
    print("[bold blue]1. Add Task")
    print("[bold blue]2. View Tasks")
    print("[bold blue]3. Remove Task")
    print("[bold blue]4. Edit")
    print("[bold blue]5. search")
    print("[bold blue]6. Clear all tasks")
    print("[bold blue]7. Exit")


while True:
    menu()
    choice = Prompt.ask("[bold cyan]\nChoose an option")
    if choice == "1":
        add()
    if choice == "2":
        view()
    if choice == "3":
        remove()
    if choice == "4":
        edit()
    if choice == "5":
        search()
    if choice == "6":
        clear()
    if choice == "7":
        exit()
