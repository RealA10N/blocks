import colorsys
from typing import Tuple


class Color:

    def __init__(self, r: int, g: int, b: int):
        self.rgb = r, g, b

    @classmethod
    def from_hsl(cls, h: float, l: float, s: float) -> 'Color':
        """ Returns a Color instance that is built from the given HLS color
        representation. """

        return cls(
            *[
                min(int(i * 256), 255)
                for i in colorsys.hls_to_rgb(h, l, s)
            ]
        )

    @property
    def float_rgb(self) -> Tuple[float, float, float]:
        """ A tuple that contains the RGB representation of the color.
        Each element in the tuple is a float in range [0,1]. """
        return tuple(i / 256 for i in self.rgb)

    @property
    def red(self) -> int:
        """ The amount of red in the color, an integer in [0, 255]. """
        return self.rgb[0]

    @property
    def green(self) -> int:
        """ The amount of green in the color, an integer in [0, 255]. """
        return self.rgb[1]

    @property
    def blue(self) -> int:
        """ The amount of blue in the color, an integer in [0, 255]. """
        return self.rgb[2]

    @property
    def float_hls(self) -> Tuple[float, float, float]:
        """ A tuple that contains the HLS representation of the color. """
        return colorsys.rgb_to_hls(*self.float_rgb)

    @property
    def hue(self) -> float:
        """ The hue of the color, a floating value in [0, 1). """
        return self.float_hls[0]

    @property
    def lightness(self) -> float:
        """ The lightness of the color, a floating value in [0, 1]. """
        return self.float_hls[1]

    @property
    def saturation(self) -> float:
        """ The saturation of the color, a floating value in [0, 1]. """
        return self.float_hls[2]

    def __str__(self) -> str:
        """ Returns a hex representation of the current color. """
        return f'#{self.red:02x}{self.green:02x}{self.blue:02x}'

    def __repr__(self) -> str:
        return f'<Color {str(self)}>'
