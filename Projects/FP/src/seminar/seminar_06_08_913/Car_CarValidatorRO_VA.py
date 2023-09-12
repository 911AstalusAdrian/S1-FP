class Car():
    def __init__(self, license, make, model, color):
        self._license = license
        self._make = make
        self._model = model
        self._color = color

    @property
    def license(self):
        return self._license

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color


class CarValidatorRO():
    def validate(self, car):
        if car.license == '' or car.make == '' or car.model == '' or car.color == '':
            raise ValueError('Invalid car!')

        for i in range(2):
            if not car.license[i].isalpha():
                raise ValueError('Invalid license!')

        for i in range(2, 4):
            if not car.license[i].isnumeric():
                raise ValueError('Invalid license!')

        for i in range(4, 7):
            if not car.license[i].isalpha():
                raise ValueError('Invalid license!')

        if car.make != 'VW' and car.make != 'Dacia':
            raise ValueError('Invalid make!')

        return True


def test_car():
    c = Car('AA00BBB', 'VW', 'Lala', 'blue')
    assert c.license == 'AA00BBB'
    assert c.make == 'VW'
    assert c.model == 'Lala'
    assert c.color == 'blue'


def test_car_validator():
    c = Car('AA00BBB', 'VW', 'Lala', 'blue')
    cv = CarValidatorRO()

    assert cv.validate(c) == True

    try:
        c = Car('AA00BBB', 'Lalala', 'Lala', 'blue')
        cv.validate(c)
        assert False
    except:
        assert True

        try:
            c = Car('0A00BBB', 'VW', 'Lala', 'blue')
            cv.validate(c)
            assert False
        except:
            assert True
