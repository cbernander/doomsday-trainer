"""Doomsday Trainer."""

from .dates import DAYS, DoomsDate
from .gui import SimpleGui

DATE_START = DoomsDate(1800, 1, 1)
DATE_END = DoomsDate(2099, 12, 31)


def weekday_match(event: str, date: DoomsDate) -> bool:
    """Return true if event matches date weekday."""
    return event == DAYS[date.weekday()]


def new_date() -> DoomsDate:
    """Return a new random DoomsDate."""
    return DoomsDate.random(DATE_START, DATE_END)


def main() -> None:
    """Run main code."""
    date: DoomsDate = new_date()
    header = f"Generating dates between {DATE_START} and {DATE_END}"

    gui = SimpleGui(date=date, header=header)

    # Event loop
    while True:
        event, values = gui.window.read()

        if event in gui.EXIT_EVENTS:
            break

        if event in DAYS:
            if weekday_match(event, date):
                gui.update_result(f"{date} is a {event}")
                date = new_date()
                gui.update_date(str(date))
            else:
                gui.update_date(str(date), error=True)
                gui.update_result(f"{date} isn't a {event}")

    gui.window.close()
