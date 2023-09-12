"""
Lecture 2
    Create a calculator program for rational numbers with the following functionalities:
        + add a rational number to the calculator
        u undo the last operation (not implemented... yet!)
        x exit

Lecture 3
    Switch to using Exceptions to treat errors
    Create test function for undo
    Implement undo functionality
    Start a command-based user interface implementation
"""

#
# All non-UI functions go here
#

# Rational number functions
# prints or inputs are not welcome here !!
# don't CALL functions that print or input

'''
 ???    
'''
from math import gcd


def create_rational(num, denom=1):
    """
    Create a rational number with given numerator and denominator (!= 0)
    :param num: Numerator
    :param denom: Denominator
    :return: A new rational number
    Raise ValueError if denom == 0
    """
    # return empty list
    # set denom = 1 => hides an error, program assumes user intent
    # return an error value => C-way of doing things => implicit and not explicit
    #    - only works if someone checks the return value
    if denom == 0:
        # ValueError is an Exception type
        # raise -> returns from current function
        # This function is the expert in its own workings

        # Single Responsibility Principle
        # my job is to signal that an error occured
        # my job is NOT to handle it
        raise ValueError('Denominator cannot be 0!')
        # return None

    # Simplify the fraction
    d = gcd(num, denom)
    num = num // d  # // means integer division
    denom = denom // d
    return {'num': num, 'denom': denom}
    # return [num, denom]


def get_num(q):
    """
    Reeturn number q's numerator
    :param q:
    :return: Numerator
    """
    return q['num']
    # return q[0]


def get_denom(q):
    return q['denom']
    # return q[1]


# Make the rational number responsible for its own representation
# __str__ -> works in a class
def to_str(q):
    """
    Return the string representing q
    :param q: The rational number
    :return: Its str representation
    """
    return str(get_num(q)) + '/' + str(get_denom(q))


def add(q1, q2):
    """
    Add two rational numbers
    :param q1: First operand
    :param q2: Second operand
    :return: The rational number representing their sum
    """
    new_num = get_num(q1) * get_denom(q2) + get_num(q2) * get_denom(q1)
    new_denom = get_denom(q1) * get_denom(q2)
    return create_rational(new_num, new_denom)


'''
    Test functions 101:
        - take no params
        - return nothing
        - can be called in any order (if nore than 1)
        - finish quietly if everything is in order
            - complain loudly otherwise => use assert
'''

#res = add(q1, q2)
# print(to_str(res)) # 1/1
#res = add(q2, q3)


# print(to_str(res)) # 0/1


# a/b + c/d = a*d + b*c / b*d
# 50/100 + 50/100 = 1 (instead of 100/100)

# Calculator functions are here
# What is exposed by the rational number type?
# 1. create_rational
# 2. add
# 3. to_str

# What is the state of the calculator?
#   - current value (we start with default 0/1)
#   - history of calculator values
def create_calculator():
    """
    Create a calculator instance
    :return: New calc instance
    """
    return {'value': create_rational(0), 'history': []}


def add_calc_number(calc, q):
    """
    Adds q to the calculator value
    :param calc: Current calculator
    :param q: Added value
    :return: -
    """
    # Record current calc value for undo purposes
    current_value = get_calc_value(calc)
    history = get_calc_history(calc)
    history.append(current_value)

    # Update calc with new value
    new_value = add(get_calc_value(calc), q)
    set_calc_value(calc, new_value)


def set_calc_value(calculator, q):
    """

    :param calculator:
    :param q:
    :return:
    """
    calculator['value'] = q


def get_calc_value(calculator):
    """
    Return current calc value
    :param calculator: The calculator
    :return: Current calc value
    """
    return calculator['value']


def get_calc_history(calculator):
    """
    Return the history of calc values
    :param calculator: current calc
    :return: A list of calc values
    """
    return calculator['history']


def undo_calc(calculator):
    """
    Undo the last operation on this calculator
    :param calculator: Current calculator
    :return: -
    Raises ValueError if there is no operation to undo
    """
    history = get_calc_history(calculator)
    # Case when there are no more undos
    if len(history) == 0:
        raise ValueError('No more undos!')
    # We have at least one undo available
    new_value = history.pop()
    set_calc_value(calculator, new_value)


#
# UI functions are here (everything with print / input, or calls a function with print / input)
#
def read_rational():
    """
    Read rational number from console
    :return: New rational number
    Raises ValueError in case of bad user input
    """
    # 1. call input
    # 2. call int on the return of input
    # 3. create variable 'num' and assign it the type and value of int()
    num = int(input('Numerator: '))
    denom = int(input('Denominator: '))
    return create_rational(num, denom)


def add_calculator_ui(calc):
    value = read_rational()
    add_calc_number(calc, value)


def undo_calculator_ui(calculator):
    undo_calc(calculator)


