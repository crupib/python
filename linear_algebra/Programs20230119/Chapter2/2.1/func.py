from numpy import pi, sin, cos, linspace
import matplotlib.pyplot as plt

zero = lambda x: 0*x
f = lambda x: x**2 - 1
g = lambda x: 2*sin(2*x)
fig = plt.figure(figsize=(20, 5))
x = linspace(-pi, pi, 101)
ax1 = fig.add_subplot(131)
for y in [zero(x), f(x), g(x), f(x) + g(x)]:
    ax1.plot(x, y)
ax2 = fig.add_subplot(132)
for y in [zero(x), f(x), -f(x), f(x)/2]:
    ax2.plot(x, y)
ax3 = fig.add_subplot(133)
for y in [zero(x), g(x), -g(x), 3*g(x)]:
    ax3.plot(x, y)
plt.show()
#plt.savefig('func.png', bbox_inches='tight', pad_inches=0)
