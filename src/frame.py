import os
from typing import List, Tuple
import numpy as np
import time
import cv2
import math

def create_frame(frame: np.ndarray, height_and_width: int, terminal: os.terminal_size) -> List[str]:
    ascii_frame = []
    for pixel_row in range(0, len(frame)-(len(frame)%height_and_width), height_and_width*2 ):
        line = []
        for pixel_column in range(0, len(frame[0])-(len(frame[0])%height_and_width), height_and_width):
            character = _fetch_character(_average_brightness([[frame[i][j]
                                                 for j in range(pixel_column, pixel_column + height_and_width, 2)]
                                                 for i in range(pixel_row, pixel_row + height_and_width - 2, 2)]))
            line.append(character)

        ascii_frame.append("".join(line).center(terminal.columns))
    
    return "\n" * (((terminal.lines - len(ascii_frame) - 1) // 2) + 1) \
    + "\n".join(ascii_frame) \
    + "\n" * ((terminal.lines - len(ascii_frame) - 1) // 2)

def create_colored_frame(frame: np.ndarray, height_and_width: int, terminal: os.terminal_size) -> List[str]:
    ascii_frame = []
    for pixel_row in range(0, len(frame), height_and_width * 2):
        line = []
        for pixel_column in range(0, len(frame[0]), height_and_width):
            character = _fetch_colored_character(_average_rgb_brightness([[frame[i][j]
                                                for j in range(pixel_column, pixel_column + height_and_width - 2, 2)]
                                                for i in range(pixel_row, pixel_row + height_and_width - 2, 2)]))
            line.append(character)

        ascii_frame.append("".join(line).center(terminal.columns))

    return "\n".join(ascii_frame)

def create_braille_frame(frame: np.ndarray, height_and_width: int, terminal: os.terminal_size) -> List[str]:
    ascii_frame = []
    bw_im = np.array([[_braille_average_brightness(pixel) > 60 for pixel in row] for row in _fetch_frames(frame, height_and_width)])

    # make the height and width a multiple of 4 and 2
    while len(bw_im) % 4:
        bw_im = np.vstack((bw_im, np.array([False for i in range(len(bw_im[0]))])) )

    while len(bw_im[0]) % 2:
        bw_im = np.hstack((bw_im, np.array([[False,] for i in range(len(bw_im))])) )

    # turn the image data into braille
    vt_group = np.array([bw_im[i * 4 : i * 4 + 4] for i in range(math.ceil(len(bw_im)/4))])
    hz_group = np.array([''.join([
    chr(10240+ a[0][b*2+0] + a[1][b*2+0]*2 + a[2][b*2+0]*4 + a[0][b*2+1]*8 + a[1][b*2+1]*16 + a[2][b*2+1]*32 + a[3][b*2+0]*64 + a[3][b*2+1]*128)
    for b in range(0, math.ceil(len(a[0])/2), 2)]).center(terminal.columns)
    for a in vt_group])
    return '\n'.join(hz_group)

def _fetch_frames(frame: np.ndarray, height_and_width: int) -> List[List[np.ndarray]]:
    frames = []
    for pixel_row in range(0, len(frame), height_and_width * 2):
        line = []
        for pixel_column in range(0, len(frame[0]), height_and_width):
            line.append([[frame[i][j] for j in 
                          range(pixel_column, pixel_column + height_and_width -1, 2)]
                          for i in range(pixel_row, pixel_row + height_and_width -1, 2)])
        frames.append(line)

    return frames

def _average_brightness(pixel):
    amount_of_rgb_values = len(pixel) * len(pixel[0]) * 3
    sum_of_rgb_values = np.sum(np.array(pixel).flatten())
    average = sum_of_rgb_values / (amount_of_rgb_values * 255)
    return average

def _braille_average_brightness(pixel):
    amount_of_rgb_values = len(pixel) * len(pixel[0]) * 3
    sum_of_rgb_values = sum(np.array(pixel).flatten())
    average = sum_of_rgb_values / (amount_of_rgb_values)
    return average

def _average_rgb_brightness(pixel) -> List[float]:
    amount_of_rgb_values = len(pixel) * len(pixel[0]) * 255
    values = [np.sum([value[i]]) for i in range(3) for row in pixel for value in row]
    return list(map(lambda x: x / amount_of_rgb_values, values))
    
def _fetch_colored_character(brightness: List[float]) -> str:
    return f"\033\033[38;2;{int(brightness[0] * 255)};{int(brightness[1] * 255)};{int(brightness[2] * 255)}m"  \
    + "█" \

def _fetch_character(brightness: float) -> str:
    if brightness < 0.03:
        return " "
    if brightness < 0.07692307692:
         return "."
    if brightness < 0.15384615384:
        return ","
    if brightness < 0.23076923076:
        return ":"
    if brightness < 0.30769230769:
        return ";"
    if brightness < 0.38461538461:
        return "*"
    if brightness < 0.46153846153:
        return "¤"
    if brightness < 0.53846153846:
        return "#"
    if brightness < 0.61538461538:
        return "9"
    if brightness < 0.69230769230:
        return "%"
    if brightness < 0.76923076923:
        return "&"
    if brightness < 0.84615384615:
        return "Ñ"
    return '@'
