"""Tests for gui module."""

from doomsday_trainer import gui


def test_simplegui():
    """Test SimpleGui class."""
    sg = gui.SimpleGui()
    assert sg is not None
