"""
Created on Nov 17, 2018

@author: Arthur
"""
from seminar.seminar_09_913.domain.Car import CarValidator
from seminar.seminar_09_913.domain.Client import ClientValidator
from seminar.seminar_09_913.domain.Rental import RentalValidator
from seminar.seminar_09_913.repository.Repository import Repository
from seminar.seminar_09_913.service.CarService import CarService
from seminar.seminar_09_913.service.ClientService import ClientService
from seminar.seminar_09_913.service.RentalService import RentalService
from seminar.seminar_09_913.service.UndoService import UndoService
from seminar.seminar_09_913.util import print_repos_with_message

'''
efficiency vs. flexibility (CSA vs. FP)
computational complexity vs. memory

At each operation we keep a snapshot of the repo(s) --> Memento design pattern
    + easy to implement
    - lot of memory required

At each operation remember the difference between now and before --> state diffing (SVN?)
    + little memory required
    - complicated

Undo/redo using the command design pattern
    design pattern -> like a recipe that we apply for a lot of common problems
    Command design pattern -> telling the program to do something at a later time
    
    + little memory
    - so-so complicated ?
'''


def undo_example_medium():
    undo_service = UndoService()
    client_repo = Repository()
    car_repo = Repository()

    '''
    Start rental Controller
    '''
    rent_repo = Repository()
    rent_validator = RentalValidator()
    rent_service = RentalService(undo_service, rent_validator, rent_repo, car_repo, client_repo)

    '''
    Start client Controller
    '''
    client_validator = ClientValidator()
    client_service = ClientService(undo_service, rent_service, client_validator, client_repo)

    '''
    Start car Controller
    '''
    car_validator = CarValidator()
    car_service = CarService(undo_service, rent_service, car_validator, car_repo)

    '''
    We add 3 clients
    '''
    sophia = client_service.create(103, "2990511035588", "Sophia")
    carol = client_service.create(104, "2670511035588", "Carol")
    bob = client_service.create(105, "2590411035588", "Bob")
    print_repos_with_message("We added 3 clients", client_repo, None, None)

    '''
    We delete 2 of the clients
    '''
    client_service.delete(103)
    client_service.delete(105)
    print_repos_with_message("Deleted Sophia and Bob", client_repo, None, None)

    '''
    We undo twice
    '''
    undo_service.undo()
    print_repos_with_message("1 undo, so Bob is back", client_repo, None, None)
    undo_service.undo()
    print_repos_with_message("Another undo, so Sophia is back too", client_repo, None, None)

    '''
    We redo once
    '''
    undo_service.redo()
    print_repos_with_message("1 redo, so Sophia is again deleted", client_repo, None, None)


undo_example_medium()
