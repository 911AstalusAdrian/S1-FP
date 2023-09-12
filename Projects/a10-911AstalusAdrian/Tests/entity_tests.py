import unittest
from datetime import date
from Entities.entities import Student, Assignment, Grade


class TestStudentEntity(unittest.TestCase):
    def setUp(self):
        print('Testing Student entity...')

    def test_student_entity(self):
        student_one = Student('1234', 'John', 911)
        student_two = Student('4321', 'Mary', 912)
        self.assertEqual(student_one.id, '1234')
        self.assertEqual(student_one.name, 'John')
        self.assertEqual(student_one.group, 911)
        self.assertEqual(student_two.id, '4321')
        self.assertEqual(student_two.name, 'Mary')
        self.assertEqual(student_two.group, 912)
        self.assertEqual(str(student_two), 'Student Id: 4321 | Name: Mary       | Group: 912')
        student_one.id = '6789'
        student_one.name = 'Mark'
        student_one.group = 915
        self.assertEqual(student_one.id, '6789')
        self.assertEqual(student_one.name, 'Mark')
        self.assertEqual(student_one.group, 915)
        self.assertNotEqual(student_one, student_two)

    def tearDown(self):
        print('Student class all good!')


class TestAssignmentEntity(unittest.TestCase):
    def setUp(self):
        print('Testing Assignment class...')

    def test_assignment_entity(self):
        assignment_one = Assignment('A123', 'test description one', date(2021, 2, 14))
        assignment_two = Assignment('A678', 'another test description', date(2021, 3, 17))
        self.assertEqual(assignment_one.id, 'A123')
        self.assertEqual(assignment_one.description, 'test description one')
        self.assertEqual(assignment_one.deadline, date(2021, 2, 14))
        self.assertEqual(assignment_two.id, 'A678')
        self.assertEqual(assignment_two.description, 'another test description')
        self.assertEqual(assignment_two.deadline, date(2021, 3, 17))
        self.assertEqual(str(assignment_one), 'Assignment ID: A123 | Description: test description one         | Deadline: 2021-02-14')
        assignment_one.id = 'A456'
        assignment_one.description = 'I have no description ideas, it is 11pm'
        assignment_one.deadline = date(2022, 12, 25)
        self.assertEqual(assignment_one.id, 'A456')
        self.assertEqual(assignment_one.description, 'I have no description ideas, it is 11pm')
        self.assertEqual(assignment_one.deadline, date(2022, 12, 25))
        self.assertNotEqual(assignment_one, assignment_two)

    def tearDown(self):
        print('Assignment class all good.')


class TestGradesEntity(unittest.TestCase):
    def setUp(self):
        print('Testing Grade class...')

    def test_grade_entity(self):
        grade_one = Grade('A123', '1234', 7.5)
        grade_two = Grade('A456', '5678', 9.9)
        self.assertEqual(grade_one.assignment_id, 'A123')
        self.assertEqual(grade_two.assignment_id, 'A456')
        self.assertEqual(grade_one.student_id, '1234')
        self.assertEqual(grade_two.student_id, '5678')
        self.assertEqual(grade_one.grade_value, 7.5)
        self.assertEqual(grade_two.grade_value, 9.9)
        self.assertEqual(str(grade_one), 'Assignment ID: A123 | Student ID: 1234 | Grade: 7.5')
        grade_one.assignment_id = 'A789'
        grade_one.student_id = '2468'
        grade_one.grade_value = 0.0
        self.assertEqual(grade_one.assignment_id, 'A789')
        self.assertEqual(grade_one.student_id, '2468')
        self.assertEqual(grade_one.grade_value, 0.0)
        self.assertNotEqual(grade_one, grade_two)
        self.assertEqual(str(grade_one), 'Assignment ID: A789 | Student ID: 2468 | Grade: Not graded yet')

    def tearDown(self):
        print("Grade class all good.")
