from numpy import arange, exp, pi, vdot
from gram_schmidt import proj


def e(k, t): return exp(2j * pi * k * t)


def lowpass(K, t, z):
    dt = 1 / len(t)
    E_K = [e(k, t) for k in range(-K, K + 1)]
    return proj(z, E_K, inner=lambda x, y: vdot(x, y) * dt)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure(figsize=(20, 8))
    t = arange(0, 1, 1 / 1000)
    for n, k  in enumerate([0, 1, 2, 100, 300, 500, 700, 900, 998, 999]):
        x = [z.real for z in e(k, t)]
        y = [z.imag for z in e(k, t)]
        #print(n, k)
        ax = fig.add_subplot(2, 5, n+1, projection="3d")
        ax.set_xlim(0, 1), ax.set_ylim(-1, 1), ax.set_zlim(-1, 1)
        ax.plot(t, x, y), ax.text(0, 1, 1, f'k = {k}', fontsize = 20)
    plt.show()
    #plt.subplots_adjust(left=0, right=0.99, bottom=0.05, top=1, hspace=0.1, wspace=0)
    #plt.savefig('fourier.png', bbox_inches='tight', pad_inches=0)
