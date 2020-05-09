import librosa


def get_file_bpm(audio_path:str):
    y, sr = librosa.load(audio_path)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo2 = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    return tempo2[0]
