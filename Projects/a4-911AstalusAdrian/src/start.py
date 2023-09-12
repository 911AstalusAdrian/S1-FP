"""
Assemble the program and start the user interface here
"""
from src.functions.functions import *


# We import all the functions from the functions.py file


def add_scores_ui(contestants_list, parameters):
    """
    UI Function for adding a contestant
    :param contestants_list: The list of contestants
    :param parameters: The user input
    """
    add_scores(contestants_list, parameters)
    print("Contestant added!")


def list_contestants_ui(contestants_list, parameters):
    """
    UI Function for the list instruction
    :param contestants_list: The list of contestants
    :param parameters: The user input
    :return:
    """
    operators = ['<', '=', '>']  # for lists with conditions, one of these 3 operators are used
    if parameters == '':
        print_list(contestants_list)  # Print the list as it is
    elif parameters == 'sorted':
        sorted_list = list_sort_by_average(contestants_list)  # Creating the sorted list
        print_list(sorted_list)  # Printing the sorted list
    elif parameters[0] in operators:
        conditions_list = list_with_condition(contestants_list,
                                              parameters)  # Creating the list depending on the condition
        print_list(conditions_list)  # Printing the list
    else:
        raise ValueError("Invalid type of listing!")


def print_list(requested_list):
    for element in requested_list:
        print(to_string(element))


def remove_command_ui(contestants_list, parameters):
    """
    Getting the parameters necessary for the remove function
    :param contestants_list: The contestants list
    :param parameters: Command parameters
    :return: -
    """
    operators = ['<', '=', '>']
    new_parameters = parameters.split()
    if len(new_parameters) == 1:
        position = int(new_parameters[0])
        remove_one_contestant(contestants_list, position)
    elif len(new_parameters) == 2:
        if new_parameters[0] not in operators:
            raise ValueError("Invalid operator!")
        condition_value = int(new_parameters[1])
        operator = new_parameters[0]
        remove_by_condition(contestants_list, operator, condition_value)
    elif len(new_parameters) == 3:
        start_position = int(new_parameters[0])
        end_position = int(new_parameters[2])
        remove_multiple_contestants(contestants_list, start_position, end_position)
    else:
        raise ValueError("Incorrect parameter input!")
    print("Contestant(s) removed!")


def insert_contestant_ui(contestants_list, parameters):
    """
    Getting the necessary parameters for the add function
    :param contestants_list: The list of contestants
    :param parameters: Command parameters (given by the user)
    :return: -
    """
    new_parameters = parameters_split(parameters)
    if len(new_parameters) != 5:
        raise ValueError("Incorrect number of parameters!")
    p1_score = int(new_parameters[0])
    p2_score = int(new_parameters[1])
    p3_score = int(new_parameters[2])
    inserting_position = int(new_parameters[4])
    insert_contestant(contestants_list, p1_score, p2_score, p3_score, inserting_position)
    print("Contestant added!")


def replace_score_ui(contestants_list, parameters):
    """
    Getting the necessary parameters for the replace function
    :param contestants_list: The list of contestants
    :param parameters: Command parameters
    :return: -
    """
    new_parameters = parameters_split(parameters)
    if len(new_parameters) != 4:
        raise ValueError("Invalid number of parameters")
    participant_nr = int(new_parameters[0])
    problem_number = new_parameters[1]
    problem_score = int(new_parameters[3])
    replace_score(contestants_list, participant_nr, problem_number, problem_score)
    print("Score replaced!")


def average_of_averages_ui(contestants_list, parameters):
    """
    The ui part of the 'avg' function
        - getting the range in which we need to calculate the average of averages
    :param contestants_list: The list with contestants
    :param parameters: The parameter given by the user, which we need to split
    :return: -
    ex: 'avg 1 to 3' -> we get the values 1 and 3 and call the function which calculates the average
    of averages between positions 1 and 3
    """
    new_parameters = parameters_split(parameters)
    if len(new_parameters) != 3:
        raise ValueError("Invalid number of parameters!")
    starting_position = int(new_parameters[0])
    ending_position = int(new_parameters[2])
    command_result = calculate_average_of_averages(contestants_list, starting_position, ending_position)
    print(command_result)


