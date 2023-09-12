import pickle
from Repositories.assignment_repository import AssignmentRepository


class PickleAssignmentRepository(AssignmentRepository):
    def __init__(self, file_name='assignment.pickle'):
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

    def add_assignment(self, assignment):
        added_assignment = super().add_assignment(assignment)
        data = super().get_all_assignments()
        self._save(data)
        return added_assignment

    def remove_assignment(self, id_):
        removed_assignment = super().remove_assignment(id_)
        data = super().get_all_assignments()
        self._save(data)
        return removed_assignment

    def update_assignment_repository(self, id_, new_deadline):
        previous_deadline = super().update_assignment_repository(id_, new_deadline)
        data = super().get_all_assignments()
        self._save(data)
        return previous_deadline
