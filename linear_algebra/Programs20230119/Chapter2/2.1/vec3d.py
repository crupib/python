from vpython import vec, arrow, mag

o = vec(0, 0, 0)
x, y, z = vec(1, 0, 0), vec(0, 1, 0), vec(0, 0, 1)
arrows = [(o, x + y), (x, y + z), (o, x + y + z), (o, x), (y, x),
          (z, x), (y + z, x), (o, y), (x, y), (z, y), (x + z, y),
          (o, z), (x, z), (y, z), (x + y, z)]
for p, v in arrows:
    arrow(pos=p, axis=v, color=v, shaftwidth=mag(v) / 50)
