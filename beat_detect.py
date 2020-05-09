import mutagen
import time
from get_dir_files import run_fast_scandir
from essentia_bpm import get_file_bpm
from progress_bar import printProgressBar

directory = r"/Volumes/Carl'S/Music"
subf, files = run_fast_scandir(
    directory, [".flac"])

files_length = len(files)
files_count = 0
print("Processing %d files" % files_length);

time1 = time.time()
printProgressBar(0, files_length, prefix='Progress:',
                 suffix='Complete', length=50)
for file in files:
    files_count = files_count + 1
    try:
        song = mutagen.File(file, easy=True)
        if(not song.get("bpm", False)):
            song["bpm"] = str(int(get_file_bpm(file)))
            song.save()
        print("Processed:" + file, file=open("output.txt", "a"))
    except:
        print("Failed:" + file, file=open("output.txt", "a"))
    printProgressBar(files_count, files_length,
                     prefix='Progress:', suffix='Complete', length=50)
time2 = time.time()

millis = int((time2 - time1) * 1000.0)
seconds = (millis / 1000) % 60
seconds = int(seconds)
minutes = (millis / (1000 * 60)) % 60
minutes = int(minutes)
hours = (millis / (1000 * 60 * 60)) % 24

print(" Took %d:%d:%d" % (hours, minutes, seconds))
