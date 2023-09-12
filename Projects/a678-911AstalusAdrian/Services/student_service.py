from random import randint
from Entities.entities import Student
from Services.undo_redo_service import FunctionCall, Operation


class StudentService:

    def __init__(self, repository, student_validator, grade_service, undo_service):
        self._student_repository = repository
        self._student_validator = student_validator
        self._grade_service = grade_service
        self._undo_service = undo_service

    def add(self, student_id, name, group):
        student = self.add_without_record(student_id, name, group)
        function_undo = FunctionCall(self.remove_without_record, student.student_id)
        function_redo = FunctionCall(self.add_without_record, student.student_id, student.student_name, student.student_group)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def add_without_record(self, student_id, name, group):
        new_student = Student(student_id, name, group)
        self._student_validator.validate(new_student)
        self._student_repository.add_student(new_student)
        return new_student

    def add_student_and_grades(self, student_id, student_name, student_group, list_of_grades):
        new_student = Student(student_id, student_name, student_group)
        self._student_validator.validate(new_student)
        self._student_repository.add_student(new_student)
        for grade in list_of_grades:
            self._grade_service.add_grade_without_record(grade[0], grade[1], grade[2])

    def remove(self, student_id):

        student, list_of_grades = self.remove_without_record(student_id)
        function_undo = FunctionCall(self.add_student_and_grades, student.student_id, student.student_name, student.student_group, list_of_grades)
        function_redo = FunctionCall(self.remove_without_record, student.student_id)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def remove_without_record(self, student_id):
        check_student_id = Student(student_id, 'test name', 911)
        self._student_validator.validate(check_student_id)
        student = self._student_repository.remove_student(student_id)
        list_of_grades = self._grade_service.remove_by_student(student_id)
        return student, list_of_grades

    def update(self, student_id, new_name):
        old_student_name = self.update_without_record(student_id, new_name)
        function_undo = FunctionCall(self.update_without_record, student_id, old_student_name)
        function_redo = FunctionCall(self.update_without_record, student_id, new_name)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def update_without_record(self, student_id, new_name):
        check_student = Student(student_id, new_name, 911)
        self._student_validator.validate(check_student)
        previous_student_name = self._student_repository.update_student(student_id, new_name)
        return previous_student_name

    def list_students(self):
        return self._student_repository.get_all_students()

    def initialise(self):
        names = ['Alex', 'Marius', 'Ionel', 'Tudor', 'Dan',
                 'Alexandra', 'Maria', 'Ioana', 'Teodora', 'Dana']
        for index in range(10):
            student_id = str(randint(1000, 9999))  # The id is a randomly-generated 4-digit string
            student_name = names[randint(0, 9)]  # We choose a random name from the list of existing names
            student_group = randint(911, 917)  # We choose a random group between 911 and 917
            self.add_without_record(student_id, student_name, student_group)  # We add the random student to the repository
