import numpy as np
from .frame import create_frame
import os
from typing import List


def process(frame: np.ndarray, height_and_width, terminal: os.terminal_size) -> List[str]:
    return create_frame(frame, height_and_width, terminal)