from random import randint
from Exceptions import RepositoryException
from Repositories.Iterable import Iterable


class StudentRepository:
    def __init__(self):
        self._student_data = Iterable()

    def __len__(self):
        return len(self._student_data)

    def add_student(self, student_to_add):
        if self.search_student(student_to_add.id) is not None:
            raise RepositoryException("Student ID already existent")
        self._student_data.append(student_to_add)
        return student_to_add

    def remove_student(self, student_id):
        removed_student = self.get_student_by_id(student_id)
        if removed_student is None:
            raise RepositoryException("Student not existent")
        index = -1
        for student in self._student_data:
            index += 1
            if student.id == student_id:
                del self._student_data[index]
        return removed_student

    def update_student(self, student_id, new_name):
        searched_student = self.get_student_by_id(student_id)
        if searched_student is None:
            raise RepositoryException("Student not existent")
        old_name = searched_student.name
        for student in self._student_data:
            if student.id == student_id:
                student.name = new_name
        return old_name

    def search_student(self, student_id):
        index = -1
        for student in self._student_data:
            index += 1
            if student.id == student_id:
                return index
        return None

    def get_student_by_id(self, student_id):
        for student in self._student_data:
            if student.id == student_id:
                return student
        return None

    def filter_id(self, value):
        filtered_list = self._student_data.filter(lambda student: student.id == value)
        return filtered_list

    def filter_name(self, value):
        filtered_list = self._student_data.filter(lambda student: student.name == value)
        return filtered_list

    def filter_group(self, value):
        filtered_list = self._student_data.filter(lambda student: student.group == value)
        return filtered_list

    def get_random_id(self):
        return self._student_data[randint(0, len(self._student_data)-1)].id

    def get_all_students(self):
        return self._student_data[:]

    def sort_id(self):
        sorted_list = self._student_data.shell_sort(lambda a, b: a.id > b.id)
        return sorted_list

    def sort_name(self):
        sorted_list = self._student_data.shell_sort(lambda a, b: a.name > b.name)
        return sorted_list

    def sort_group(self):
        sorted_list = self._student_data.shell_sort(lambda a, b: a.group > b.group)
        return sorted_list
