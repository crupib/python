from numpy import arange, cumsum, sqrt
from numpy.random import seed, normal
from trigonometric import lowpass
#from fourier import lowpass
import matplotlib.pyplot as plt

seed(2021)

n = 1000
dt = 1 / n
t = arange(0, 1, dt)
f = cumsum(normal(0, sqrt(dt), n))

fig, ax = plt.subplots(3, 3, figsize=(16, 8))
for k, K in enumerate([0, 1, 2, 4, 8, 16, 32, 64, 128]):
    i, j = divmod(k, 3)
    f_K = lowpass(K, t, f)
    ax[i][j].plot(t, f), ax[i][j].plot(t, f_K)
    ax[i][j].text(0.1, -0.5, f'K = {K}', fontsize = 20)
    ax[i][j].set_xlim(0, 1)
plt.show()
#plt.savefig('brown.png', bbox_inches='tight', pad_inches=0)
