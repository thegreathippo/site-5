from collections import namedtuple

MINUTE = 0.00069444444
HOUR = 0.04166666666


class GameClock:
    """Base class for the in-game clock.

    GameClock uses an internal decimal (_value) to track the in-game time. Anything to the left of the decimal point
    represents the # of days since January 1st, 1900; anything to the right is the fraction of time that has passed
    during the current day.
    """

    def __init__(self, date_and_time=0.0):
        self._value = date_and_time

    def advance(self, length=1.0):
        self._value += length

    @property
    def date_and_time(self):
        clock_tuple = namedtuple("date_and_time", ["year", "month", "day", "hour", "minute"])
        date_and_time = clock_tuple(self.year, self.month, self.day, self.hour, self.minute)
        return date_and_time

    @property
    def date(self):
        date_tuple = namedtuple("date", ["year", "month", "day"])
        date = date_tuple(self.year, self.named_month, self.named_day)
        return date

    @property
    def time(self):
        time_tuple = namedtuple("time", ["hour", "minute"])
        time = time_tuple(self.hour, self.minute)
        return time

    @property
    def year(self):
        return 1900

    @property
    def month(self):
        return 1

    @property
    def day(self):
        return 1

    @property
    def hour(self):
        return 0

    @property
    def minute(self):
        return 0

    @property
    def named_day(self):
        return "Monday"

    @property
    def named_month(self):
        return "January"

