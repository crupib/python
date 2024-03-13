from numpy import linspace, pi, sin, cos, exp
from math import factorial
from matplotlib import pyplot

X = linspace(-2 * pi, 2 * pi, 256, endpoint=True)
Y = [X**n / factorial(n) for n in range(12)]
F = [sin, cos, exp]

fig, ax = pyplot.subplots(1, 3, figsize=(16, 8))
for n in range(3):
    f = F[n](X)
    ax[n].axis('scaled')
    ax[n].plot(X, f, lw=3)
    ax[n].set_xlim(-2 * pi, 2 * pi)
    ax[n].set_ylim(-5, 5)

f = 0
for y in [Y[1], -Y[3], Y[5], -Y[7], Y[9], -Y[11]]:
    f += y
    ax[0].plot(X, f)

f = 0
for y in [Y[0], -Y[2], Y[4], -Y[6], Y[8], -Y[10]]:
    f += y
    ax[1].plot(X, f)

f = 0
for y in Y:
    f += y
    ax[2].plot(X, f)
'''
import os
import sys
name =  os.path.basename(sys.argv[0]).split('.')[0]
plt.savefig('image.pdf', format='pdf')
os.system('pdfcrop image.pdf ' + name + '.pdf')
'''
pyplot.show()
