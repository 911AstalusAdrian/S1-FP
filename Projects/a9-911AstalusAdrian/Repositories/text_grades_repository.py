from Entities.entities import Grade
from Repositories.grade_repository import GradesRepository


class TextGradesRepository(GradesRepository):
    def __init__(self, file_name='grade.txt'):
        super().__init__()
        self._file_name = file_name
        self._load()

    def add_grade(self, grade):
        added_grade = super().add_grade(grade)
        self._save()
        return added_grade

    def remove_by_student(self, student_id):
        removed_grade = super().remove_by_student(student_id)
        self._save()
        return removed_grade

    def remove_by_assignment(self, id_):
        removed_grade = super().remove_by_assignment(id_)
        self._save()
        return removed_grade

    def update_grade(self, assignment_id, student_id, assignment_grade):
        super().update_grade(assignment_id, student_id, assignment_grade)
        self._save()

    def _save(self):
        file = open(self._file_name, 'wt')
        for grade in self._grades_data:
            line = grade.grade_assignment_id + ';' + grade.grade_student_id + ';' + str(grade.grade_value)
            file.write(line)
            file.write('\n')
        file.close()

    def _load(self):
        file = open(self._file_name, 'rt')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.split(';')
            super().add_grade(Grade(line[0], line[1], float(line[2])))
