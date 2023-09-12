from Exceptions import UndoRedoException


class UndoService:
    def __init__(self):
        self._history = []
        self._index = -1

    def record(self, operation):
        self._history.append(operation)
        self._index += 1

    def undo(self):
        if self._index == -1:
            raise UndoRedoException("No op to undo")

        self._history[self._index].undo()
        self._index -= 1
        return True

    def redo(self):
        if self._index == len(self._history) - 1:
            raise UndoRedoException("No op to redo")

        self._index += 1
        self._history[self._index].redo()
        return True


class Operation:
    def __init__(self, function_call_undo, function_call_redo):
        self._function_call_undo = function_call_undo
        self._function_call_redo = function_call_redo

    def undo(self):
        self._function_call_undo()

    def redo(self):
        self._function_call_redo()


class FunctionCall:
    def __init__(self, function_ref, *function_parameters):
        self._function_ref = function_ref
        self._function_parameters = function_parameters

    def call(self):
        return self._function_ref(*self._function_parameters)

    def __call__(self):
        return self.call()
