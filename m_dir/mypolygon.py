import turtle
import math

def circle(t,r):
   arc(t, r, 360)

def polygon(t,n,length):
   angle = 360 / n
   polyline(t, n, length, angle)

def arc(t, r, angle):
   arc_length = 2 * math.pi * r * angle / 360
   n = int(arc_length / 3) + 1
   step_length = arc_length / n
   step_angle = angle / n
   for i in range(n):
       t.fd(step_length)
       t.lt(step_angle)

def polyline(t, n, length, angle):
   """Draws n line segments with the given length and angle (in degrees) between them. t is turtle.
   """
   for i in range(n):
      t.fd(length)
      t.lt(angle)      
bob = turtle.Turtle()
#polygon(bob,n=11,length=70)
#circle(bob,100)
arc(bob, 50, 275)
turtle.mainloop()
