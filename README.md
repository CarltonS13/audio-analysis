## Some tools for audio analysis

##Dependencies
Essentia music analysis library
Librosa can be used instead (2.5x - 10x slower)

### beat_detect.py

A python script to recursively get all flac and music files in the directory indicated by the "directory" variable and find their bpm.


## Todo
1. Create a CLI command for get_beat.py to set directory and algorithm for analysis(Librosa or Essentia)

2. Create method to detect energy in music 

3. Create script to split music by variation in energy
