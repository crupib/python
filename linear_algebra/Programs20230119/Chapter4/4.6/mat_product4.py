def matrix_multiply(A, B):
    m, el, n = len(A), len(A[0]), len(B[0])
    C = [[sum([A[i][k] * B[k][j] for k in range(el)])
          for j in range(n)] for i in range(m)]
    return C

if __name__ == '__main__':
    from numpy.random import normal
    import matplotlib.pyplot as plt
    from time import time

    N = range(10, 210, 10)
    T = []
    for n in N:
        A = normal(0, 1, (n, n)).tolist()
        t0 = time()
        matrix_multiply(A, A)
        t1 = time()
        print(n, end=', ')
        T.append(t1 - t0)
    plt.plot(N, T), plt.show()
    #plt.savefig('mat_product4.png', bbox_inches='tight', pad_inches=0)
