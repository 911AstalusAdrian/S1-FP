#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)


def get_p1_score(contestant):
    """
    Returns the first score of a contestant
    :param contestant: The list of a contestant's scores
    :return: Score for P1
    """
    return contestant[0]


def get_p2_score(contestant):
    """
    Returns the second score of a contestant
    :param contestant: The list of a contestant's scores
    :return: Score for P2
    """
    return contestant[1]


def get_p3_score(contestant):
    """
    Returns the third score of a contestant
    :param contestant: The list of a contestant's scores
    :return: Score for P3
    """
    return contestant[2]


def get_average(contestant):
    """
    Returns the average score of a contestant
    :param contestant: The list of a contestant's scores
    :return: The average score
    """
    return contestant[3]


def calculate_average(scores):
    """
    Calculating the average of a contestant's scores
    :param scores:
    :return: The average score (float)
    """
    scores_sum = scores[0] + scores[1] + scores[2]
    return scores_sum / 3


def list_sort(given_list):
    """
    Sorting a given list by the average score
    :param given_list: List to be sorted
    :return: The given list, sorted
    """
    new_list = sorted(given_list, key=lambda x: x[3])
    return new_list


def recalculate_average(given_list, position):
    """
    Recalculating a contestant's average after changing a score
    :param given_list: The list of contestant scores
    :param position: The position of the contestant that needs the average score recalculated
    """
    scores_sum = given_list[position][0] + given_list[position][1] + given_list[position][2]
    scores_average = scores_sum/3
    given_list[position][3] = scores_average

# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values


def create_contestant(scores):
    """
    Creating a list of a contestant's scores and the corresponding average
    :param scores: The list of scores
    :return: List of the scores and the average
    """
    if not len(scores) == 3:
        raise ValueError('Invalid number of scores!')
    for i in range(3):
        if scores[i] < 1 or scores[i] > 10:
            raise ValueError('The scores must be an integer between 1 and 10')
    score_average = calculate_average(scores)
    return [scores[0], scores[1], scores[2], score_average]


def to_string(contestant):
    """
    Transforming a contestant's data into a string for printing
    """
    return "P1:" + str(get_p1_score(contestant)).rjust(2) + ", P2:" + str(get_p2_score(contestant)).rjust(2) + ", P3:" + str(get_p3_score(contestant)).rjust(2) + ", average:" + str(get_average(contestant))


def parameters_split(parameters):
    """
    Splitting the parameters given by the user
    :param parameters: The user input
    :return: A list of each 'word' of the parameter
    """
    split_parameters = parameters.split()
    for parameter in split_parameters:
        parameter.strip()
    return split_parameters


def command_split(command):
    """
    Dividing the user input into a command and parameters
    :param command: user input
    :return: command word and parameters
    """
    user_input = command.strip().split(' ', 1)
    user_input[0] = user_input[0].strip().lower()
    return user_input[0], '' if len(user_input) == 1 else user_input[1].strip().lower()


def list_with_condition(given_list, parameters):
    """
    Creating a list (from the existent one) that has a certain property
    :param given_list: The initial list
    :param parameters: The necessary condition
    :return: A new list
    """
    new_list = []
    new_parameters = parameters_split(parameters)
    compared_number = float(new_parameters[1])
    if compared_number < 1 or compared_number > 10:
        raise ValueError("The number you want to compare with is not valid!")
    if new_parameters[0] == '<':
        for element in given_list:
            if element[3] < compared_number:
                new_list.append(element)
    elif new_parameters[0] == '=':
        for element in given_list:
            if element[3] == compared_number:
                new_list.append(element)
    elif new_parameters[0] == '>':
        for element in given_list:
            if element[3] > compared_number:
                new_list.append(element)
    else:
        raise ValueError("Wrong operator!")
    return new_list


