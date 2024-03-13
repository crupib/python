from numpy import random, exp, dot
from tkinter import Tk, Canvas


class Screen:
    def __init__(self, N, size=600):
        self.N = N
        self.unit = size // self.N
        tk = Tk()
        self.canvas = Canvas(tk, width=size, height=size)
        self.canvas.pack()
        self.pallet = ['white', 'black']
        self.matrix = [[self.pixel(i, j) for j in range(N)]
                       for i in range(N)]

    def pixel(self, i, j):
        rect = self.canvas.create_rectangle
        x0, x1 = i * self.unit, (i + 1) * self.unit
        y0, y1 = j * self.unit, (j + 1) * self.unit
        return rect(x0, y0, x1, y1)

    def update(self, X):
        config = self.canvas.itemconfigure
        for i in range(self.N):
            for j in range(self.N):
                c = self.pallet[X[i, j]]
                ij = self.matrix[i][j]
                config(ij, outline=c, fill=c)
        self.canvas.update()


def reverse(X, i, j):
    i0, i1 = i - 1, i + 1
    j0, j1 = j - 1, j + 1
    n, s, w, e = [X[i0, j], X[i1, j], X[i, j0], X[i, j1]]
    nw, ne, sw, se = [X[i0, j0], X[i0, j1], X[i1, j0], X[i1, j1]]

    a = X[i, j]
    b = 1 - 2 * a
    intr1 = b
    intr20 = b * sum([n, s, w, e])
    intr21 = b * sum([nw, ne, sw, se])
    intr3 = b * sum([n * ne, ne * e, e * n, e * se,
                     se * s, s * e, s * sw, sw * w,
                     w * s, w * nw, nw * n, n * w])
    intr4 = b * sum([n * ne * e, e * se * s,
                     s * sw * w, w * nw * n])
    return intr1, intr20, intr21, intr3, intr4


N = 100
#beta, J = 1.0, [-4.0, 1.0, 1.0, 0.0, 0.0]
#beta, J = 2.0, [0.0, 1.0, -1.0, 0.0, 0.0]
#beta, J = 4.0, [-2.0, 2.0, 0.0, -1.0, 2.0]
beta, J = 1.5, [-2.0, -1.0, 1.0, 1.0, -2.0]
scrn = Screen(N)
X = random.randint(0, 2, (N, N))
while True:
    for i in range(-1, N - 1):
        for j in range(-1, N - 1):
            S = reverse(X, i, j)
            p = exp(beta * dot(J, S))
            if random.uniform(0.0, 1.0) < p / (1 + p):
                X[i, j] = 1 - X[i, j]
    scrn.update(X)
