from datetime import time

# flightException IS A type of Exception
from random import randint


class flightException(Exception):
    def __init__(self, msg):
        self._msg = msg


# TODO Disregard flights that land the next day (depart 23:50 -> arrive at 00:45 the next day)
class flight:
    """
    Represent one flight departing from/arriving at the airport
    """

    def __init__(self, id_, departure_time, arrival_time, is_departure=True):
        """
        create flight
        @param id_:
        @param departure_time:
        @param arrival_time:
        @param is_departure:
        Raises flightException on incorrect data
        """
        if departure_time >= arrival_time:
            raise flightException('Arrival time set before departure!')

        self._id = id_
        self._departure = departure_time
        self._arrival = arrival_time
        self._is_departure = is_departure

    @property
    def id(self):
        return self._id

    @property
    def departure(self):
        return self._departure

    @property
    def arrival(self):
        return self._arrival

    @property
    def is_departure(self):
        return self._is_departure

    def __lt__(self, other):
        if not isinstance(other, flight):
            raise TypeError('Cannot compare flight to ' + str(type(other)))
        return self.departure < other.departure

    def __str__(self):
        return self._id + ' | ' + str(self.departure) + ' -> ' + str(self._arrival)

    def __eq__(self, other):
        if not isinstance(other, flight):
            raise TypeError('Cannot compare flight to ' + str(type(other)))
        # V1 - only check id
        # V2 - check everything
        return self.id == other.id


def test_flight():
    f = flight('RO640', time(6, 40), time(8, 0), True)
    assert 'RO640' == f.id
    assert f.departure == time(6, 40), 'departure time wrong!'
    assert f.arrival == time(8, 0)

    # check departure / arrival times
    for index in range(1000):
        dep_time = time(randint(0, 23), randint(0, 59))
        arr_time = time(randint(0, 23), randint(0, 59))

        try:
            f = flight('ABCD', dep_time, arr_time)
            assert f.departure < f.arrival, str(f.departure) + '->' + str(f.arrival)
            # if f.departure > f.arrival:
            #     assert False, str(dep_time) + ' -> ' + str(arr_time)
        except flightException:
            assert True


if __name__ == '__main__':
    f1 = flight('RO640', time(6, 40), time(8, 0), True)
    f2 = flight('RO640', time(5, 45), time(7, 0), True)

    print(str(f1))
    print(f1 < f2)

test_flight()
