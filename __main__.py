import os
import sys
from typing import List
from src.video_file import VideoFile
from src.frame import create_frame
from src.scale import scale
import time
from tqdm import tqdm
import concurrent.futures
import numpy as np


def process(frame: np.ndarray, height_and_width) -> List[str]:
    terminal = os.get_terminal_size()
    return create_frame(frame, height_and_width, terminal)


def main():

    if len(sys.argv) < 2:
        raise ValueError("Directory of video file not specified.")

    if not sys.argv[1].endswith(".mp4"):
        raise ValueError("Name of given file must end with .mp4.")

    if sys.argv[1] in os.listdir(f"{os.path.dirname(__file__)}"):
        video = VideoFile(f"{os.path.dirname(__file__)}/{sys.argv[1]}")
    else:
        if sys.argv[1] in os.listdir(f"{os.path.dirname(__file__)}/.."):
            video = VideoFile(f"{os.path.dirname(__file__)}/../{sys.argv[1]}")
        else:
            raise ValueError(f".mp4 file of name {sys.argv[1]} not found.")

    terminal = os.get_terminal_size()
    if terminal.lines <= 8 or terminal.columns <= 8:
        raise ValueError(
            f"Terminal of size {terminal.lines} lines and {terminal.columns} columns too small."
        )

    ascii_frames = []
    height_and_width = scale(os.get_terminal_size(), *video.get_resolution())

    with concurrent.futures.ProcessPoolExecutor() as exec:
        for i in (
            t := tqdm(range(int(sys.argv[2]), video.frame_count(), int(sys.argv[2])))
        ):
            results = [
                exec.submit(process, video.get_frame(i - j), height_and_width)
                for j in range(int(sys.argv[2]) - 1, -1, -1)
            ]
            t.set_description("Loading frames...")
            for i in range(int(sys.argv[2])):
                ascii_frames.append(results[i].result())
            # for f in concurrent.futures.as_completed(results):
            #     ascii_frames.append(f.result())

    if input("Input anything to start"):
        for frame in ascii_frames:
            print(frame)
            time.sleep(1 / 24)


if __name__ == "__main__":
    main()
