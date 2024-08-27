"""
Title: Functions for CLI Task List project
Author:  John Gilger
These functions are for a simple CLI application for creating task lists.
"""
def get_todos(filepath="tasks.txt"):
    """ Read a text file and return a list of tasks """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath="tasks.txt"):
    """ Write a task list to a text file """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

