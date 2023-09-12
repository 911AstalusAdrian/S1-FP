"""
The ui module
"""
from seminar.seminar_06_08_913.Car_CarValidatorRO_VA import Car


class MenuUI:

    def __init__(self, car_service, client_service, rental_service):
        self._car_service = car_service
        self._client_service = client_service
        self._rental_service = rental_service

    def start(self):

        command_dict = {"1": self.add_car, "2": self.remove_car}

        done = False
        while not done:
            command = input("The command: ")
            if done == "0":
                done = True
            elif command in command_dict:
                try:
                    command_dict[command]()
                except Exception as ex:
                    print(ex)
            else:
                print("Bad command!")

    def add_car(self):
        license = input("License: ")
        make = input("Make: ")
        model = input("Model: ")
        color = input("Color: ")
        self._car_service.add(license, make, model, color)

    def remove_car(self):
        the_id = input("The id to be removed: ")

        self._car_service.remove(the_id)
