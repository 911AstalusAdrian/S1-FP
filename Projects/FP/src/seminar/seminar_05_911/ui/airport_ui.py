from seminar.seminar_05_911.domain.entities import flight
from seminar.seminar_05_911.service.airport import airport

'''
    ui -> airport
    ui -> flight
    airport -> flight
'''


class ui:
    def __init__(self):
        self._airport = airport()

    def start(self):
        """
        Start the UI here
        @return:
        """
        pass

        self._airport.add_flight(flight('..,'))


airport_ui = ui()
airport_ui.start()
