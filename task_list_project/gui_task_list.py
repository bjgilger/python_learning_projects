import functions as fn
import PySimpleGUI as sg  # Corrected import
import time

sg.theme('PythonPlus')
clock = sg.Text('', key='clock')
label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter task", key='task')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todos(), key='tasks',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('A Simple Task List',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Noto Sans', 16))

while True:
    event, values = window.read(timeout=100)
    window['clock'].Update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == sg.WIN_CLOSED:
        break

    match event:
        case 'Add':
            tasks = fn.get_todos()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            fn.write_todos(tasks)
            window['tasks'].update(values=tasks)

        case 'Edit':
            try:
                task_to_edit = values['tasks'][0]
                new_task = values['task']

                tasks = fn.get_todos()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                fn.write_todos(tasks)
                window['tasks'].update(values=tasks)
            except IndexError:
                sg.popup("Please select an item to edit.", font=('Noto Sans', 18))

        case 'Complete':
            try:
                task_to_complete = values['tasks'][0]
                tasks = fn.get_todos()
                tasks.remove(task_to_complete)
                fn.write_todos(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value='')
            except IndexError:
                sg.popup("Please select an item to complete.", font=('Noto Sans', 18))

        case 'Exit':
            break

        case 'tasks':
            window['task'].update(value=values['tasks'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()