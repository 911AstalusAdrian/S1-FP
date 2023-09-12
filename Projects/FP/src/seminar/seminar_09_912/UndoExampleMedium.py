"""
Created on Nov 17, 2018

@author: Arthur
"""
from seminar.seminar_09_912.domain.Car import CarValidator
from seminar.seminar_09_912.domain.Client import ClientValidator
from seminar.seminar_09_912.domain.Rental import RentalValidator
from seminar.seminar_09_912.repository.Repository import Repository
from seminar.seminar_09_912.service.CarService import CarService
from seminar.seminar_09_912.service.ClientService import ClientService
from seminar.seminar_09_912.service.RentalService import RentalService
from seminar.seminar_09_912.service.UndoService import UndoService
from seminar.seminar_09_912.util import print_repos_with_message

"""
How to implement Undo / Redo
-> The kind of problem that shows up in many programs => design patterns (like a recipe) to the resQ !!!!

1. Before each operation, deep copy the repository(ies) - similar to Memento pattern
    + easy to implement (A3-4 solution)
    - requires a lot of memory 

2. Memento++ is state diffing ('remember' the difference in state before/after repos) 
    + memory-efficient
    - complex implemenetation (you have to know what the state is)

3. 'Remember' the operation and how to undo/redo it => Command design pattern
    + memory-efficient
    - more complex than 1., but less than 2

Car 
Client
Rental -> linked entity with a Car and a Client
"""

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
