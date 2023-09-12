"""
Created on Oct 7, 2016

@author: Arthur

2017.09.30 Changed to menu-driven, added observations
2018.10.07 Updated representation for student entity
2020.10.06 Observe Python code style guide
"""

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

    Observations:
        - When starting the program, it already has data entered!
        - We have two types of functions: those for the UI and those for functionalities
        - We have specification for non-UI functions
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It can report errors from non-UI functions too!
        - You can crash the program by providing incorrect input
        - Make sure you understand the representation of student
        - We reuse functions (e.g. __showStudents) for several functionalities. Less code to write and test!
        - We can develop this program in a feature-driven manner by going through functionalities 
        - We don't use global variables!
"""

"""
    Functions to work with a student
    NB! Not the UI part, so no print or input here
    -----------------------------------------------------------------
"""


def create_student(student_id, student_name, student_grade):
    """
    Create and return a new student
    :param student_id: Unique id (str) of the student
    :param student_name: Student name
    :param student_grade: Student grade
    :return: A new student instance, or None if student could not be created (e.g. no id given)
    """
    if len(student_id) == 0 or len(student_name) == 0 or student_grade < 1 or student_grade > 10:
        return None
    return [student_id, student_name, student_grade]


"""
    Specification for getters/setters is not mandatory, 
    as long as they are simple & clear
"""


def get_id(student):
    return student[0]


def get_name(student):
    return student[1]


def get_grade(student):
    return student[2]


def to_str(student):
    """
    Return the student's str representation
    :param student: Target student
    :return: str representing the student
    """
    return student[0] + " | name " + str(student[1]).ljust(16) + " | grade " + str(student[2]).rjust(2)


"""
    Function that implement program functionalities
    NB! Not the UI part, so no print or input here
    -----------------------------------------------------------------
"""


def find_by_id(student_list, student_id):
    """
    Searches for a student by id.
    :param student_list: the list of students
    :param student_id: ID of the searched student
    :return: Position of the student in the list, -1 if no student with given ID
    """
    pos = -1
    for i in range(0, len(student_list)):
        s = student_list[i]
        if get_id(s) == student_id:
            pos = i
            break
    return pos


def list_to_str(student_list):
    """
    Build the string representation for a list of students
    :param student_list: The list of students
    :return: The str representation
    """
    result = ""
    for s in student_list:
        result += to_str(s)
        result += "\n"
    return result


def add_student(student_list, student):
    """
    Adds the student to the list, if there is no other student with the same id.
    :param student_list: the list of students
    :param student: tuple that represents the student
    :return: True if the operation was completed successfully
    """
    pos = find_by_id(student_list, get_id(student))
    if pos == -1:  # If another student with this id does not exist => add
        student_list.append(student)
        return True
    return False


def delete_student(student_list, student_id):
    """
    Delete the student with the given id from the list studentList
    :param student_list: the list of students
    :param student_id: The id of the student to remove
    :return: True if the operation was completed successfully
    """
    # Search the index of the student with the given id
    pos = find_by_id(student_list, student_id)
    if pos == -1:  # Student with the given id does not exist
        return False
    else:
        student_list.pop(pos)
        return True


def filter_by_grades(student_list, student_grade):
    """
    Return students with grade > student_grade
    :param student_list: the list of students
    :param student_grade: target grade
    :return: The filtered list of students
    """
    result_list = []
    for student in student_list:
        if get_grade(student) >= student_grade:
            result_list.append(student)
    return result_list


"""
    UI functions
    NB! This should only include the I/O part, and no functionalities 
    NB! Specifications or tests are not required for the UI
    -----------------------------------------------------------------
"""


def print_main_menu():
    menu_string = '\nMenu:\n'
    menu_string += '\t 1 - Add student\n'
    menu_string += '\t 2 - Delete student\n'
    menu_string += '\t 3 - Show all students\n'
    menu_string += '\t 4 - Filter students by grade\n'
    menu_string += '\t 0 - Exit\n'
    print(menu_string)


def start():
    student_list = []

    '''
    We add a few students so that we do not start from scratch
    '''
    test_init(student_list)

    stop = False
    while not stop:
        print_main_menu()
        command = input("Enter command: ")
        if command == '1':
            add_submenu(student_list)
        elif command == '2':
            delete_submenu(student_list)
        elif command == '3':
            show_students(student_list, -1)
        elif command == '4':
            grade = int(input("Grade to filter by:"))
            show_students(student_list, grade)
        elif command == '0':
            stop = True
        else:
            print("Invalid command!")


def add_submenu(student_list):
    """
    Add a new student
    :param student_list: The list of students
    :return: True if student was added successfully, False otherwise
    """
    student_id = input("Enter student id:")
    student_name = input("Enter student name:")
    student_grade = int(input("Enter student grade:"))

    student = create_student(student_id, student_name, student_grade)
    if student is None:
        print("Invalid input. Student was not added")
        return False

    if not add_student(student_list, student):
        print("Student could not be added.")
    return True


def delete_submenu(student_list):
    student_id = input("Enter student id: ")

    if not delete_student(student_list, student_id):
        print("Invalid input. No student was deleted")


def show_students(student_list, grade):
    sublist = filter_by_grades(student_list, grade)
    print(list_to_str(sublist))


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
