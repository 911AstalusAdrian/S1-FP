from seminar.seminar_05_912.domain.alarm import alarm


class alarmClock:
    """
    Functionalities for alarm clock
    """

    def __init__(self):
        self._alarms = []
        # TODO Keep it simple silly
        self._hour = 0
        self._minute = 0

    def add_alarm(self, alarm):
        """
        Create a new alarm
        @param alarm: The new alarm
        @return: -
        Raise exception if alarm at that time already exists
        """
        # TODO Code to check duplicate alarms
        self._alarms.append(alarm)

    def delete_alarm(self, alarm):
        pass

    def tick(self):
        """
        Simulate 1 minute passing
        @return: The alarm at this moment in time, or None if no alarm set for this minute
        """
        self._minute += 1
        if self._minute == 60:
            self._hour += 1
            self._minute = 0
        if self._hour == 24:
            # A new day has come
            self._hour = 0

        for alarm in self._alarms:
            if alarm.hours == self._hour and alarm.minutes == self._minute:
                return alarm
        return None

    def __len__(self):
        return len(self._alarms)


def test_alarm_clock():
    clock = alarmClock()
    assert len(clock) == 0, 'no alarms should be set'

    clock.add_alarm(alarm(0, 12))
    clock.add_alarm(alarm(4, 15))
    clock.add_alarm(alarm(7, 40))

    for tick in range(1, 24 * 60):
        _alarm = clock.tick()

        if tick in [12, 4 * 60 + 15, 7 * 60 + 40]:
            assert not (_alarm is None), str(tick) + "," + str(_alarm)
        else:
            assert _alarm is None, str(tick) + ' ' + str(_alarm)


test_alarm_clock()
