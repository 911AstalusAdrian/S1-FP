class RepositoryException(Exception):
    """
    Error class for the Repositories
    """
    def __init__(self, message=''):
        self._message = message

    def __str__(self):
        return self._message


class EntityException(Exception):
    """
    Error class for the Entities
    """
    def __init__(self, message=''):
        self._message = message

    def __str__(self):
        return self._message

class UndoRedoException(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message