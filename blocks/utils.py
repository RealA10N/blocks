import re
from typing import List


ANSI_ESCAPE_RE = re.compile(r'(\x1B|\\x1(b|B))\[[0-9,]+m')


def strlen(s: str) -> int:
    """ Returns the length of the string, while ignoring special (invisible)
    characters, like ANSI styling ones. """

    return len(ANSI_ESCAPE_RE.sub('', s))


def strljust(s: str, amount: int, fill: str = ' ') -> str:
    """ Justify the given string to the left using the 'strlen' function to
    determine the current length of the string. """

    to_add = max(0, amount - strlen(s))
    return s + (to_add * fill)


def append_lines(src: List[str], add: List[str]) -> None:
    """ Appends each line in the 'add' text block to the end of the
    corresponding line in the 'src' text block. """

    to_add = max(0, len(add) - len(src))
    src.extend('' for _ in range(to_add))

    for i in range(len(add)):
        src[i] += add[i]
