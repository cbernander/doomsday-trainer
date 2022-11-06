"""Tests for trainer module."""

from doomsday_trainer import trainer


def test_doomsday_trainer():
    """Test DoomsdayTrainer class."""
    dt = trainer.DoomsdayTrainer(1850, 1950)

    assert str(dt.start_date) == "1850-01-01"
    assert str(dt.end_date) == "1950-12-31"
    assert dt.date is not None
