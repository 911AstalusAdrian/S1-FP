"""
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

    - how we represent each student?
    - how we divide program into functions?
    - how functions talk to each other
    - function specification
    - simple feature-driven development
        -> pick a feature and implement it !
    - each function does only one thing!



    - no global variables!
    - how do we represent 1 student as a str?
    - how do we print out a list of students?
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
        return None
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


'''
    Functions for user interface 
        - ALL print/input statements are here
'''


def read_student():
    """
    Read a new student
    :return: The new student, or None if student could not be created
    """
    student_id = input('Enter id: ')
    name = input('Enter name: ')
    # int(...) might crash -> deal with it next week!
    grade = int(input('Enter grade: '))
    return create_student(student_id, name, grade)


def add_student_ui(student_list):
    """
    Add a new student to our list
    :param student_list: The list of students
    :return: -
    """
    student = read_student()
    if student is None:
        print('Invalid student params!')
        return
    # Check unique ID
    if find_by_id(student_list, get_id(student)) > -1:
        print('Duplicate student id!')
        return
    student_list.append(student)


def show_students_ui(student_list):
    for student in student_list:
        print(to_str(student))


def print_menu():
    print('1. Add student')
    print('3. Show all students')
    print('0. Exit')


def start():
    """
    Steps for my UI:
        1. print menu
        2. read user input
        3. handle it!
    """
    student_list = []
    test_init(student_list)

    command_dict = {'3': show_students_ui, '1': add_student_ui}
    are_we_done_yet = False
    while not are_we_done_yet:
        print_menu()
        command = input('Enter command: ')
        # V1
        # if ... elif ... elif ... else
        #
        # We do V2 - dict-based commands
        if command == '0':
            are_we_done_yet = True
        elif command not in command_dict:
            print('Invalid command!')
        else:
            # assume command == '3'
            # show_students_ui -> variable storing a function
            # command_dict[command] = show_students_ui
            # command_dict[command]() = show_students_ui()
            # () -> function call operator
            x = command_dict[command]
            x(student_list)


# forward function declaration in C ?
def test_init(student_list):
    student_list.append(create_student('1', "Pop Ioana", 10))
    student_list.append(create_student('2', "Man Ionel", 5))
    student_list.append(create_student('3', "Marian Sofia", 9))
    student_list.append(create_student('4', "Boca Mihaela", 6))
    student_list.append(create_student('5', "Popa Adela", 5))
    student_list.append(create_student('6', "Costin Daniel", 7))
    student_list.append(create_student('7', "Zaharia Vasile", 8))
    student_list.append(create_student('8', "Mihnea Loredana", 9))


start()

'''
    1. create a new entry in command dict + new entry in print_menu
    2. create a new ui function (read student id)
    3. create a function to delete the student from the list
'''
