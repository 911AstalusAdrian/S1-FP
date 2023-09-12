from seminar_6.domain.car import Car


class CarValidator:

    @staticmethod
    def validate(car):
        if len(car.license_plate) == 0:
            raise ValueError("Invalid license plate, empty value provided")

        if len(car.make) == 0:
            raise ValueError("Invalid make, empty value provided")

        if len(car.model) == 0:
            raise ValueError("Invalid model, empty value provided")


def test_car_validator():
    try:
        Car('', 'make', 'model', 'color')
    except ValueError:
        assert True


test_car_validator()
