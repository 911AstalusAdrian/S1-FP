"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


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
