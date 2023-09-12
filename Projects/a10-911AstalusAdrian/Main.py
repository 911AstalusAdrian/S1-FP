from Repositories.pickle_grades_repository import PickleGradesRepository
from Repositories.pickle_student_repository import PickleStudentRepository
from Repositories.pickle_assignment_repository import PickleAssignmentRepository
from Repositories.text_student_repository import TextStudentRepository
from Repositories.text_assignment_repository import TextAssignmentRepository
from Repositories.text_grades_repository import TextGradesRepository
from Repositories.student_repository import StudentRepository
from Repositories.assignment_repository import AssignmentRepository
from Repositories.grade_repository import GradesRepository
from Services.student_service import StudentService
from Services.assignment_service import AssignmentService
from Services.grade_service import GradesService
from Services.undo_redo_service import UndoService
from UI.gui import GUI
from UI.ui import UI
from Validators.validators import StudentValidator, AssignmentValidator, GradesValidator


assignment_validator = AssignmentValidator()
student_validator = StudentValidator()
undo_service = UndoService()

"""
    Depending on the value of 'repository' (from the 'settings.properties' file), we will initialise our Repositories differently
    In the same way, the program will start either using the UI or the GUI
    If the values from the file are not valid, a message will show
"""

file = open("settings.properties", 'rt')
repository_data = file.readline().strip().split()
student_data = file.readline().strip().split()
assignment_data = file.readline().strip().split()
grades_data = file.readline().strip().split()
ui_type = file.readline().strip().split()
ui_type = ui_type[2]

if repository_data[2] == "in_memory":
    student_repository = StudentRepository()
    assignment_repository = AssignmentRepository()
    grades_repository = GradesRepository()
elif repository_data[2] == 'textfiles':
    student_file = student_data[2]
    assignment_file = assignment_data[2]
    grades_file = grades_data[2]
    student_repository = TextStudentRepository(student_file)
    assignment_repository = TextAssignmentRepository(assignment_file)
    grades_repository = TextGradesRepository(grades_file)
elif repository_data[2] == 'binaryfiles':
    student_file = student_data[2]
    assignment_file = assignment_data[2]
    grades_file = grades_data[2]
    student_repository = PickleStudentRepository(student_file)
    assignment_repository = PickleAssignmentRepository(assignment_file)
    grades_repository = PickleGradesRepository(grades_file)
else:
    print("Invalid repository type!")

grades_validator = GradesValidator(assignment_repository, student_repository)
grades_service = GradesService(student_repository, assignment_repository, grades_repository, grades_validator, undo_service)
student_service = StudentService(student_repository, student_validator, grades_service, undo_service)
assignment_service = AssignmentService(assignment_repository, assignment_validator, grades_service, undo_service)


if ui_type == 'ui':
    ui = UI(student_service, assignment_service, grades_service, undo_service)
    ui.run()
elif ui_type == 'gui':
    gui = GUI(student_service, assignment_service, grades_service, undo_service)
    gui.start()
else:
    print("Invalid ui type")

