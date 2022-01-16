import os
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from zblocks import SmartStr


class Block(ABC):
    """ The most basic text container. Defines the basic behavior of all blocks
    in zblocks, including the get and __str__ methods. """

    @abstractmethod
    def get(self, width: int, height: int) -> 'SmartStr':
        """ Returns the generated block as a smart string instance. """

    def __str__(self) -> 'SmartStr':
        """ Returns the generated block as a smart string instance, while the
        dimensions of the block are determined using the terminal size. """

        width, height = os.get_terminal_size()
        return self.get(width, height)
