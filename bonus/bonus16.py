# Files compresssion program , more widgets to go-- for now we have label input button in this program
import FreeSimpleGUI as sg
from zip_creator import make_archive
label1 = sg.Text("Select Files to Compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("choose the Files", key = "files")

label2 = sg.Text("Select Destination Folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose the Folder", key = "folder")
compress_button = sg.Button("Compress")
output_label = sg.Text(key = "output", text_color= "green")
window = sg.Window("File Compressor", layout = [[label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(';')
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value = "compression completed!") # to print update is completed




window.read()
window.close()
