from numpy import pi, sin, cos, linspace
import matplotlib.pyplot as plt

zero = lambda x: 0*x
f = lambda x: x**2 - 1
g = lambda x: 2*sin(2*x)
x = linspace(-pi, pi, 101)
plt.plot(x, zero(x))
plt.plot(x, f(x), label='zero$(x)$')
plt.plot(x, f(x), label='$f(x)$')
plt.plot(x, g(x), label='$g(x)$')
plt.plot(x, f(x) + g(x), label='$f(x) + g(x)$')
plt.legend()
#plt.savefig('fig2-4-left.pdf', bbox_inches='tight', pad_inches=0)
#plt.savefig('fig2-4-left.png', bbox_inches='tight', pad_inches=0)
plt.show()
