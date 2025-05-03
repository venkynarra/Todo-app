import functions
import FreeSimpleGUI as sg
import time
sg.theme("DarkPurple4")
clock = sg.Text('', key = "clock" )
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip= "Enter todo", key = "todo") # key istodo here, tooltip tell what to do like a small logo on the input box
add_button = sg.Button("ADD") # adding button
list_box = sg.Listbox(values = functions.get_todos(), key = "todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                       [label],
                           [input_box, add_button]
                       ,[list_box, edit_button, complete_button],
                        [exit_button]],
                  font=('helvetica', 20)) # layout is a argument, it expect lists. these lists contain FreeSimpleGUI instances
while True:
    event, values = window.read(timeout = 200)
    window['clock'].update(value = time.strftime("%b %d, %Y, %H:%M:%S"))
    print(1, event)  # event gets the values of add from line 6
    print(2, values)  # values get the key from line 5 and input text from same line
    print(3, values['todos'])
    match event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"  #we are giving values of the key which we given on top
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos) #using this to print adding values in GUI.
        case "Edit":
            try:

                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] #todo is key here getting new todo to edit function
                todos = functions.get_todos()
                index = todos.index(todo_to_edit) #all thse 4 lines of code is replacing new todo with existing todo, this is edit function
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos) # this will give list box instace ,
            except IndexError:
                sg.popup("please select an item first", font = ("Helvetica", 20))
        case "complete":
            try:

                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos) # updating the list and wiritng new todos
                window['todos'].update(values = todos)
                window['todo'].update(value = '') # making sure there is no value in todo in entering the input
            except IndexError:
                sg.popup("please select an item first", font = ("Helvetica", 20))
        case "exit":
            break
        case 'todos':
            window['todo'].update(value = values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()