def add_command_ui(calculator, params):
    """
    Handle all forms of the add command
    :param params: command parameters
    :param calculator: Current calc
    :return: -
    """
    # 1/2,3/4,5/6
    tokens = params.split(',')
    for token in tokens:
        # each token represents a rational number
        token = token.strip()
        num_denom_str = token.split('/')
        # TODO More specific error msg when converting to int
        q = create_rational(int(num_denom_str[0]), int(num_denom_str[1]))
        # add number to calc
        add_calc_number(calculator, q)


def undo_command_ui(calculator, step_count):
    try:
        step_count = int(step_count)
    except ValueError as ve:
        print ('<step_count> not an integer')
        return
    while step_count > 0:
        undo_calc(calculator)
        step_count -= 1


def print_menu():
    print('\n')
    print('\t+ add a rational number to the calculator')
    print('\tu undo the last operation')
    print('\tx exit')


def start_menu_ui():
    """
    Handle the main menu

    :return: Returns once the program is finished
    """
    calc = create_calculator()

    done = False

    while not done:
        print_menu()
        print('Total= ' + to_str(get_calc_value(calc)))
        option = input('Enter operation: ')

        try:
            if option == '+':
                add_calculator_ui(calc)
            elif option == 'u':
                undo_calculator_ui(calc)
            elif option == 'x':
                print('Bye bye!')
                # return
                done = True
            else:
                print('Bad command!')
        except ValueError as ve:
            print('An error occurred! ' + str(ve))


'''
    command for calculator:
    > add 1/2, 1/3, 1/4 # we can add several numbers in one command
    > undo <steps> # how many steps we want to undo at the same time
    > exit    
'''
def split_command(command):
    '''
    for add 1/2, 1/3, 1/4
    command = add
    params = 1/2, 1/3, 1/4
    '''
    # index = command.find(' ')
    tokens = command.split(' ', 1)
    return tokens[0].strip().lower(), tokens[1].strip() if len(tokens) == 2 else ''


def start_command_ui():
    calc = create_calculator()
    done = False

    command_dict = {'add': add_command_ui, 'undo': undo_command_ui}

    while not done:
        try:
            print('total='+to_str(get_calc_value(calc)))
            # Read user command
            command = input('command >').strip()
            # Which command is requested?
            command_word, command_params = split_command(command)
            if 'exit' == command_word:
                done = True
            elif command_word in command_dict:
                # command_dict -> dict variable
                # command_dict[command_word] -> function reference variable
                # command_dict[command_word]() -> function call
                # () -> function call operator
                command_dict[command_word](calc, command_params)
            else:
                print('bad command')
        except ValueError as ve:
            print(str(ve))

# You need to actually call the function

# UI -> functions -> rational numbers

# 1. Menu-driven UI
# start_menu_ui()
# 2. Command based UI
start_command_ui()
# 3. Graphical User interface
# 4. web application


#
# My test functions go here
#

'''
    assert <true_expression> => does nothing
    assert <false_expression> => raise AssertionError
        - this means that a test failed
        - this means that a precondition was violated
        - you should NOT catch AssertionError
'''


def test_create_rational():
    q = create_rational(50, 100)
    assert get_num(q) == 1 and get_denom(q) == 2
    q = create_rational(3, 4)
    assert get_num(q) == 3 and get_denom(q) == 4

    # How do i test a ValueError was raised?
    try:
        q = create_rational(1, 0)
        # The line above is supposed to raise an Exception =>
        # The line below should not run
        assert False
    except ValueError as ve:
        assert True


def test_undo_calc():
    # We first set up the test cases
    c = create_calculator()

    # Try to undo with no operations available
    try:
        undo_calc(c)
        # Function should raise exception, so line below does not run
        assert False
    except ValueError:
        # the function was supposed to raise an exception
        assert True

    # Undo 1 operation
    add_calc_number(c, create_rational(1, 3))
    undo_calc(c)
    calc_value = get_calc_value(c)
    assert get_num(calc_value) == 0 and get_denom(calc_value) == 1

    # Undo several operations
    add_calc_number(c, create_rational(1, 2))
    add_calc_number(c, create_rational(1, 3))
    add_calc_number(c, create_rational(1, 4))

    undo_calc(c)
    calc_value = get_calc_value(c)
    assert get_num(calc_value) == 5 and get_denom(calc_value) == 6

    undo_calc(c)
    calc_value = get_calc_value(c)
    assert get_num(calc_value) == 1 and get_denom(calc_value) == 2

    undo_calc(c)
    calc_value = get_calc_value(c)
    assert get_num(calc_value) == 0 and get_denom(calc_value) == 1

    # No more undos
    try:
        undo_calc(c)
        # Function should raise exception, so line below does not run
        assert False
    except ValueError:
        # the function was supposed to raise an exception
        assert True


# test_undo_calc()
# test_create_rational()
