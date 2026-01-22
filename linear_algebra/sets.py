from numpy import pi
import math

x = 1 + 2j
print(x.real, x.imag, abs(x), x.conjugate())
print(x)
y = 3 + 4j
print(x + y, x * y, x / y)
print(math.e**(pi * 1j))