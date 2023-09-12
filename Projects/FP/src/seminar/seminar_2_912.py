"""
Write an application that manages a list of students.
Each student has a unique id (string), a name (string) and a grade (integer).
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

    - simple feature-driven development
        -> pick a feature and implement it !
    - no global variables!
    - how do we represent 1 student as a str?
    - how do we print out a list of students?
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
    """
    # print(type(student_id)) -> what's my type?
    if len(student_id) == 0 or len(student_name) == 0 or student_grade < 1 or student_grade > 10:
        '''
        raise Exception -> next week :)
        print - not allowed
        return empty student -> not a good idea 
        '''
        return None
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
UI 
(calls functions that implement features)
'''


def read_student():
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
        if student is None:
            print('Invalid student params!')
    return student


def print_menu():
    print('1. Add student')
    print('3. Show all students')
    print('0. Exit')


def add_student_ui(student_list):
    student = read_student()
    # Check for duplicate student id
    if find_by_id(student_list, get_id(student)):
        print('Duplicate student id!')
        return
    student_list.append(student)


def show_all_students_ui(student_list):
    for student in student_list:
        print(to_str(student))


def start():
    '''
    1. print menu
    2. read user input
    3. call a function that fulfills that requirement
    '''
    # List of students in my program
    student_list = []
    # These students help me test my program
    test_init(student_list)
    command_dict = {'3': show_all_students_ui, '1': add_student_ui}
    done = False
    while not done:
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


def test_init(student_list):
    student_list.append(create_student('1', "Pop Ioana", 10))
    student_list.append(create_student('2', "Man Ionel", 5))
    student_list.append(create_student('3', "Marian Sofia", 9))
    student_list.append(create_student('4', "Boca Mihaela", 6))
    student_list.append(create_student('5', "Popa Adela", 5))
    student_list.append(create_student('6', "Costin Daniel", 7))
    student_list.append(create_student('7', "Zaharia Vasile", 8))
    student_list.append(create_student('8', "Mihnea Loredana", 9))


'''
Delete a student
    create delete_student_ui function
    add the new command to the print_menu and to command_dict
    create the delete_student function (not in the UI)
        - handle when given ID does not exist => error message
    create read_student_id function (in the UI)
'''

start()
