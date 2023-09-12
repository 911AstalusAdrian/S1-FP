from random import randint
from Exceptions import RepositoryException


class StudentRepository:
    def __init__(self):
        self._student_data = []

    def add_student(self, student_to_add):
        if student_to_add in self._student_data:
            raise RepositoryException("Student ID already existent")
        self._student_data.append(student_to_add)
        return student_to_add

    def remove_student(self, student_id):
        searched_student = self.get_student_by_id(student_id)
        if searched_student is None:
            raise RepositoryException("Student not existent!")
        self._student_data.remove(searched_student)
        return searched_student

    def update_student(self, student_id, new_name):
        searched_student = self.get_student_by_id(student_id)
        if searched_student is None:
            raise RepositoryException("Student not existent!")
        student_previous_name = self.get_student_by_id(student_id).student_name
        searched_student.student_name = new_name
        return student_previous_name

    def search_student_id(self, student_id):
        for student in self._student_data:
            if student.student_id == student_id:
                return True
        return False

    def get_student_by_id(self, student_id):
        for student in self._student_data:
            if student.student_id == student_id:
                return student
        return None

    def get_random_id(self):
        return self._student_data[randint(0, len(self._student_data)-1)].student_id

    def get_number_of_students(self):
        return len(self._student_data)

    def get_all_students(self):
        return self._student_data[:]
