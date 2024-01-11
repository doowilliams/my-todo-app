import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
