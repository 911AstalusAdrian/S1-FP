'''
these are predefined data types (they are already defined in Python)
ValueError
TypeError
NameError
'''


class CarException(Exception):
    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return self._msg


class CarValidationException(CarException):
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


class Car:

    def __init__(self, license_plate, make, model, color):
        self._license_plate = license_plate
        self._make = make
        self._model = model
        self._color = color

    @property
    def license_plate(self):
        return self._license_plate

    @property
    def model(self):
        return self._model

    @property
    def make(self):
        return self._make

    @property
    def color(self):
        return self._color


class CarValidator:
    """
    Generic validator for car instance
    """

    def validate(self, car):
        """
        Validate given car
        @param car:
        @return: Raise CarValidationException if car instance is not valid
        """
        errors = []
        if len(car.license_plate) == 0:
            errors.append("Invalid license plate, empty value provided")
        if len(car.make) == 0:
            errors.append("Invalid make, empty value provided")
        if len(car.model) == 0:
            errors.append("Invalid model, empty value provided")
        raise CarValidationException(errors)


try:
    my_car = Car('CJ01XYZ', '', '', 'red')
    cv = CarValidator()
    cv.validate(my_car)
except CarValidationException as e:
    print(e.errors)

def test_car():
    my_car = Car('CJ01XYZ', 'Dacia', 'Logan', 'white')
    assert 'CJ01XYZ' == my_car.license_plate
    assert 'Dacia' == my_car.make
    assert 'Logan' == my_car.model
    assert 'white' == my_car.color


test_car()
