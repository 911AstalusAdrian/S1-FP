from random import randint
from Entities.entities import Assignment
from Exceptions import RepositoryException
from Services.undo_redo_service import FunctionCall, Operation
from datetime import date


class AssignmentService:

    def __init__(self, repository, assignment_validator, grade_service, undo_service):
        self._assignment_repository = repository
        self._assignment_validator = assignment_validator
        self._grade_service = grade_service
        self._undo_service = undo_service

    def add(self, assignment_id, description, deadline):
        new_assignment = self.add_without_record(assignment_id, description, deadline)
        self._assignment_validator.validate(new_assignment)
        function_undo = FunctionCall(self.remove_without_record, new_assignment.id)
        function_redo = FunctionCall(self.add_without_record, new_assignment.id,
                                     new_assignment.description, new_assignment.deadline)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def add_without_record(self, assignment_id, description, deadline):
        new_assignment = Assignment(assignment_id, description, deadline)
        self._assignment_repository.add_assignment(new_assignment)
        return new_assignment

    def add_assignment_and_grades(self, assignment_id, description, deadline, list_of_grades):
        new_assignment = Assignment(assignment_id, description, deadline)
        self._assignment_repository.add_assignment(new_assignment)
        for grade in list_of_grades:
            self._grade_service.add_grade_without_record(grade[0], grade[1], grade[2])

    def remove(self, assignment_id):
        assignment, list_of_grades = self.remove_without_record(assignment_id)
        function_undo = FunctionCall(self.add_assignment_and_grades, assignment.id, assignment.description, assignment.deadline, list_of_grades)
        function_redo = FunctionCall(self.remove_without_record, assignment.id)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def remove_without_record(self, assignment_id):
        check_assignment = Assignment(assignment_id, 'test description', date(2030, 1, 1))
        self._assignment_validator.validate(check_assignment)
        assignment = self._assignment_repository.remove_assignment(assignment_id)
        list_of_grades = self._grade_service.remove_by_assignment(assignment_id)
        return assignment, list_of_grades

    def update(self, assignment_id, new_deadline):
        old_deadline = self.update_without_record(assignment_id, new_deadline)
        function_undo = FunctionCall(self.update_without_record, assignment_id, old_deadline)
        function_redo = FunctionCall(self.update_without_record, assignment_id, new_deadline)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def update_without_record(self, assignment_id, new_deadline):
        check_assignment = Assignment(assignment_id, 'test description', new_deadline)
        self._assignment_validator.validate(check_assignment)
        previous_deadline = self._assignment_repository.update_assignment(assignment_id, new_deadline)
        return previous_deadline

    def list_assignments(self):
        return self._assignment_repository.get_all_assignments()

    def sort(self, criteria):
        sort_options = ['id', 'deadline', 'description']
        if criteria in sort_options:
            self._assignment_repository.sort(criteria)
        else:
            raise RepositoryException("Invalid sorting criteria for this list!")

    def initialise(self):
        # The list of possible Descriptions
        descriptions = [
            'Students Register Management',
            'Student Lab Assignment',
            'Movie Rental',
            'Library',
            'Activity Planner',
            'Complex numbers',
            'Expenses',
            'Students',
            'Books'
        ]
        for index in range(10):
            assignment_id = 'A' + str(randint(100, 999))  # The ID is a string made from the letter 'A' and a 3-digit number
            assignment_description = descriptions[randint(0, 8)]  # We choose a description from the list randomly
            assignment_deadline_year = randint(2020, 2021)  # We use the year 2021 to avoid possible errors
            assignment_deadline_month = randint(1, 12)  # We choose a random month
            if assignment_deadline_month == 2:
                assignment_deadline_day = randint(1, 28)  # We choose a random day from 1 to 28 if the month is February
            else:
                assignment_deadline_day = randint(1, 31)  # We choose a random day
            assignment_deadline = date(assignment_deadline_year, assignment_deadline_month, assignment_deadline_day)  # The random deadline is created
            self.add_without_record(assignment_id, assignment_description, assignment_deadline)

    def filter_assignments(self, criteria, value):
        if criteria == "id":
            if len(value) == 4 and value[0] == 'A':
                filtered_list = self._assignment_repository.filter_id(value)
            else:
                raise RepositoryException("Invalid value for ID criteria")
        elif criteria == 'description':
            if len(value) != 0:
                filtered_list = self._assignment_repository.filter_description(value)
            else:
                raise RepositoryException("Invalid value for Description criteria")
        elif criteria == 'deadline':
            filtered_list = self._assignment_repository.filter_deadline(value)
        else:
            raise RepositoryException("Invalid filtering criteria for Assignments")
        return filtered_list

    def sort_assignments(self, criteria):
        if criteria == 'id':
            sorted_list = self._assignment_repository.sort_id()
        elif criteria == 'description':
            sorted_list = self._assignment_repository.sort_description()
        elif criteria == 'deadline':
            sorted_list = self._assignment_repository.sort_deadline()
        else:
            raise RepositoryException("Invalid sorting criteria for Assignments")
        return sorted_list

    def reorder_assignments(self, sorted_list):
        assignments_list = self.list_assignments()
        for index in range(len(assignments_list)):
            assignments_list[index] = sorted_list[index]
