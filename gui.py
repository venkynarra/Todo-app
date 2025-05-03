import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip= "Enter todo", key = "todo") # key istodo here
add_button = sg.Button("ADD") # adding button
list_box = sg.Listbox(values = functions.get_todos(), key = "todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button],[list_box, edit_button]],
                  font=('helvetica', 20)) # layout is a argument, it expect lists. these lists contain FreeSimpleGUI instances
while True:
    event, values = window.read()
    print(1, event)  # event gets the values of add from line 6
    print(2, values)  # values get the key from line 5 and input text from same line
    print(3, values['todos'])
    match event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"  #we are giving values of the key which we given on top
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] #todo is key here getting new todo to edit function
            todos = functions.get_todos()
            index = todos.index(todo_to_edit) #all thse 4 lines of code is replacing new todo with existing todo, this is edit function
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos) # this will give list box instace ,
        case 'todos':
            window['todo'].update(value = values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()