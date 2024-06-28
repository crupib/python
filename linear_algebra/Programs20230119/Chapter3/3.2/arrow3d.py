from vpython import vec, arrow, mag

o = vec(0, 0, 0)
for p in [(1, 2, 3), (2, 3, 4), (3, 4, 5), (3, 1, 2)]:
    v = vec(*p)
    arrow(pos=o, axis=v, color=v, shaftwidth=mag(v) * 0.02)
