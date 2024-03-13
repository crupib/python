from numpy import linspace, pi, sin, cos, exp
import matplotlib.pyplot as plt

x = linspace(-pi, pi, 101)
plt.xlim(-pi, pi), plt.ylim(-2, 4)
for y in [x - 1, x**2, sin(x), cos(x), exp(x)]:
    plt.plot(x, y)
plt.show()


