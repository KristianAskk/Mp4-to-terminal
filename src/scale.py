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
    # if lines < terminal.lines*2 and columns < terminal.columns*4:
    #     return 1

    # for divisor in range(1, terminal.columns*4 // 1 + 1):
    #     print(columns,lines,divisor,(columns / divisor))
    #     if (not lines % divisor) and (not columns % divisor):
    #
    #         if (lines / divisor) / 2 < terminal.lines*2 and (
    #             columns / divisor
    #         ) < terminal.columns*4:
    #             print(int(lines / (lines / divisor)))
    print((terminal.columns),columns, columns/(terminal.columns*2))

    print( lines/(terminal.lines*4),columns/(terminal.columns*2) )
    print (math.ceil((max(1,max( lines/(terminal.lines*4),columns/(terminal.columns*2) )))))
    return math.ceil(max(1,max( lines/(terminal.lines*4),columns/(terminal.columns*2) )))
