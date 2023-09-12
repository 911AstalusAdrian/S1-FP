from random import randint
from Entities.entities import Grade
from Services.statistic_service import StudentGradeForAssignment, LateStudents, SchoolSituation
from Services.undo_redo_service import FunctionCall, Operation
from Exceptions import EntityException, RepositoryException
from datetime import date
from Repositories.Iterable import non_iterable_shell_sort

class GradesService:
    def __init__(self, student_repository, assignment_repository, grades_repository, grades_validator, undo_service):
        self._students_repository = student_repository
        self._assignments_repository = assignment_repository
        self._grades_repository = grades_repository
        self._grades_validator = grades_validator
        self._undo_service = undo_service

    def add_grade(self, assignment_id, student_id, grade=0.0):
        self.add_grade_without_record(assignment_id, student_id)
        function_undo = FunctionCall(self.remove_last_grades, 1)
        function_redo = FunctionCall(self.add_grade_without_record, assignment_id, student_id)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def add_grade_without_record(self, assignment_id, student_id, grade=0.0):
        new_grade = Grade(assignment_id, student_id, grade)
        self._grades_validator.validate(new_grade)
        self._grades_repository.add_grade(new_grade)
        return new_grade

    def remove_by_student(self, student_id):
        list_of_grades = []
        for grade in self._grades_repository.get_all_grades():
            if grade.student_id == student_id:
                grade_details = (grade.assignment_id, grade.student_id, grade.grade_value)
                list_of_grades.append(grade_details)
                self._grades_repository.remove_grade(grade.student_id, grade.assignment_id)
        return list_of_grades

    def remove_by_assignment(self, assignment_id):
        list_of_grades = []
        for grade in self._grades_repository.get_all_grades():
            if grade.assignment_id == assignment_id:
                grade_details = (grade.assignment_id, grade.student_id, grade.grade_value)
                list_of_grades.append(grade_details)
                self._grades_repository.remove_grade(grade.student_id, grade.assignment_id)
        return list_of_grades

    def remove_last_grades(self, number_of_grades):
        self._grades_repository.remove_last_grades(number_of_grades)

    def is_graded(self, student_id, assignment_id):
        for grade in self._grades_repository.get_all_grades():
            if grade.student_id == student_id and grade.assignment_id == assignment_id:
                return True
        return False

    def add_grade_to_group(self, assignment_id, group):
        number_of_additions = self.add_to_group_without_record(assignment_id, group)
        function_undo = FunctionCall(self.remove_last_grades, number_of_additions)
        function_redo = FunctionCall(self.add_grade_to_group, assignment_id, group)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def add_to_group_without_record(self, assignment_id, group):
        number_of_additions = 0
        if group < 911 or group > 917:
            raise EntityException("Invalid student group! ")
        for student in self._students_repository.get_all_students():
            if student.group == group and not self.is_graded(student.id, assignment_id):
                self.add_grade_without_record(assignment_id, student.id)
                number_of_additions += 1
        return number_of_additions

    def show_student_assignments(self, student_id):
        student_assignments = []
        for grade in self._grades_repository.get_all_grades():
            if grade.student_id == student_id and grade.grade_value == 0.0:
                student_assignments.append(grade.assignment_id)
        return student_assignments

    def calculate_average(self, student_id):
        grades_sum = 0
        grades_number = 0
        for grade in self._grades_repository.get_all_grades():
            if grade.student_id == student_id and grade.grade_value != 0.0:
                grades_sum += grade.grade_value
                grades_number += 1
        if grades_number == 0:
            return 0.0
        else:
            grades_average = grades_sum / grades_number
            return grades_average

    def give_grade(self, assignment_id, student_id, assignment_grade):
        self.give_grade_without_record(assignment_id, student_id, assignment_grade)
        function_undo = FunctionCall(self.give_grade_without_record, assignment_id, student_id, 0.0)
        function_redo = FunctionCall(self.give_grade_without_record, assignment_id, student_id, assignment_grade)
        operation = Operation(function_undo, function_redo)
        self._undo_service.record(operation)

    def give_grade_without_record(self, assignment_id, student_id, assignment_grade):
        if self._grades_repository.search_if_grade_exists(assignment_id, student_id) is False:
            raise RepositoryException("The student and the assignment aren't linked!")
        self._grades_repository.update_grade(assignment_id, student_id, assignment_grade)

    def list_grades(self):
        return self._grades_repository.get_all_grades()

    def sort(self, criteria):
        sort_options = ['student id', 'assignment id', 'grade']
        if criteria in sort_options:
            self._grades_repository.sort(criteria)
        else:
            raise RepositoryException("Invalid sorting criteria for this list!")

    def initialise(self):
        for index in range(30):
            random_student_id = self._students_repository.get_random_id()
            random_assignment_id = self._assignments_repository.get_random_id()
            random_grade = float(randint(0, 10))
            random_grade = Grade(random_assignment_id, random_student_id, random_grade)
            if random_grade not in self._grades_repository.get_all_grades():
                self._grades_repository.add_grade(random_grade)
            else:
                index -= 1

    def filter_grades(self, criteria, value):
        if criteria == "student id":
            if len(value) == 4 and value.isdigit():
                filtered_list = self._grades_repository.filter_student(value)
            else:
                raise RepositoryException("Invalid value for Student ID criteria")
        elif criteria == 'assignment id':
            if len(value) == 4 and value[0] == 'A':
                filtered_list = self._grades_repository.filter_assignment(value)
            else:
                raise RepositoryException("Invalid value for Assignment ID criteria")
        elif criteria == 'grade':
            if 0.0 <= float(value) <= 10.0:
                filtered_list = self._grades_repository.filter_grade(float(value))
            else:
                raise RepositoryException("Invalid value for Grade Value criteria")
        else:
            raise RepositoryException("Invalid filtering criteria for Grades")
        return filtered_list

    def sort_grades(self, criteria):
        if criteria == 'student id':
            sorted_list = self._grades_repository.sort_student()
        elif criteria == 'assignment id':
            sorted_list = self._grades_repository.sort_assignment()
        elif criteria == 'grade':
            sorted_list = self._grades_repository.sort_grade()
        else:
            raise RepositoryException("Invalid sorting criteria for Grades")
        return sorted_list

    def reorder_grades(self, sorted_list):
        grades_list = self.list_grades()
        for index in range(len(grades_list)):
            grades_list[index] = sorted_list[index]

    def first_statistic(self, assignment_for_statistic):
        if self._grades_repository.search_assignment_id(assignment_for_statistic) is False:
            raise RepositoryException("Assignment ID invalid / doesn't exist.")
        list_to_sort = []
        grades_dictionary = {}
        final_sorted_list = []
        for grade in self._grades_repository.get_all_grades():
            if grade.assignment_id == assignment_for_statistic:
                grades_dictionary[grade.student_id] = grade.grade_value
        for element in grades_dictionary:
            list_to_sort.append([element, grades_dictionary[element]])
        list_to_sort = non_iterable_shell_sort(list_to_sort, lambda student, another_student: student[1] > another_student[1])
        for element in list_to_sort:
            final_sorted_list.append(StudentGradeForAssignment(element[0], element[1]))
        return final_sorted_list

    def second_statistic(self):
        statistic_result = []
        late_students = {}
        for grade in self._grades_repository.get_all_grades():
            assignment_deadline = self._assignments_repository.get_assignment_deadline(grade.assignment_id)
            if grade.grade_value == 0.0 and assignment_deadline < date.today():
                late_students[grade.student_id] = grade.assignment_id
        for element in late_students:
            statistic_result.append(LateStudents(element, late_students[element]))
        return statistic_result

    def third_statistic(self):
        list_to_sort = []
        school_situation = {}
        final_sorted_list = []
        for grade in self._grades_repository.get_all_grades():
            if grade.student_id in school_situation:
                continue
            else:
                grades_average = self.calculate_average(grade.student_id)
                school_situation[grade.student_id] = grades_average
        for element in school_situation:
            list_to_sort.append([element, school_situation[element]])
        list_to_sort = non_iterable_shell_sort(list_to_sort, lambda student, another_student: student[1] < another_student[1])
        for element in list_to_sort:
            final_sorted_list.append(SchoolSituation(element[0], element[1]))
        return final_sorted_list
