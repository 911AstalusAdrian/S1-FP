import unittest
from datetime import date
from Exceptions import UndoRedoException, RepositoryException
from Repositories.student_repository import StudentRepository
from Repositories.assignment_repository import AssignmentRepository
from Repositories.grade_repository import GradesRepository
from Services.student_service import StudentService
from Services.assignment_service import AssignmentService
from Services.grade_service import GradesService
from Services.undo_redo_service import UndoService
from Validators.validators import StudentValidator, AssignmentValidator, GradesValidator, EntityException
from Services.statistic_service import SchoolSituation, LateStudents, StudentGradeForAssignment


class TestAllServices(unittest.TestCase):
    def setUp(self):
        student_repository = StudentRepository()
        student_validator = StudentValidator()
        assignment_repository = AssignmentRepository()
        assignment_validator = AssignmentValidator()
        grades_repository = GradesRepository()
        grades_validator = GradesValidator(assignment_repository, student_repository)
        self._undo_service = UndoService()
        self._grade_service = GradesService(student_repository, assignment_repository, grades_repository, grades_validator, self._undo_service)
        self._student_service = StudentService(student_repository, student_validator, self._grade_service, self._undo_service)
        self._assignment_service = AssignmentService(assignment_repository, assignment_validator, self._grade_service, self._undo_service)

    def test_initialises(self):
        self._student_service.initialise()
        list_of_students = self._student_service.list_students()
        self.assertLessEqual(len(list_of_students), 10)

        self._assignment_service.initialise()
        list_of_assignments = self._assignment_service.list_assignments()
        self.assertLessEqual(len(list_of_assignments), 10)

        self._grade_service.initialise()
        list_of_grades = self._grade_service.list_grades()
        self.assertLessEqual(len(list_of_grades), 30)

    def test_student_add(self):
        self._student_service.add('1234', 'Michael', 911)
        list_of_students = self._student_service.list_students()
        self.assertEqual(len(list_of_students), 1)
        self._undo_service.undo()
        list_of_students = self._student_service.list_students()
        self.assertEqual(len(list_of_students), 0)
        self.assertRaises(UndoRedoException, self._undo_service.undo)
        self._undo_service.redo()
        list_of_students = self._student_service.list_students()
        self.assertEqual(len(list_of_students), 1)
        self.assertRaises(UndoRedoException, self._undo_service.redo)

    def test_student_remove(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 913)
        self._student_service.remove('1234')
        list_of_students = self._student_service.list_students()
        self.assertEqual(len(list_of_students), 2)

    def test_student_update(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 913)
        self._student_service.update('1234', 'Alex')
        list_of_students = self._student_service.list_students()
        first_student = list_of_students[0]
        self.assertEqual(first_student.name, 'Alex')

    def test_assignment_add(self):
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        list_of_assignments = self._assignment_service.list_assignments()
        self.assertEqual(len(list_of_assignments), 1)
        self._undo_service.undo()
        list_of_assignments = self._assignment_service.list_assignments()
        self.assertEqual(len(list_of_assignments), 0)
        self.assertRaises(UndoRedoException, self._undo_service.undo)
        self._undo_service.redo()
        list_of_assignments = self._assignment_service.list_assignments()
        self.assertEqual(len(list_of_assignments), 1)
        self.assertRaises(UndoRedoException, self._undo_service.redo)

    def test_assignment_remove(self):
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._assignment_service.remove('A123')
        list_of_assignments = self._assignment_service.list_assignments()
        self.assertEqual(len(list_of_assignments), 2)

    def test_assignment_update(self):
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._assignment_service.update('A123', date(2021, 4, 4))
        list_of_assignments = self._assignment_service.list_assignments()
        first_assignment = list_of_assignments[0]
        self.assertEqual(first_assignment.deadline, date(2021, 4, 4))

    def test_grades_add(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 913)
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._grade_service.add_grade('A123', '1234', 6.9)
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 1)
        self._undo_service.undo()
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 0)
        self._undo_service.redo()
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 1)
        self.assertRaises(UndoRedoException, self._undo_service.redo)

    def test_grade_remove_by_student(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 913)
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._grade_service.add_grade('A123', '1234', 6.9)
        list_of_grades = self._grade_service.remove_by_student('1234')
        self.assertEqual(len(list_of_grades), 1)

    def test_grade_remove_by_assignment(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 913)
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._grade_service.add_grade('A123', '1234', 6.9)
        list_of_grades = self._grade_service.remove_by_assignment('A123')
        self.assertEqual(len(list_of_grades), 1)

    def test_if_graded(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 913)
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._grade_service.add_grade('A123', '1234', 6.9)
        self.assertTrue(self._grade_service.is_graded('1234', 'A123'))
        self.assertFalse(self._grade_service.is_graded('1234', 'A124'))

    def test_grading(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 913)
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._grade_service.add_grade_without_record('A123', '1234', 7.0)
        self._grade_service.add_grade_without_record('A124', '1234')
        ungraded_assignments = self._grade_service.show_student_assignments('1234')
        self.assertEqual(len(ungraded_assignments), 1)
        grades_average = self._grade_service.calculate_average('1234')
        self.assertEqual(grades_average, 7.0)
        self._grade_service.give_grade('A124', '1234', 9.0)
        grades_average = self._grade_service.calculate_average('1234')
        self.assertEqual(grades_average, 8.0)
        self._undo_service.undo()
        grades_average = self._grade_service.calculate_average('1234')
        self.assertEqual(grades_average, 7.0)
        self.assertRaises(RepositoryException, self._grade_service.give_grade_without_record, 'A123', '1236', 10.0)

    def test_add_grade_to_group(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 911)
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._grade_service.add_grade_to_group('A123', 911)
        grades_list = self._grade_service.list_grades()
        self.assertEqual(len(grades_list), 2)
        self.assertRaises(EntityException, self._grade_service.add_grade_to_group, 'A123', 920)

    def test_first_statistic(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 911)
        self._assignment_service.add('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add('A125', 'description three', date(2022, 3, 3))
        self._grade_service.add_grade_without_record('A123', '1234', 7.5)
        statistic_result = self._grade_service.first_statistic('A123')
        self.assertEqual(len(statistic_result), 1)
        self.assertEqual(str(statistic_result[0]), 'Student 1234 got 7.5 for this assignment.')
        self._grade_service.add_grade_without_record('A124', '1235')
        statistic_result = self._grade_service.first_statistic('A124')
        self.assertEqual(str(statistic_result[0]), "Student 1235 hasn't been graded yet.")
        self.assertRaises(RepositoryException, self._grade_service.first_statistic, 'A999')

    def test_second_statistic(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._student_service.add('1236', 'Mary', 911)
        self._assignment_service.add_without_record('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add_without_record('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add_without_record('A125', 'description three', date(2019, 3, 3))
        self._grade_service.add_grade_without_record('A123', '1234', 7.5)
        statistic_results = self._grade_service.second_statistic()
        self.assertEqual(len(statistic_results), 0)
        self._grade_service.add_grade('A125', '1236')
        statistic_results = self._grade_service.second_statistic()
        self.assertEqual(len(statistic_results), 1)
        self.assertEqual(str(statistic_results[0]), "The Student 1236 is late for Assignment A125")

    def test_third_statistic(self):
        self._student_service.add('1234', 'Michael', 911)
        self._student_service.add('1235', 'John', 912)
        self._assignment_service.add_without_record('A123', 'description three', date(2019, 3, 3))
        self._assignment_service.add_without_record('A124', 'description two', date(2022, 2, 2))
        self._grade_service.add_grade_without_record('A123', '1234', 7.5)
        statistic_results = self._grade_service.third_statistic()
        self.assertEqual(len(statistic_results), 1)
        self.assertEqual(str(statistic_results[0]), 'Student 1234 has an average grade of 7.5')
        self._grade_service.add_grade_without_record('A123', '1235')
        statistic_results = self._grade_service.third_statistic()
        self.assertEqual(str(statistic_results[1]), "Student 1235 doesn't have any grades yet.")

    def test_cascading_undo_assignments(self):
        self._student_service.add_without_record('1234', 'Michael', 911)
        self._student_service.add_without_record('1235', 'John', 912)
        self._student_service.add_without_record('1236', 'Mary', 911)
        self._assignment_service.add_without_record('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add_without_record('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add_without_record('A125', 'description three', date(2019, 3, 3))
        self._grade_service.add_grade_without_record('A123', '1234', 9.0)
        self._grade_service.add_grade_without_record('A123', '1235', 8.0)
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 2)
        self._assignment_service.remove('A123')
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 0)
        self._undo_service.undo()
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 2)

    def test_cascading_undo_students(self):
        self._student_service.add_without_record('1234', 'Michael', 911)
        self._student_service.add_without_record('1235', 'John', 912)
        self._student_service.add_without_record('1236', 'Mary', 911)
        self._assignment_service.add_without_record('A123', 'description one', date(2022, 1, 1))
        self._assignment_service.add_without_record('A124', 'description two', date(2022, 2, 2))
        self._assignment_service.add_without_record('A125', 'description three', date(2019, 3, 3))
        self._grade_service.add_grade_without_record('A123', '1234', 7.8)
        self._grade_service.add_grade_without_record('A125', '1234', 8.4)
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 2)
        self._student_service.remove('1234')
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 0)
        self._undo_service.undo()
        list_of_grades = self._grade_service.list_grades()
        self.assertEqual(len(list_of_grades), 2)