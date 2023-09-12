from seminar.seminar_06_08_912.domain.car import CarValidatorRO, CarValidatorES
from seminar.seminar_06_08_912.repository.CarRepository import CarRepo
from seminar.seminar_06_08_912.repository.ClientRepository import ClientRepo
from seminar.seminar_06_08_912.repository.RentalRepository import RentalRepo
from seminar.seminar_06_08_912.service.CarService import CarService
from seminar.seminar_06_08_912.service.ClientService import ClientService
from seminar.seminar_06_08_912.service.RentalService import RentalService
from seminar.seminar_06_08_912.ui.menu_ui import UI

'''
Layered Architecture
    UI(car_service, client_service, rental_service) -> UI is at the top
    
    RentalService(rental_repo, car_repo, client_repo) -> functionalities
    ClientService(client_repo)
    ClientService(client_repo)
    
    car_repo = CarRepo() -> data storage, bottom layer?
    client_repo = ClientRepo()
    rental_repo = RentalRepo()
'''

# TODO This is a later week bonus
# sql_car_repo = SQLCarRepo() # car repository backed by a SQL database


# car stuff
car_repo = CarRepo()
car_validator_ro = CarValidatorRO()
car_validator_es = CarValidatorES()
# car_service = CarService(sql_car_repo, car_validator_ro)

# client stuff
client_repo = ClientRepo()
client_service = ClientService(client_repo)

# rental stuff
rental_repo = RentalRepo()
rental_service = RentalService(rental_repo, car_repo, client_repo)

# I need to start the UI to get the program working :)
# The UI needs access to each service object
ui = UI(car_service, client_service, rental_service)
ui.start()
