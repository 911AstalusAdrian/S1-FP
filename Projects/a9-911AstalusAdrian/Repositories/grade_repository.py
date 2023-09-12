from Exceptions import RepositoryException


class GradesRepository:
    def __init__(self):
        self._grades_data = []

    def add_grade(self, grade_to_add):
        if grade_to_add in self._grades_data:
            raise RepositoryException("Grade already existent!")
        self._grades_data.append(grade_to_add)
        return grade_to_add

    def remove_by_student(self, student_id):
        for grade in self._grades_data:
            if grade.grade_student_id == student_id:
                self._grades_data.remove(grade)
                return grade

    def remove_by_assignment(self, assignment_id):
        for grade in self._grades_data:
            if grade.grade_assignment_id == assignment_id:
                self._grades_data.remove(grade)
                return grade

    def remove_grade(self, student_id, assignment_id):
        for grade in self._grades_data:
            if grade.grade_student_id == student_id and grade.grade_assignment_id == assignment_id:
                self._grades_data.remove(grade)
                return grade

    def search_student_id(self, student_id):
        for grade in self._grades_data:
            if grade.grade_student_id == student_id:
                return True
        return False

    def search_assignment_id(self, assignment_id):
        for grade in self._grades_data:
            if grade.grade_assignment_id == assignment_id:
                return True
        return False

    def search_if_grade_exists(self, assignment_id, student_id):
        for grade in self._grades_data:
            if grade.grade_student_id == student_id and grade.grade_assignment_id == assignment_id:
                return True
        return False

    def remove_last_grades(self, number_of_grades):
        for index in range(number_of_grades):
            self._grades_data.pop()

    def update_grade(self, assignment_id, student_id, assignment_grade):
        for grade in self._grades_data:
            if grade.grade_assignment_id == assignment_id and grade.grade_student_id == student_id:
                if grade.grade_value == 0.0 and assignment_grade != 0.0:
                    grade.grade_value = assignment_grade
                elif grade.grade_value != 0.0 and assignment_grade == 0.0:
                    grade.grade_value = assignment_grade
                else:
                    raise RepositoryException("Cannot change the grade!")

    def get_number_of_grades(self):
        return len(self._grades_data)

    def get_all_grades(self):
        return self._grades_data[:]
