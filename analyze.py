import pyaudio
import wave
import numpy as np
import librosa
from scipy.fft import fft, fftfreq
import sys
from functions import *

import matplotlib.pyplot as plt


def find_frequency_and_string(filename):
    # Load the .wav file
    
    y, sr = librosa.load(filename, sr = None)

    # Find the index of the loudest sound

    # Compute the FFT
    # y = slice(y, loudest_time)
    N = len(y)
    yf = fft(y)
    xf = fftfreq(N, 1 / sr)

    # Take only the positive frequencies
    positive_freq_indices = np.where(xf > 0)
    xf = xf[positive_freq_indices]
    yf = np.abs(yf[positive_freq_indices])

    # Create the frequency-amplitude array
    frequency_amplitude = np.zeros_like(xf)
    for i, freq in enumerate(xf):
        frequency_amplitude[i] = yf[i]

    # frequency_amplitude now contains frequencies and their corresponding amplitudes

    # Normalize the y-value by dividing all values by max y
    max_y = max(yf)
    yf = [yf[i]/max_y for i in range(len(yf))]


    #PRINTS FREQENCIES OUTPUTTED BY FFT
    # for i, freq in enumerate(xf):
    #     print(f"Index {i}: Frequency = {freq:.2f} Hz, Amplitude = {yf[i]:.2f}")
        

    #Find fundamental frequency and guess string
    fund_freq = find_fundamental_freq(xf, yf)
    # print("I'm a computer and I know music, you plucked the ", guess_string(fund_freq))
    # print("The fundamental frequency found is: ", fund_freq)
    # sys.stdout.flush()



    #ACTUAL AMPLITUDE VS. FREQUENCY
    # plt.plot(xf, yf)
    # plt.show()
    print(len(xf))
    return fund_freq, guess_string(fund_freq)


# find_frequency_and_string('./guitar_strings/B_string.wav')