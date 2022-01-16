import re
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import TypeVar
    T = TypeVar('T')


class SmartStr(str):
    """ An objects that acts as a regular string, but its length is calculated
    while ignoring invisible unicode and ANSI characters. """

    _ANSI_ESCAPE_RE = re.compile(r'(\x1B|\\x1(b|B))\[[0-9,]+m')

    def __len__(self) -> int:
        return len(self._ANSI_ESCAPE_RE.sub('', self))

    def ljust(self: 'T', width: int, fill: str = ' ') -> 'T':
        to_add = max(0, width - len(self))
        return type(self)(self + (to_add * fill))

    def rjust(self: 'T', width: int, fill: str = ' ') -> 'T':
        to_add = max(0, width - len(self))
        return type(self)((to_add * fill) + self)
