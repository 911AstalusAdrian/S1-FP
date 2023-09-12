import unittest
from datetime import date
from Exceptions import RepositoryException
from Repositories.assignment_repository import AssignmentRepository
from Repositories.student_repository import StudentRepository
from Repositories.grade_repository import GradesRepository
from Entities.entities import Student, Assignment, Grade


class TestStudentRepository(unittest.TestCase):
    def setUp(self):
        self._student_repository = StudentRepository()
        self._student_repository.add_student(Student('1234', 'Mike', 913))
        self._student_repository.add_student(Student('1235', 'Lucas', 917))
        self._student_repository.add_student(Student('1236', 'Anna', 915))
        self._student_repository.add_student(Student('1237', 'Mary', 911))
        self._student_list = self._student_repository.get_all_students()

    def test_repository_store(self):
        self.assertEqual(self._student_repository.get_number_of_students(), 4)
        self.assertRaises(RepositoryException, self._student_repository.add_student, Student('1234', 'John', 913))

    def test_repository_remove(self):
        self._student_repository.remove_student('1234')
        self.assertEqual(self._student_repository.get_number_of_students(), 3)
        self.assertRaises(RepositoryException, self._student_repository.remove_student, '9999')

    def test_search_student(self):
        self.assertTrue(self._student_repository.search_student_id('1235'))
        self.assertFalse(self._student_repository.search_student_id('1231'))

    def test_update_student(self):
        self._student_repository.update_student('1234', 'Miguel')
        self.assertEqual(self._student_list[0].student_name, 'Miguel')
        self.assertRaises(RepositoryException, self._student_repository.update_student, '1239', 'Miguel')

    def test_get_student_by_id(self):
        self.assertIsNone(self._student_repository.get_student_by_id('7895'))
        self.assertEqual(self._student_repository.get_student_by_id('1234'), self._student_list[0])

    def test_get_random_id(self):
        student_id = int(self._student_repository.get_random_id())
        self.assertGreaterEqual(student_id, 1234)
        self.assertLessEqual(student_id, 1237)


class TestAssignmentRepository(unittest.TestCase):
    def setUp(self):
        self._assignment_repository = AssignmentRepository()
        self._assignment_repository.add_assignment(Assignment('A123', 'First description', date(2022, 3, 17)))
        self._assignment_repository.add_assignment(Assignment('A124', 'Second description', date(2022, 4, 16)))
        self._assignment_repository.add_assignment(Assignment('A125', 'Third description', date(2022, 6, 15)))
        self._assignment_repository.add_assignment(Assignment('A126', 'Fourth description', date(2021, 8, 14)))
        self._assignment_list = self._assignment_repository.get_all_assignments()

    def test_repository_store(self):
        self.assertEqual(self._assignment_repository.get_number_of_assignments(), 4)
        self.assertRaises(RepositoryException, self._assignment_repository.add_assignment, Assignment('A123', 'Test Description', date.today()))

    def test_repository_remove(self):
        self._assignment_repository.remove_assignment('A123')
        self.assertEqual(self._assignment_repository.get_number_of_assignments(), 3)
        self.assertRaises(RepositoryException, self._assignment_repository.remove_assignment, 'A999')

    def test_search_assignment(self):
        self.assertTrue(self._assignment_repository.search_assignment_id('A124'))
        self.assertFalse(self._assignment_repository.search_assignment_id('A999'))

    def test_update_assignment(self):
        self._assignment_repository.update_assignment_repository('A123', date(2021, 1, 1))
        self.assertEqual(self._assignment_repository.get_assignment_deadline('A123'), date(2021, 1, 1))
        self.assertRaises(RepositoryException, self._assignment_repository.update_assignment_repository, 'A999', date.today())

    def test_get_assignment_by_id(self):
        self.assertIsNone(self._assignment_repository.get_assignment_by_id('A999'))
        self.assertEqual(self._assignment_repository.get_assignment_by_id('A123'), self._assignment_list[0])

    def test_get_random_id(self):
        assignment_id = self._assignment_repository.get_random_id()
        assignment_id = int(assignment_id[1:])
        self.assertGreaterEqual(assignment_id, 123)
        self.assertLessEqual(assignment_id, 126)


class TestGradesRepository(unittest.TestCase):
    def setUp(self):
        self._grades_repository = GradesRepository()
        self._grades_repository.add_grade(Grade('A123', '1234', 1.0))
        self._grades_repository.add_grade(Grade('A456', '2345', 2.7))
        self._grades_repository.add_grade(Grade('A789', '3456', 6.5))
        self._grades_repository.add_grade(Grade('A420', '6969', 6.9))
        self._grades_repository.add_grade(Grade('A777', '9000', 0.0))
        self._grades_list = self._grades_repository.get_all_grades()

    def test_repository_store(self):
        self.assertEqual(self._grades_repository.get_number_of_grades(), 5)
        self.assertRaises(RepositoryException, self._grades_repository.add_grade, Grade('A420', '6969', 4.2))

    def test_repository_remove(self):
        self._grades_repository.remove_by_assignment('A123')
        self.assertEqual(self._grades_repository.get_number_of_grades(), 4)
        self._grades_repository.remove_by_student('2345')
        self.assertEqual(self._grades_repository.get_number_of_grades(), 3)

    def test_remove_grade(self):
        grade_to_remove = self._grades_repository.remove_grade('1234', 'A123')
        self.assertEqual(grade_to_remove.grade_value, 1.0)

    def test_searches(self):
        self.assertTrue(self._grades_repository.search_student_id('1234'))
        self.assertFalse(self._grades_repository.search_student_id('1122'))
        self.assertTrue(self._grades_repository.search_assignment_id('A123'))
        self.assertFalse(self._grades_repository.search_assignment_id('A787'))
        self.assertTrue(self._grades_repository.search_if_grade_exists('A123', '1234'))
        self.assertFalse(self._grades_repository.search_if_grade_exists('A123', '3456'))

    def test_update_grade(self):
        self._grades_repository.update_grade('A777', '9000', 5.0)
        self.assertEqual(self._grades_list[4].grade_value, 5)
        self.assertRaises(RepositoryException, self._grades_repository.update_grade, 'A123', '1234', 10.0)
        self._grades_repository.update_grade('A123', '1234', 0.0)
        self._grades_list = self._grades_repository.get_all_grades()
        self.assertEqual(self._grades_list[0].grade_value, 0.0)

    def test_remove_last_grades(self):
        self._grades_repository.remove_last_grades(2)
        self.assertEqual(self._grades_repository.get_number_of_grades(), 3)