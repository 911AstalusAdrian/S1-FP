
def to_string(functions, function_index):
    function_name = functions[function_index][0]
    function_return = functions[function_index][1]
    return 'The Mamba function ' + str(function_name) + ' returns: ' + str(function_return)


def create_function(functions_list, function_name, function_return):
    created_function = [function_name, function_return]
    functions_list.append(created_function)


def search_function(functions_list, function_name):
    index = -1
    for i in range(len(functions_list)):
        if functions_list[i][0] == function_name:
            index = i
    return index


def command_split(command):
    """
    Dividing the user input into a command and parameters
    :param command: user input
    :return: command word and parameters
    """
    user_input = command.strip().split(' ', 1)
    user_input[0] = user_input[0].strip().lower()
    return user_input[0], '' if len(user_input) == 1 else user_input[1].strip().lower()


def add_function_ui(functions, command_parameters):
    """
    ui part for adding a function
    :param functions: The list of already existing functions
    :param command_parameters: the user's input, i.e the mamba function's name and what it returns
    :return: -
    The user input is split into parts, so we can 'obtain' the mamba function's name and what it returns
    After that, we create our function, and store it in a functions list
    If the function name is already in the list, we raise an error
    """
    function_name, function_actions = command_parameters.split('(', 1)
    function_actions_split = function_actions.split('=', 1)
    function_return = function_actions_split[1]
    create_function(functions, function_name, function_return)
    if function_name in functions:
        raise ValueError("Mamba function already declared!")


def list_function_ui(functions, command_parameters):
    command_parameters = command_parameters.strip()
    function_index = search_function(functions, command_parameters)
    if function_index == -1:
        raise ValueError("Mamba function not declared!")
    else:
        print(to_string(functions, function_index))


def eval_function_ui(functions, command_parameters):
    function_name = command_parameters.split('(', 1)
    index = search_function(functions, function_name)
    if index == -1:
        raise ValueError("Mamba function not existent!")


def start_ui():
    mamba_functions = []
    are_we_done = False
    while not are_we_done:

        command = input("command> ")
        command_word, command_parameters = command_split(command)
        if command_word == 'add':
            try:
                add_function_ui(mamba_functions, command_parameters)
                print("Mamba function added")
            except ValueError as ve:
                print(str(ve))
        elif command_word == 'list':
            try:
                list_function_ui(mamba_functions, command_parameters)
            except ValueError as ve:
                print(str(ve))
        elif command_word == 'eval':
            try:
                eval_function_ui(mamba_functions, command_parameters)
            except ValueError as ve:
                print(str(ve))
        elif command_word == 'exit':
            are_we_done = True
        else:
            print("Bad command!")


start_ui()

# Here's a wild-ass comment to check if we push to git