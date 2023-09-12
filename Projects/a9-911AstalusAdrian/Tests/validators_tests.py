import unittest
from datetime import date
from Exceptions import RepositoryException, EntityException
from Entities.entities import Student, Assignment, Grade
from Repositories.student_repository import StudentRepository
from Repositories.assignment_repository import AssignmentRepository
from Repositories.grade_repository import GradesRepository
from Validators.validators import StudentValidator, AssignmentValidator, GradesValidator


class TestStudentValidator(unittest.TestCase):
    def setUp(self):
        self._validator = StudentValidator()
        self._student_one = Student('12345', 'Johnny', 911)
        self._student_two = Student('1234', 'Ant0n10', 915)
        self._student_three = Student('1234', 'Mike', 920)
        self._student_four = Student('1234', '', 912)

    def test_validate_students(self):
        self.assertRaises(EntityException, self._validator.validate, self._student_one)
        self.assertRaises(EntityException, self._validator.validate, self._student_two)
        self.assertRaises(EntityException, self._validator.validate, self._student_three)
        self.assertRaises(EntityException, self._validator.validate, self._student_four)


class TestAssignmentValidator(unittest.TestCase):
    def setUp(self):
        self._validator = AssignmentValidator()
        self._assignment_one = Assignment('B2345', 'short description', date(2022, 1, 1))
        self._assignment_two = Assignment('A123', '', date(2022, 1, 1))
        self._assignment_three = Assignment('A125', 'another short description', date(2019, 1, 1))

    def test_validate_assignments(self):
        self.assertRaises(EntityException, self._validator.validate, self._assignment_one)
        self.assertRaises(EntityException, self._validator.validate, self._assignment_two)
        self.assertRaises(EntityException, self._validator.validate, self._assignment_three)


class TestGradesValidator(unittest.TestCase):
    def setUp(self):
        self._student_repository = StudentRepository()
        self._assignment_repository = AssignmentRepository()
        self._validator = GradesValidator(self._assignment_repository, self._student_repository)
        self._student_repository.add_student(Student('1234', 'Dan', 911))
        self._assignment_repository.add_assignment(Assignment('A123', 'description', date(2022, 1, 1)))
        self._grade_one = Grade('A123', '4567', 7.5)
        self._grade_two = Grade('A777', '1234', 9.9)
        self._grade_three = Grade('A123', '1234', 12.5)

    def test_grades_validation(self):
        self.assertRaises(EntityException, self._validator.validate, self._grade_one)
        self.assertRaises(EntityException, self._validator.validate, self._grade_two)
        self.assertRaises(EntityException, self._validator.validate, self._grade_three)