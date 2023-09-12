class alarmException(Exception):
    """
    This is a custom Exception class, inherited from Python's Exception
     inherited - this 'is an' Exception
    """

    def __init__(self, msg):
        self._msg = msg


class alarm:
    """
    Class that represents a set alarm
    """

    def __init__(self, hours, minutes, description=''):
        self.hours = hours
        self.minutes = minutes
        self._description = description

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @hours.setter
    def hours(self, value):
        if value < 0 or value > 23:
            raise alarmException('Invalid value for hours')
        self._hours = value

    @minutes.setter
    def minutes(self, value):
        if value < 0 or value > 59:
            raise alarmException('Invalid value for minutes')

        self._minutes = value

    @property
    def description(self):
        return self._description

    def add_time(self, hours, minutes):
        # TODO Extra work when alarm skips to a new day
        add_minutes = hours * 60 + minutes
        new_alarm_time = self.hours * 60 + self.minutes + add_minutes

        self.hours = (new_alarm_time // 60) % 24
        self.minutes = new_alarm_time % 60

    # def __sub__(self, other):
    #     pass

    def __add__(self, other):
        # Create a new alarm instance
        new_alarm = alarm(self.hours, self.minutes, self.description)
        new_alarm.add_time(0, other)
        return new_alarm

    def __str__(self):
        return str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + " - " + self.description


if __name__ == '__main__':
    # TODO This stuff should be in the test function
    a = alarm(8, 0, 'FP seminar')
    print(str(a))

    # Postpone by 30 minutes
    a = a + (24 * 60 - 59)

    print(str(a))


# print(str(b))


def test_alarm():
    for h in range(24):
        for m in range(60):
            a = alarm(h, m)
            assert a.hours == h, str(h) + ' is too early!'
            assert a.minutes == m
    assert a.description == ''

    a = alarm(0, 0, 'wake up')
    assert a.description == 'wake up'

    # Make sure these raise an alarmException
    bad_hours = [-10, -1, 4, 24, 40, 100, 2000]
    bad_minutes = [-10, -1, 50, 60, 100, 1000]
    for hour in bad_hours:
        for minute in bad_minutes:
            if hour == 4 and minute == 50:
                continue
            try:
                alarm(hour, minute)
                assert False, 'here be exceptions !?'
            except alarmException:
                assert True


test_alarm()