def minimum_average_ui(contestants_list, parameters):
    """
    The ui part of the 'min' function (similar process with the 'avg' function)
    :param contestants_list: The list of the scores of the contestants, stored as lists
    :param parameters: The parameter given by the user, which we split
    :return: -
    """
    new_parameters = parameters_split(parameters)
    if len(new_parameters) != 3:
        raise ValueError("Invalid number of parameters!")
    starting_position = int(new_parameters[0])
    ending_position = int(new_parameters[2])
    command_result = calculate_minimum_average(contestants_list, starting_position, ending_position)
    print(command_result)


def podium_ui(contestants_list, parameters):
    """
    The ui part of the 'top' function:
        - depending on how many parameters the user gives, we have more opdium types:
            -> podium by average, if there's only one parameter (the parameter is the nr of contestants in the top)
            -> podium by a certain score, if there are 2 parameters (nr. of contestants and the problem by which we sort)
    :param contestants_list: The list of the scores of the contestants
    :param parameters: The parameter given by the user, which we then split into parts
    :return: -
    """
    new_parameters = parameters_split(parameters)
    if len(new_parameters) == 1:
        number_of_contestants = int(new_parameters[0])
        if number_of_contestants >= len(contestants_list):
            # In case the top is bigger than the nr. of contestants, we raise an error
            raise ValueError("Podium too big!")
        podium = podium_by_average(contestants_list, number_of_contestants)
        print_list(podium)
        # creating a podium from the list sorted by average & printing it
    elif len(new_parameters) == 2:
        number_of_contestants = int(new_parameters[0])
        if number_of_contestants >= len(contestants_list):
            raise ValueError("Podium too big!")
        podium_criterion = new_parameters[1]
        # the second parameter is the problem by which we establish the podium
        podium = podium_by_criterion(contestants_list, number_of_contestants, podium_criterion)
        # creating the podium based on the required problem & printing it
        print_list(podium)
    else:
        raise ValueError("Invalid number of parameters given!")


def start_command_ui():
    contestants = []
    test_init(contestants)
    history_list = []
    # We split the commands into two categories:
    #   - That don't modify the list of contestants
    #   - That modify the list, and can be undone
    undoable_commands = {
        'add': add_scores_ui,
        'remove': remove_command_ui,
        'insert': insert_contestant_ui,
        'replace': replace_score_ui
    }
    commands = {
        'list': list_contestants_ui,
        'avg': average_of_averages_ui,
        'min': minimum_average_ui,
        'top': podium_ui
    }
    are_we_done = False
    while not are_we_done:
        command = input("command> ")
        # Splitting the command
        command_word, command_parameters = command_split(command)
        # Accessing each command word function + error handling
        if command_word in commands:
            try:
                commands[command_word](contestants, command_parameters)
            except ValueError as ve:
                print(str(ve))
        elif command_word in undoable_commands:
            # For the undoable commands, we put the current list into a so-called history list
            # The history list will be a list of lists
            # In this list we'll have all the iterations of the contestants list before making undoable changes
            try:
                contestants_tuple = tuple(contestants)  # tuples are immovable
                history_list.append(contestants_tuple)
                contestants = list(contestants)
                undoable_commands[command_word](contestants, command_parameters)
            except ValueError as ve:
                print(str(ve))
        elif command_word == 'undo':
            # When we undo, we put into our contestants list the last iteration of the list before a undoable change
            # We also pop that iteration from the history list
            if len(history_list) != 0:
                contestants.clear()
                previous_list = list(history_list[len(history_list) - 1])
                for element in previous_list:
                    contestants.append(element)
                history_list.pop()
                print("Action undone!")
            else:
                print("No action to be undone!")
        elif command_word == 'exit':
            are_we_done = True
        else:
            print("bad command")


def test_init(test_list):
    test_list.append(create_contestant([1, 2, 3]))
    test_list.append(create_contestant([4, 6, 8]))
    test_list.append(create_contestant([9, 9, 9]))
    test_list.append(create_contestant([3, 2, 3]))
    test_list.append(create_contestant([8, 10, 10]))
    test_list.append(create_contestant([5, 7, 3]))
    test_list.append(create_contestant([4, 7, 4]))
    test_list.append(create_contestant([8, 3, 8]))
    test_list.append(create_contestant([6, 2, 9]))
    test_list.append(create_contestant([2, 3, 10]))


start_command_ui()
