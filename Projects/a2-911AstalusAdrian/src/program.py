"""
1. Use functions to:
    - read a complex number from the console,
    - write a complex number to the console,
    - implement each required functionality.
2. Functions communicate using input parameter(s) and the return statement (DO NOT use global variables)
    - Each complex number should be represented as a list, tuple or dictionary
    - (e.g. 1-2i as [1, -2], (1, -2) or {'real': 1, 'imag': -2} respectively).
    - To access or modify numbers, use getter and setter functions.
3. Separate input/output functions (those using print and input statements) from those performing the calculations (see program.py)
4. Provide the user with a menu-driven console-based user interface.
    - Input data should be read from the console and the results printed to the console.
    - At each step, the program must provide the user the context of the operation (do not display an empty prompt).
"""


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values
# print('Hello A2'!) -> prints aren't allowed here!


def create_complex(real, imaginary):
    complex_number = []
    complex_number.append(real)
    complex_number.append(imaginary)
    return complex_number


def get_real(number):
    return number[0]


def get_imaginary(number):
    return number[1]


def to_string(number):
    real = get_real(number)
    imaginary = get_imaginary(number)
    if real != 0 and imaginary != 0:
        if imaginary < 0:
            return str(real) + '' + str(imaginary) + 'i'
        else:
            return str(real) + '+' + str(imaginary) + 'i'
    elif real == 0 and imaginary != 0:
        return str(imaginary) + 'i'
    else:
        return str(real)


def get_real_sequence(list):
    """
    Determining the length and the last index of the longest sequence of real numbers
    :param list: The list we're about to check
    :return: A list, where the first element is the length, the second being the last index
    """
    sequence_data = []
    final_position = 0
    temporary_position = 0
    maximum_length = 0
    temporary_length = 0
    for index, number in enumerate(list):
        if get_imaginary(number) == 0:
            temporary_length += 1
            temporary_position = index
        else:
            if temporary_length >= maximum_length:
                maximum_length = temporary_length
                final_position = temporary_position
            temporary_length = 0
    if temporary_length >= maximum_length:
        maximum_length = temporary_length
        final_position = temporary_position
    sequence_data.append(maximum_length)
    sequence_data.append(final_position)
    return sequence_data


def get_distinct_sequence(list):
    sequence_data = []
    previous_element = list[0]
    maximum_length = 0
    sequence_length = 0
    final_index = 0
    index = 0
    for i in range(1, len(list)):
        number = list[i]
        if get_imaginary(number) != get_imaginary(previous_element) or get_real(number) != get_real(previous_element):
            sequence_length += 1
            index = i
        else:
            if sequence_length >= maximum_length:
                maximum_length = sequence_length
                final_index = i
            sequence_length = 0
        previous_element = number
    if sequence_length >= maximum_length:
        maximum_length = sequence_length
        final_index = i
    sequence_data.append(maximum_length)
    sequence_data.append(final_index)
    return sequence_data


# UI section
# (write all functions that have input or print statements here).
# Ideally, this section should not contain any calculations relevant to program functionalities


def read_complex():
    """
    Read a complex number
    :return: The complex number
    """
    real = int(input("Give the real part: "))
    imaginary = int(input("Give the imaginary part: "))
    return create_complex(real, imaginary)


def read_complex_ui(complex_list):
    """
    Add a list of complex numbers
    :param complex_list: The initial list of complex numbers
    :return: -
    """
    number_of_numbers = int(input("How many numbers do you want to add to the list? "))
    for i in range(number_of_numbers):
        complex_number = read_complex()
        complex_list.append(complex_number)
        print("Complex number added!")


def show_complex_ui(complex_list):
    for complex_nr in complex_list:
        print(to_string(complex_nr))


def real_sequence_ui(complex_list):
    """
    Printing the longest sequence of real numbers from the list
    :param complex_list: The list of complex numbers
    :return:
    """
    # Getting the length and the last index of the longest sequence
    sequence_data = get_real_sequence(complex_list)
    # Calculating the margins of the sequence
    start_position = sequence_data[1] - sequence_data[0] + 1
    final_position = sequence_data[1]
    # Printing the elements of the sequence
    for i in range(start_position, final_position + 1):
        print(to_string(complex_list[i]))


def distinct_sequence_ui(complex_list):
    sequence_data = get_distinct_sequence(complex_list)
    final_position = sequence_data[1]
    start_position = sequence_data[1] - sequence_data[0]
    for i in range(start_position, final_position + 1):
        print(to_string(complex_list[i]))


def print_menu():
    print("1. Read several complex numbers")
    print("2. Display the list")
    print("3. Display the first sequence (Longest sequence of real numbers)")
    print("4. Display the second sequence (Longest sequence of distinct numbers")
    print("0. Exit")


def start():
    """
    Steps:
        1. Initialised the list for complex numbers
        2. Also initialised a dictionary for the menu commands
        3. Printing the menu
        4. Reading user input and handling it
    :return:
    """
    complex_list = []
    list_init(complex_list)
    command_dictionary = {
        '1': read_complex_ui,
        '2': show_complex_ui,
        '3': real_sequence_ui,
        '4': distinct_sequence_ui,
    }
    done = False
    while not done:
        print_menu()
        command = input("Enter your command: ")
        if command == '0':
            done = True
        elif command not in command_dictionary:
            print("Invalid command")
        else:
            instruction = command_dictionary[command]
            instruction(complex_list)


def list_init(complex_list):
    """
    Adding some initial complex numbers to our list
    :param complex_list: The list used to store the complex numbers
    :return: -
    """
    complex_list.append(create_complex(-1, 3))
    complex_list.append(create_complex(7, 0))
    complex_list.append(create_complex(7, 0))
    complex_list.append(create_complex(1, 7))
    complex_list.append(create_complex(3, -7))
    complex_list.append(create_complex(9, 0))
    complex_list.append(create_complex(6, 0))
    complex_list.append(create_complex(-4, 1))


start()
