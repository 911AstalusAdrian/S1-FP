"""
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
        return None
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


'''
    Functions for User interface
    NB! The only place where we find print/input ! 
'''


def read_student():
    """
    Read student from the console
    :return: The new student, or None if invalid input
    """
    student_id = input('enter id: ')
    student_name = input('enter name: ')
    # TODO This crashes for invalid input, but we fix it during week 3 :)
    student_grade = int(input('enter grade: '))
    return create_student(student_id, student_name, student_grade)


def add_student_ui(student_list):
    # 1. Read student
    # 2. Check for valid student input
    # 3. Check student id is unique
    # 4. Add student to list
    student = read_student()
    if student is None:
        print("Invalid input. Student was not created!")
        return
    if find_by_id(student_list, get_id(student)) == -1:
        student_list.append(student)
    else:
        print("Duplicate student id!")


def show_all_students_ui(student_list):
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


def start():
    # 1. Print menu
    # 2. Read user input
    # 3. Call the correct function
    student_list = []
    test_init(student_list)

    command_dict = {'3': show_all_students_ui, '1': add_student_ui}
    are_we_done_yet = False

    while not are_we_done_yet:
        print_menu()
        command = input('Enter command: ')
        # V1
        # if command == '3':
        #     show_all_students_ui()
        # elif ...
        #     ...
        # else:
        #     ...

        # V2
        if command == '0':
            print('Bye!')
            are_we_done_yet = True
        elif command in command_dict:
            # command_dict['3'] =  show_all_students_ui
            # show_all_students_ui -> variable that holds a reference to a function
            # show_all_students_ui() -> function call
            # () -> function call operator
            command_dict[command](student_list)
        else:
            print('Invalid command')


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
    1. Together we implement: 
        show all students (feature 1)
    2. You tell me what and where to write for
        add a student (feature 2)
    What do we need to implement?
        -> update start and print_menu with the new command
        -> function read_student()
        -> function add_student_ui()
        -> check that new student id is unique
        
    3. You work to implement
        delete a student (feature 3)
        -> new entry in print_menu and command_dict
        -> function to read id of student to be deleted
        -> function delete_student_ui() (reuse find_by_id() !)
'''