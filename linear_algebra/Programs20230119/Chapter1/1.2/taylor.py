from numpy import linspace, pi, sin, cos, exp
from math import factorial
import matplotlib.pyplot as plt

X = linspace(-2 * pi, 2 * pi, 256, endpoint=True)
Y = [X**n / factorial(n) for n in range(12)]
F = [sin, cos, exp]

plt.figure(figsize=(16, 8))
for n in range(3):
    plt.subplot(131+n)
    f = F[n](X)
    plt.axis('scaled')
    plt.plot(X, f, lw=3)
    plt.xlim(-2 * pi, 2 * pi)
    plt.ylim(-5, 5)

f = 0
for y in [Y[1], -Y[3], Y[5], -Y[7], Y[9], -Y[11]]:
    f += y
    plt.subplot(131)
    plt.plot(X, f)
    plt.title('$\sin x$')

f = 0
for y in [Y[0], -Y[2], Y[4], -Y[6], Y[8], -Y[10]]:
    f += y
    plt.subplot(132)
    plt.plot(X, f)
    plt.title('$\cos x$')

f = 0
for y in Y:
    f += y
    plt.subplot(133)
    plt.plot(X, f)
    plt.title('$\exp x$')

plt.savefig('taylor.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()
