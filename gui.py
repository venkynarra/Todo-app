import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip= "Enter todo")
add_button = sg.Button("ADD") # adding button
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]]) # layout is a argument, it expect lists. these lists contain FreeSimpleGUI instances
window.read()
window.close()