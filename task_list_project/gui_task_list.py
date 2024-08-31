"""
Title: GUI Task List
Author:  John Gilger
This is a simple GUI application for creating task lists.
"""

import functions
import FreeSimpleGUI as sg

label = sg.Text("Add a task")
input_box = sg.InputText(tooltip="Enter a task")
add_button = sg.Button("Add")

window = sg.Window('A Simple Task List', layout=[
    [label],
    [input_box, add_button]
])
window.read()
window.close()
