"""
Functions that implement program features. They should call each other, or other functions from the domain
"""
from src.domain.entity import get_p1_score, get_p2_score, get_p3_score, calculate_average, get_average


def list_sort_by_average(given_list):
    """
    Sorting a given list by the average score
    :param given_list: List to be sorted
    :return: The given list, sorted
    """
    new_list = sorted(given_list, key=lambda x: x[3])
    return new_list


def list_sort_by_first_score(given_list):
    """
    Sorting a given list by the first score
    :param given_list: List to be sorted
    :return: The given list, sorted
    """
    new_list = sorted(given_list, key=lambda x: x[0])
    return new_list


def list_sort_by_second_score(given_list):
    """
    Sorting a given list by the second score
    :param given_list: List to be sorted
    :return: The given list, sorted
    """
    new_list = sorted(given_list, key=lambda x: x[1])
    return new_list


def list_sort_by_third_score(given_list):
    """
    Sorting a given list by the third score
    :param given_list: List to be sorted
    :return: The given list, sorted
    """
    new_list = sorted(given_list, key=lambda x: x[2])
    return new_list


def recalculate_average(given_list, position):
    """
    Recalculating a contestant's average after changing a score
    :param given_list: The list of contestant scores
    :param position: The position of the contestant that needs the average score recalculated
    """
    scores_sum = given_list[position][0] + given_list[position][1] + given_list[position][2]
    scores_average = scores_sum / 3
    given_list[position][3] = scores_average


def create_contestant(scores):
    """
    Creating a list of a contestant's scores and the corresponding average
    :param scores: The list of scores
    :return: List of the scores and the average
    """
    if not len(scores) == 3:
        raise ValueError('Invalid number of scores!')
    for i in range(3):
        if scores[i] < 0 or scores[i] > 10:
            raise ValueError('The scores must be an integer between 1 and 10')
    score_average = calculate_average(scores)
    return [scores[0], scores[1], scores[2], score_average]


def to_string(contestant):
    """
    Transforming a contestant's data into a string for printing
    """
    return "P1:" + str(get_p1_score(contestant)).rjust(2) + ", P2:" + str(get_p2_score(contestant)).rjust(
        2) + ", P3:" + str(get_p3_score(contestant)).rjust(2) + ", average:" + str(get_average(contestant))


def parameters_split(parameters):
    """
    Splitting the parameters given by the user
    Getting each string different than ' ' typed in by the user
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
    :param given_list: The list in which we want to add a contestant
    :param parameters: Scores for P1, P2, P3 (Given as a single parameter)
    """
    if parameters == '':
        raise ValueError("You didn't give any scores!")
    scores = parameters.split()
    # Getting each individual score by splitting the parameter
    # If the number of parameters resulted after the split is different than 3, an error is raised
    if len(scores) != 3:
        raise ValueError("Too many / Not enough scores!")
    # For each score, we get rid of the additional spaces
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
    given_list.pop(contestant_position)
    insert_contestant(given_list, 0, 0, 0, contestant_position)
    # We pop all the scores (and the average) of the contestant
    # We insert on the same position a 'new' contestant with all the scores 0
    # In this way, we can undo this action using the 'undo' command


def remove_multiple_contestants(given_list, start_position, end_position):
    """
    'Removing' multiple contestants (Setting their scores to 0)
    :param given_list: The existing list in which we 'remove' the contestants
    :param start_position: The index of the contestant starting position
    :param end_position: The index of the contestant final position
    If the end_position is outside the length of the list, then we 'remove' all the contestants until the end of the list
    """
    if start_position >= len(given_list):
        raise ValueError("Starting position out of bounds!")
    if end_position >= len(given_list):
        raise ValueError("End position out of bounds!")
    for i in range(start_position, end_position + 1):
        remove_one_contestant(given_list, i)


