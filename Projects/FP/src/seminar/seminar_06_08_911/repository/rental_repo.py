from seminar.seminar_06_08_911.domain.rental import Rental
from seminar.seminar_06_08_911.domain.client import Client
from seminar.seminar_06_08_911.domain.car import Car

import datetime


class RentalRepositoryException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class RentalRepository:
    def __init__(self, rentals=None):
        self._data = {}
        if rentals is not None:
            self.add_all(rentals)

    def add_all(self, rentals):
        for rental in rentals:
            self.data[rental.id] = rental

    @property
    def data(self):
        return self._data

    def add(self, rental):
        self.data[rental.id] = rental

    def remove(self, rental_id):
        if rental_id in self.data:
            del self.data[rental_id]
        else:
            raise RentalRepositoryException("Rental was not found")

    def get(self, rental_id):
        if rental_id not in self._data:
            raise RentalRepositoryException("Rental was not found")
        else:
            return self._data[rental_id]

    def get_loaded_repo():
        rentals = {
            1: Rental(1, Car(), Client(1, "teo", 12), datetime.datetime.now(),
                      datetime.datetime.now() + datetime.timedelta(15))
        }
        return RentalRepository(rentals)

    def test_add_rental():
        rentalRepo = get_loaded_repo()
        rental = Rental(1, Car(), Client(2, "andrew", 15), datetime.datetime.now(),
                        datetime.datetime.now() + datetime.timedelta(15))
        rentalRepo.add(rental)
        added_rental = rentalRepo.get(rental.id)
        assert added_rental.id == rental.id
        assert added_rental.client.id == rental.client.id
        assert added_rental.car.id == rental.car.id

    def test_remove_rental():
        rentalRepo = get_loaded_repo()
        rentalRepo.remove(1)
        foundRental = rentalRepo.get(1)
        assert foundRental == None
        try:
            rentalRepo.remove(1)
            assert False
        except RentalRepositoryException:
            pass


class RentalRepoList:
    def __init__(self, rentals=None):
        self._rentals = []
        # self._validator = validator
        if rentals is not None:
            self._rentals = rentals

    @property
    def rentals(self):
        return self._rentals

    def add_rental(self, rental):
        '''
        Add a rental object to the rentals list
        The object is already validated in the RentalService so we just add it to the list
        '''
        self._rentals.append(rental)

    def search_rental_by_id(self, id):
        """
        Identifies a rental object based on its id and returns it (?)
        """
        for rental in self._rentals:
            # TODO Replace with rentals's ID property
            if id == rental._rental_id:  # to be imported from rental class I guess
                return rental  # rental is an object consisting of rental_id,client_id, car_license, start_date, end_date
        return None

    def remove_rental(self, rental_id):
        """
        Remove a rental object based on its id
        Id is given from RentalService I guess?
        """
        rental_object = self.search_rental_by_id(rental_id)
        if rental_object is None:
            raise ValueError("Rental not in the list")  # not ok, should modify it based on the RentalException
        self._rentals.remove(rental_object)


def test_repo():
    rent_repo = RentalRepo()
    # need a rental object to add it to the rent_repo
