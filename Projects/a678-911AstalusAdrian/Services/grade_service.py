from random import randint
from Entities.entities import Grade
from Services.statistic_service import StudentGradeForAssignment, LateStudents, SchoolSituation
from Services.undo_redo_service import FunctionCall, Operation
from Exceptions import EntityException, RepositoryException
from datetime import date


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
            if grade.grade_student_id == student_id:
                grade_details = (grade.grade_assignment_id, grade.grade_student_id, grade.grade_value)
                list_of_grades.append(grade_details)
                self._grades_repository.remove_grade(grade.grade_student_id, grade.grade_assignment_id)
        return list_of_grades

    def remove_by_assignment(self, assignment_id):
        list_of_grades = []
        for grade in self._grades_repository.get_all_grades():
            if grade.grade_assignment_id == assignment_id:
                grade_details = (grade.grade_assignment_id, grade.grade_student_id, grade.grade_value)
                list_of_grades.append(grade_details)
                self._grades_repository.remove_grade(grade.grade_student_id, grade.grade_assignment_id)
        return list_of_grades

    def remove_last_grades(self, number_of_grades):
        self._grades_repository.remove_last_grades(number_of_grades)

    def is_graded(self, student_id, assignment_id):
        for grade in self._grades_repository.get_all_grades():
            if grade.grade_student_id == student_id and grade.grade_assignment_id == assignment_id:
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
            if student.student_group == group and not self.is_graded(student.student_id, assignment_id):
                self.add_grade_without_record(assignment_id, student.student_id)
                number_of_additions += 1
        return number_of_additions

    def show_student_assignments(self, student_id):
        student_assignments = []
        for grade in self._grades_repository.get_all_grades():
            if grade.grade_student_id == student_id and grade.grade_value == 0.0:
                student_assignments.append(grade.grade_assignment_id)
        return student_assignments

    def calculate_average(self, student_id):
        grades_sum = 0
        grades_number = 0
        for grade in self._grades_repository.get_all_grades():
            if grade.grade_student_id == student_id and grade.grade_value != 0.0:
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

    def first_statistic(self, assignment_for_statistic):
        if self._grades_repository.search_assignment_id(assignment_for_statistic) is False:
            raise RepositoryException("Assignment ID invalid / doesn't exist.")
        statistic_result = []
        grades_dictionary = {}
        for grade in self._grades_repository.get_all_grades():
            if grade.grade_assignment_id == assignment_for_statistic:
                grades_dictionary[grade.grade_student_id] = grade.grade_value
        for element in grades_dictionary:
            statistic_result.append(StudentGradeForAssignment(element, grades_dictionary[element]))

        statistic_result.sort(key=lambda x: x.grade, reverse=True)
        return statistic_result

    def second_statistic(self):
        statistic_result = []
        late_students = {}
        for grade in self._grades_repository.get_all_grades():
            assignment_deadline = self._assignments_repository.get_assignment_deadline(grade.grade_assignment_id)
            if grade.grade_value == 0.0 and assignment_deadline < date.today():
                late_students[grade.grade_student_id] = grade.grade_assignment_id
        for element in late_students:
            statistic_result.append(LateStudents(element, late_students[element]))
        return statistic_result

    def third_statistic(self):
        statistic_result = []
        school_situation = {}
        for grade in self._grades_repository.get_all_grades():
            if grade.grade_student_id not in school_situation:
                #continue
            #else:
                grades_average = self.calculate_average(grade.grade_student_id)
                school_situation[grade.grade_student_id] = grades_average
        for element in school_situation:
            statistic_result.append(SchoolSituation(element, school_situation[element]))
        statistic_result.sort(key=lambda x: x.average_grade, reverse=True)
        return statistic_result
