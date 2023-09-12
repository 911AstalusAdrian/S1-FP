from lecture.examples.ex17_happyBakery.domain.exceptions import BakeryException


class RepositoryException(BakeryException):
    def __init__(self, msg):
        # self._msg = msg
        super().__init__(msg)


class Repository:
    def __init__(self):
        self._data = []

    def store(self, item):
        """
        Store a new item into Repository
        """
        if self.find(item.id) != -1:
            raise RepositoryException("Item with id=" + str(item.id) + " already in repo.")
        self._data.append(item)

    def delete(self, id_):
        """
        Delete item with given ID from repository
        """
        index = self.find(id_)
        if index == -1:
            raise RepositoryException("Item with ID=" + str(id_) + " not in repo.")
        del self._data[index]

    def find(self, id_):
        """
        Find item having given ID
        """
        for i in range(len(self._data)):
            if self._data[i].id == id_:
                return i
        return -1

    def __getitem__(self, id_):
        """
        Override the [] operator
        Return the stored element having the given ID
        Raise BakeryException if element not contained in the repo
        """
        for elem in self._data:
            if elem.id == id_:
                return elem
        raise RepositoryException("Entity not found. ID=", id_)

    def __str__(self):
        result = "Repository:\n"
        for entity in self._data:
            result += str(entity)
            result += '\n'
        return result

    def __len__(self):
        return len(self._data)
