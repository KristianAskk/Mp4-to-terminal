import argparse
import os
import sys
from typing import List
from src.video_file import VideoFile
from src.frame import create_frame, create_braille_frame, create_colored_frame
from src.scale import scale, braille_scale
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
    parser.add_argument("-p", "--processes", help="specify the number of processes that will be converting the video.", default='1')
    parser.add_argument("-t", "--type", help='Choose to either display the video in color or braille. Set to displaying video with characters by default.', default='chars', choices=('chars', 'braille', 'color'))
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

    if not args.file in os.listdir(f"{os.path.dirname(__file__)}/.."):
        os.listdir(f"{os.path.dirname(__file__)}/..")
        raise ValueError("file not found")

    video = VideoFile(f'{os.path.dirname(__file__)}/../{args.file}')

    scaler = scale
    frame_processor = create_frame

    if args.type:
        if args.type == 'braille':
            scaler = braille_scale
            frame_processor = create_braille_frame
        elif args.type == 'color':
            scaler = scale
            frame_processor = create_colored_frame

    height_and_width = scaler(os.get_terminal_size(), *video.get_resolution())
    ascii_frames = []

    with concurrent.futures.ProcessPoolExecutor() as exec:
        for i in (t := tqdm(range(int(args.processes), video.frame_count(), int(args.processes)))):
            results = [
                exec.submit(frame_processor, video.get_frame(i - j), height_and_width, terminal)
                for j in range(int(args.processes) - 1, -1, -1)
            ]

            t.set_description("Loading frames...")
            for i in range(int(args.processes)):
                ascii_frames.append(results[i].result())
    os.system("clear")
    input("Input anything to start")
    for frame in ascii_frames:
        print(frame)
        time.sleep(1 / 24)
    print("End")
    



if __name__ == "__main__":
    main()
