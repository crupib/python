import turtle
def	polygon(t,n,length):
        if n > 0:
           angle = 360/n
        else:
             print("n not a valid number n>0")
             return -1
        for i in range(n):
                t.fd(length)
                t.lt(angle)
bob = turtle.Turtle()
polygon(bob,n=11,length=70)
turtle.mainloop()
	
