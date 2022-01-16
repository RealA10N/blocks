from zblocks import Block, SmartStr
from enum import Enum
from math import inf


class Glue(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    MIDDLE = 'middle'


class BoxWrapper(Block):
    """ Represents blocks that wrap other blocks and add functionally to them. 
    Those blocks receive the dependent block in their constructor and they can
    not initialize without other blocks. """

    def __init__(self, block: Block) -> None:
        self._block = block


class Box(BoxWrapper):
    """ Adds padding to a block, to make the length of the lines equal. """

    def __init__(
        self,
        block: Block,
        fill: str = ' ',
        glue: Glue = Glue.LEFT,
    ) -> None:
        self._fill = fill
        self._glue = glue
        super().__init__(block)

    def get(self, width: int, height: int) -> SmartStr:
        lines = self._block.get(width, height).splitlines(keepends=False)
        max_width = max(len(SmartStr(line)) for line in lines)

        def just(s: str):
            if self._glue == Glue.MIDDLE:
                add = max(0, max_width - len(s))
                less = add // 2
                more = add - less
                return(self._fill * more) + s + (self._fill * less)

            elif self._glue == Glue.RIGHT:
                return s.rjust(max_width, self._fill)
            else:
                return s.ljust(max_width, self._fill)

        return SmartStr('\n'.join(just(SmartStr(line)) for line in lines))


class Bounder(BoxWrapper):
    """ Set a maximum width and height to other blocks. """

    def __init__(
        self,
        block: Block,
        maxwidth: int = inf,
        maxheight: int = inf,
    ) -> None:
        self._maxwidth, self._maxheight = maxwidth, maxheight
        super().__init__(block)

    def get(self, width: int, height: int) -> SmartStr:
        return self._block.get(
            width=min(width, self._maxwidth),
            height=min(height, self._maxheight)
        )


class Expend(BoxWrapper):
    """ Adds padding to other blocks, if possible. """

    def __init__(self, block: Block, fill: str = ' ') -> None:
        self._fill = fill
        super().__init__(block)

    def get(self, width: int, height: int) -> SmartStr:
        lines = self._block.get(width, height).splitlines(keepends=False)

        missing_lines = max(0, height - len(lines))
        missing_back = missing_lines // 2
        missing_front = missing_lines - missing_back
        lines = ([''] * missing_front) + lines + ([''] * missing_back)

        for i, line in enumerate(lines):
            line = SmartStr(line)
            missing = max(0, width - len(line))
            back = missing // 2
            front = missing - back
            lines[i] = (self._fill * front) + line + (self._fill * back)

        return SmartStr('\n'.join(lines))


class Margin(BoxWrapper):
    """ Adds margin to other blocks, reducing the size of the block it
    contains. """

    def __init__(
        self,
        block: Block,
        fill: str = ' ',
        top: int = 0,
        bottom: int = 0,
        left: int = 0,
        right: int = 0,
    ) -> None:
        self._fill = fill
        self._top, self._bottom = top, bottom
        self._left, self._right = left, right
        super().__init__(block)

    def get(self, width: int, height: int) -> SmartStr:
        return self._block.get(
            width=width - self._left - self._right,
            height=height - self._top - self._bottom,
        )
