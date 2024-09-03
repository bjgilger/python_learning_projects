"""
Title: GUI Task List
Author:  John Gilger
This is a simple GUI application for creating task lists.
"""

import functions
import FreeSimpleGUI as sg

label = sg.Text("Add a task")
input_box = sg.InputText(tooltip="Enter a task", key="TASK")
add_button = sg.Button("Add")

window = sg.Window('A Simple Task List',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20)
                   )

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_task = values["TASK"] + '\n'
            todos.append(new_task)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break


window.close()
