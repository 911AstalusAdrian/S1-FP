"""
    1. Add Exceptions where it makes sense
    2. Turn into command-line app
    3. Add some unit tests

    -> We do add student together
    add 999, Popa Marian, 5

    requirements:
        - unique ID (int)
        - name length > 3
        - grade is int between 1 and 10


    -> You try to implement delete by yourselves
    delete 2,3,4,5 # deletes students having one of the given id's
    delete 2 - 6  # deletes students where 2 <= id <= 6


Write an application that manages a list of students.
Each student has a unique id (int), a name (string) and a grade (integer).
The application will provide the following features:

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
Functions that work with student(s)
'''


def create_student(student_id, student_name, student_grade):
    """
    Create student with given parameters
    :param student_id: ID of the student (non-empty)
    :param student_name:  Name (non-empty)
    :param student_grade: 1 <= value (int) <= 10 (non-empty)
    :return: Created student,
    Raise ValueError if student cannot be created with given params
    """
    # print(type(student_id)) -> what's my type?
    if len(student_id) == 0 or len(student_name) == 0 or student_grade < 1 or student_grade > 10:
        '''
        raise Exception -> next week :)
        print - not allowed
        return empty student -> not a good idea 
        '''
        # return None is implicit
        # return None
        # raise Exception is explicit -> PEP-20
        raise ValueError('Cannot create student using given arguments')
    return {'id': student_id, 'name': student_name, 'grade': student_grade}


# Straightforward getters/setters don't need spec
def get_id(student):
    return student['id']


def get_name(student):
    return student['name']


def get_grade(student):
    return student['grade']


def to_str(student):
    """
    Build the str representation for a student
    :param student: The student
    :return: Its str representation
    """
    return get_id(student) + ' name: ' + str(get_name(student)).ljust(16) + ' grade: ' + str(get_grade(student)).rjust(2)


'''
functions that implement required features
(this part knows about students)
'''

'''
    Idea for easy implementation of student deletion
        1. Change find_by_id so that it return:
            -> position of student in list (if found)
            -> -1, if not found
            NB! Check for the return value and beware student_list[-1], which
            is valid in Python but not in C/++/Java/...
'''


def add_student(student_list, student):
    """
    Add student to the list
    :param student_list: list of students
    :param student: The new student
    :return: -
    Raise ValueError in case of duplicate student ID
    """
    if find_by_id(student_list, get_id(student)):
        raise ValueError('Duplicate student id')
    student_list.append(student)


def find_by_id(student_list,student_id):
    '''
    Find the student with the given id
    :param student_list: list of students
    :param student_id: The id we are sarching for
    :return: The student with given id, or None if student does not exist
    '''
    for student in student_list:
        if student_id == get_id(student):
            return student
    # functions return None by default
    # explicit > implicit (one of the Python mantras https://www.python.org/dev/peps/pep-0020/)
    return None


'''
    Menu-driven user interface 
'''


def read_student():
    '''
    There could be 2 exceptions:
        1. Failure to convert to int
        2. Raised from create_student
    '''
    student = None
    while not student:
        student_id = input('Enter id: ')
        student_name = input('Enter name: ')
        '''
        1. Crash if console input cannot be converted to int
        2. Next week we learn what to do about it 
            => deal with it!
        '''
        student_grade = int(input('Enter grade: '))
        student = create_student(student_id, student_name, student_grade)
        # check if error
        # if student is None:
        #     print('Invalid student params!')
    return student


def print_menu():
    print('1. Add student')
    print('3. Show all students')
    print('0. Exit')


def add_student_menu_ui(student_list):
    student = read_student()
    add_student(student_list, student)


def show_all_students_ui(student_list, params = None):
    for student in student_list:
        print(to_str(student))


def start_menu_ui():
    '''
    1. print menu
    2. read user input
    3. call a function that fulfills that requirement
    '''
    # List of students in my program
    student_list = []
    # These students help me test my program
    test_init(student_list)
    command_dict = {'3': show_all_students_ui, '1': add_student_menu_ui}
    done = False
    while not done:
        try:
            print_menu()
            command = input("Enter command: ")
            if command in command_dict:
                # NB! show_all_students -> variable that references a function
                # show_all_students() -> function call
                # () -> function call operator
                command_dict[command](student_list)
            elif command == '0':
                print('Bye bye!')
                done = True
            else:
                print('Invalid command!')
        except ValueError as ve:
            print(str(ve))


'''
    Command-driven user interface 
'''


def split_command(command):
    """
    Split command string into command word and parameters
    :return: (command_word, command_params)
    """
    # add 999, Popa Marian, 5
    # command_word = add
    # command_params = 999, Popa Marian, 5
    command = command.strip()
    # separate the first appearance of ' '
    # command.split( ... ), or command.find(' ')
    tokens = command.split(' ', 1)
    command_word = tokens[0].strip().lower()
    command_params = tokens[1].strip() if len(tokens) == 2 else ''

    return command_word, command_params


def add_student_command_ui(student_list, cmd_params):
    # '999, Popa Marian, 5'
    tokens = cmd_params.split(',')
    if len(tokens) != 3:
        raise ValueError('Invalid parameter count')

    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()

    student = create_student(tokens[0], tokens[1], int(tokens[2]))
    add_student(student_list, student)


def delete_student_command_ui(student_list, cmd_params):
    pass


def start_command_ui():
    # List of students in my program
    student_list = []
    # These students help me test my program
    test_init(student_list)
    command_dict = {'list': show_all_students_ui, 'add': add_student_command_ui, 'delete': delete_student_command_ui}
    done = False
    while not done:
        command = input('command> ')
        try:
            # 1. split into command_word and command_params
            cmd_word, cmd_params = split_command(command)
            # 2. have separate functions for each command word
            if cmd_word in command_dict:
                command_dict[cmd_word](student_list, cmd_params)
            elif cmd_word == 'exit':
                done = True
            else:
                print('bad command')
        except ValueError as ve:
            print(str(ve))


def test_init(student_list):
    student_list.append(create_student('1', "Pop Ioana", 10))
    student_list.append(create_student('2', "Man Ionel", 5))
    student_list.append(create_student('3', "Marian Sofia", 9))
    student_list.append(create_student('4', "Boca Mihaela", 6))
    student_list.append(create_student('5', "Popa Adela", 5))
    student_list.append(create_student('6', "Costin Daniel", 7))
    student_list.append(create_student('7', "Zaharia Vasile", 8))
    student_list.append(create_student('8', "Mihnea Loredana", 9))


#start_menu_ui()


'''
    Here be tests!
'''


def test_add_student():
    student_list = []
    test_init(student_list)
    # Test that we can add a valid student
    s = create_student('11', 'Popa Marian', 8)
    add_student(student_list, s)
    student = find_by_id(student_list, 11)
    assert s == student

    # Try to add the same student again
    try:
        add_student(student_list, s)
        assert False  # this means the exception was NOT raised
    except ValueError:
        assert True


# test_add_student()
start_command_ui()


'''
    How to implement -> delete 2,3,4,5 # deletes students having one of the given id's
    1. add command in command_dict
    2. implement function delete_student_command_ui
    3. implement function delete_student -> deletes one student from list 
'''
