import math

def acirc(radius):
	a = math.pi * radius**2
	return a

def absolute_value(x):
	if x < 0:
		return -x
	else:
		return x

print(acirc(10))
print(absolute_value(-5))


