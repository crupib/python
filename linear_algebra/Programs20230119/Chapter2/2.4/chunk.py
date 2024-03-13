import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

rate, Data = wav.read('bird.wav')
wav.write('stereo.wav', rate, Data)
