"""Tests for dates module."""

from doomsday_trainer import dates

date1 = dates.DoomsDate(1970, 1, 1)


def test_doomsdate_str():
    """Test DoomsDate string representation."""
    assert str(date1) == "1970-01-01"


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
