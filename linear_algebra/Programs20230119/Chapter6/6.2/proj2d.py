from vpython import proj, color, curve, vec, hat, box, arrow,\
  label

def proj2d(x, e}: return x - proj(x, e)

def draw_cube(o, x, y, z):
    axes, cols = [x, y, z], [color.red, color.green, color.blue]
    planes = [(y, z), (z, x), (x, y)]
    for ax, col, p in zip(axes, cols, planes):
        face = [o, o + p[0], o + p[0] + p[1], o + p[1]]
        for vertex in face:
            curve(pos=[vertex, vertex + ax], color=col)

o, e, u = vec(0, 0, 0), hat(vec(1, 2, 3)), vec(5, 5, 5)
x, y, z = vec(1, 0, 0), vec(0, 1, 0), vec(0, 0, 1)
box(pos=-0.1 * e, axis=e, up=proj2d(y, e),
    width=20, height=20, length=0.1, opacity=0.5)
arrow(axis=3 * e)
for ax, lbl in [(x, 'x'), (y, 'y'), (z, 'z')]:
    curve(pos=[-5 * ax, 10 * ax], color=vec(1, 1, 1) - ax)
    label(pos=10 * ax, text=lbl)
    curve(pos=[proj2d(-5 * ax, e), proj2d(10 * ax, e)], color=ax)
    label(pos=proj2d(10 * ax, e), text=f"{lbl}'")
c1 = [u, 2*x, 2*y, 2*z]
c2 = [proj2d(v, e) for v in c1]
draw_cube(*c1), draw_cube(*c2)
