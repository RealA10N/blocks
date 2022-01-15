import re
from typing import List


ANSI_ESCAPE_RE = re.compile(r'(\x1B|\\x1(b|B))\[[0-9,]+m')


def strlen(s: str) -> int:
    """ Returns the length of the string, while ignoring special (invisible)
    characters, like ANSI styling ones. """

    return len(ANSI_ESCAPE_RE.sub('', s))


def append_lines(src: List[str], add: List[str]) -> None:
    """ Appends each line in the 'add' text block to the end of the
    corresponding line in the 'src' text block. """

    lines = max(len(src), len(add))
    to_add = max(0, lines - len(src))
    src.extend('' for _ in range(to_add))

    for i in range(lines):
        src[i] += add[i]
