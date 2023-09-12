"""
    CarRepositoryWithDict [stores the cars in a dict]
        add(self,car)
        remove(self, car_id)
        get_all(self) [return all car instasnces]
"""


class CarRepositoryWithDict:

    def __init__(self):
        self._cars = {}

    def add(self, car):
        """
        :type car: Car
        :return:
        """
        if car.license in self._cars:
            raise ValueError('Car with license {} already exists'.format(car.license))
        self._cars[car.license] = car

    def remove(self, car_is):
        return self._cars.pop(car_is)

    def get_add(self):
        return self._cars.values()


def test_add():
    car_repo = CarRepositoryWithDict()


test_add()
