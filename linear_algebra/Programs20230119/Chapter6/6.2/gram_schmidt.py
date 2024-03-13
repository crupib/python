from numpy import array, vdot, sqrt


def proj(x, E, inner=vdot):
    return sum([inner(e, x) * e for e in E])


def gram_schmidt(A, inner=vdot):
    E = []
    while A != []:
        a = array(A.pop(0))
        b = a - proj(a, E, inner)
        c = sqrt(inner(b, b))
        if c >= 1.0e-15:
            E.append(b / c)
    return E


if __name__ == '__main__':
    A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    E = gram_schmidt(A)
    for n, e in enumerate(E):
        print(f'e{n+1} = {e}')
    print(array([[vdot(e1, e2) for e2 in E] for e1 in E]))

'''
e1 = [0.26726124 0.53452248 0.80178373]
e2 = [ 0.87287156  0.21821789 -0.43643578]
[[1.00000000e+00 6.51017134e-17]
 [6.51017134e-17 1.00000000e+00]]
'''
