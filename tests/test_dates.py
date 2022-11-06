"""Tests for dates module."""

import random
from doomsday_trainer import dates

date1 = dates.DoomsDate(1970, 1, 1)


def test_doomsdate_str():
    """Test DoomsDate string representation."""
    assert str(date1) == "1970-01-01"


def test_doomsdayrule_century_anchor():
    """Test DoomsdayRule.century_anchor() method."""
    for centuries in [(18, 5), (19, 3), (20, 2), (21, 0)]:
        century = centuries[0]
        anchor = centuries[1]
        year = century * 100 + random.randrange(0, 100, 1)
        month = random.randrange(1, 13, 1)
        day = random.randrange(1, 29, 1)
        rule = dates.DoomsdayRule(dates.DoomsDate(year, month, day))
        assert rule.century_anchor().number == anchor


def test_doomsweekday_names_iso_order():
    """Test DoomsWeekday.names_iso_order() method."""
    assert dates.DoomsWeekday.names_iso_order() == (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
