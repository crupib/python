import numpy as np

with open('data.csv', 'r') as fd:
    lines = fd.readlines()
data = [np.array(eval(line)) for line in lines[1:]]

if __name__ == '__main__':
    from vpython import *

    o = vector(0, 0, 0)
    x, y, z = vector(1, 0, 0), vector(0, 1, 0), vector(0, 0, 1)
    curve(pos=[o, x * 100], color=color.red)
    curve(pos=[o, y * 100], color=color.green)
    curve(pos=[o, z * 100], color=color.blue)
    points(pos=[vector(*xyz) for xyz in data], radius=3)
