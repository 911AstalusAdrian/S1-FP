from Exceptions import RepositoryException
from Repositories.Iterable import Iterable


class GradesRepository:
    def __init__(self):
        self._grades_data = Iterable()

    def __len__(self):
        return len(self._grades_data)

    def add_grade(self, grade_to_add):
        if self.search_if_grade_exists(grade_to_add.assignment_id, grade_to_add.student_id) is True:
            raise RepositoryException("Grade already exists!")
        else:
            self._grades_data.append(grade_to_add)
       # if grade_to_add in self._grades_data:
       #     raise RepositoryException("Grade already existent!")
       # self._grades_data.append(grade_to_add)
       # return grade_to_add

    def remove_by_student(self, student_id):
        index = self.search_by_student(student_id)
        if index is None:
            raise RepositoryException("Student ID doesn't exist")
        removed_grade = self._grades_data[index]
        del self._grades_data[index]
        return removed_grade

    def remove_by_assignment(self, assignment_id):
        index = self.search_by_assignment(assignment_id)
        if index is None:
            raise RepositoryException("Assignment ID doesn't exist")
        removed_grade = self._grades_data[index]
        del self._grades_data[index]
        return removed_grade

    def remove_grade(self, student_id, assignment_id):
        index = self.search_grade(student_id, assignment_id)
        if index is not None:
            removed_grade = self._grades_data[index]
            del self._grades_data[index]
            return removed_grade

    def search_grade(self, student_id, assignment_id):
        for index in range(len(self._grades_data)):
            if self._grades_data[index].student_id == student_id and self._grades_data[index].assignment_id == assignment_id:
                return index
        return None

    def search_by_student(self, student_id):
        for index in range(len(self._grades_data)):
            if self._grades_data[index].student_id == student_id:
                return index
        return None

    def search_by_assignment(self, assignment_id):
        for index in range(len(self._grades_data)):
            if self._grades_data[index].assignment_id == assignment_id:
                return index
        return None

    def search_if_grade_exists(self, assignment_id, student_id):
        for index in range(len(self._grades_data)):
            if self._grades_data[index].assignment_id == assignment_id and self._grades_data[index].student_id == student_id:
                return True
        return False

    def search_assignment_id(self, assignment_id):
        for grade in self._grades_data:
            if grade.assignment_id == assignment_id:
                return True
        return False

    def remove_last_grades(self, number_of_grades):
        for index in range(number_of_grades):
            self._grades_data.pop()

    def update_grade(self, assignment_id, student_id, assignment_grade):
        for grade in self._grades_data:
            if grade.assignment_id == assignment_id and grade.student_id == student_id:
                if grade.grade_value == 0.0 and assignment_grade != 0.0:
                    grade.grade_value = assignment_grade
                elif grade.grade_value != 0.0 and assignment_grade == 0.0:
                    grade.grade_value = assignment_grade
                else:
                    raise RepositoryException("Cannot change the grade!")

    def filter_student(self, value):
        filtered_list = self._grades_data.filter(lambda grade: grade.student_id == value)
        return filtered_list

    def filter_assignment(self, value):
        filtered_list = self._grades_data.filter(lambda grade: grade.assignment_id == value)
        return filtered_list

    def filter_grade(self, value):
        filtered_list = self._grades_data.filter(lambda grade: grade.grade_value == value)
        return filtered_list

    def sort_student(self):
        sorted_list = self._grades_data.shell_sort(lambda a, b: a.student_id > b.student_id)
        return sorted_list

    def sort_assignment(self):
        sorted_list = self._grades_data.shell_sort(lambda a, b: a.assignment_id > b.assignment_id)
        return sorted_list

    def sort_grade(self):
        sorted_list = self._grades_data.shell_sort(lambda a, b: a.grade_value > b.grade_value)
        return sorted_list


    def get_all_grades(self):
        return self._grades_data[:]
