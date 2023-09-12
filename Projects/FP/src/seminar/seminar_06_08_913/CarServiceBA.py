from seminar.seminar_06_08_913.Car_CarValidatorRO_VA import Car


class CarService:
    def __init__(self, car_repo, car_validator):
        self._car_repo = car_repo
        self._car_validator = car_validator

    def add(self, car_licence, car_make, car_model, car_color):
        car = Car(car_licence, car_make, car_model, car_color)
        self._car_validator.validate(car)
        self._car_repo.add(car)

    def delete_car(self, car_id):
        self._car_repo.delete_car(car_id)

    def get_all(self):
        self._car_repo.get_all()
