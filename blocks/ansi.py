from blocks import Color


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class ANSI:
    """ Foreground and background functions assume that the terminal supports
    ANSI 8bit colors.
    Data provided by: https://en.wikipedia.org/wiki/ANSI_escape_code """

    @classproperty
    def esc(cls):
        return '\u001b'

    @classproperty
    def bold(cls):
        return cls.compile(1)

    @classproperty
    def italic(cls):
        return cls.compile(3)

    @classproperty
    def underline(cls):
        return cls.compile(4)

    @classproperty
    def strike(cls):
        return cls.compile(9)

    @classproperty
    def reset(cls):
        return cls.compile(0)

    @classproperty
    def reset_fg(cls):
        return cls.compile(39)

    @classproperty
    def reset_bg(cls):
        return cls.compile(49)

    @classproperty
    def reset_bold(cls):
        return cls.compile(21, 22)

    @classproperty
    def reset_italic(cls):
        return cls.compile(23)

    @classproperty
    def reset_underline(cls):
        return cls.compile(24)

    @classproperty
    def reset_strike(cls):
        return cls.compile(29)

    @classmethod
    def compile(cls, *vals: int) -> str:
        return f"{cls.esc}[{';'.join(str(v) for v in vals)}m"

    @classmethod
    def fg(cls, c: 'Color') -> str:
        return cls.compile(38, 2, c.red, c.green, c.blue)

    @classmethod
    def bg(cls, c: 'Color') -> str:
        return cls.compile(48, 2, c.red, c.green, c.blue)
