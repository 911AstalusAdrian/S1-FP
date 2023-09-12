from Exceptions import RepositoryException
from random import randint


class AssignmentRepository:
    def __init__(self):
        self._assignment_data = []

    def add_assignment(self, assignment_to_add):
        if assignment_to_add in self._assignment_data:
            raise RepositoryException("Assignment ID already existent!")
        self._assignment_data.append(assignment_to_add)
        return assignment_to_add

    def remove_assignment(self, assignment_id):
        searched_assignment = self.get_assignment_by_id(assignment_id)
        if searched_assignment is None:
            raise RepositoryException("Assignment not existent!")
        self._assignment_data.remove(searched_assignment)
        return searched_assignment

    def update_assignment_repository(self, assignment_id, new_deadline):
        old_assignment = self.get_assignment_by_id(assignment_id)
        if old_assignment is None:
            raise RepositoryException("Assignment ID not existent!")
        old_deadline = self.get_assignment_deadline(assignment_id)
        old_assignment.assignment_deadline = new_deadline
        return old_deadline

    def search_assignment_id(self, assignment_id):
        for assignment in self._assignment_data[:]:
            if assignment.assignment_id == assignment_id:
                return True
        return False

    def get_assignment_by_id(self, assignment_id):
        for assignment in self._assignment_data:
            if assignment.assignment_id == assignment_id:
                return assignment
        return None

    def get_assignment_deadline(self, assignment_id):
        for assignment in self._assignment_data:
            if assignment.assignment_id == assignment_id:
                return assignment.assignment_deadline

    def get_random_id(self):
        return self._assignment_data[randint(0, len(self._assignment_data)-1)].assignment_id

    def get_number_of_assignments(self):
        return len(self._assignment_data)

    def get_all_assignments(self):
        return self._assignment_data[:]
