from numpy import array, linspace, identity, exp, pi, linalg
from numpy.polynomial.legendre import Legendre
import matplotlib.pyplot as plt

with open('tablet.txt', 'r') as fd:
    y = eval(fd.read())
m = len(y)
x = linspace(0.0, 1.0, m)


def phi1(n): 
    return array([(x0 >= x).astype('int')
                  for x0 in linspace(0, 1, n)]).T


def phi2(n):
    return array([exp(2 * pi * k * 1j * x)
                  for k in range(-n // 2, n // 2 + 1)]).T


def phi3(n):
    return array([Legendre.basis(j, domain=[0, 1])(x)
                  for j in range(n)]).T


fig, axs = plt.subplots(3, 5, figsize=(15, 8))
for i, f in enumerate([phi1, phi2, phi3]):
    for j, n in enumerate([8, 16, 32, 64, 128]):
        ax = axs[i, j]
        c = linalg.lstsq(f(n), y, rcond=None)[0]
        z = f(n).dot(c)
        ax.scatter(z.real, z.imag, s=5), ax.plot(z.real, z.imag)
        ax.axis('scaled'), ax.set_xlim(-1, 1), ax.set_ylim(-1, 1)
        ax.tick_params(labelbottom=False, labelleft=False,
                       color='white')
        ax.text(-0.9, 0.8, f'n={n}', fontsize=12)

plt.subplots_adjust(left=0.2, right=0.8, bottom=0.1, top=0.9,
                    hspace=0.01, wspace=0.02)
plt.show()
#plt.savefig('moji.png', bbox_inches='tight', pad_inches=0.05)
