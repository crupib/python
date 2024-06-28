from numpy import inner, pi, sin, cos, sqrt, ones
from gram_schmidt import proj


def e(k, t):
    if k < 0:
        return sin(2 * k * pi * t) * sqrt(2)
    elif k == 0:
        return ones(len(t))
    elif k > 0:
        return cos(2 * k * pi * t) * sqrt(2)


def lowpass(K, t, f):
    n = len(t)
    E_K = [e(k, t) for k in range(-K, K + 1)]
    return proj(f, E_K, inner=lambda x, y: inner(x, y) / n)


if __name__ == '__main__':
    from numpy import arange
    import matplotlib.pyplot as plt
    t = arange(0, 1, 1 / 1000)
    plt.figure(figsize=(15, 5))
    plt.subplot(121)
    for k in range(-3, 0):
        plt.plot(t, e(k, t))
    plt.subplot(122)
    for k in range(4):
        plt.plot(t, e(k, t))
    plt.show()
    #plt.savefig('trigonometric.png', bbox_inches='tight', pad_inches=0)
