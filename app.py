from colorama import Fore
import datetime
import os
import json

todo_list = []

def menu():
    print(Fore.BLUE + "\nTo-Do List Menu\n" + "-" * 20)
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")

    
def add():
    task = input(Fore.CYAN + "\nEnter a task: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    todo_list.append((task, timestamp))
    print(f"Task '{task}' added! ({timestamp}).")
    
def view():
    if not todo_list:
        print(Fore.CYAN + "\nYour to-do list in empty.")
    else:
        print(Fore.CYAN + "\nYour Tasks:")
        for idx, (task, timestamp)  in enumerate(todo_list, start=1):
            print(f"{idx}. {task} (added on {timestamp})")
            
def remove():
    view()
    try:
        task_num = int(input(Fore.CYAN + "\nEnter the number of the taks to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(Fore.RED + f"Task '{removed[0]}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    
while True:
    menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        add()
    if choice == "2":
        view() 
    if choice == "3":
        remove()