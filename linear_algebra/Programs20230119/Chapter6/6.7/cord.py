from numpy import arange, pi, sin
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

tmax = 2
rate = 22050
dt = 1 / rate
T = arange(0, tmax, dt)


def f(hz):
    return sin(2 * pi * hz * T) * 0.9


A = [f(440.000000 * 2**n) for n in range(-2, 3)]
B = [f(493.883301 * 2**n) for n in range(-2, 3)]
C = [f(523.251131 * 2**n) for n in range(-2, 3)]
D = [f(587.329536 * 2**n) for n in range(-2, 3)]
E = [f(659.255114 * 2**n) for n in range(-2, 3)]
F = [f(698.456463 * 2**n) for n in range(-2, 3)]
G = [f(783.990872 * 2**n) for n in range(-2, 3)]
CEG = (C[2] + E[2] + G[2]) / 3
Data = (CEG * 32768).astype('int16')
wav.write('CEG.wav', rate, Data)

for Y in [C[2], E[2], G[2], CEG]:
    plt.plot(T, Y)
plt.xlim(1, 1.01), plt.show()
#plt.savefig('cord.png', bbox_inches='tight', pad_inches=0)
