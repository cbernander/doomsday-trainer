"""Testing module."""

from doomsday_trainer import dates


def test_doomsdate():
    """Assert DoomsDate class."""
    dd = dates.DoomsDate(1970, 1, 1)
    assert str(dd) == "1970-01-01"
