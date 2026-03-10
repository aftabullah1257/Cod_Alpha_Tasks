# Note: Requires 'librosa' and 'tensorflow'
import librosa
import numpy as np

def extract_mfcc(file_path):
    # Extracting Mel-Frequency Cepstral Coefficients (MFCCs)
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40).T, axis=0)
    return mfccs

# You would then feed these features into a CNN or LSTM model