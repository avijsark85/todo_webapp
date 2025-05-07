# Learning deploying
# Streamlit needs tobe installed on the new project
# and use this commend to create requirements.txt that tell server about all packages required to run teh web qapp
#  pip freeze > requirements.txt
# then upload project to github

import streamlit as st
from streamlit import checkbox
import functions as f



# below is the function call when text box changes and results in the addition of the updated value to teh webapp
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    f.write_todos(todos)

todos = f.get_todos()

# creates the top section
st.title("ToDo App")
st.subheader("This is a app to track To-Do tasks!")
st.write("This app is to increase your productivity")

#creates the list of To do with checkboxes on them
for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key= item)
    if checkbox:
         todos.pop(index)
         f.write_todos(todos)
         del st.session_state[item]             # deletes the to do item from the displayed list too
         st.rerun()

#creates the input box for to do and add a function call to add_todo when value in it changes
st.text_input(key='new_todo', label = "", placeholder = "Add a To Do here...", on_change = add_todo)

print("Hello")
st.session_state
