# doomsday-trainer

A simple program for exercising the ability to calculate the day of week for
a given date.

The name is taken from the
[Doomsday rule](https://en.wikipedia.org/wiki/Doomsday_rule) - an algorithm
devised by [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in
1973 for this specific purpose.

## Dependencies

- Python 3.7+

- [Poetry](https://python-poetry.org/) for dependency management and packaging.

- [tox](https://pypi.org/project/tox/) for testing.

## Installation

### From source (using Poetry)

```
git clone https://github.com/cbernander/doomsday-trainer.git
cd doomsday-trainer
poetry build
pip install dist/doomsday_trainer-*.whl
```

## Running the program

```
doomsday-trainer
```
