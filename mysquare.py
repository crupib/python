import turtle
def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
       t.fd(length)
       t.lt(angle)

bob = turtle.Turtle()
polygon(bob, 360, 1)
turtle.mainloop()
