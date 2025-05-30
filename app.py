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
    task = Prompt.ask("[bold yellow]\nEnter a task")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d || %H:%M:%S")
    todo_list.append((task, timestamp))
    time.sleep(2)
    print(f"[bold green]\nTask '{task}' added! ({timestamp}).")


def view():
    if not todo_list:
        print("[bold red]\nYour to-do list is empty.")
    else:
        print("[bold yellow]\nYour Tasks:")
        for idx, (task, timestamp) in enumerate(todo_list, start=1):
            print(f"[bold green]{idx}. {task} (added on: {timestamp})")


def remove():
    view()
    try:
        task_num = int(Prompt.ask("[bold yellow]\nEnter task number to remove"))
        removed = todo_list.pop(task_num - 1)
        print(f"[bold red]\nTask '{removed[0]}' removed.")
    except (IndexError, ValueError):
        print("[bold red]\nInvalid input!")


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


def exit():
    print("[bold green]\nExiting the program...")
    time.sleep(2)
    sys.exit()


def menu():
    print("[bold blue]\nTo-Do List Menu\n" + "-" * 20)
    print("[bold blue]1. Add Task")
    print("[bold blue]2. View Task")
    print("[bold blue]3. Remove Task")
    print("[bold blue]4. Edit")
    print("[bold blue]5. search")
    print("[bold blue]6. Exit")


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
        exit()
