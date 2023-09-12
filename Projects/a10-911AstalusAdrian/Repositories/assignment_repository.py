from Exceptions import RepositoryException
from random import randint
from Repositories.Iterable import Iterable


class AssignmentRepository:
    def __init__(self):
        self._assignment_data = Iterable()

    def __len__(self):
        return len(self._assignment_data)

    def add_assignment(self, assignment_to_add):
        """
        if assignment_to_add in self._assignment_data:
            raise RepositoryException("Assignment ID already existent!")
        self._assignment_data.append(assignment_to_add)
        return assignment_to_add
        """
        if self.search_assignment(assignment_to_add.id) is not None:
            raise RepositoryException("Assignment ID already existent")
        self._assignment_data.append(assignment_to_add)
        return assignment_to_add

    def remove_assignment(self, assignment_id):
        """
        assignment_index = self.search_assignment(assignment_id)
        if assignment_index is None:
            raise RepositoryException("Assignent not existent!")
        removed_assignment = self._assignment_data[assignment_index]
        del self._assignment_data[assignment_index]
        return removed_assignment
        """
        removed_assignment = self.get_assignment_by_id(assignment_id)
        if removed_assignment is None:
            raise RepositoryException("Assignment not existent")
        index = -1
        for assignment in self._assignment_data:
            index += 1
            if assignment.id == assignment_id:
                del self._assignment_data[index]
        return removed_assignment

    def update_assignment(self, assignment_id, new_deadline):
        """
        assignment_index = self.search_assignment(assignment_id)
        if assignment_index is None:
            raise RepositoryException("Assignment ID non-existent!")
        old_deadline = self._assignment_data[assignment_index].deadline
        assignment_description = self._assignment_data[assignment_index].description
        self._assignment_data[assignment_index] = Assignment(assignment_id, assignment_description, new_deadline)
        return old_deadline
        """
        searched_assignment = self.get_assignment_by_id(assignment_id)
        if searched_assignment is None:
            raise RepositoryException("Assignment not existent")
        old_deadline = searched_assignment.deadline
        for assignment in self._assignment_data:
            if assignment.id == assignment_id:
                assignment.deadline = new_deadline
        return old_deadline

    ''' 
    def update_assignment(self, assignment_id, new_deadline):
        old_assignment = self.get_assignment_by_id(assignment_id)
        if old_assignment is None:
            raise RepositoryException("Assignment ID not existent!")
        old_deadline = self.get_assignment_deadline(assignment_id)
        old_assignment.deadline = new_deadline
        return old_deadline
    '''

    def search_assignment(self, assignment_id):
        """
        for index in range(len(self._assignment_data)):
            if self._assignment_data[index].id == assignment_id:
                return index
        return None
        """
        index = -1
        for assignment in self._assignment_data:
            index += 1
            if assignment.id == assignment_id:
                return index
        return None

    def get_assignment_by_id(self, assignment_id):
        for assignment in self._assignment_data:
            if assignment.id == assignment_id:
                return assignment
        return None

    '''
    def sort(self, criteria):
        """
        We sorted the Assignments based on their deadline, in an ascending order
        The sorting method used is Shell Sort
        :return:
        """
        if criteria == 'id':
            interval = len(self._assignment_data) // 2
            while interval > 0:
                for index in range(interval, len(self._assignment_data)):
                    temporary_value = self._assignment_data[index]
                    j = index
                    while j >= interval and self._assignment_data[j-interval].id > temporary_value.id:
                        self._assignment_data[j] = self._assignment_data[j-interval]
                        j -= interval
                    self._assignment_data[j] = temporary_value
                interval //= 2
        elif criteria == 'deadline':
            interval = len(self._assignment_data) // 2
            while interval > 0:
                for index in range(interval, len(self._assignment_data)):
                    temporary_value = self._assignment_data[index]
                    j = index
                    while j >= interval and self._assignment_data[j-interval].deadline > temporary_value.deadline:
                        self._assignment_data[j] = self._assignment_data[j-interval]
                        j -= interval
                    self._assignment_data[j] = temporary_value
                interval //= 2
        else:
            interval = len(self._assignment_data) // 2
            while interval > 0:
                for index in range(interval, len(self._assignment_data)):
                    temporary_value = self._assignment_data[index]
                    j = index
                    while j >= interval and self._assignment_data[j-interval].description > temporary_value.description:
                        self._assignment_data[j] = self._assignment_data[j-interval]
                        j -= interval
                    self._assignment_data[j] = temporary_value
                interval //= 2
    '''

    def filter_id(self, value):
        filtered_list = self._assignment_data.filter(lambda assignment: assignment.id == value)
        return filtered_list

    def filter_description(self, value):
        filtered_list = self._assignment_data.filter(lambda assignment: assignment.description == value)
        return filtered_list

    def filter_deadline(self, value):
        filtered_list = self._assignment_data.filter(lambda assignment: assignment.deadline == value)
        return filtered_list

    def sort_id(self):
        sorted_list = self._assignment_data.shell_sort(lambda a, b: a.id > b.id)
        return sorted_list

    def sort_description(self):
        sorted_list = self._assignment_data.shell_sort(lambda a, b: a.description > b.description)
        return sorted_list

    def sort_deadline(self):
        sorted_list = self._assignment_data.shell_sort(lambda a, b: a.deadline > b.deadline)
        return sorted_list

    def get_random_id(self):
        return self._assignment_data[randint(0, len(self._assignment_data)-1)].id

    def get_all_assignments(self):
        return self._assignment_data[:]
