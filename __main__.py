import os
import sys
from src.video_file import VideoFile
from src.frame import create_frame
from src.scale import scale
import time
from tqdm import tqdm


def main():
    video = VideoFile(f"{os.path.dirname(__file__)}/{sys.argv[1]}")
    ascii_frames = []
    width, height = scale(os.get_terminal_size(), *video.get_resolution())
 
    for i in (t := tqdm(range(0, 100, 1))):
        frame = create_frame(video.get_frame(i), width, height)
        t.set_description("Loading frames...")
        ascii_frames.append(frame)

    if input("Input anything to start"):
        for frame in ascii_frames:
            print(frame)
            time.sleep(1/24)
        
if __name__ == "__main__":
    main()
