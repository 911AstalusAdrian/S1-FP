"""
Create a calculator program for rational numbers with the following functionalities:
    + add a rational number to the calculator
    u undo the last operation
    x exit
"""

#
# All non-UI functions go here
#

# Rational number functions
# prints or inputs are not welcome here !!
# don't CALL functions that print or input

'''
Everything we define has ONE function
 => Single responsibility principle


What's the deal with implementing this?
    - each rational number is represented by one variable (list, tuple, dict)
    - i want to be able to change the representation of rat. numbers later (?)
    - access rational numbers using functions (getters setters <=> accessors modifiers)

list representation:
    1 / 3 => [1, 3]
tuple representation:
    1 / 3 => (1, 3) -> immutable
dict representation:    
    1 / 3 => {'num': 1, 'denom': 3}    
'''
from math import gcd

def create_rational(num, denom=1):
    """
    Create a rational number with given numerator and denominator (!= 0)
    :param num: Numerator
    :param denom: Denominator
    :return: A new rational number
    """

    # return empty list
    # set denom = 1 => hides an error, program assumes user intent
    if denom == 0:
        return None

    # Simplify the fraction
    d = gcd(num, denom)
    # num, denom almost passed by value :)
    num = num // d # // means integer division
    denom = denom // d
    # return {'num': num, 'denom': denom}
    return [num, denom]


def get_num(q):
    """
    Reeturn number q's numerator
    :param q:
    :return: Numerator
    """
    # return q['num']
    return q[0]


def get_denom(q):
    # return q['denom']
    return q[1]

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
    new_num = get_num(q1)*get_denom(q2) + get_num(q2) * get_denom(q1)
    new_denom = get_denom(q1) * get_denom(q2)
    return create_rational(new_num, new_denom)


# TODO Next week we write a test function for this stuff
q1 = create_rational(50,100)
q2 = create_rational(50,100)
q3 = create_rational(-50,100)


res = add(q1,q2)
# print(to_str(res)) # 1/1
res = add(q2,q3)
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


#
# UI functions are here (everything with print / input, or calls a function with print / input)
#
def read_rational():
    """
    Read rational number from console
    :return: New rational number
    """
    num = input('Numerator: ')
    denom = input('Denominator: ')
    # TODO Some error handling is required ... try ... except ...
    return create_rational(int(num), int(denom))


def add_calculator_ui(calc):
    value = read_rational()
    add_calc_number(calc, value)


def undo_calculator_ui():
    # TODO How do I know I have an op to undo?
    # If no operation is available, we cannot undo -> tell the user
    # History of calculator values
    print('undo')
    pass


def print_menu():
    print('\n')
    print('\t+ add a rational number to the calculator')
    print('\tu undo the last operation')
    print('\tx exit')


def start():
    """
    Handle the main menu

    :return: Returns once the program is finished
    """
    calc = create_calculator()

    done = False
    # while True:
    while not done:
        print_menu()
        print('Total= ' + to_str(get_calc_value(calc)))
        option = input('Enter operation: ')

        # V1 handling user input
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


# You need to actually call the function
start()

'''
Quick recap
    -> UI all print/input goes here, nothing else
    -> calculator
        - we have a representation of a calculator
        - we encapsulate the representation using functions
    
    -> rational 
        - we have a representation of a rational number
        - we encapsulate the representation using functions

UI <-> calculator <-> rational <-> UI <-> calculator
    => spaghetti code 


UI -> calculator -> rational
      
UI can call calculator, rational functions
calculator can call rational functions
rational only calls rational functions
'''
