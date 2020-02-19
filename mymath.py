import math

def acirc(radius):
	a = math.pi * radius**2
	return a

def absolute_value(x):
	if x < 0:
		return -x
	else:
		return x
def distance(x1,y1,x2,y2):
	dx = x2-x1
	dy = y2-y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result 
def circle_area(xc,yc,xp,yp):
	return acirc(distance(xc,yc,xp,yp))

print(acirc(10))
print(absolute_value(-5))
print(distance(1,2,4,6))
print(circle_area(4,4,10,10))
	

