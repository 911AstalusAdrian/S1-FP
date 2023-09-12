from Entities.entities import Student
from Repositories.student_repository import StudentRepository


class TextStudentRepository(StudentRepository):
    def __init__(self, file_name='student.txt'):
        super().__init__()
        self._file_name = file_name
        self._load()

    def add_student(self, student):
        added_student = student = super().add_student(student)
        self._save()
        return added_student

    def remove_student(self, id_):
        removed_student = super().remove_student(id_)
        self._save()
        return removed_student

    def update_student(self, id_, new_name_):
        student_previous_name = super().update_student(id_, new_name_)
        self._save()
        return student_previous_name

    def _save(self):
        file = open(self._file_name, 'wt')
        for student in self._student_data:
            line = student.id + ';' + student.name + ';' + str(student.group)
            file.write(line)
            file.write('\n')
        file.close()

    def _load(self):
        file = open(self._file_name, 'rt')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.split(';')
            super().add_student(Student(line[0], line[1], int(line[2])))
