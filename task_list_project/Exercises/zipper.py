import FreeSimpleGUI as sg
from zip_creator import make_archive


label1 = sg.Text("Select files to zip")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",key='folder')

compress_button = sg.Button("Compress")
output_label = sg.Text(key='output')

window = sg.Window('A Simple File Zipper',
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [compress_button, output_label],
                   ])

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    window['output'].update('Success!')


window.close()