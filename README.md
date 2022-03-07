# Mp4 to Terminal

A small conversion program that converts a .mp4 file to text and displays it in the terminal. Videoes can be displayed with both braille and characters respectively. 

![example](https://user-images.githubusercontent.com/77408372/157014508-cb7e3923-2350-401a-a63f-13e9d9420fb9.gif)

## Quick start

- Clone the github repository
- Move your .mp4 file in the same directory as the cloned repo
- Install dependencies listed in __requirements.txt__
- Run the program while specifying the name of the video file and the number of processes that will be converting the video. 

E.g:
```
python3 Mp4-to-terminal -f video.mp4 -p 2
```


## TODO: 
- [x] Rewrite or edit the __scale__ method ( it's a mess )
- [x] Improve video processing time 
- [x] Make the project runnable as a whole instead of running it with __main__.py ( in other words, fix importing )
- [x] The function __scale__ is currently returning None if the terminal is too small.
- [x] Remove unused methods in the VideoFile class
- [x] Add threading
- [x] Center the video being displayed
- [x] Add whitespaces to ensure that only one frame is being displayed at a time.
- [ ] Add comments 
- [ ] Write installation process and proper description
- [x] Add multiprocessing limit

## Credits

- @Feeenix for making option for video being displayed in braille possible
