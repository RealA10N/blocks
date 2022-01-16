from zblocks import Color, ANSI


class Label:

    def __init__(self, text: str, bg: Color, fg: Color) -> None:
        self.text = text
        self.bg = bg
        self.fg = fg

    def __str__(self) -> str:
        s = ANSI.bg(self.bg) + ANSI.fg(self.fg) + ANSI.bold
        return s + f' {self.text} ' + ANSI.reset

    def __len__(self) -> int:
        return len(f' {self.text} ')
