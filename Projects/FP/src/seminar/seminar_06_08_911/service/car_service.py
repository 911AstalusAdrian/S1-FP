from seminar.seminar_06_08_911.domain.car import Car


class CarService:
    def __init__(self, car_repo, car_validator):
        # self._repo = CarRepository()
        self._repo = car_repo
        self._validator = car_validator

    def create_car(self, license, make, model, color):
        """
        Add car to application
        @param license: 
        @param make:
        @param model:
        @param color:
        @return:
        """
        self._validator.validate(Car(license, make, model, color))
        new_car = Car(license, make, model, color)
        self._repo.add_all(new_car)

    def remove_car(self, car_id):
        self._repo.remove(car_id)
