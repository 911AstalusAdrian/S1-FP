from seminar.seminar_09_913.repository.RepositoryException import RepositoryException

"""
Seminar 10
    UML class diagrams 
    Working with files (text + binary files)
    Practice using inheritance

UML class diagram - visibility modifiers
    + public (field can be accessed from anywhere)
    # protected (field can be accessed from derived classes, or the same package)
    - private (field can be accessed only from within the class)
C#/C++/Java
    public, protected, private - keywords
Python
    _, __         -> private, maybe protected
    no underscore -> public
    
    class CarTextRepo(Repository):
        pass

Inheritance - what does it mean?
    - CarTextRepo has all the attributes, properties and methods of Repository
    - isinstance(CarTextRepo, Repository) -> True
    - allows to reuse code
    - modules <-> independent, interchangeable

What should you do (attendance / seminar bonus)
    1. Start with seminar 9 example 
    2. Implement text file repos
    3. Implement binary file repo (using pickle?)
    4. Make UndoExample* work with file-based repositories
        a. With minimal changes to source code 
        b. Decide based on the contents of a .properties file (example in A9)
"""


class Repository:
    """
    Repository for storing IDObject instances
    """

    def __init__(self):
        self._objects = []

    def store(self, obj):
        if self.find(obj.id) != None:
            raise RepositoryException("Element having id=" + str(obj.id) + " already stored!")
        self._objects.append(obj)

    def update(self, object):
        """
        Update the instance given as parameter. The provided instance replaces the one having the same ID
        object - The object that will be updated
        Raises RepositoryException in case the object is not contained within the repository
        """
        el = self.find(object.id)
        if el == None:
            raise RepositoryException("Element not found!")
        idx = self._objects.index(el)
        self._objects.remove(el)
        self._objects.insert(idx, object)

    def find(self, objectId):
        for e in self._objects:
            if objectId == e.id:
                return e
        return None

    def delete(self, objectId):
        """
        Remove the object with given objectId from repository
        objectId - The objectId that will be removed
        Returns the object that was removed
        Raises RepositoryException if object with given objectId is not contained in the repository
        """
        object = self.find(objectId)
        if object == None:
            raise RepositoryException("Element not in repository!")
        self._objects.remove(object)
        return object

    def getAll(self):
        return self._objects;

    def __len__(self):
        return len(self._objects)

    def __str__(self):
        r = ""
        for e in self._objects:
            r += str(e)
            r += "\n"
        return r
