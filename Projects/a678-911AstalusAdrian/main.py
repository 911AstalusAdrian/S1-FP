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


# The start of our program

undo_service = UndoService()
student_repository = StudentRepository()
assignment_repository = AssignmentRepository()
grades_repository = GradesRepository()
student_validator = StudentValidator()
assignment_validator = AssignmentValidator()
grades_validator = GradesValidator(assignment_repository, student_repository)
grades_service = GradesService(student_repository, assignment_repository, grades_repository, grades_validator, undo_service)
student_service = StudentService(student_repository, student_validator, grades_service, undo_service)
assignment_service = AssignmentService(assignment_repository, assignment_validator, grades_service, undo_service)


# ui = UI(student_service, assignment_service, grades_service, undo_service)
# ui.run()


gui = GUI(student_service, assignment_service, grades_service, undo_service)
gui.start()
