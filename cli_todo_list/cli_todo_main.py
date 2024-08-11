"""
Title: TODO LIST CLI
Author:  John Gilger
This is a simple CLI application for creating TODO lists.
"""


todos = []

prompt = "Enter a todo: "

while True:
    todo = input(prompt)
    todos.append(todo)
    print(todos)
    break
