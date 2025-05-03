FILEPATH = "todos.txt"
def get_todos(filepath = FILEPATH):# this function has only one argument (I didn't mention here, (filepath is argument) )
    """reading a text file and return the list of to-do items.print(help(get_todo)) gives what get_todo to do , it helps in large code base
    """
    with open(filepath, 'r') as file_local: # instead of the todos.txt we can give filepath here ()
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):       # (filepath, todos_arg) -- both are local variables
    with open(filepath, 'w') as file:  # no spaces while defining below remember
        file.writelines(todos_arg)


print(__name__)
if __name__ == "__main__":
    print("hello")
    print(get_todos())