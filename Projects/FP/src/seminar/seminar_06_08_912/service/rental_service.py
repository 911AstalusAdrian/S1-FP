from seminar.seminar_06_08_912.domain.exceptions import CarException
from seminar.seminar_06_08_912.domain.rental import Rental


class RentalService:
    """
    Controller for rental operations
    """

    def __init__(self, validator, rental_repo, car_repo, client_repo):
        self._validator = validator
        self._repository = rental_repo
        self._carRepo = car_repo
        self._cliRepo = client_repo

    def create_rental(self, rental_id, client, car, start, end):
        rental = Rental(rental_id, start, end, client, car)
        self._validator.validate(rental)

        '''
        Check the car's availability for the given period 
        '''
        if self.is_car_available(rental.car, rental.start, rental.end) is False:
            raise CarException("Car is not available during that time!")

        self._repository.store(rental)
        return rental

    def delete_rental(self, rental_id):
        return self._repository.delete(rental_id)

    def is_car_available(self, car, start, end):
        """
        Check the availability of the given car to be rented in the provided time period
        car - The availability of this car is verified
        start, end - The time span. The car is available if it is not rented in this time span
        Return True if the car is available, False otherwise
        """
        rentals = self.filter_rentals(None, car)
        for rent in rentals:
            if start > rent.end or end < rent.start:
                continue
            return False
        return True

    def filter_rentals(self, client, car):
        """
        Return a list of rentals performed by the provided client for the provided car
        client - The client performing the rental. None means all clients
        cars - The rented car. None means all cars 
        """
        result = []
        for rental in self._repository.get_all():
            if client is not None and rental.getClient() != client:
                continue
            if car is not None and rental.car != car:
                continue
            result.append(rental)
        return result

    def most_often_rented_car_make(self):
        """
        The list of car makes, sorted by the number of rental days
        """
        result = []

        # Compute stat using an interim dictionary
        rentals_dict = {}
        for rental in self._repository.get_all():
            if rental.car.make not in rentals_dict:
                rentals_dict[rental.car.make] = 0
            rentals_dict[rental.car.make] += len(rental)

        # Move data to sorted list of values
        for entry in rentals_dict:
            result.append(CarMakeRentalDays(entry, rentals_dict[entry]))
        # Sort the list
        # lambda <parameter list> : <function body>
        result.sort(key=lambda x: x.rental_days, reverse=True)
        return result


class CarMakeRentalDays:
    """
    Data Transfer Object for statistics
    SRP: Move data between application layers
    """

    def __init__(self, car_make, car_make_rental_days):
        self._car_make = car_make
        self._car_make_rental_days = car_make_rental_days

    @property
    def make(self):
        return self._car_make

    @property
    def rental_days(self):
        return self._car_make_rental_days

    def __str__(self):
        return self.make + ' - ' + str(self.rental_days)
