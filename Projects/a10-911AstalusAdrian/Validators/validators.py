from datetime import date
from Exceptions import EntityException


class StudentValidator:

    @staticmethod
    def validate(student):
        if (len(student.id) == 0 or len(student.id) != 4) or not student.id.isdigit():
            raise EntityException("Invalid student ID, ID must be 4 characters long!")
        if len(student.name) == 0:
            raise EntityException("Invalid student Name, empty value provided.")
        if not student.name.replace(" ", "").isalpha():
            raise EntityException("Invalid student Name, it must contain only letters!")
        if student.group < 911 or student.group > 917:
            raise EntityException("Invalid student Group, number too big or too small.")


class AssignmentValidator:

    @staticmethod
    def validate(assignment):
        if len(assignment.id) != 4 or assignment.id[0] != 'A':
            raise EntityException("Invalid assignment ID, ID must have 4 charaters, first one being A")
        if len(assignment.description) == 0:
            raise EntityException("Invalid assignment description, empty value provided.")


class GradesValidator:
    def __init__(self, assignment_repository, student_repository):
        self._assignment_repository = assignment_repository
        self._student_repository = student_repository

    def validate(self, grade):
        is_assignment = False
        is_student = False
        for assignment in self._assignment_repository.get_all_assignments():
            if grade.assignment_id == assignment.id:
                is_assignment = True

        for student in self._student_repository.get_all_students():
            if grade.student_id == student.id:
                is_student = True
        if is_assignment is False:
            raise EntityException("Invalid assignment ID, ID doesn't exist.")
        if is_student is False:
            raise EntityException("Invalid student ID, ID doesn't exist.")
        if grade.grade_value < 0.0 or grade.grade_value > 10.0:
            raise EntityException("Invalid grade, grade must be float between 0 and 10.")