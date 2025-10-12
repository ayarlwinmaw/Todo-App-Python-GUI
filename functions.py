FILEPATH = "todos.txt"

def show_todos():
    todos = []
    with open(FILEPATH, 'r') as file:
        todos = [todo.strip() for todo in file.readlines()]

    if len(todos) == 0:
        print("There is no todo yet! Please add some")
        return
    for i, todo in enumerate(todos, start=1):
        print(f"{i} -> {todo.title()}")

def get_todos(filepath= FILEPATH):
    """ Read a text file and return a list of todos
    :param filepath:
    :return: todos
    """
    todos = []
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filepath= FILEPATH):
    """
    Write todos to a text file line by line
    :param todos:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)