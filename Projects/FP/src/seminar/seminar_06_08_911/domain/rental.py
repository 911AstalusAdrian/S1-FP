from datetime import date

from seminar.seminar_06_08_911.domain.car import Car
from seminar.seminar_06_08_911.domain.client import Client


class RentalException(Exception):
    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return self._msg


class RentalValidationException(RentalException):
    def __init__(self, error_list):
        self._errors = error_list

    @property
    def errors(self):
        # Gives access to the list of errors
        return self._errors

    def __str__(self):
        # str representation
        result = ''
        for e in self.errors:
            result += e
            result += '\n'
        return result


class Rental:
    def __init__(self, rental_id, client, car, start_date, end_date):
        self._rental_id = rental_id
        self._client = client
        self._car = car
        self._start_date = start_date
        self._end_date = end_date

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def client(self):
        return self._client

    @property
    def car(self):
        return self._car

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date


class RentalValidator:
    """
    Generic validator for car instance
    """

    def validate(self, rental):
        """
        Validate given car
        @param car:
        @return: Raise CarValidationException if car instance is not valid
        """
        errors = []
        if rental.rental_id == 0:
            errors.append("Invalid rental id, empty value provided")
        if len(rental.client) == 0:
            errors.append("Invalid client, empty value provided")
        if len(rental.car) == 0:
            errors.append("Invalid car, empty value provided")
        if rental.start_date == date(1, 1, 1):
            errors.append("Invalid start date, default value provided (1, 1, 1)")
        if rental.end_date == date(1, 1, 1):
            errors.append("Invalid end date, default value provided (1, 1, 1)")
        if rental.start_date > rental.end_date:
            errors.append("Start date is bigger than end date")
        if len(errors) != 0:
            raise RentalValidationException(errors)


def test_rental():
    r = Rental(1, Client(1, "Popescu Ion", 47), Car("FTSG2S", "Dacia", "Logan", "black"), date(2020, 12, 6),
               date(2020, 12, 7))
    assert r.rental_id == 1
    assert r.client == Client(1, "Popescu Ion", 47)
    assert r.car == Car("FTSG2S", "Dacia", "Logan", "black")
    assert date(2020, 12, 6) == r.start_date
    assert date(2020, 12, 7) == r.end_date
    rv = RentalValidator()
    rv.validate(r)
