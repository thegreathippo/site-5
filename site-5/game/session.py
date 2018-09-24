from . import clock


INTERVAL = 1


class Session:

    def __init__(self):
        self.clock = clock.GameClock()
        self.time = "  00:00 (AM), 01 Jan 1900 (Mon)  "

    def advance(self):
        self.clock.tick(INTERVAL)
        self.time = _time_and_date_format(self.clock)


def _time_and_date_format(clock):
    hour, minute = clock.hour, clock.minute
    str_time = _time_format(hour, minute)
    day, named_month, year, named_day = clock.day, clock.named_month, clock.year, clock.named_day
    str_date = _date_format(day, named_month, year, named_day)
    return "  " + str_time + ", " + str_date + "  "


def _date_format(day, month_name, year, named_day):
    _day = ""
    if day < 10:
        _day = "0" + str(day)
    else:
        _day = str(day)
    return _day + " " + month_name[:3] + " " + str(year) + " (" + named_day[:3] + ")"


def _time_format(hour, minute):
    _hour, _minute, m = "", "", " (AM)"
    if hour >= 12:
        m = " (PM)"
    if hour < 10:
        _hour = "0" + str(hour)
    else:
        _hour = str(hour)
    if minute < 10:
        _minute = "0" + str(minute)
    else:
        _minute = str(minute)
    return _hour + ":" + _minute + m