def insert_contestant(given_list, p1_score, p2_score, p3_score, position):
    """
    Inserting a contestant into a specific position
    :param given_list: The existing list
    :param p1_score: P1 Score (The first score)
    :param p2_score: P2 Score (The second score)
    :param p3_score: P3 Score (The third score)
    :param position: The position where we insert the contestant
    We first create a contestant, then we insert the contestant at the given position
    """
    scores = [p1_score, p2_score, p3_score]
    contestant = create_contestant(scores)
    if position >= len(given_list):
        raise ValueError("Inserting position out of bounds!")
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
        raise ValueError("Participant number out of bounds!")
    # We 'extract' all three scores of the contestant
    # Depending on the problem we replace, one of these scores will be replaced with the 'score' variable
    first_score = get_p1_score(given_list[participant_number])
    second_score = get_p2_score(given_list[participant_number])
    third_score = get_p3_score(given_list[participant_number])
    if problem_number == 'p1':
        given_list.pop(participant_number)
        insert_contestant(given_list, score, second_score, third_score, participant_number)
    elif problem_number == 'p2':
        given_list.pop(participant_number)
        insert_contestant(given_list, first_score, score, third_score, participant_number)
    elif problem_number == 'p3':
        given_list.pop(participant_number)
        insert_contestant(given_list, first_score, second_score, score, participant_number)
    else:
        raise ValueError("Invalid problem number!")
    # After we replace a score, we have to recalculate the average score of the contestant
    recalculate_average(given_list, participant_number)


def calculate_average_of_averages(given_list, starting_index, ending_index):
    """
    Calculating the average of the average scores between the two given indexes
    :param given_list: The list from which we get the averages
    :param starting_index: The index of the first contestant in the range
    :param ending_index: The index of the last contestant in the range
    :return:
    """
    if starting_index >= len(given_list):
        raise ValueError("Starting position out of bounds!")
    if ending_index >= len(given_list):
        raise ValueError("Ending position out of bounds!")
    average_sum = 0
    contestants_number = ending_index - starting_index + 1
    for index in range(starting_index, ending_index + 1):
        contestant_average = get_average(given_list[index])
        average_sum = average_sum + contestant_average
    average_of_averages = average_sum / contestants_number
    return average_of_averages


def calculate_minimum_average(given_list, starting_index, ending_index):
    """
    Calculating the smallest average between two contestants
    :param given_list: The list of contestants where we find the smallest average
    :param starting_index: The index of the first contestant who's average we 'evaluate'
    :param ending_index: The index of the last contestant
    :return: The smallest average between the given indexes
    """
    if starting_index >= len(given_list):
        raise ValueError("Starting position out of bounds!")
    if ending_index >= len(given_list):
        raise ValueError("Ending position out of bounds!")
    minimum_average = get_average(given_list[starting_index])
    for index in range(starting_index + 1, ending_index + 1):
        contestant_average = get_average(given_list[index])
        if contestant_average < minimum_average:
            minimum_average = contestant_average
    return minimum_average


def podium_by_average(given_list, number_of_contestants):
    """
    Creating a podium based on the average of the contestants
    :param given_list: The list of contestants based on which we create the podium
    :param number_of_contestants: The number of contestants on the podium
    :return: The podium
    """
    podium_list = []
    sorted_list = list_sort_by_average(given_list)
    for i in range(number_of_contestants):
        podium_list.append(sorted_list[len(given_list)-i-1])
    return podium_list


def podium_by_criterion(given_list, number_of_contestants, criterion):
    """
    Establishing the podium based by a certain problem's score
    :param given_list:  The list of scores based on which we create the podium
    :param number_of_contestants: The numbers of contestants on the podium
    :param criterion: The criterion of our podium (p1, p2 or p3)
    :return: The list of the contestants on the podium
    If there are more contestants with the same score, they are placed based on the order they appear in the initial list
    """
    podium_list = []
    if criterion == 'p1':
        sorted_list = list_sort_by_first_score(given_list)
    elif criterion == 'p2':
        sorted_list = list_sort_by_second_score(given_list)
    elif criterion == 'p3':
        sorted_list = list_sort_by_third_score(given_list)
    else:
        raise ValueError("Invalid criterion!")
    for i in range(number_of_contestants):
        podium_list.append(sorted_list[len(given_list)-i-1])
    return podium_list


def remove_by_condition(given_list, operator, value):
    """
    The function that sets the scores of the contestants whose averages fulfill the condition to 0
    :param given_list: The list in which we 'remove' the contestants
    :param operator: The operator of the condition ( < | = | > )
    :param value: The value we compare the averages with
    :return: -
    """
    updated_value = value / 10 # Because we have values less than 10, we write the value as a number smaller than 10
    # ex: ab becomes a,b
    if operator == '<':
        for index in range(len(given_list)):
            if given_list[index][3] < updated_value:
                remove_one_contestant(given_list, index)
    elif operator == '=':
        for index in range(len(given_list)):
            if given_list[index][3] == updated_value:
                remove_one_contestant(given_list, index)
    elif operator == '>':
        for index in range(len(given_list)):
            if given_list[index][3] > updated_value:
                remove_one_contestant(given_list, index)


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