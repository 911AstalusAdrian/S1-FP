class Student:
    def __init__(self, student_id, name, group):
        self._student_id = student_id
        self._name = name
        self._group = group

    @property
    def id(self):
        return self._student_id

    @id.setter
    def id(self, value):
        self._student_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    def __str__(self):
        return 'Student Id: ' + str(self.id) + ' | Name: ' + str(self.name).ljust(10) + ' | Group: ' + str(self.group)

    def __eq__(self, other):
        return self.id == other.id


class Assignment:
    def __init__(self, assignment_id, description, deadline):
        self._assignment_id = assignment_id
        self._description = description
        self._deadline = deadline

    @property
    def id(self):
        return self._assignment_id

    @id.setter
    def id(self, value):
        self._assignment_id = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value

    def __str__(self):
        return 'Assignment ID: ' + str(self.id) + ' | Description: ' + str(self.description).ljust(28) + ' | Deadline: ' + str(self.deadline)

    def __eq__(self, other):
        return self.id == other.id


class Grade:
    def __init__(self, assignment_id, student_id, value):
        self._assignment_id = assignment_id
        self._student_id = student_id
        self._value = value

    @property
    def assignment_id(self):
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        self._assignment_id = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def grade_value(self):
        return self._value

    @grade_value.setter
    def grade_value(self, value):
        self._value = value

    def __str__(self):
        """
        The string representation of a Grade entity
        :return: The way which a Grade entity is displayed
        If the value of a grade is 0.0 (the default value), it means that a grade hasn't been given yet and we display a different message in the grade section
        """
        if self._value == 0.0:
            return 'Assignment ID: ' + str(self.assignment_id) + ' | Student ID: ' + str(self.student_id) + ' | Grade: Not graded yet'
        else:
            return 'Assignment ID: ' + str(self.assignment_id) + ' | Student ID: ' + str(self.student_id) + ' | Grade: ' + str(self.grade_value)

    def __eq__(self, other):
        return self.assignment_id == other.assignment_id and self.student_id == other.student_id
