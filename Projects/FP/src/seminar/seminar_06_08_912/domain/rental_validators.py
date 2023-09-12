from datetime import date

from seminar.seminar_06_08_912.domain.exceptions import ValidatorException
from seminar.seminar_06_08_912.domain.rental import Rental


class RentalValidator:
    @staticmethod
    def validate(rental):
        if isinstance(rental, Rental) is False:
            raise TypeError("Not a Rental")

        _errorList = []
        now = date(2000, 1, 1)
        if rental.start < now:
            _errorList.append("Rental starts in past;")
        if len(rental) < 1:
            _errorList.append("Rental must be at least 1 day;")
        if len(_errorList) > 0:
            raise ValidatorException(_errorList)