def add_scores(given_list, parameters):
    """
    Creating and adding a contestant to the existing list
    :param given_list: The existing list
    :param parameters: Scores for P1, P2, P3
    """
    if parameters == '':
        raise ValueError("You didn't give any scores!")
    scores = parameters.split()
    if len(scores) != 3:
        raise ValueError("Too many / Not enough scores!")
    score_1 = int(scores[0].strip())
    score_2 = int(scores[1].strip())
    score_3 = int(scores[2].strip())
    given_list.append(create_contestant([score_1, score_2, score_3]))


def remove_one_contestant(given_list, contestant_position):
    """
    Setting a specific contestant's scores to 0
    :param given_list: The existing list
    :param contestant_position: The position of the contestant in the list
    """
    if contestant_position >= len(given_list):
        raise ValueError("Invalid contestant position!")
    for i in range(4):
        given_list[contestant_position][i] = 0


def remove_multiple_contestants(given_list, start_position, end_position):
    """
    'Removing' multiple contestants
    :param given_list: The existing list
    :param start_position: The index of the contestant starting position
    :param end_position: The index of the contestant final position
    If the end_position is outside the length of the list, then we 'remove' all the contestants until the end of the list
    """
    if start_position >= len(given_list):
        raise ValueError("Invalid starting position!")
    for i in range(start_position, end_position+1):
        remove_one_contestant(given_list, i)


def insert_contestant(given_list, p1_score, p2_score, p3_score, position):
    """
    Inserting a contestant into a specific position
    :param given_list: The existing list
    :param p1_score: P1 Score
    :param p2_score: P2 Score
    :param p3_score: P3 Score
    :param position: The position where we insert the contestant
    We first create a contestant, then we insert the contestant at the given position
    """
    scores = [p1_score, p2_score, p3_score]
    contestant = create_contestant(scores)
    if position >= len(given_list):
        raise ValueError("Inserting position not found!")
    given_list.insert(position, contestant)


def replace_score(given_list, participant_number, problem_number, score):
    """
    Replacing the score of a problem at an indicated contestant
    :param given_list: The existing list
    :param participant_number: The index of the contestant
    :param problem_number: The problem's number (P1, P2 or P3)
    :param score: The score to be replaced with
    """
    if participant_number >= len(given_list):
        raise ValueError("Invalid participant number!")

    if problem_number == 'p1':
        given_list[participant_number][0] = score
    elif problem_number == 'p2':
        given_list[participant_number][1] = score
    elif problem_number == 'p3':
        given_list[participant_number][2] = score
    else:
        raise ValueError("Invalid problem number!")
    recalculate_average(given_list, participant_number)


# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities
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
        sorted_list = list_sort(contestants_list)  # Creating the sorted list
        print_list(sorted_list)  # Printing the sorted list
    elif parameters[0] in operators:
        conditions_list = list_with_condition(contestants_list, parameters)  # Creating the list depending on the condition
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
    new_params = parameters.split()
    if len(new_params) == 1:
        position = int(new_params[0])
        remove_one_contestant(contestants_list, position)
    elif len(new_params) == 3:
        start_position = int(new_params[0])
        end_position = int(new_params[2])
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


def start_command_ui():
    contestants = []
    test_init(contestants)
    commands = {
        'add': add_scores_ui,
        'list': list_contestants_ui,
        'remove': remove_command_ui,
        'insert': insert_contestant_ui,
        'replace': replace_score_ui
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
        elif 'exit' == command_word:
            are_we_done = True
        else:
            print("bad command")


# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert


def test_command_split():
    command = '   adD  5, 6, 7  '
    command_word, command_parameters = command_split(command)
    assert command_word == "add"
    assert command_parameters == "5, 6, 7"

    command = '  lIsT'
    command_word, command_parameters = command_split(command)
    assert command_word == "list"
    assert command_parameters == ""

    command = 'iNseRt 10 10 9  At 5'
    command_word, command_parameters = command_split(command)
    assert command_word == "insert"
    assert command_parameters == "10 10 9  at 5"


test_command_split()


def remove_one_contestant_test():
    test_list = [create_contestant([1, 2, 3])]
    remove_one_contestant(test_list, 0)
    assert test_list[0] == [0, 0, 0, 0]


remove_one_contestant_test()


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
