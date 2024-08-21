"""
Title: Task List CLI
Author:  John Gilger
This is a simple CLI application for creating task lists.
"""


def get_todos():
    with open("tasks.txt", "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')
        with open("tasks.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}: {item.title()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter the new task: ")
            todos[number] = new_todo + '\n'

            with open("tasks.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Please enter a number")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            task_to_remove = todos[index].strip('\n')
            number = number - 1
            todos.pop(index)
            with open("tasks.txt", "w") as file:
                file.writelines(todos)
            message = f"Task {task_to_remove} completed."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input")

print("Bye!")
