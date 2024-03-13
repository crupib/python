import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

file_name = 'mono'
ext = 'png'
rate, Data = wav.read(file_name + '.wav')
print(rate, Data.shape)
n = len(Data)
t = n / rate
dt = 1 / rate
print(t, dt)

#x = np.arange(n) / n
x = np.arange(0, n*dt, dt)
#x = np.linspace(0, t, n, endpoint=False)
y = Data / 32768

if len(Data.shape) == 1:
    plt.plot(x, y)
    plt.xlim(0, t), plt.ylim(-1, 1)
elif len(Data.shape) == 2:
    fig, ax = plt.subplots(2)
    for i in range(2):
        ax[i].plot(x, y[:, i])
        ax[i].set_xlim(0, t), ax[i].set_ylim(-1, 1)
if ext:
    plt.savefig(file_name + '.' + ext, bbox_inches='tight', pad_inches=0)
else:
    plt.show()
