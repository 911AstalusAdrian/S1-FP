from seminar.seminar_09_911.repository.RepositoryException import RepositoryException


"""
Seminar 10
    UML class diagrams
    Work with Files (text + binary)
        easy mode -> files (.txt, binary, .xml, .json)
        real mode -> database (SQL or NoSQL) 
    Apply inheritance (reuse source code, modules are interchageable etc.)

we will use the seminar 9 started code

Attribute/method visibility in UML diagrams
    + public (can be called / accessed by any class)
    # protected (can be called from derived classes, or the same package)
    - private (can be called only from inside the class)

Java/C++/C#
    private, protected, public - keywords
Python
    _, __ -> private, protected
    no underscore -> public
    
CarTextRepo
    - inherits from Repository class 
        1. isinstance(CarTextRepo, Repository) -> True
        2. all attributes, prperties, methods of class Repository are also in CarTextRepo
        
        class CarTextRepo(Repository):
            pass
    - adds attribute _file_name and methods _load_file() and _save_file (all private)

RentalTextRepo
    - dependency to CarTextRepo and ClientTextRepo (!?)
     
Seminar 10 TODO:
    Run the UndoExample*.py code using any of the following repo sets:
        a. In memory (Repository class) the way it is now
        b. Text files (CarTextRepo etc) - needs to be implemented
        c. Binary files (PickleFileRepo) - needs to be implemented
    We should be able to change the set of repositories easily
        step 1. update some source code
        step 2. using a .properties file
        
    File-based repositories:
        - load the input file in constructor
        - save changes to repo after each operation
        - otherwise indistinguishable from Repository class (allows interchanging them)
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
