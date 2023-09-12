class Student:
    def __init__(self, student_id, name, group):
        self._student_id = student_id
        self._name = name
        self._group = group

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def student_name(self):
        return self._name

    @student_name.setter
    def student_name(self, value):
        self._name = value

    @property
    def student_group(self):
        return self._group

    @student_group.setter
    def student_group(self, value):
        self._group = value

    def __str__(self):
        return 'Student Id: ' + str(self._student_id) + ' | Name: ' + str(self._name) + ' | Group: ' + str(self._group)

    def __eq__(self, other):
        return self._student_id == other._student_id


class Assignment:
    def __init__(self, assignment_id, description, deadline):
        self._assignment_id = assignment_id
        self._description = description
        self._deadline = deadline

    @property
    def assignment_id(self):
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        self._assignment_id = value

    @property
    def assignment_description(self):
        return self._description

    @assignment_description.setter
    def assignment_description(self, value):
        self._description = value

    @property
    def assignment_deadline(self):
        return self._deadline

    @assignment_deadline.setter
    def assignment_deadline(self, value):
        self._deadline = value

    def __str__(self):
        return 'Assignment ID: ' + str(self._assignment_id) + ' | Description: ' + str(self._description) + ' | Deadline: ' + str(self._deadline)

    def __eq__(self, other):
        return self._assignment_id == other._assignment_id


class Grade:
    def __init__(self, assignment_id, student_id, value):
        self._assignment_id = assignment_id
        self._student_id = student_id
        self._value = value

    @property
    def grade_assignment_id(self):
        return self._assignment_id

    @grade_assignment_id.setter
    def grade_assignment_id(self, value):
        self._assignment_id = value

    @property
    def grade_student_id(self):
        return self._student_id

    @grade_student_id.setter
    def grade_student_id(self, value):
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
            return 'Assignment ID: ' + str(self._assignment_id) + ' | Student ID: ' + str(self._student_id) + ' | Grade: Not graded yet'
        else:
            return 'Assignment ID: ' + str(self._assignment_id) + ' | Student ID: ' + str(self._student_id) + ' | Grade: ' + str(self._value)

    def __eq__(self, other):
        return self._assignment_id == other._assignment_id and self._student_id == other._student_id
