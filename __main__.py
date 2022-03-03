import argparse
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

MULTIPROCESS_LIMIT = 9


def main():

    terminal = os.get_terminal_size()
    if terminal.lines <= 8 or terminal.columns <= 8:
        raise ValueError(
            f"Terminal of size {terminal.lines} lines and {terminal.columns} columns too small."
        )

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Name of .mp4 file", required=True)
    parser.add_argument(
        "-p",
        "--processes",
        help="Number of processes that will be converting the video.",
        required=True
    )
    args = parser.parse_args()

    try:
        if not args.processes.isnumeric():
            raise ValueError(
                f"Value of type {type(args.processes)} not valid, use an integer."
            )
    except Exception as e:
        raise ValueError("Number of processes not given")

    if int(args.processes) >= MULTIPROCESS_LIMIT:
        raise ValueError(f"Cannot exceed {MULTIPROCESS_LIMIT} processes")

    if args.file:
        if not args.file in os.listdir("."):
            raise ValueError("file not found")

    else:
        raise ValueError("Name of file not given")

    video = VideoFile(args.file)
    ascii_frames = []
    height_and_width = scale(os.get_terminal_size(), *video.get_resolution())
    with concurrent.futures.ProcessPoolExecutor() as exec:
        for i in (
            t := tqdm(
                range(int(args.processes), video.frame_count(), int(args.processes))
            )
        ):
            results = [
                exec.submit(
                    create_frame, video.get_frame(i - j), height_and_width, terminal
                )
                for j in range(int(args.processes) - 1, -1, -1)
            ]
            t.set_description("Loading frames...")
            for i in range(int(args.processes)):
                ascii_frames.append(results[i].result())

    if input("Input anything to start"):
        for frame in ascii_frames:
            prev_time = time.time()
            print(frame)
            new_time = time.time()
            time.sleep(max(0,(1 / 30)-(new_time -prev_time)))


if __name__ == "__main__":
    main()
