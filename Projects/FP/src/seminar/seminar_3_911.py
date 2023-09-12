"""
Seminar 3
    -> add Exceptions
    -> add unit tests
    -> implement command-based user interface
        add 100, Pop Marian, 5
        delete 2,3, 4, 6 # delete students having one of those id's
        delete 2 - 10 # delete all students where 2 <= id <= 10
        list # display the list of students
        exit

Write an application that manages a list of students.
Each student has a unique id (string), a name (string) and a grade (integer, between 1 and 10).
The application will have a menu-driven user interface and will provide the following features:

    1. Add a student
        - adds the student with the given id, name and grade to the list.
        - error if giving existing id, the name or grade fields not given or empty

    2. Delete a student
        - deletes the student with the given id from the list
        - error if non-existing id given

    3. Show all students
        - shows all students
        (bonus: sort students in descending order of name or grade)

    4. Show students whose grade is > than given one
        (bonus: sort students by descending order of grade)

    5. exit
        - exit the program
"""


'''
    Functions that deal with a student
        - talks using params and return values
'''


def create_student(student_id, student_name, student_grade):
    """
    Create a student with given attributes
    :param student_id: The id
    :param student_name: Student name
    :param student_grade: Student's grade, int between 1 and 10
    :return: The new student, or None if could not be created
    """
    if student_grade < 1 or student_grade > 10:
        # return None -> implicit
        # raise ValueError -> explicit
        # PEP-20 -> Explicit is better than implicit
        raise ValueError('student grade must be int in [1, 10]')

    # TODO Proper validation is done in a validate() functions or class
    student_name_aux = str(student_name).replace(' ', '')
    if not str(student_name_aux).isalpha():
        raise ValueError('invalid student name')
    return {'id': student_id, 'name': student_name, 'grade': student_grade}


def get_id(student):
    '''
    Return student ID
    :param student: -
    :return: -
    '''
    return student['id']


def get_name(student):
    return student['name']


def get_grade(student):
    return student['grade']


# We represent as a str, as we are not allowed to print!
def to_str(student):
    # TODO Best practice says .xjust should be in printing the list
    return str(get_id(student)).rjust(3) + ', name: ' + str(get_name(student)).ljust(16) + ', grade: '+str(get_grade(student)).rjust(2)


'''
    Functions that implement program features
        - talks using params and return values
        add_student, delete_student, ...
'''


def find_by_id(student_list, student_id):
    """
    Find the student with the given id
    :param student_list: List of students
    :param student_id: this is the id (str) we are searching for
    :return: The index of the student, -1 if student not found
    """
    for index in range(len(student_list)):
        if student_id == get_id(student_list[index]):
            return index
    # NB! list[-1] is valid in Python and points to the last element
    return -1


def add_student(student_list, student):
    if find_by_id(student_list, get_id(student)) > -1:
        # We signal that there's an error
        # Handling it is not our responsibility
        raise ValueError('Duplicate student id!')
    student_list.append(student)


def test_add_student():
    # TODO Implement test function (done with 912)
    pass


'''
    Menu-based user interface functions 
        - ALL print/input statements are here
'''


def read_student():
    """
    Read a new student
    :return: The new student, or None if student could not be created
    Raises ValueError if student could not be read
    """
    student_id = input('Enter id: ')
    name = input('Enter name: ')
    # int(...) might crash -> deal with it next week!
    grade = int(input('Enter grade: '))
    return create_student(student_id, name, grade)


def add_student_menu_ui(student_list):
    """
    Add a new student to our list
    :param student_list: The list of students
    :return: -
    Raises ValueError on error
    """
    # 1. Exception could be raised in read_student() -> create_student()
    student = read_student()
    add_student(student_list, student)


def show_students_ui(student_list):
    for student in student_list:
        print(to_str(student))


def print_menu():
    print('1. Add student')
    print('3. Show all students')
    print('0. Exit')


def start_menu_ui():
    """
    Steps for my UI:
        1. print menu
        2. read user input
        3. handle it!
    """
    student_list = []
    test_init(student_list)

    command_dict = {'3': show_students_ui, '1': add_student_menu_ui}
    are_we_done_yet = False
    while not are_we_done_yet:
        print_menu()
        command = input('Enter command: ')
        if command == '0':
            are_we_done_yet = True
        elif command not in command_dict:
            print('Invalid command!')
        else:
            # The try except below handles all expected error situations
            # The try block does not know about all function that raise exceptions
            try:
                command_dict[command](student_list)
            except ValueError as exception_obj:
                print(str(exception_obj))


'''
    Command-based user interface functions 
        - ALL print/input statements are here
'''


def show_students_command_ui(*args):
    for student in args[0]:
        print(to_str(student))


def split_command(command):
    """
    Divide user command into command word and command params
    :param command: user command
    :return: command word, params
    """
    # add 100, Pop Marian, 5
    # command_word='add'
    # command_params='100, Pop Marian, 5'
    tokens = command.strip().split(' ', 1)
    # convert command word to lowercase
    tokens[0] = tokens[0].strip().lower()
    # Always returns a double-tuple
    return tokens[0], '' if len(tokens) == 1 else tokens[1].strip()


def test_split_command():
    cmd = '    aDd 100, Pop Marian    , 5 '
    cmd_word, cmd_params = split_command(cmd)
    assert cmd_word == 'add'
    assert cmd_params == '100, Pop Marian    , 5'

    cmd = 'eXit'
    cmd_word, cmd_params = split_command(cmd)
    assert cmd_word == 'exit'
    assert cmd_params == ''  # blank str for command with no params


test_split_command()


def add_student_command_ui(student_list, parameters):
    # 1. Process parameters
    tokens = parameters.split(',')
    if len(tokens) != 3:
        raise ValueError('invalid param count to create student')

    student_id = tokens[0].strip()
    student_name = tokens[1].strip()
    student_grade = int(tokens[2].strip())  # ValueError?
    # 2. Create student entity
    student = create_student(student_id, student_name, student_grade)

    # 3. Check for duplicate ID!
    # 4. Add to list
    add_student(student_list, student)


def delete_student_command_ui(student_list, parameters):
    pass


def start_command_ui():
    student_list = []
    test_init(student_list)

    command_dict = {'list': show_students_command_ui, 'delete': delete_student_command_ui, 'add': add_student_command_ui}
    are_we_done_yet = False
    while not are_we_done_yet:
        # add 100, Pop Marian, 5
        command = input("command> ")
        # 1. Divide user input into command word and command parameters
        command_word, command_params = split_command(command)

        # 2. Create a separate function for each command word
        if command_word in command_dict:
            # () -> function call operator
            try:
                command_dict[command_word](student_list, command_params)
            except ValueError as ve:
                print(str(ve))
        elif 'exit' == command_word:
            are_we_done_yet = True
        else:
            print('bad command')


def test_init(student_list):
    student_list.append(create_student('1', "Pop Ioana", 10))
    student_list.append(create_student('2', "Man Ionel", 5))
    student_list.append(create_student('3', "Marian Sofia", 9))
    student_list.append(create_student('4', "Boca Mihaela", 6))
    student_list.append(create_student('5', "Popa Adela", 5))
    student_list.append(create_student('6', "Costin Daniel", 7))
    student_list.append(create_student('7', "Zaharia Vasile", 8))
    student_list.append(create_student('8', "Mihnea Loredana", 9))


start_menu_ui()
# start_command_ui()