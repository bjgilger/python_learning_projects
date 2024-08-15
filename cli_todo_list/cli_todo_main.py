"""
Title: Task List CLI
Author:  John Gilger
This is a simple CLI application for creating task lists.
"""


while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a task: ")

            file = open("tasks.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("tasks.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("tasks.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                print(f"{index + 1}: {item.title()}")
        case "edit":
            number = int(input("Enter the number of the task item to edit: "))
            number = number - 1
            new_todo = input("Enter the new task: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter the number of the task item completed: "))
            number = number - 1
            todos.pop(number)
        case "exit":
            break

print("Bye!")



