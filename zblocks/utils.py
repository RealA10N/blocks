from typing import List


def append_lines(src: List[str], add: List[str]) -> None:
    """ Appends each line in the 'add' text block to the end of the
    corresponding line in the 'src' text block. """

    to_add = max(0, len(add) - len(src))
    src.extend('' for _ in range(to_add))

    for i in range(len(add)):
        src[i] += add[i]
