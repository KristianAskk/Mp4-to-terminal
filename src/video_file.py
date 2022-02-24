from typing import Any, List, Tuple

import cv2
import numpy as np


class VideoFile:
    """An object representing a video file."""

    def __init__(self, file_dir: str):
        self._file_dir = file_dir
        self._cap = cv2.VideoCapture(file_dir)

    def get_resolution(self) -> Tuple[int, int]:
        """Returns a tuple containing the height and width of the video.

        Returns
        -------
        Tuple[int, int]
            the first int returning the height and the second return the width. (x, y)
        """
        self._cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        _, frame = self._cap.read()
        return (len(frame), len(frame[0]))

    def get_frames(self):
        frames = []
        for fno in range(0, int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))):
            self._cap.set(cv2.CAP_PROP_POS_FRAMES, fno)
            _, image = self._cap.read()
            frames.append(image)
        print("Frames are done")
        return frames

    def get_frame(self, frame: int) -> np.ndarray:
        """Returns the specific frame.

        Parameters
        ----------
        frame : int
            the frame number.

        Returns
        -------
        np.ndarray
            returns a numpy array containing the rgb values of each individual pixel in the frame.
        """
        try:
            self._cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
            _, frame = self._cap.read()
            return frame
        except Exception as e:
            print(e)

    def frame_count(self) -> int:
        return int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))
