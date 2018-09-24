from collections import namedtuple

DAY_OF_MONTH = \
    {1: 31,
     2: 28,
     3: 31,
     4: 30,
     5: 31,
     6: 30,
     7: 31,
     8: 31,
     9: 30,
     10: 31,
     11: 30,
     12: 31}

LEAP_DAY_OF_MONTH = \
    {1: 31,
     2: 29,
     3: 31,
     4: 30,
     5: 31,
     6: 30,
     7: 31,
     8: 31,
     9: 30,
     10: 31,
     11: 30,
     12: 31}

DAYS_OF_WEEK = \
    {0: "Monday",
     1: "Tuesday",
     2: "Wednesday",
     3: "Thursday",
     4: "Friday",
     5: "Saturday",
     6: "Sunday"}

MONTHS = \
    {1: "January",
     2: "February",
     3: "March",
     4: "April",
     5: "May",
     6: "June",
     7: "July",
     8: "August",
     9: "September",
     10: "October",
     11: "November",
     12: "December"}


class GameClock:
    """Base class for the in-game clock.

    GameClock uses an internal timer (_timer) to track the time that has passed since the start of the
    game (January 1st, 1900).
    """

    def __init__(self, days=0):
        self._timer = _Clock(days)

    def tick(self, minutes=1):
        self._timer.advance(minutes)

    @property
    def date_and_time(self):
        """Return a namedtuple with the following fields:

            year (int): Current year.
            month (int): Current month.
            day (int): Current day-of-the-month.
            hour (int): Current hour-of-the-day.
            minute (int): Current minute-of-the-hour.

        """

        clock_tuple = namedtuple("date_and_time", ["year", "month", "day", "hour", "minute"])
        date_and_time = clock_tuple(self.year, self.month, self.day, self.hour, self.minute)
        return date_and_time

    @property
    def date(self):
        """Return a namedtuple with the following fields:

            year (int): Current year.
            month (int): Current month.
            day (int): Current day-of-the-month.

        """
        date_tuple = namedtuple("date", ["year", "month", "day"])
        date = date_tuple(self.year, self.named_month, self.named_day)
        return date

    @property
    def time(self):
        """Return a namedtuple with the following fields:

            hour (int): Current hour-of-the-day.
            minute (int): Current minute-of-the-hour.

        """
        time_tuple = namedtuple("time", ["hour", "minute"])
        time = time_tuple(self.hour, self.minute)
        return time

    @property
    def year(self):
        """Return the current year (int)."""
        return self._timer.year

    @property
    def month(self):
        """Return the current month (int)."""
        return self._timer.month

    @property
    def day(self):
        """Return the current day-of-the-month (int)."""
        return self._timer.day

    @property
    def hour(self):
        """Return the current hour-of-the-day (int)."""
        return self._timer.hour

    @property
    def minute(self):
        """Return the current minute-of-the-hour (int)."""
        return self._timer.minute

    @property
    def named_day(self):
        """Return the current day-of-the-week (str)."""
        return self._timer.named_day

    @property
    def named_month(self):
        """Return the current month (str)."""
        return self._timer.named_month

    @property
    def total_days(self):
        """Return the current total number of days that have passed (int)."""
        return self._timer.days


class _Clock:

    def __init__(self, days=0):
        self._days = days
        self.minute = 0
        self.hour = 0
        self.day, self.month, self.year = calculate_date(days)

    def advance(self, minutes):
        self.minute += minutes
        self._update()

    def _update(self):
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0
            self.day += 1
            self._days += 1
        if is_leap_year(self.year):
            day_of_month = LEAP_DAY_OF_MONTH
        else:
            day_of_month = DAY_OF_MONTH
        if self.day > day_of_month[self.month]:
            self.day = 1
            self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1

    @property
    def named_day(self):
        day = self._days % 7
        return DAYS_OF_WEEK[day]

    @property
    def named_month(self):
        return MONTHS[self.month]

    @property
    def days(self):
        return self._days


def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            return False
        return True


def calculate_date(num_of_days):
    day = 1
    month = 1
    year = 1900

    for d in range(0, num_of_days):
        day += 1
        if is_leap_year(year):
            day_of_month = LEAP_DAY_OF_MONTH
        else:
            day_of_month = DAY_OF_MONTH
        if day > day_of_month[month]:
            day = 1
            month += 1
        if month == 13:
            month = 1
            year += 1
    return day, month, year
