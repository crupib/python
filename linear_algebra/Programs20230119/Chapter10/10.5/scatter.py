import numpy as np
import vpython as vp
import matplotlib.pyplot as plt

with open('data.csv', 'r') as fd:
    lines = fd.readlines()
data = np.array([eval(line) for line in lines[1:]])

def scatter3d(data):
    o = vp.vec(0, 0, 0)
    vp.curve(pos=[o, vp.vec(100, 0, 0)], color=vp.color.red)
    vp.curve(pos=[o, vp.vec(0, 100, 0)], color=vp.color.green)
    vp.curve(pos=[o, vp.vec(0, 0, 100)], color=vp.color.blue)
    vp.points(pos=[vp.vec(*a) for a in data], radius=3)

def scatter2d(data, savefig=None):
    A = data.T
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    for n, B in enumerate([A[[0, 1]], A[[0, 2]], A[[1, 2]]]):
        s = B.dot(B.T)
        cor = s[0, 1] / np.sqrt(s[0, 0]) / np.sqrt(s[1, 1])
        print(f'{cor:.3}')
        axs[n].scatter(B[0], B[1])
    if savefig is not None:
        plt.savefig(f'{savefig}.png', bbox_inches='tight', pad_inches=0.05)
    else:
        plt.show()

if __name__ == '__main__':
    scatter3d(data)
    scatter2d(data)


