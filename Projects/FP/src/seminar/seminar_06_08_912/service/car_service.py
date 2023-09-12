from seminar.seminar_06_08_912.domain.car import Car


class CarService:
    def __init__(self, validator, repository):
        self._validator = validator
        self._repository = repository

    def create(self, id_, license_plate, car_make, car_model):
        car = Car(id_, license_plate, car_make, car_model)
        self._validator.validate(car)
        self._repository.store(car)
        return car

    def delete(self, car_id):
        return self._repository.delete(car_id)

    def find_by_id(self, car_id):
        return self._repository.find(car_id)

    def filter(self, make, model):
        return self._repository.filter(make, model)

    def update(self, client):
        self._repository.update(client)

    def get_car_count(self):
        return len(self._repository)
