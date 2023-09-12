from unittest import TestCase

from seminar.seminar_06_08_912.domain.car import Car, CarException


class TestCar(TestCase):
    def test_init(self):
        car_list = []
        car = Car(license_plate='SJ01XXX', make='audi', model='a30', color='black')
        car_list.append(car)
        car_list.append(Car('CJ01AAA', 'audi', 'a41', 'red'))
        car_list.append(Car('CJ01AAA', 'dacia', 'logan', 'blue'))
        car_list.append(Car('CJ01AAA', 'ford', 'focus', 'white'))
        car_list.append(Car('CJ01AAA', 'ford', 'fiesta', 'red'))
        try:
            car = Car('asd', 4, 345, 14)
            self.assertFalse('not ok')
        except CarException:
            self.assertTrue('ok')

    def test_car(self):
        self.assertTrue('ok')
