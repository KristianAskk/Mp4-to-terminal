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
    terminal = os.get_terminal_size()
    height_and_width = scale(os.get_terminal_size(), *video.get_resolution())
 
    for i in (t := tqdm(range(0, video.frame_count(), 1))):
        frame = create_frame(video.get_frame(i), height_and_width, terminal)
        t.set_description("Loading frames...")
        ascii_frames.append(frame)

    if input("Input anything to start"):
        for frame in ascii_frames:
            print(frame)
            time.sleep(1/24)
        
if __name__ == "__main__":
    main()
