"""
Seminar 3
    - add exceptions
    - add unit tests
    - add command-based user interface

    features:
    -> add a student:
        add 1, Pop Ionescu, 5
    -> delete students
        delete 3, 4, 5,  6 -> deletes students with given IDs
        delete 1 - 5 -> deletes students where 1 <= id <= 5
    -> exit the program
        exit
-----------------
Write an application that manages a list of students.
Each student has a unique id (string), a name (string) and a grade (integer, 1 <= grade <= 10).
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


    - each function should do exactly one thing! => SRP single responsibility principle
    - functions should not cover more than 1 page (code smell ?)
"""

'''
    Functions that deal with students
    - lowest level of the program
    - functions talk using input parameters and return values 
'''


def create_student(student_id, student_name, student_grade):
    """
    Creates a new student with given attributes
    :param student_id: the id
    :param student_name: the name
    :param student_grade: the grade
    :return: The new student, or None if it could not be created
    """
    if student_grade < 1 or student_grade > 10:
        raise ValueError('Grade should be integer in [1, 10]')
    return {'id': student_id, 'name': student_name, 'grade': student_grade}


def get_id(student):
    return student['id']


def get_name(student):
    return student['name']


def get_grade(student):
    return student['grade']


# From this point on, we no longer refer to the student dict


def to_str(student):
    """
    Build the str representation for given student
    :param student: Given student
    :return: Its str representation
    """
    return get_id(student) + ', name: ' + get_name(student).ljust(16) + ', grade: ' + str(get_grade(student)).rjust(2)


'''
    Functions that implement functionalities
    - add students, delete, etc.
    - functions talk using input parameters and return values
'''


def find_by_id(student_list, student_id):
    """
    Search for student using id field
    :param student_list: The list of students
    :param student_id: The id we are searching for
    :return: The index of the student, or -1 if not found
    """
    for index in range(len(student_list)):
        if student_id == get_id(student_list[index]):
            return index
    return -1


def delete_student(student_list, student_id):
    """
    Function deletes student given by id
    :param student_list: list of students
    :param student_id: id of student to be deleted
    :return: -
    Raises ValueError if student_id not found
    """
    student_index = find_by_id(student_list, student_id)
    if student_index == -1:
        raise ValueError('student was not found')
    student_list.pop(student_index)



# Test function have no params and do not return anything
def test_delete_student():
    student_list = []
    test_init(student_list)
    list_len = len(student_list)

    # Test deleting a student
    delete_student(student_list, '4')
    assert find_by_id(student_list, '4') == -1 and len(student_list) == list_len - 1

    # Delete first and last students in list
    delete_student(student_list, '1')
    assert find_by_id(student_list, '1') == -1 and len(student_list) == list_len - 2

    delete_student(student_list, '8')
    assert find_by_id(student_list, '8') == -1 and len(student_list) == list_len - 3

    # Try to delete an already deleted student
    for student_id in ['1', '4', '8', '9', '10']:
        try:
            delete_student(student_list, student_id)
            assert False
        except ValueError:
            assert True


'''
    Functions for User interface
    NB! The only place where we find print/input ! 
'''


def read_student():
    """
    Read student from the console
    :return: The new student, or None if invalid input
    Raises ValueError in case of error at student creation
    """
    student_id = input('enter id: ')
    student_name = input('enter name: ')
    student_grade = int(input('enter grade: '))
    return create_student(student_id, student_name, student_grade)


def add_student_ui(student_list):
    student = read_student()
    if find_by_id(student_list, get_id(student)) == -1:
        student_list.append(student)
    else:
        raise ValueError("Duplicate student id!")


# TODO There should normally not be 2 params here
# 2nd parameter of this function is a code smell
def show_all_students_ui(student_list, param = None):
    # The same as the version below, but not as clear
    # for i in range(len(student_list)):
    #     print(to_str(student_list[i]))
    for student in student_list:
        print(to_str(student))


def print_menu():
    '''
    In order to not clutter the start function
    '''
    print('1. Add student')
    print('3. Show all students')
    print('0. Exit')


def delete_student_menu_ui(student_list):
    student_id = input('give student id to delete: ')
    delete_student(student_list, student_id)


def start_menu_ui():
    student_list = []
    test_init(student_list)

    command_dict = {'3': show_all_students_ui, '1': add_student_ui, '2': delete_student_menu_ui}
    are_we_done_yet = False

    while not are_we_done_yet:
        print_menu()
        command = input('Enter command: ')
        if command == '0':
            print('Bye!')
            are_we_done_yet = True
        elif command in command_dict:
            try:
                command_dict[command](student_list)
            except ValueError as val_error:
                print(str(val_error))
        else:
            print('Invalid command')


def add_student_command_ui(student_list, command_params):
    pass


def delete_students_command_ui(student_list, command_params):
    id_list = command_params.split(',')
    for student_id in id_list:
        delete_student(student_list, student_id.strip())


def split_command(command):
    """
    Separate user command into command word and parameters
    :param command: User command
    :return: (command word, command parameters)
    """
    tokens = command.strip().split(' ', 1)
    command_word = tokens[0].lower().strip()
    command_params = tokens[1].strip() if len(tokens) == 2 else ''

    return command_word, command_params


def test_split_command():
    for cmd in ['add 1, Pop Ionescu, 5', '  AdD 1, Pop Ionescu, 5', 'aDd      1, Pop Ionescu, 5   ', 'add 1, Pop '
                                                                                                   'Ionescu, 5      ']:
        cmd_word, cmd_params = split_command(cmd)
        assert cmd_word == 'add' and cmd_params == '1, Pop Ionescu, 5'

    # a,b = c ????
    cmd_word, cmd_params = split_command('exit')
    assert cmd_word == 'exit' and cmd_params == ''


test_split_command()


def start_command_ui():
    # 1. read user command from input
    # 2. separate command and its parameters
    # 3. call a separate function for each valid command
    student_list = []
    test_init(student_list)
    command_dict = {'delete': delete_students_command_ui, 'show': show_all_students_ui, 'add': add_student_command_ui}

    done = False
    while not done:
        command = input('command> ')
        command_word, command_params = split_command(command)

        if command_word in command_dict:
            try:
                command_dict[command_word](student_list, command_params)
            except ValueError as val_error:
                print(str(val_error))
        elif command_word == 'exit':
            done = True
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


# test_delete_student()
start_menu_ui()
# start_command_ui()
