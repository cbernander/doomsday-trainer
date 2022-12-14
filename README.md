# doomsday-trainer

A simple GUI program for exercising the ability to calculate the day of week for
a given date (Gregorian calendar).

The name is taken from the
[Doomsday rule](https://en.wikipedia.org/wiki/Doomsday_rule) - an algorithm
devised by [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in
1973 for this specific purpose.

## Dependencies

- Python 3.7+

- [tkinter](https://docs.python.org/3/library/tkinter.html) ([Installation instructions](#tkinter-installation))

## Installation

```bash
pip install doomsday-trainer
```

## Usage

```
usage: doomsday-trainer [-h] [--start-year START_YEAR] [--end-year END_YEAR]

optional arguments:
  -h, --help            show this help message and exit
  --start-year START_YEAR
                        Start year [1800]
  --end-year END_YEAR   End year [2099]
```

## Installation from source (using Poetry)

```bash
git clone https://github.com/cbernander/doomsday-trainer.git
cd doomsday-trainer
poetry build
pip install dist/doomsday_trainer-*.whl
```

## tkinter installation

### macOS

```bash
$ brew install python-tk
```

### Ubuntu / Debian

```bash
$ sudo apt get install python3-tk
```

### Arch Linux

```bash
$ sudo pacman -S tk
```

### Fedora

```bash
$ sudo dnf install python3-tkinter
```

### RHEL / CentOS / Oracle Linux

```bash
$ sudo yum install -y tkinter tk-devel
```

## Development tools


- [Poetry](https://python-poetry.org/) for dependency management and packaging.

- [tox](https://pypi.org/project/tox/) for testing.

- [Black](https://black.readthedocs.io/en/stable/index.html) for code
  formatting.

- GUI built using [PySimpleGUI](https://www.pysimplegui.org/)
