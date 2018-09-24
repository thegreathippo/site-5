from game import clock
import unittest


class TestDayZero(unittest.TestCase):
    """Test the GameClock object at the start (January 1st, 1900)."""
    start_at = 0
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


class TestDayOne(TestDayZero):
    """Test the GameClock object on the next day (January 2nd, 1900)."""
    start_at = 1
    day = 2
    named_day = "Tuesday"


class TestDaySixty(TestDayZero):
    """Test the GameClock object sixty days later (Monday, March 2nd, 1900)."""
    start_at = 60
    month = 3
    day = 2
    named_month = "March"
    named_day = "Friday"


class TestDayTenThousand(TestDayZero):
    """Test the GameClock object ten thousand days later (Friday, May 20th, 1927)."""
    start_at = 10000
    year = 1927
    month = 5
    day = 20
    named_month = "May"
    named_day = "Friday"


class TestDayFiftyThousand(TestDayZero):
    """Test the GameClock object fifty thousand days later (Sunday, November 23rd, 2036)."""
    start_at = 50000
    year = 2036
    month = 11
    day = 23
    named_month = "November"
    named_day = "Sunday"


class TestDayFiveHundredThousand(TestDayZero):
    """Test the GameClock object five hundred thousand days later (Friday, December 14th, 3628)."""
    start_at = 500000
    year = 3268
    month = 12
    day = 14
    named_month = "December"
    named_day = "Friday"


class TestAdvanceToDaySixty(TestDaySixty):
    """Manually advance GameClock by sixty days (Monday, March 2nd, 1900) and then test it."""
    start_at = 0

    def setUp(self):
        self.clock = clock.GameClock(self.start_at)
        for m in range(0, (60 * 1440)):
            self.clock.tick()


unittest.main()

