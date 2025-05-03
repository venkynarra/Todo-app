import streamlit as st
import functions #functions is backend
todos = functions.get_todos()
st.title("My Todo App")
st.subheader("this is my todo app")
st.write("this app is to increase your productivity")
for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")

st.text_input(label= "", placeholder= "add new todo")