import matplotlib.pyplot as plt
def ball_trajectory(x):
    location = 10*x -5*(x**2)
    return(location)
xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]
xs2 = [0.1,2]
ys2 = [ball_trajectory(0.1),0]
xs3 = [0.2,2]
ys3 = [ball_trajectory(0.2),0]
xs4 = [0.3,2]
ys4 = [ball_trajectory(0.3),0]
xs5 = [0.3,0.3]
ys5 = [ball_trajectory(0.3),0]
xs6 = [0.3,2]
ys6 = [0,0]
plt.title('The Trajectory of a Thrown Ball')
plt.xlabel('Horizontal Postion of Ball')
plt.ylabel('Vertical Position of Ball')
plt.axhline(y = 0)
plt.plot(xs,ys,xs4, ys4,xs4,ys5,xs6, ys6)
plt.show()
