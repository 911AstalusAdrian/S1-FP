"""
    Assemble the application

"""
from seminar.seminar_06_08_911.domain.car import CarValidator
from seminar.seminar_06_08_911.domain.client import ClientValidator
from seminar.seminar_06_08_911.domain.rental import RentalValidator
from seminar.seminar_06_08_911.repository.car_repo import CarRepository
from seminar.seminar_06_08_911.repository.client_repo import ClientRepo
from seminar.seminar_06_08_911.repository.rental_repo import RentalRepo
from seminar.seminar_06_08_911.service.car_service import CarService
from seminar.seminar_06_08_911.service.client_service import ClientService
from seminar.seminar_06_08_911.service.rental_service import RentalService
from seminar.seminar_06_08_911.ui.menu import UI

"""
    What should we implement?

    1. Client class + ClientValidator class + test -> Duma Amalia
    2. Rental class + RentalValidator class + test -> Hriscu Octavia
    3. ClientRepo class using a list to store client + test -> Deac Iulian
    4. ClientRepo class using a dict to store client + test 
    5. RentalRepo class using a list to store rental + test -> Diaconu Ana-Maria
    6. RentalRepo class using a dict to store rental + test -> Filp Teodor
    7. CarService class + test -> Boda Viktoria
    8. ClientService class + test -> Arion Dan-Vasile
    9. RentalService class + test -> Albu Flaviu
    10. menu-driven UI
    11. command-driven UI 
"""



'''
    Start from the bottom and go to the top
'''
car_repo = CarRepository()
# car_file_repo = CarFileRepository()
# car_sql_repo = CarSQLRepository()


car_validator = CarValidator()
# TODO Stuff to read up on
# encapsulation
# abstraction
# dependency injection
car_service = CarService(car_repo, car_validator)

# rinse and repeat for client -> car and client entities are similar
client_repo = ClientRepo()
client_validator = ClientValidator()
client_service = ClientService(client_repo, client_validator)

#
# What about the Rental?
# 1 Rental has a link to 1 Car and to 1 Client
#
rent_repo = RentalRepo()
rent_validator = RentalValidator()
rent_service = RentalService(client_repo, car_repo, rent_repo, rent_validator)

ui = UI(client_service, car_service, rent_service)
ui.start()