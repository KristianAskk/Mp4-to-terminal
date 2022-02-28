import os
from typing import List
import numpy as np
import time
import cv2

def create_frame(frame: np.ndarray, height_and_width: int, terminal: os.terminal_size) -> List[str]:
    ascii_frame = []
    frames_fetched = _fetch_frames(frame, height_and_width)
    for row in frames_fetched:
        frame_line = "".join([_fetch_character(_average_brightness(pixel)) for pixel in row])
        ascii_frame.append(frame_line.center(terminal.columns)) 
    
    return "\n" * (((terminal.lines - len(ascii_frame) - 1) // 2) + 1) \
    + "\n".join(ascii_frame) \
    + "\n" * ((terminal.lines - len(ascii_frame) - 1) // 2)

def _fetch_frames(frame: np.ndarray, height_and_width: int) -> List[List[np.ndarray]]:
    frames = []
    for pixel_row in range(0, len(frame), height_and_width * 2):
        line = []
        for pixel_column in range(0, len(frame[0]), height_and_width):
            line.append([[frame[i][j] for j in 
                          range(pixel_column, pixel_column + height_and_width, 2)]
                          for i in range(pixel_row, pixel_row + height_and_width, 2)])
        frames.append(line)
    return frames

def _average_brightness(pixel: List[np.ndarray]) -> float:
    amount_of_rgb_values = len(pixel) * len(pixel[0]) * 3
    sum_of_rgb_values = sum([sum(rgb) for pix in pixel for rgb in pix])
    average = sum_of_rgb_values / (amount_of_rgb_values * 255)
    return average

def _fetch_character(brightness: float) -> str:
    if brightness >= 0.85:
        return "#"
    if brightness >= 0.7:
        return "%"
    if brightness >= 0.6:
        return "*"
    if brightness >= 0.4:
        return "-"
    if brightness >= 0.2:
        return ":"
    if brightness >= 0.1:
        return "."
    return " "

