

from Entities.entities import Assignment
from Repositories.assignment_repository import AssignmentRepository


class TextAssignmentRepository(AssignmentRepository):
    def __init__(self, file_name='assignment.txt'):
        super().__init__()
        self._file_name = file_name
        self._load()

    def add_assignment(self, assignment):
        added_assignment = super().add_assignment(assignment)
        self._save()
        return added_assignment

    def remove_assignment(self, id_):
        removed_assignment = super().remove_assignment(id_)
        self._save()
        return removed_assignment

    def update_assignment_repository(self, id_, new_deadline_):
        previous_deadline = super().update_assignment_repository(id_, new_deadline_)
        self._save()
        return previous_deadline

    def _save(self):
        file = open(self._file_name, 'wt')
        for assignment in self._assignment_data:
            line = assignment.assignment_id + ';' + assignment.assignment_description + ';' + str(assignment.assignment_deadline)
            file.write(line)
            file.write('\n')
        file.close()

    def _load(self):
        file = open(self._file_name, 'rt')
        lines = file.readlines()
        file.close()
        for line in lines:
            new_line = line.split(';')
            if len(new_line) == 1:
                continue
            assignment_name = new_line[0]
            assignment_description = new_line[1]
            remove_endline = new_line[2].split("\n")
            assignment_deadline = remove_endline[0]
            super().add_assignment(Assignment(assignment_name, assignment_description, assignment_deadline))
