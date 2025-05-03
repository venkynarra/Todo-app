from optparse import Values
from zip_extractor import extract_archive

import FreeSimpleGUI as sg


from bonus.zip_extractor import extract_archive

sg.theme("Black")
label1 = sg.Text("Select Archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("choose", key = "archive")

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
choose_button2 = sg.FileBrowse("choose", key = "folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key = "output", text_color= "green")

window = sg.Window("Archive Extractor0",
                   layout = [[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [extract_button, output_label]])
while True:
    event, Values = window.read()
    print(event, Values)
    archivepath = Values["archive"]
    dest_dir =Values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value = "extraction completed")

window.close()