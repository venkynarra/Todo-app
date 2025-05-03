import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip= "Enter todo", key = "todo") # key istodo here
add_button = sg.Button("ADD") # adding button
window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                  font=('helvetica', 20)) # layout is a argument, it expect lists. these lists contain FreeSimpleGUI instances
while True:
    event, values = window.read()
    print(event)  # event gets the values of add from line 6
    print(values)  # values get the key from line 5 and input text from same line
    match event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            print("Add button clicked")
            print("Written to file:", todos)
        case sg.WIN_CLOSED:
            break


window.close()