from typing import List
import numpy as np
import time

def create_frame(
        frame: np.ndarray,
        pixel_width: int,
        pixel_height: int) -> List[str]:
 
    ascii_frame = []
    frames_fetched = _fetch_frames(frame, pixel_width, pixel_height)
    for row in frames_fetched:
        frame_line = "".join([_fetch_character(_average_brightness(pixel)) for pixel in row])
        ascii_frame.append(frame_line) 
    return "\n".join(ascii_frame[::2])
   
def _fetch_frames(frame: np.ndarray, pixel_width: int, 
                  pixel_height: int) -> List[List[np.ndarray]]:
    frames = []
    for pixel_row in range(0, len(frame), pixel_height):
        line = []
        for pixel_column in range(0, len(frame[0]), pixel_width):
            line.append([[frame[i][j] for j in 
                      range(pixel_column, pixel_column + pixel_width)]
                      for i in range(pixel_row, pixel_row + pixel_height)])
            
        frames.append(line)
    return frames

def _average_brightness(pixel: List[np.ndarray]) -> float:
    amount_of_rgb_values = (len(pixel) * len(pixel[0])) * 3
    sum_of_rgb_values = sum([sum(rgb) for pix in pixel for rgb in pix])
    average = sum_of_rgb_values / (amount_of_rgb_values * 255)
    return average

def _fetch_character(brightness: float) -> str:
    match brightness:
        case brightness if brightness >= 0.85:
            return "#"
        case brightness if brightness >= 0.7:
            return "%"
        case brightness if brightness >= 0.6:
            return "*"
        case brightness if brightness >= 0.4:
            return "-"
        case brightness if brightness >= 0.2:
            return ":"
        case brightness if brightness >= 0.1:
            return "."
        case _:
            return " "
        
           
            
            
