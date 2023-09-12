"""
domain classes:
    Client
        id (str, unique, driver license)
        name (str)
        age (int)

    ClientValidatorRO
        validate(self, client) function
            no Client field is empty
            age >= 18
            driver license is 10 char str
            -> raise ValueError in case of problems [all validators]

    ClientValidatorUSA
        validate(self, client) function
            no Client field is empty
            age >= 21
            driver license is 2 letters + 6 digits
            -> raise ValueError in case of problems [all validators]

    test_client function
    test_client_validator function

    Car
        license (str, unique)
        make
        model
        color

    CarValidatorRO
        validate(self, car) function
            no Car field is empty
            license is leter_leter_digit_digit_letter_letter_letter
            make one of 'VW' or 'Dacia'
            -> raise ValueError in case of problems [all validators]


    CarValidatorUSA
        validate(self, car) function
            no Car field is empty
            make one of 'Dodge', 'Ford', 'Tesla'
            -> raise ValueError in case of problems [all validators]

    test_car function
    test_car_validator function

    Rental
        car - instance of Car
        client - instance of Client
        start_date, end_date - date (Python data type

    Rental_Validator
        validate(self, rental) function
            no fields are empty
            start_date in future
            end data at least 1 day after
            -> raise ValueError in case of problems [all validators]

    test_rental function
    test_rental_valdiator function

repository classes:
    CarRepositoryWithList [stores the cars in a list]
        add(self,car)
        remove(self, car_id)
        get_all(self) [return all car instasnces]

    CarRepositoryWithDict [stores the cars in a dict]
        add(self,car)
        remove(self, car_id)
        get_all(self) [return all car instasnces]

    + test_car_repository
    + test_cat_repo_init -> add 10 cars

    # CarRepositoryWithFile
    # CarRepositoryWithSQL

    ClientRepositoryWithList
        add(self,client)
        remove(self, client_id)
        get_all(self) [return all client instasnces]

    ClientRepositoryWithDict
        add(self,client)
        remove(self, client_id)
        get_all(self) [return all client instasnces]

    RentalRepositoryWithList
        add(self,rental)
        remove(self, rental_id)
        get_all(self) [return all rental instasnces]

    RentalRepositoryWithDict
        add(self,rental)
        remove(self, rental_id)
        get_all(self) [return all rental instasnces]

service classes:
    CarService
        __init__(car_repo, car_validator)
        add(self, <list of car attributes>) [car_id, car_make, bla bla...]
            a. create car instance
            b. validate it
            c. add it to car_repo
        remove(self, car_id)
        get_all(self) [return all car instasnces]
    + test_car_service

    ClientService
        __init__(client_repo, client_validator)
        add(self, <list of client attributes>)
        remove(self, client_id)
        get_all(self) [return all client instasnces]
    + test_client_service

    RentalService
        __init__(rental_repo, client_repo, car_repo, rental_validator)
        add(self, <list of rental attributes>)
        remove(self, rental_id)
        get_all(self) [return all rental instasnces]
    + test_rental_service

user interface class:
    MenuUI
        __init__(car_service, client_service, rental_service)
        start()

    CommandUI
        __init__(car_service, client_service, rental_service)
        start()
"""
from seminar.seminar_06_08_913.Birtalan_Csaba_Adrian_console import MenuUI
from seminar.seminar_06_08_913.CarServiceBA import CarService
from seminar.seminar_06_08_913.Car_CarValidatorRO_VA import CarValidatorRO
from seminar.seminar_06_08_913.mboicu_car_repo_with_dict import CarRepositoryWithDict

car_repo = CarRepositoryWithDict()
car_valid = CarValidatorRO()
car_service = CarService(car_repo, car_valid)
ui = MenuUI(car_service, None, None)
ui.start()