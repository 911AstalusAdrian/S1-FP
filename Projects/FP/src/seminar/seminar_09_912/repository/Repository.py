from seminar.seminar_09_912.repository.RepositoryException import RepositoryException

'''
UML field visibility
    + means public (everyone can call)
    # means protected (can be called in same package or from derived classes)
    - means private (cannot be called from outside of class)
    
Java/C++/C#
    you have keywords (public, protected, private)
Python
    _, __ implicit protected or private
    doesn't start with - means public

CarTextRepo inherits from Repository

class CarTextRepo(Repository):
    pass
    
What does this means?
    - CarTextRepo has all the attributes, properties and methods of the Repository class
    - isinstance(car_text_repo, Repository) -> True
    - wherever you've used Repository for storing cars, you should get away with using CarTextRepo
    
CarTextRepo
    - stores Car instances in a text file
    - text file name provided through class constructor
    - _load_file -> called on program start up (in class constrcutor)
    - _save_file -> called on every car change  

What you need to do (for attendance, bonus?)
    1. Implement the given class diagram
        1 set of Repositories based on text-files
        1 set of Repositories based on Pickle
    2. Integrate both into seminar_09_912
        (run the Undo*Example, only without the undo)
    3. Upload into seminar repo, seminar_10 folder
'''

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
