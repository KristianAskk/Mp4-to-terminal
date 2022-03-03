import os
from typing import List, Any
import math


def scale(terminal: os.terminal_size, lines: int, columns: int) -> int:
    """Calculates how many pixels of the video each character in the terminal represents.

    Parameters
    ----------
    terminal : os.terminal_size
        Fetches the size of the terminal.
    lines : int
        Height of the video i
    columns : int

    Returns
    -------
    List[int]
        Returns how many pixels in width and height in the video are
        being represented as one pixel in the terminal.
    """
    for divisor in range(2, terminal.columns // 2 + 1):
            if (lines / divisor).is_integer() and (columns / divisor).is_integer():
                if (lines / divisor) / 2 < terminal.lines and (columns / divisor) < terminal.columns:
                    print('this is getting returned', int(lines / (lines / divisor)))
                    return int(lines / (lines / divisor))

def braille_scale(terminal: os.terminal_size, lines: int, columns: int) -> int:
    return math.ceil(max(1,max( lines/(terminal.lines*4),columns/(terminal.columns*2) )))