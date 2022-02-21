import os
from typing import List, Any


def scale(terminal: os.terminal_size, lines: int, columns: int) -> List[int]:
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
    if lines < terminal.lines and columns < terminal.columns:
        return 1, 1

    for divisor in range(2, terminal.columns // 2 + 1):
        if (lines / divisor).is_integer() and (columns / divisor).is_integer():
            if (lines /
                divisor) < terminal.lines and (columns /
                                               divisor) < terminal.columns:
                # TODO: only work sometimes
                return int(lines / (lines / divisor)), int(columns / (columns / divisor))