import streamlit as st
import functions #functions is backend
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]  + "\n"# dictinoary syntax session state
    todos.append(todo) # updated to do list
    functions.write_todos(todos)
st.title("My Todo App")
st.subheader("this is my todo app")
st.write("this app is to increase your productivity")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}-{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
          # deleting the todo from session state
        st.rerun()


st.text_input(label= "", placeholder= "add new todo",
              on_change=add_todo, key='new_todo')

