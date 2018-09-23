from game import clock
import unittest


class TestDayZero(unittest.TestCase):
    """Test the GameClock object at the start (January 1st, 1900)."""
    start_at = 0.0
    year = 1900
    month = 1
    day = 1
    hour = 0
    minute = 0
    named_month = "January"
    named_day = "Monday"

    def setUp(self):
        self.clock = clock.GameClock(self.start_at)

    def test_properties_date_and_time(self):
        """A GameClock's date_and_time property returns a namedtuple containing the correct numerical values for the
        current in-game year, month, day, hour, and minute.
        """
        date = self.clock.date_and_time
        self.assertEqual(date.year, self.year)
        self.assertEqual(date.month, self.month)
        self.assertEqual(date.day, self.day)
        self.assertEqual(date.hour, self.hour)
        self.assertEqual(date.minute, self.minute)

    def test_properties_date(self):
        """A GameClock's date property returns a namedtuple containing the correct numerical value for the in-game
        year, and string values for the month and day.
        """
        date = self.clock.date
        self.assertEqual(date.year, self.year)
        self.assertEqual(date.month, self.named_month)
        self.assertEqual(date.day, self.named_day)

    def test_properties_time(self):
        """A GameClock's time property returns a namedtuple containing the correct numerical values for the in-game
        hour and minute.
        """
        time = self.clock.time
        self.assertEqual(time.hour, self.hour)
        self.assertEqual(time.minute, self.minute)


class TestDayHalf(TestDayZero):
    """Test the GameClock object 12 hours into Monday, January 1st, 1900."""
    start_at = 0.5
    hour = 12


class TestDayOne(TestDayZero):
    """Test the GameClock object on the next day (January 2nd, 1900)."""
    start_at = 1.0
    day = 2
    named_day = "Tuesday"


class TestDaySixty(TestDayZero):
    """Test the GameClock object (its publicly available attributes and methods) sixty days later (Monday, March 2nd,
    1900).
    """
    start_at = 60.0
    month = 2
    day = 2
    named_month = "March"
    named_day = "Monday"


class TestDayTenThousand(TestDayZero):
    start_at = 10000.0
    year = 1927
    month = 5
    day = 20
    named_month = "May"
    named_day = "Friday"


unittest.main()

