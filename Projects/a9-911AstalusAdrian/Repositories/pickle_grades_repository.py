from Repositories.grade_repository import GradesRepository
import pickle

class PickleGradesRepository(GradesRepository):
    def __init__(self, file_name='grade.pickle'):
        super().__init__()
        self._file_name = file_name
        self._load()

    def _load(self):
        result = []
        try:
            file = open(self._file_name, 'rb')
            self._list = pickle.load(file)
        except EOFError:
            return []
        except IOError as error:
            print(str(error))
            raise error
        return result

    def _save(self, data):
        file = open(self._file_name, 'wb')
        pickle.dump(data, file)
        file.close()

    def add_grade(self, grade_to_add):
        added_grade = super().add_grade(grade_to_add)
        data = super().get_all_grades()
        self._save(data)
        return added_grade

    def remove_by_student(self, student_id):
        removed_grade = super().remove_by_student(student_id)
        data = super().get_all_grades()
        self._save(data)
        return removed_grade

    def remove_by_assignment(self, assignment_id):
        removed_grade = super().remove_by_student(assignment_id)
        data = super().get_all_grades()
        self._save(data)
        return removed_grade

    def update_grade(self, assignment_id, student_id, assignment_grade):
        super().update_grade(assignment_id, student_id, assignment_grade)
        data = super().get_all_grades()
        self._save(data)
