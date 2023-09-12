from Repositories.student_repository import StudentRepository
import pickle


class PickleStudentRepository(StudentRepository):
    def __init__(self, file_name='student.pickle'):
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

    def add_student(self, student):
        added_student = super().add_student(student)
        data = super().get_all_students()
        self._save(data)
        return added_student

    def remove_student(self, id_):
        removed_student = super().remove_student(id_)
        data = super().get_all_students()
        self._save(data)
        return removed_student

    def update_student(self, id_, new_name):
        student_previous_name = super().update_student(id_, new_name)
        data = super().get_all_students()
        self._save(data)
        return student_previous_name
