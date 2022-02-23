import os
import sys
from src.video_file import VideoFile
from src.frame import create_frame
from src.scale import scale
import time
from tqdm import tqdm


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
        raise ValueError(f"Terminal of size {terminal.lines} lines and {terminal.columns} columns too small.")

    height_and_width = scale(terminal, *video.get_resolution())
 
    ascii_frames = []
    for i in (loader := tqdm(range(0, video.frame_count(), 1))):
        frame = create_frame(video.get_frame(i), height_and_width, terminal)
        loader.set_description("Loading frames...")
        ascii_frames.append(frame)

    if input("Input anything to start"):
        for frame in ascii_frames:
            print(frame)
            time.sleep(1/24)
        
if __name__ == "__main__":
    main()
