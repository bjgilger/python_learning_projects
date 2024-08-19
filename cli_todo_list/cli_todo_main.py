"""
Title: Task List CLI
Author:  John Gilger
This is a simple CLI application for creating task lists.
"""


while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:]

        with open("tasks.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("tasks.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("tasks.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}: {item.title()}")

    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open("tasks.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter the new task: ")
        todos[number] = new_todo + '\n'

        with open("tasks.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("tasks.txt", "r") as file:
            todos = file.readlines()
            index = number - 1

        task_to_remove = todos[index].strip('\n')
        number = number - 1
        todos.pop(index)

        with open("tasks.txt", "w") as file:
            file.writelines(todos)

        message = f"Task {task_to_remove} completed."
        print(message)

    elif "exit" in user_action:
        break

    else:
        print("Invalid input")

print("Bye!")



