from datetime import time

from seminar.seminar_05_911.domain.entities import flight, flightException


class airport():
    """
    Functionalities related to the airport itself
    """

    def __init__(self):
        self._flights = []

    def add_flight(self, flight):
        """
        Add a flight
        @param flight: the new flight
        @return: -
        Raise flightException on error
        """
        if flight not in self._flights:
            self._flights.append(flight)
        else:
            raise flightException('runway busy')

        for f in self._flights:

            # 2 departures cannot have same departure time
            if f.is_departure and flight.is_departure:
                if f.departure == flight.departure:
                    raise flightException('Two flights cannot depart at same time')
            # 2 arrivals cannot have same arrival time
            # 1 arrival & 1 departure -> must check time at airport
            pass

    def __len__(self):
        return len(self._flights)


def test_airport():
    a = airport()
    assert len(a) == 0

    a.add_flight(flight('RO640', time(6, 40), time(8, 0), True))
    assert len(a) == 1

    try:
        a.add_flight(flight('RO640', time(6, 40), time(8, 0), True))
    except flightException:
        assert True
    assert len(a) == 1

    a.add_flight(flight('RO640', time(6, 40), time(8, 0), False))
    assert len(a) == 2
    a.add_flight(flight('RO640', time(6, 40), time(8, 1), False))
    assert len(a) == 3

# f2 = flight('RO641', time(6, 40), time(8, 0), True)
# f1 = flight('RO640', time(6, 40), time(8, 0), True)
# f3 = flight('RO640', time(5, 40), time(9, 0), True)
#
# print(f3 in [f1, f2])

# test_airport()
