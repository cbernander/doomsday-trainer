"""Date handling."""
import random
from datetime import datetime


class DoomsDate:
    """A custom date implementation."""

    def __init__(self, year: int, month: int, day: int) -> None:
        """Initialize object."""
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def random(cls, start, end):
        """Return a random DoomsDate between start and end (inclusive)."""
        dt_start = datetime(start.year, start.month, start.day)
        dt_end = datetime(end.year, end.month, end.day)
        dt_random = dt_start + (dt_end - dt_start) * random.random()
        return DoomsDate(dt_random.year, dt_random.month, dt_random.day)

    def doomsweekday(self):
        """Return a DoomsWeekday object for date."""
        return DoomsWeekday(datetime(self.year, self.month, self.day).isoweekday())

    def __str__(self) -> str:
        """Return string representation (YYYY-mm-dd)."""
        return f"{self.year}-{self.month:02}-{self.day:02}"


class DoomsWeekday:
    """A custom weekday implementation."""

    DAYS = (
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    )

    def __init__(self, isoweekday):
        """Init method."""
        self.number = isoweekday % 7

    def __eq__(self, other) -> bool:
        """Test for object equality."""
        if isinstance(other, DoomsWeekday):
            return self.number == other.number

        return False

    def number(self):
        """Get Doomsday number."""
        return self.number

    @classmethod
    def create_from_name(cls, name):
        """Return a new DoomsWeekday from a weekday name."""
        if name in cls.DAYS:
            return DoomsWeekday(cls.DAYS.index(name))

        return None

    @classmethod
    def names_iso_order(cls):
        """Return tuple of weekday names in ISO order."""
        weekdays = list(cls.DAYS[1:])
        weekdays.append(cls.DAYS[0])
        return tuple(weekdays)
