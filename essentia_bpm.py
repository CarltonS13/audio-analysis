import essentia
from essentia.streaming import *

def get_file_bpm(audio_path:str):
    loader = MonoLoader(filename = audio_path)
    rhythm_extractor = RhythmExtractor2013(method="degara")

    # code for if using essentia.standard
    # slightly less memory effecient
    # audio = loader()
    # rhythm = rhythm_extractor(audio)
    # return rhythm[0]

    # code for percival estimator
    # pool = essentia.Pool()
    # percival_bpm_estimator = PercivalBpmEstimator()
    # loader.audio >> rhythm_extractor.signal
    # percival_bpm_estimator.bpm >> (pool, 'rhythm')

    pool = essentia.Pool()
    loader.audio >> rhythm_extractor.signal
    rhythm_extractor.ticks >> None
    rhythm_extractor.confidence >> None
    rhythm_extractor.bpm >> (pool, 'rhythm')
    rhythm_extractor.estimates >> None
    rhythm_extractor.bpmIntervals >> None
    essentia.run(loader)
    return pool['rhythm']
