from functions import get_todos, write_todos# functions is Separate file , it is called modules
import time
now = time.strftime("%b %d, %Y, %H:%M:%S")
print("the time is", now)
while True:
    user_action = input("type add or show, edit , complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:].strip() + "\n"

        todos = get_todos()   # this is first function def get_todos
        todos.append(todo)

        write_todos("todos.txt", todos) # defined this function def write_todos, if you want to mention filepath = todos.txt, and todos_arg = todos--you can (argument and argument value)

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:].strip())
            number = number - 1
            todos = get_todos()
            print('Here are the existing todos:', todos)
            new_todo = input("Enter a new todo: ") + '\n'
            todos[number] = new_todo
            write_todos = ("todos.txt", todos)  # function defined on top
            print('Here is the updated list:', todos)
        except ValueError:
            print("Your command is not valid. Please enter a number after 'edit'.")
        except IndexError:
            print("There is no todo with that number.")

    elif user_action.startswith('complete'):
        try:
            number_str = user_action[9:].strip()
            number = int(number_str)
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos = ("todos.txt", todos)  # function defined on top
            print(f"Todo '{todo_to_remove}' was removed from the list.")
        except ValueError:
            print("Please enter a valid number after 'complete'.")
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid.')

print("Bye dude!")
