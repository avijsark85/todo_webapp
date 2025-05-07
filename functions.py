import os
filepath = 'todos.txt'

#if os.path.exists(filepath):
#    with open(filepath, "r") as f:
#        data = f.read()
#else:
#    print("Not found!")

def get_todos(filepath_local = filepath):
#
    with open(filepath_local, 'r') as file:
        todos_local = file.readlines()
        return todos_local

def write_todos(todos_local, filepath_local=filepath):
#    """ Write the to-do items into a text file."""
    with open(filepath_local, 'w') as file:
        file.writelines(todos_local)
if __name__ == "__main__":
    #Executed only when this file is run directly instead of being imported into another py file.
    todos = get_todos()
    print(todos)