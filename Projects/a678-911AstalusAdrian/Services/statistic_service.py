
class StudentGradeForAssignment:

    def __init__(self, student_id, student_grade):
        self._student_id = student_id
        self._grade = student_grade

    @property
    def student_id(self):
        return self._student_id

    @property
    def grade(self):
        return self._grade

    def __str__(self):
        if self.grade == 0.0:
            return "Student " + str(self.student_id) + " hasn't been graded yet."
        else:
            return "Student " + str(self.student_id) + " got " + str(self.grade) + " for this assignment."


class LateStudents:

    def __init__(self, student_id, assignment_id):
        self._student = student_id
        self._assignment = assignment_id

    @property
    def student(self):
        return self._student

    @property
    def assignment(self):
        return self._assignment

    def __str__(self):
        return "The Student " + str(self.student) + " is late for Assignment " + str(self.assignment)


class SchoolSituation:

    def __init__(self, student_id, average_grade):
        self._student_id = student_id
        self._average_grade = average_grade

    @property
    def student_id(self):
        return self._student_id

    @property
    def average_grade(self):
        return self._average_grade

    def __str__(self):
        if self._average_grade == 0.0:
            return "Student " + str(self.student_id) + " doesn't have any grades yet."
        else:
            return "Student " + str(self.student_id) + " has an average grade of " + str(self.average_grade)
