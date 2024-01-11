
def get_todos(filepath="todos.txt"):
    """
    :param filepath: Read a text files.
    :return: the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,filepath="todos.txt"):
    """
    :param todos_arg:write the items in the text files.
    :param filepath: write the to-do items list to the text files.
    :return: none.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)