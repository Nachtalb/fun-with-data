import sys
from datetime import datetime

ERASE_LINE = '\x1b[2K'


def one_line_print(message):
    sys.stdout.write(ERASE_LINE)
    sys.stdout.write(f'\r{message}')


def rgba(red, green, blue, alpha=None):
    alpha = alpha or 1

    def c(value):
        return 1 / 255 * value

    return c(red), c(green), c(blue), alpha


def datetime_from_string(string):
    time = None
    try:
        time = datetime.fromisoformat(string)
    except ValueError:
        time = datetime.fromisoformat(string[:-1])
    return time
