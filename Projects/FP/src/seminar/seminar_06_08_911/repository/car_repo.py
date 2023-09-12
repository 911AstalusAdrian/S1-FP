"""
    c. Repository class + test_repository function + test_init_car function (to add car instances)
        - remove, find methods
"""
from seminar.seminar_06_08_911.domain.car import Car, CarValidator


class CarRepository:

    def __init__(self, cars=None):
        self._cars = []
        # self._validator = validator
        if cars is not None:
            self.add_all(cars)

    @property
    def cars(self):
        return self._cars

    def add_all(self, cars):
        for car in cars:
            # self._validator.validate(car)
            self._cars = cars

    """
        keep cars matching filter
    """

    def remove(self, filter_func):
        self._cars = list(filter(filter_func, self._cars))


def test_init_car():
    cars = [Car('CJ01XYZ', 'Dacia', 'Logan', 'white'),
            Car('CJ02XYZ', 'Dacia', 'Sandero', 'blue'),
            Car('CJ03XYZ', 'Dacia', 'Duster', 'white'),
            Car('CJ04XYZ', 'Renault', 'Megane', 'yellow')]
    repo = CarRepository(cars)
    assert len(repo.cars) == 4

    return repo


def test_remove_repo():
    repo = test_init_car()

    repo.remove(lambda car: not car.color == 'white')

    assert len(repo.cars) == 2


test_init_car()
test_remove_repo()
