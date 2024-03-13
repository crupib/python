from numpy import arange
import matplotlib.pyplot as plt


def taylor_1st(x, v, dt):
    dx = v * dt
    dv = -x * dt
    return x + dx, v + dv

   
def taylor_2nd(x, v, dt):
    dx = v * dt - x / 2 * dt ** 2
    dv = -x * dt - v / 2 * dt ** 2
    return x + dx, v + dv

fig = plt.figure(figsize=(18,6))
update = taylor_1st  # taylor_2nd
for dt, pos in [(0.1, 131),  (0.01, 132), (0.001, 133)]:
    plt.subplot(pos)
    plt.axis('scaled'), plt.xlim(-3.0, 3.0), plt.ylim(-3.0, 3.0)
    path = [(2.0, 0.0)]  # (x, v)
    for t in arange(0, 500, dt):
        x, v = path[-1]
        path.append(update(x, v, dt))
    plt.plot(*zip(*path))
plt.show()
#plt.savefig('taylor1.png', bbox_inches='tight', pad_inches=0.05)
