from numpy import exp, pi, linspace
import matplotlib.pyplot as plt

f = lambda n, t: exp(1j * n * t)
t = linspace(0, 2 * pi, 1001)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
for n in range(-2, 3):
    z = f(n, t)
    ax.plot(t, z.real, z.imag)
plt.show()
#plt.savefig('cfunc.png', bbox_inches='tight', pad_inches=0)
