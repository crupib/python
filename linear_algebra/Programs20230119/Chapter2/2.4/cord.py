from numpy import arange, pi, sin
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

xmax, rate = 2, 22050
x = arange(0, xmax, 1 / rate)


def f(hz):
    return [sin(2 * pi * hz * x) * 0.9 for n in range(-2, 3)]


A = f(440.000000)
B = f(493.883301)
C = f(523.251131) 
D = f(587.329536)
E = f(659.255114)
F = f(698.456463)
G = f(783.990872)
CEG = (C[2] + E[2] + G[2]) / 3
Data = (CEG * 32768).astype('int16')
wav.write('CEG.wav', rate, Data)
for y in [C[2], E[2], G[2], CEG]:
    plt.plot(x, y)
plt.xlim(1, 1.01)
plt.show()
#plt.savefig('cord.png', bbox_inches='tight', pad_inches=0)
