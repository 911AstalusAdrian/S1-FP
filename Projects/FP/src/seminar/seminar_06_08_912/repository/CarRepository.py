from seminar.seminar_06_08_912.domain.car import Car


class CarRepo:
    def __init__(self):
        self._car_list = []

    @property
    def car_list(self):
        return self._car_list

    def add_car(self, id, make, model, color):
        self._car_list.append(Car(id, make, model, color))

    # FIXME just fix it :) 
    def update_car(self, id, make, model, color):
        done = False
        for car in self._car_list:
            if car.id == id:
                car.color(color)
                car.make(make)
                car.model(model)
                done = True
        if not done:
            raise ValueError('Car with the given id not found')

    # FIXME Add car_id parameter
    def delete_car(self):
        done = False
        for car in self._car_list:
            if car.id == id:
                self._car_list.remove(car)
