from seminar.seminar_06_08_911.domain.rental import Rental


class RentalService:
    def __init__(self, client_repo, car_repo, rental_repo, rental_validator):
        self._repo = rental_repo
        self._validator = rental_validator
        self._car_repo = car_repo
        self._client_repo = client_repo

    def create_rental(self, client_id, car_id, start_date, end_date):
        rental = Rental(client_id, car_id, start_date, end_date)
        self._validator.validate(rental)
        self._repo.addRental(rental)

    def remove_rental(self, rental_id):
        rental = self._repo.remove_rental(rental_id)
