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
            todo = input("Enter a task: ") + '\n'

            with open("tasks.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("tasks.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("tasks.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}: {item.title()}")

        case "edit":
            number = int(input("Enter the number of the task item to edit: "))
            number = number - 1

            with open("tasks.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter the new task: ")
            todos[number] = new_todo + '\n'

            with open("tasks.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Enter the number of the task item completed: "))

            with open("tasks.txt", "r") as file:
                todos = file.readlines()
                index = number - 1

            task_to_remove = todos[index].strip('\n')
            print(task_to_remove)
            number = number - 1
            todos.pop(index)

            with open("tasks.txt", "w") as file:
                file.writelines(todos)

            message = f"Task {task_to_remove} completed."
            print(message)

        case "exit":
            break

print("Bye!")



