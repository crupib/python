import turtle
import math
def polygon(t,n,length):
        if n > 0:
           angle = 360/n
        else:
             print("n not a valid number n>0")
             return -1
#       for i in range(n):
#               t.fd(length)
#               t.lt(angle)
        polyline(t,n,length,angle)
# circle def
def circle(t,r):
	circumference = 2 * math.pi * r
	n = int(circumference/3) + 1
	length = circumference / n
	polygon(t,n,length)
def circle2(t,r):
       arc(t,r,360)
def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t,n,step_length,step_angle)
#    for i in range(n):
#        t.fd(step_length)
#        t.lt(step_angle)
"""Draws n line segments with the given length and
angle (in degrees) between them. t is a turtle.
"""
def polyline(t,n,length,angle):
   for i in range(n):
       t.fd(length)
       t.lt(angle)
bob = turtle.Turtle()
polygon(bob,n=11,length=70)
#circle2(bob,100)
turtle.mainloop()

