# Mp4 to Terminal

A small conversion program that converts an .mp4 file to text and displays it in the terminal.

## Quick start

- Clone the github repository
- Move your .mp4 file to the same directory as the repo
- Run the program while specifying the name of the video file and the number of processes that will be converting the video. 

E.g:
```
python3 Mp4-to-terminal video.mp4 2
```


## TODO: 
- [ ] Rewrite or edit the __scale__ method ( it's a mess )
- [x] Improve video processing time 
- [x] Make the project runnable as a whole instead of running it with __main__.py ( in other words, fix importing )
- [x] The function __scale__ is currently returning None if the terminal is too small.
- [x] Remove unused methods in the VideoFile class
- [x] Add threading
- [x] Center the video being displayed
- [x] Add whitespaces to ensure that only one frame is being displayed at a time.
- [ ] Add comments 
- [ ] Write installation process and proper description
- [ ] Add multiprocessing limit
